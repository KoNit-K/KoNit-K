#!/usr/bin/env python3
"""Publish an auditable, custom primary-plus-coauthor commit ranking.

Only Python's standard library is required. GitHub account associations are read
again on every run; previous JSON files are never used as an attribution cache.
"""

import argparse
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
import json
import os
from pathlib import Path
import re
import shutil
import sys
import tempfile
import time
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


API_URL = "https://api.github.com/graphql"
RATE_FIELDS = "rateLimit { cost remaining resetAt }"
AUTHOR_FIELDS = """totalCount pageInfo { hasNextPage endCursor }
    edges { cursor node { user { id login } } }"""
HEAD_QUERY = """query($owner:String!, $repo:String!, $target:String!) {
  repository(owner:$owner, name:$repo) {
    nameWithOwner url defaultBranchRef { name target { oid __typename } }
  }
  user(login:$target) { id login }
  """ + RATE_FIELDS + "}"
HISTORY_QUERY = """query($owner:String!, $repo:String!, $head:GitObjectID!, $after:String) {
  repository(owner:$owner, name:$repo) {
    object(oid:$head) { ... on Commit { oid history(first:100, after:$after) {
      totalCount pageInfo { hasNextPage endCursor }
      edges { cursor node { oid authors(first:100) { """ + AUTHOR_FIELDS + """ } } }
    } } }
  }
  """ + RATE_FIELDS + "}"
AUTHORS_QUERY = """query($owner:String!, $repo:String!, $head:GitObjectID!, $after:String) {
  repository(owner:$owner, name:$repo) {
    object(oid:$head) { ... on Commit { oid authors(first:100, after:$after) {
      """ + AUTHOR_FIELDS + """
    } } }
  }
  """ + RATE_FIELDS + "}"


class ScanError(RuntimeError):
    """The scan cannot safely publish a complete snapshot."""


def _progress(message):
    print(message, file=sys.stderr, flush=True)


class GitHubGraphQLClient:
    def __init__(self, token, *, max_runtime_seconds=1740, progress=_progress):
        if not token:
            raise ScanError("Set GH_TOKEN or GITHUB_TOKEN before running this script.")
        if not 1 <= max_runtime_seconds <= 1800:
            raise ValueError("max_runtime_seconds must be between 1 and 1800")
        self.token = token
        self.deadline = time.monotonic() + max_runtime_seconds
        self.progress = progress
        self.query_count = 0
        self.query_cost = 0
        self.remaining = None
        self.reset_at = None

    def check_deadline(self):
        left = self.deadline - time.monotonic()
        if left <= 0:
            raise ScanError("Runtime budget exhausted; old outputs were not replaced.")
        return left

    def _wait(self, seconds, reason):
        seconds = max(0, seconds)
        if seconds + 1 >= self.check_deadline():
            raise ScanError(f"{reason}; required wait exceeds the remaining runtime budget.")
        self.progress(f"{reason}; waiting {seconds:.0f}s")
        until = time.monotonic() + seconds
        while time.monotonic() < until:
            time.sleep(max(0, min(30, until - time.monotonic())))
            self.check_deadline()

    def _retry_delay(self, headers, attempt, *, limited=False):
        retry_after = headers.get("retry-after")
        if retry_after:
            try:
                return max(0, float(retry_after)) + 1
            except ValueError:
                return max(0, parsedate_to_datetime(retry_after).timestamp() - time.time()) + 1
        if headers.get("x-ratelimit-remaining") == "0":
            try:
                return max(0, float(headers["x-ratelimit-reset"]) - time.time()) + 1
            except (KeyError, ValueError):
                pass
        if limited and self.remaining == 0 and self.reset_at:
            return max(0, datetime.fromisoformat(self.reset_at.replace("Z", "+00:00")).timestamp() - time.time()) + 1
        return min(600, (60 if limited else 2) * 2 ** attempt)

    def query(self, query, variables):
        """Return complete GraphQL data, rejecting all partial/error responses."""
        payload = json.dumps({"query": query, "variables": variables}).encode()
        for attempt in range(6):
            if self.remaining == 0 and self.reset_at:
                self._wait(self._retry_delay({}, attempt, limited=True), "Primary rate limit exhausted")
                self.remaining = None
            request = Request(API_URL, data=payload, headers={
                "Authorization": f"Bearer {self.token}",
                "Accept": "application/vnd.github+json",
                "Content-Type": "application/json",
                "User-Agent": "hermes-contributions-audit/1",
            })
            self.query_count += 1
            try:
                with urlopen(request, timeout=min(45, self.check_deadline())) as response:
                    status, headers, raw = response.status, response.headers, response.read()
            except HTTPError as error:
                status, headers, raw = error.code, error.headers, error.read()
            except (URLError, TimeoutError, OSError) as error:
                if attempt == 5:
                    raise ScanError(f"Network request failed after retries ({type(error).__name__}).") from error
                self._wait(2 ** (attempt + 1), "Transient network failure")
                continue
            try:
                result = json.loads(raw)
            except (ValueError, UnicodeDecodeError):
                result = {}
            data = result.get("data") if isinstance(result, dict) else None
            rate = data.get("rateLimit") if isinstance(data, dict) else None
            if isinstance(rate, dict):
                self.query_cost += rate.get("cost", 0)
                self.remaining, self.reset_at = rate.get("remaining"), rate.get("resetAt")
            errors = result.get("errors", []) if isinstance(result, dict) else []
            # Classify errors without logging response bodies, credentials, or author data.
            error_text = json.dumps({"errors": errors, "message": result.get("message") if isinstance(result, dict) else None}).casefold()
            limited = status == 429 or "rate_limit" in error_text or "rate limit" in error_text
            limited = limited or (bool(errors) or status == 403) and headers.get("x-ratelimit-remaining") == "0"
            limited = limited or (status == 403 and bool(headers.get("retry-after")))
            retryable = status in (202, 429) or 500 <= status <= 599 or limited
            retryable = retryable or any(x in error_text for x in ("timeout", "timed out", "internal", "service unavailable"))
            if retryable and attempt < 5:
                self._wait(self._retry_delay(headers, attempt, limited=limited), f"Retryable GitHub response (HTTP {status})")
                continue
            if status != 200 or errors or not isinstance(data, dict):
                first = errors[0] if isinstance(errors, list) and errors and isinstance(errors[0], dict) else {}
                if not first and isinstance(result, dict) and result.get("message"):
                    first = {"message": result["message"]}
                summary = json.dumps({key: first[key] for key in ("type", "path", "message") if key in first}, ensure_ascii=False)
                summary = summary.replace(self.token, "[redacted]")
                summary = re.sub(r"[^\s\"<>]+@[^\s\"<>]+", "[redacted-email]", summary)[:300]
                raise ScanError(f"GitHub returned HTTP {status}, {len(errors)} GraphQL errors, or incomplete data; first error: {summary}; no snapshot published.")
            if not isinstance(rate, dict) or not isinstance(self.remaining, int):
                raise ScanError("Missing GraphQL rate-limit accounting; no snapshot published.")
            return data
        raise ScanError("GitHub retries exhausted.")


def _connection(connection, label):
    if not isinstance(connection, dict):
        raise ScanError(f"Missing {label} connection.")
    total, edges, info = connection.get("totalCount"), connection.get("edges"), connection.get("pageInfo")
    if type(total) is not int or total < 0 or not isinstance(edges, list) or not isinstance(info, dict):
        raise ScanError(f"Invalid {label} pagination data.")
    if type(info.get("hasNextPage")) is not bool:
        raise ScanError(f"Missing {label} hasNextPage.")
    for edge in edges:
        if not isinstance(edge, dict) or not edge.get("cursor") or not isinstance(edge.get("node"), dict):
            raise ScanError(f"Null or malformed edge in {label}.")
    end = info.get("endCursor")
    if edges and end != edges[-1]["cursor"]:
        raise ScanError(f"Invalid {label} endCursor.")
    if info["hasNextPage"] and (not edges or not end):
        raise ScanError(f"Incomplete {label} page.")
    return total, edges, end if info["hasNextPage"] else None


def _commit_object(data, expected_sha):
    repository = data.get("repository") or {}
    obj = repository.get("object") or {}
    if obj.get("oid") != expected_sha:
        raise ScanError("The requested fixed commit is missing or does not match its SHA.")
    return obj


def _fetch_authors(client, owner, repo, sha, connection):
    authors, seen, cursors, expected = [], {}, set(), None
    while True:
        total, edges, after = _connection(connection, "authors")
        if expected is not None and expected != total:
            raise ScanError(f"Author totalCount changed for {sha}.")
        expected = total
        for edge in edges:
            actor = edge["node"]
            if "user" not in actor:
                raise ScanError("Missing GitActor.user; null must be explicit.")
            user = actor["user"]
            if user is not None and (not isinstance(user, dict) or not user.get("id") or not user.get("login")):
                raise ScanError("Incomplete linked author identity.")
            user = {"id": user["id"], "login": user["login"]} if user else None
            cursor = edge["cursor"]
            if cursor in seen:
                if seen[cursor] != user:
                    raise ScanError(f"Author attribution changed during pagination for {sha}.")
                continue
            seen[cursor] = user
            authors.append({"user": user, "role": "primary" if not authors else "coauthor"})
        if not after:
            break
        if after in cursors:
            raise ScanError(f"Repeated author pagination cursor for {sha}.")
        cursors.add(after)
        data = client.query(AUTHORS_QUERY, {"owner": owner, "repo": repo, "head": sha, "after": after})
        connection = _commit_object(data, sha).get("authors")
    if not authors or len(seen) != expected:
        raise ScanError(f"Incomplete authors for {sha}: {len(seen)} unique edges, totalCount={expected}.")
    return authors


def fetch_history(client, owner="NousResearch", repo="hermes-agent", progress=_progress, *, target_login="KoNit-K"):
    """Pin the current default-branch head and fully paginate history + authors."""
    data = client.query(HEAD_QUERY, {"owner": owner, "repo": repo, "target": target_login})
    repository = data.get("repository") or {}
    branch = repository.get("defaultBranchRef") or {}
    target = branch.get("target") or {}
    sha = target.get("oid")
    if not sha or target.get("__typename") != "Commit" or not branch.get("name"):
        raise ScanError("The repository has no readable default-branch commit.")
    if repository.get("nameWithOwner", "").casefold() != f"{owner}/{repo}".casefold():
        raise ScanError("Repository identity does not match the requested repository.")
    target_user = data.get("user")
    if not isinstance(target_user, dict) or not target_user.get("id") or not target_user.get("login"):
        raise ScanError("Target account identity could not be resolved; retaining the previous snapshot and badges.")
    progress(f"Pinned {repository['nameWithOwner']}:{branch['name']} at {sha}")
    commits, cursors, expected, after, pages, duplicates = {}, set(), None, None, 0, 0
    while True:
        data_page = client.query(HISTORY_QUERY, {"owner": owner, "repo": repo, "head": sha, "after": after})
        connection = _commit_object(data_page, sha).get("history")
        total, edges, after = _connection(connection, "history")
        if expected is not None and expected != total:
            raise ScanError("history.totalCount changed despite the pinned SHA.")
        expected = total
        for edge in edges:
            node = edge["node"]
            oid = node.get("oid")
            if not isinstance(oid, str) or not oid:
                raise ScanError("Missing commit SHA in history.")
            authors = _fetch_authors(client, owner, repo, oid, node.get("authors"))
            if oid in commits:
                duplicates += 1
                if commits[oid]["authors"] != authors:
                    raise ScanError(f"Conflicting duplicate commit attribution for {oid}.")
            else:
                commits[oid] = {"oid": oid, "authors": authors}
        pages += 1
        progress(f"History page {pages}: {len(commits)}/{expected} commits; requests={getattr(client, 'query_count', '?')}, cost={getattr(client, 'query_cost', '?')}, remaining={getattr(client, 'remaining', '?')}")
        if not after:
            break
        if after in cursors:
            raise ScanError("Repeated history pagination cursor.")
        cursors.add(after)
    if expected != len(commits) or sha not in commits:
        raise ScanError(f"Incomplete history: {len(commits)} unique SHAs, history.totalCount={expected}; no snapshot published.")
    return {"targetUser": data.get("user"), "commits": list(commits.values()), "source": {
        "repository": repository["nameWithOwner"], "repositoryUrl": repository["url"],
        "defaultBranch": branch["name"], "headSha": sha, "historyTotalCount": expected,
        "uniqueCommits": len(commits), "historyPages": pages, "duplicateCommitRows": duplicates,
        "paginationComplete": True, "queryCount": getattr(client, "query_count", None),
        "queryCost": getattr(client, "query_cost", None), "rateLimitRemaining": getattr(client, "remaining", None),
    }}


def aggregate_contributors(commits):
    """Count each (commit SHA, stable user id) once; primary overrides coauthor."""
    accounts, roles = {}, {}
    for commit in commits:
        sha = commit["oid"]
        for index, author in enumerate(commit["authors"]):
            user = author["user"]
            if user is None:
                continue
            uid, login = user["id"], user["login"]
            role = author.get("role", "primary" if index == 0 else "coauthor")
            if role not in ("primary", "coauthor"):
                raise ScanError("Unknown author role.")
            accounts.setdefault(uid, set()).add(login)
            key = (sha, uid)
            if key not in roles or role == "primary":
                roles[key] = role
    result = {uid: {"id": uid, "login": min(logins, key=lambda x: (x.casefold(), x)),
                   "primary_author_commits": 0, "coauthored_commits": 0, "total_commits": 0}
              for uid, logins in accounts.items()}
    for (_, uid), role in roles.items():
        result[uid]["primary_author_commits" if role == "primary" else "coauthored_commits"] += 1
        result[uid]["total_commits"] += 1
    ordered = sorted(result.values(), key=lambda row: (-row["total_commits"], row["login"].casefold(), row["id"]))
    previous, rank = None, 0
    for position, row in enumerate(ordered, 1):
        if row["total_commits"] != previous:
            rank = position
        row["rank"] = rank
        previous = row["total_commits"]
    return ordered


def build_snapshot(history, target_login="KoNit-K", generated_at=None):
    commits = {row["oid"]: row for row in history["commits"]}
    source = dict(history["source"])
    if source.get("paginationComplete") is not True or source.get("historyTotalCount") != len(commits):
        raise ScanError("Cannot build a snapshot from incomplete history.")
    contributors = aggregate_contributors(history["commits"])
    linked = sum(any(a["user"] is not None for a in c["authors"]) for c in commits.values())
    source.update({"uniqueCommits": len(commits), "linkedCommits": linked,
                   "unlinkedCommits": len(commits) - linked,
                   "commitsWithUnlinkedAuthors": sum(any(a["user"] is None for a in c["authors"]) for c in commits.values()),
                   "unlinkedAuthorAttributions": sum(a["user"] is None for c in commits.values() for a in c["authors"]),
                   "linkedAccountAttributions": sum(c["total_commits"] for c in contributors)})
    target_user = history.get("targetUser") or {}
    target_id = target_user.get("id")
    matches = [c for c in contributors if c["id"] == target_id] if target_id else [c for c in contributors if c["login"].casefold() == target_login.casefold()]
    target = dict(matches[0]) if matches else {"id": target_id, "login": target_user.get("login", target_login),
             "rank": None, "primary_author_commits": 0, "coauthored_commits": 0, "total_commits": 0}
    target.update({"requestedLogin": target_login, "found": bool(matches)})
    primary_shas, coauthor_shas = set(), set()
    for commit in history["commits"]:
        for index, author in enumerate(commit["authors"]):
            if author["user"] is not None and author["user"]["id"] == target["id"]:
                role = author.get("role", "primary" if index == 0 else "coauthor")
                (primary_shas if role == "primary" else coauthor_shas).add(commit["oid"])
    coauthor_shas.difference_update(primary_shas)
    if len(primary_shas) != target["primary_author_commits"] or len(coauthor_shas) != target["coauthored_commits"]:
        raise ScanError("Target commit evidence does not match the aggregate counts.")
    target.update({"primary_commit_shas": sorted(primary_shas), "coauthored_commit_shas": sorted(coauthor_shas)})
    return {"schemaVersion": 1, "generatedAt": generated_at or datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z"),
            "method": {"name": "custom-primary-plus-coauthor-commit-ranking", "version": 1,
                       "api": API_URL, "authors": "GitHub Commit.authors; first entry is primary",
                       "scope": "All commits reachable from the pinned default-branch head; no history filters",
                       "includesMergeCommits": True, "includesEmptyCommits": True,
                       "linkedBotsIncluded": True, "unlinkedAuthorsIncluded": False,
                       "identity": "GitHub user.id", "deduplication": "One count per (commit SHA, user.id); primary takes precedence",
                       "coauthoredCommits": "Coauthor-only commits; excludes commits also credited as primary",
                       "ranking": "Competition rank (1,2,2,4); display ties by login.casefold(), then user.id",
                       "officialInsightsRanking": False, "attributionCache": False,
                       "unlinkedAuthorNote": "GitActor.user=null may include bot identities. No account is inferred from names or email addresses.",
                       "attributionTiming": "Commit set is pinned; GitHub account associations are observed during this run and may change later.",
                       "documentation": ["https://docs.github.com/en/graphql/reference/commits#commit", "https://docs.github.com/en/graphql/reference/git#gitactor"]},
            "source": source, "target": target, "contributors": contributors}


def render_markdown(snapshot):
    source, target = snapshot["source"], snapshot["target"]
    repo_url, sha = source["repositoryUrl"], source["headSha"]
    rows = snapshot["contributors"][:100]
    lines = ["# Hermes Agent contribution audit", "", "This is a **custom primary-plus-coauthor ranking**, not GitHub Insights or the REST contributors ranking.", "",
             f"Generated: {snapshot['generatedAt']}", "",
             f"Source: [{source['repository']}]({repo_url}), default branch `{source['defaultBranch']}`, pinned commit [`{sha}`]({repo_url}/commit/{sha}).", "",
             "## Method", "",
             "- Scan the complete unfiltered history of the pinned default-branch head, including merge and empty commits.",
             "- Read all pages of GitHub `Commit.authors`, including nested author pagination. The first author is primary; the others are coauthors.",
             "- Group linked accounts by stable GitHub user ID. Count each account once per commit SHA; primary authorship takes precedence over coauthorship.",
             "- Include every linked account, including linked bots. Exclude unlinked authors without guessing identities from names or emails; those unlinked entries may include bots.",
             "- Rank by total commits using competition ranks (1, 2, 2, 4). Display ties by case-folded login, then stable user ID.",
             "- Resolve account associations afresh on each run. The commit set is pinned; account associations are observed during the scan and can change later.", "",
             "References: [GitHub Commit.authors and history](https://docs.github.com/en/graphql/reference/commits#commit) · [GitActor.user](https://docs.github.com/en/graphql/reference/git#gitactor) · [generator source](../scripts/update_hermes_contributions.py) · [complete JSON](hermes-contributions.json).", "",
             "## Completeness and attribution", "",
             f"- History pages: {source['historyPages']}; declared history total: {source['historyTotalCount']:,}; unique commit SHAs: {source['uniqueCommits']:,}; all pagination completed and totals matched.",
             f"- Commits with at least one linked account: {source['linkedCommits']:,}; commits with no linked account: {source['unlinkedCommits']:,}.",
             f"- Commits with any unlinked author: {source['commitsWithUnlinkedAuthors']:,}; unlinked author entries: {source['unlinkedAuthorAttributions']:,}.",
             f"- Linked account-commit credits: {source['linkedAccountAttributions']:,}; accounts: {len(snapshot['contributors']):,}. A commit credited to multiple accounts contributes once to each account.",
             f"- GraphQL requests: {source.get('queryCount')}; reported query cost: {source.get('queryCost')}; remaining rate-limit points: {source.get('rateLimitRemaining')}.", "",
             f"## {target['login']}", "",
             f"Total commits: **{target['total_commits']:,}** · primary: **{target['primary_author_commits']:,}** · coauthor-only: **{target['coauthored_commits']:,}** · custom rank: **{'#' + str(target['rank']) if target['rank'] is not None else 'unranked'}**.", "",
             f"## {'All contributors' if len(snapshot['contributors']) <= 100 else 'First 100 contributor rows'}", "",
             "The table includes rows 5–20 where present. Rank ties can make row positions differ from competition ranks.", "",
             "| Position | Custom rank | Account | Primary | Coauthor-only | Total |",
             "| ---: | ---: | --- | ---: | ---: | ---: |"]
    lines.extend(f"| {i} | {c['rank']} | [{c['login']}](https://github.com/{c['login']}) | {c['primary_author_commits']:,} | {c['coauthored_commits']:,} | {c['total_commits']:,} |" for i, c in enumerate(rows, 1))
    return "\n".join(lines) + "\n"


def write_outputs(snapshot, output_dir):
    """Stage all files before replacing; roll back an ordinary replacement error."""
    target = snapshot["target"]
    if target.get("found") is not True or type(target.get("rank")) is not int or target["rank"] < 1:
        raise ScanError("Target account could not be ranked; retaining the previous snapshot and badges.")
    badge = lambda label, message, color: {"schemaVersion": 1, "label": label, "message": message, "color": color, "cacheSeconds": 3600}
    payloads = {"hermes-contributions.json": snapshot,
                "hermes-commits.json": badge("COMMITS", str(target["total_commits"]), "8B5CF6"),
                "hermes-contributor-rank.json": badge("COMMIT RANK", f"#{target['rank']}", "22c55e")}
    contents = {name: json.dumps(value, ensure_ascii=False, indent=2) + "\n" for name, value in payloads.items()}
    contents["hermes-contributions.md"] = render_markdown(snapshot)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".hermes-staging-", dir=output_dir) as staging:
        staging = Path(staging)
        originals, replaced = {}, []
        for name, content in contents.items():
            (staging / name).write_text(content, encoding="utf-8")
            destination = output_dir / name
            originals[name] = destination.exists()
            if originals[name]:
                shutil.copy2(destination, staging / (name + ".old"))
        try:
            for name in contents:
                os.replace(staging / name, output_dir / name)
                replaced.append(name)
        except OSError:
            for name in reversed(replaced):
                if originals[name]:
                    os.replace(staging / (name + ".old"), output_dir / name)
                else:
                    (output_dir / name).unlink()
            raise


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repository", default="NousResearch/hermes-agent")
    parser.add_argument("--target", default="KoNit-K")
    parser.add_argument("--output-dir", type=Path, default=Path(__file__).resolve().parents[1] / "data")
    parser.add_argument("--max-runtime-seconds", type=int, default=1740)
    args = parser.parse_args(argv)
    try:
        owner, repo = args.repository.split("/")
        if not owner or not repo:
            raise ValueError("Repository must be OWNER/REPO")
        client = GitHubGraphQLClient((os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN") or "").strip(), max_runtime_seconds=args.max_runtime_seconds)
        history = fetch_history(client, owner, repo, target_login=args.target)
        snapshot = build_snapshot(history, target_login=args.target)
        client.check_deadline()
        write_outputs(snapshot, args.output_dir)
        target = snapshot["target"]
        _progress(f"Published {len(snapshot['contributors'])} accounts; {target['login']}: {target['total_commits']} commits, custom rank {target['rank']}.")
        return 0
    except (ScanError, OSError, ValueError, KeyError, TypeError) as error:
        _progress(f"ERROR: {error}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
