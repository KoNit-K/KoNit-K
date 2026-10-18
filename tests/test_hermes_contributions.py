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


def fetch_history(client, *, progress=lambda _: None, expected_shas=None, **kwargs):
    if expected_shas is None:
        expected_shas = {
            edge["node"]["oid"]
            for response in client.responses
            for edge in response.get("repository", {}).get("object", {}).get("history", {}).get("edges", [])
        }
    return stats.fetch_history(client, progress=progress,
        reachable_shas_provider=lambda owner, repo, sha: set(expected_shas), **kwargs)


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
        history = fetch_history(client)
        self.assertEqual(len(history["commits"]), 2)
        self.assertEqual([call[1]["head"] for call in client.calls[1:]], ["head", "head"])
        self.assertEqual(client.calls[2][1]["after"], "c0")
        self.assertTrue(history["source"]["paginationComplete"])

    def test_nested_authors_pagination_preserves_primary_role(self):
        node = {"oid": "head", "authors": connection([{"user": None}], 2, has_next=True, prefix="a")}
        client = FakeClient(HEAD, history_page([node], 1),
            {"repository": {"object": {"oid": "head", "authors": connection([{"user": KONIT}], 2, prefix="a", start=1)}}})
        history = fetch_history(client)
        row = stats.aggregate_contributors(history["commits"])[0]
        self.assertEqual((row["primary_author_commits"], row["coauthored_commits"]), (0, 1))
        self.assertEqual(client.calls[2][1]["after"], "a0")

    def test_incomplete_history_is_rejected(self):
        client = FakeClient(HEAD, history_page([graphql_commit("head", KONIT)], 2))
        with self.assertRaises(stats.ScanError):
            fetch_history(client)

    def test_incomplete_author_connection_is_rejected(self):
        node = {"oid": "head", "authors": connection([{"user": KONIT}], 2)}
        with self.assertRaises(stats.ScanError):
            fetch_history(FakeClient(HEAD, history_page([node], 1)))

    def test_repeated_history_cursor_is_rejected(self):
        page = history_page([graphql_commit("head", KONIT)], 2, has_next=True)
        with self.assertRaises(stats.ScanError):
            fetch_history(FakeClient(HEAD, page, page))

    def test_git_reachable_set_repairs_commits_omitted_by_history_pagination(self):
        recovered = graphql_commit("older", BOB, KONIT)
        client = FakeClient(HEAD, history_page([graphql_commit("head", KONIT)], 2),
            {"repository": {"object": recovered}})
        history = fetch_history(client, expected_shas={"head", "older"})
        self.assertEqual({c["oid"] for c in history["commits"]}, {"head", "older"})
        self.assertEqual(history["source"]["recoveredCommitShas"], ["older"])
        self.assertTrue(history["source"]["gitReachabilityVerified"])
        self.assertEqual(client.calls[-1][1]["head"], "older")
        self.assertEqual(stats.build_snapshot(history)["target"]["total_commits"], 2)

    def test_equal_counts_do_not_hide_a_non_reachable_commit(self):
        client = FakeClient(HEAD, history_page([
            graphql_commit("head", KONIT), graphql_commit("not-reachable", BOB)], 2))
        with self.assertRaises(stats.ScanError):
            fetch_history(client, expected_shas={"head", "missing"})


class PublishingTests(unittest.TestCase):
    def snapshot(self):
        history = fetch_history(FakeClient(HEAD,
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


class UncertaintyTests(unittest.TestCase):
    def unavailable_response(self):
        return {"repository": {"nameWithOwner": "NousResearch/hermes-agent", "object": None}}

    def unresolved_history(self, **kwargs):
        client = FakeClient(HEAD,
            history_page([graphql_commit("head", KONIT)], 2),
            self.unavailable_response(), self.unavailable_response())
        return fetch_history(client, expected_shas={"head", "unavailable"}, **kwargs)

    def test_unavailable_objects_remain_unknown_in_a_complete_git_partition(self):
        history = self.unresolved_history()
        source = history["source"]
        self.assertTrue(source["gitReachabilityVerified"])
        self.assertFalse(source["authorAttributionComplete"])
        self.assertEqual(source["uniqueCommits"], 2)
        self.assertEqual(source["resolvedCommits"], 1)
        self.assertEqual(source["unresolvedCommits"], 1)
        self.assertEqual(source["unresolvedCommitShas"], ["unavailable"])
        self.assertEqual([c["oid"] for c in history["commits"]], ["head"])
        snapshot = stats.build_snapshot(history)
        self.assertEqual((snapshot["target"]["total_commits_min"], snapshot["target"]["total_commits_max"]), (1, 2))
        with tempfile.TemporaryDirectory() as directory:
            stats.write_outputs(snapshot, directory)
            badge = json.loads((Path(directory) / "hermes-commits.json").read_text())
            self.assertEqual(badge["message"], "1+")
            report = (Path(directory) / "hermes-contributions.md").read_text()
            self.assertIn("unavailable", report)

    def test_expression_lookup_preserves_actual_github_authors(self):
        client = FakeClient(HEAD,
            history_page([graphql_commit("head", KONIT)], 2),
            self.unavailable_response(),
            {"repository": {"nameWithOwner": "NousResearch/hermes-agent", "object": graphql_commit("older", BOB, KONIT)}})
        history = fetch_history(client, expected_shas={"head", "older"})
        self.assertTrue(history["source"]["authorAttributionComplete"])
        self.assertEqual(client.calls[-1][1]["expression"], "older")
        self.assertEqual(stats.build_snapshot(history)["target"]["total_commits"], 2)

    def test_missing_repository_is_an_error_not_an_unknown_author(self):
        client = FakeClient(HEAD,
            history_page([graphql_commit("head", KONIT)], 2), {"repository": None})
        with self.assertRaises(stats.ScanError):
            fetch_history(client, expected_shas={"head", "older"})

    def test_snapshot_rejects_equal_size_but_different_git_partition(self):
        history = self.unresolved_history()
        history["source"]["unresolvedCommitShas"] = ["different-commit"]
        with self.assertRaises(stats.ScanError):
            stats.build_snapshot(history)

    def test_failed_recovery_retains_the_full_scan_checkpoint(self):
        client = FakeClient(HEAD,
            history_page([graphql_commit("head", KONIT)], 2),
            {"repository": {"object": {"oid": "wrong-sha"}}})
        with tempfile.TemporaryDirectory() as directory:
            checkpoint = Path(directory) / "scan.json"
            with self.assertRaises(stats.ScanError):
                fetch_history(client, expected_shas={"head", "older"}, checkpoint_path=checkpoint)
            saved = json.loads(checkpoint.read_text())
            self.assertFalse(saved["complete"])
            self.assertFalse(saved["source"]["paginationComplete"])
            self.assertEqual([c["oid"] for c in saved["commits"]], ["head"])
            self.assertIn("older", saved["missingCommitShas"])

    def test_rank_bounds_cover_all_shared_credit_assignments_and_ties(self):
        known = [5, 3, 2]
        rows = [{"id": str(i), "login": str(i), "total_commits": n, "rank": i + 1}
                for i, n in enumerate(known)]
        bounded = stats.apply_uncertainty_bounds(rows, 2)
        # Each of two unknown commits can credit any subset of the three known
        # accounts and one previously unseen account; credit is not a shared pie.
        for first in range(16):
            for second in range(16):
                totals = known + [0]
                for mask in (first, second):
                    for i in range(4):
                        totals[i] += bool(mask & (1 << i))
                for i, row in enumerate(bounded):
                    rank = 1 + sum(t > totals[i] for j, t in enumerate(totals) if j != i)
                    self.assertLessEqual(row["rank_min"], rank)
                    self.assertGreaterEqual(row["rank_max"], rank)
        self.assertIsNotNone(bounded[2]["rank_max"])  # unseen accounts can tie 2, not exceed it

    def test_wide_gaps_give_exact_rank_while_small_tail_can_be_unbounded(self):
        rows = [{"id": str(i), "login": str(i), "total_commits": n, "rank": i + 1}
                for i, n in enumerate([500, 382, 300, 1])]
        bounded = stats.apply_uncertainty_bounds(rows, 3)
        self.assertEqual((bounded[1]["rank_min"], bounded[1]["rank_max"]), (2, 2))
        self.assertTrue(bounded[1]["rank_is_exact"])
        self.assertEqual((bounded[1]["total_commits_min"], bounded[1]["total_commits_max"]), (382, 385))
        self.assertIsNone(bounded[3]["rank_max"])


if __name__ == "__main__":
    unittest.main()
