"""Regression checks for inclusive counting and incomplete GitHub responses."""

import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch


SCRIPT = Path(__file__).resolve().parents[1] / "scripts/update_hermes_contributions.py"
SPEC = importlib.util.spec_from_file_location("hermes_stats", SCRIPT)
stats = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(stats)

KONIT = {"id": "U_KONIT", "login": "KoNit-K"}
BOB = {"id": "U_BOB", "login": "bob"}
CAROL = {"id": "U_CAROL", "login": "carol"}
BOT = {"id": "BOT_SEAEYE", "login": "hermes-seaeye[bot]"}


def commit(sha, *users):
    return {"oid": sha, "authors": [
        {"user": user, "role": "primary" if i == 0 else "coauthor"}
        for i, user in enumerate(users)
    ]}


def connection(nodes, total=None, *, has_next=False, prefix="c", start=0):
    edges = [{"cursor": f"{prefix}{i}", "node": node}
             for i, node in enumerate(nodes, start)]
    return {"totalCount": len(nodes) if total is None else total, "edges": edges,
            "pageInfo": {"hasNextPage": has_next,
                         "endCursor": edges[-1]["cursor"] if edges else None}}


def graphql_commit(sha, *users):
    return {"oid": sha, "authors": connection([{"user": user} for user in users], prefix="a")}


def history_page(nodes, total, **kwargs):
    return {"repository": {"object": {"oid": "head", "history": connection(nodes, total, **kwargs)}}}


HEAD = {"repository": {"nameWithOwner": "NousResearch/hermes-agent",
        "url": "https://github.com/NousResearch/hermes-agent",
        "defaultBranchRef": {"name": "main", "target": {"oid": "head", "__typename": "Commit"}}},
        "user": KONIT}


class FakeClient:
    def __init__(self, *responses):
        self.responses = list(responses)
        self.calls = []

    def query(self, query, variables):
        self.calls.append((query, variables))
        if not self.responses:
            raise AssertionError("Unexpected additional API call")
        return self.responses.pop(0)


class CountingTests(unittest.TestCase):
    def test_primary_coauthor_duplicates_and_duplicate_shas_count_once(self):
        first = commit("one", KONIT, KONIT, BOB, BOB)
        rows = stats.aggregate_contributors([first, commit("two", BOB, KONIT), first])
        for row in rows:
            self.assertEqual((row["primary_author_commits"], row["coauthored_commits"], row["total_commits"]), (1, 1, 2))
            self.assertEqual(row["rank"], 1)

    def test_account_id_unifies_renames_and_case_variants(self):
        renamed = {"id": KONIT["id"], "login": "renamed-user"}
        rows = stats.aggregate_contributors([commit("one", KONIT), commit("two", renamed)])
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["total_commits"], 2)

    def test_anonymous_primary_does_not_promote_linked_coauthor(self):
        rows = stats.aggregate_contributors([commit("one", None, KONIT), commit("two", BOT, None)])
        by_id = {row["id"]: row for row in rows}
        self.assertEqual(set(by_id), {KONIT["id"], BOT["id"]})
        self.assertEqual(by_id[KONIT["id"]]["primary_author_commits"], 0)
        self.assertEqual(by_id[KONIT["id"]]["coauthored_commits"], 1)
        self.assertEqual(by_id[BOT["id"]]["primary_author_commits"], 1)

    def test_coauthor_only_accounts_participate_and_ties_use_competition_rank(self):
        rows = stats.aggregate_contributors([
            commit("one", KONIT, CAROL), commit("two", KONIT, CAROL),
            commit("three", KONIT, BOB), commit("four", BOB, CAROL),
            commit("five", BOB, CAROL), commit("six", BOT),
        ])
        self.assertEqual([(r["login"], r["total_commits"], r["rank"]) for r in rows],
                         [("carol", 4, 1), ("bob", 3, 2), ("KoNit-K", 3, 2), ("hermes-seaeye[bot]", 1, 4)])


class PaginationTests(unittest.TestCase):
    def test_history_uses_pinned_head_and_reads_all_pages(self):
        client = FakeClient(HEAD,
            history_page([graphql_commit("head", KONIT)], 2, has_next=True),
            history_page([graphql_commit("older", BOB, KONIT)], 2, start=1))
        history = stats.fetch_history(client, progress=lambda _: None)
        self.assertEqual(len(history["commits"]), 2)
        self.assertEqual([call[1]["head"] for call in client.calls[1:]], ["head", "head"])
        self.assertEqual(client.calls[2][1]["after"], "c0")
        self.assertTrue(history["source"]["paginationComplete"])

    def test_nested_authors_pagination_preserves_primary_role(self):
        node = {"oid": "head", "authors": connection([{"user": None}], 2, has_next=True, prefix="a")}
        client = FakeClient(HEAD, history_page([node], 1),
            {"repository": {"object": {"oid": "head", "authors": connection([{"user": KONIT}], 2, prefix="a", start=1)}}})
        history = stats.fetch_history(client, progress=lambda _: None)
        row = stats.aggregate_contributors(history["commits"])[0]
        self.assertEqual((row["primary_author_commits"], row["coauthored_commits"]), (0, 1))
        self.assertEqual(client.calls[2][1]["after"], "a0")

    def test_incomplete_history_is_rejected(self):
        client = FakeClient(HEAD, history_page([graphql_commit("head", KONIT)], 2))
        with self.assertRaises(stats.ScanError):
            stats.fetch_history(client, progress=lambda _: None)

    def test_incomplete_author_connection_is_rejected(self):
        node = {"oid": "head", "authors": connection([{"user": KONIT}], 2)}
        with self.assertRaises(stats.ScanError):
            stats.fetch_history(FakeClient(HEAD, history_page([node], 1)), progress=lambda _: None)

    def test_repeated_history_cursor_is_rejected(self):
        page = history_page([graphql_commit("head", KONIT)], 2, has_next=True)
        with self.assertRaises(stats.ScanError):
            stats.fetch_history(FakeClient(HEAD, page, page), progress=lambda _: None)


class PublishingTests(unittest.TestCase):
    def snapshot(self):
        history = stats.fetch_history(FakeClient(HEAD,
            history_page([graphql_commit("head", KONIT), graphql_commit("older", BOB, KONIT)], 2)),
            progress=lambda _: None)
        return stats.build_snapshot(history, generated_at="2026-10-18T12:00:00Z")

    def test_badges_and_audit_share_one_complete_snapshot(self):
        snapshot = self.snapshot()
        with tempfile.TemporaryDirectory() as directory:
            stats.write_outputs(snapshot, directory)
            output = Path(directory)
            saved = json.loads((output / "hermes-contributions.json").read_text())
            count = json.loads((output / "hermes-commits.json").read_text())
            rank = json.loads((output / "hermes-contributor-rank.json").read_text())
            self.assertEqual(saved["target"]["total_commits"], 2)
            self.assertEqual(saved["target"]["primary_commit_shas"], ["head"])
            self.assertEqual(saved["target"]["coauthored_commit_shas"], ["older"])
            self.assertEqual(count["message"], "2")
            self.assertEqual(rank["message"], "#1")
            self.assertEqual(count["label"], "COMMITS")
            self.assertEqual(rank["label"], "COMMIT RANK")
            self.assertIn("head", (output / "hermes-contributions.md").read_text())

    def test_unresolved_target_preserves_previous_files(self):
        snapshot = self.snapshot()
        snapshot["target"].update(found=False, rank=None, total_commits=0)
        with tempfile.TemporaryDirectory() as directory:
            previous = Path(directory) / "hermes-commits.json"
            previous.write_text("last successful count\n")
            with self.assertRaises(stats.ScanError):
                stats.write_outputs(snapshot, directory)
            self.assertEqual(previous.read_text(), "last successful count\n")

    def test_http_200_with_graphql_errors_is_not_accepted(self):
        class Response:
            status = 200
            headers = {}
            def __enter__(self): return self
            def __exit__(self, *_): pass
            def read(self):
                return json.dumps({"data": {"repository": {}, "rateLimit": {"cost": 1, "remaining": 999, "resetAt": "2026-10-18T13:00:00Z"}},
                                   "errors": [{"message": "Could not resolve a required resource"}]}).encode()
        with patch.object(stats, "urlopen", return_value=Response()):
            client = stats.GitHubGraphQLClient("test-token", progress=lambda _: None)
            with self.assertRaises(stats.ScanError):
                client.query("query { repository { id } }", {})


if __name__ == "__main__":
    unittest.main()
