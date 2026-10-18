#!/usr/bin/env python3
"""Publish an auditable, custom primary-plus-coauthor commit ranking.

Python's standard library and Git are required. GitHub account associations are
read again on every run; previous JSON files are never used as an attribution cache.
"""

import argparse
from bisect import bisect_right
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
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
EXPRESSION_AUTHORS_QUERY = """query($owner:String!, $repo:String!, $expression:String!, $after:String) {
  repository(owner:$owner, name:$repo) {
    object(expression:$expression) { __typename oid ... on Commit { authors(first:100, after:$after) {
      """ + AUTHOR_FIELDS + """
    } } }
  }
  """ + RATE_FIELDS + "}"
DIAGNOSE_QUERY = """query($owner:String!, $repo:String!, $head:GitObjectID!, $expression:String!) {
  repository(owner:$owner, name:$repo) {
    byOid: object(oid:$head) { __typename oid ... on Commit { authors(first:100) {
      """ + AUTHOR_FIELDS + """
    } } }
    byExpression: object(expression:$expression) { __typename oid ... on Commit { authors(first:100) {
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
    repository = data.get("repository")
    obj = repository.get("object") if isinstance(repository, dict) else None
    if not isinstance(obj, dict) or obj.get("oid") != expected_sha:
        returned = obj.get("oid") if isinstance(obj, dict) else None
        kind = obj.get("__typename") if isinstance(obj, dict) else None
        raise ScanError(f"Commit object mismatch: expected={expected_sha}, returned={returned}, type={kind}, repository_null={repository is None}, object_null={obj is None}.")
    return obj


def _write_checkpoint(path, payload):
    """Atomically retain incomplete diagnostic data, never publishable badges."""
    if path is None:
        return
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", prefix=path.name + ".", dir=path.parent, delete=False) as handle:
            temporary = Path(handle.name)
            json.dump(payload, handle, ensure_ascii=False, separators=(",", ":"))
            handle.write("\n")
        os.replace(temporary, path)
    finally:
        if temporary is not None and temporary.exists():
            temporary.unlink()


def _describe_object(obj):
    """Only expose queried public identifiers and shape information."""
    if not isinstance(obj, dict):
        return {"objectIsNull": obj is None, "objectType": type(obj).__name__}
    authors = obj.get("authors") or {}
    edges = authors.get("edges") or []
    return {"objectIsNull": False, "keys": sorted(obj), "oid": obj.get("oid"), "type": obj.get("__typename"),
            "authorsTotalCount": authors.get("totalCount"), "returnedAuthorEdges": len(edges),
            "pageInfo": authors.get("pageInfo"),
            "authorAccounts": [((edge or {}).get("node") or {}).get("user") for edge in edges]}


def diagnose_commits(client, owner, repo, shas):
    """Compare the production author query and two explicit object lookups."""
    results = []
    for sha in dict.fromkeys(shas):
        if not re.fullmatch(r"[0-9a-fA-F]{40}|[0-9a-fA-F]{64}", sha):
            raise ScanError(f"Diagnostic SHA must be a full hexadecimal object ID: {sha}")
        sha = sha.lower()
        result = {"expectedSha": sha}
        try:
            data = client.query(AUTHORS_QUERY, {"owner": owner, "repo": repo, "head": sha, "after": None})
            result["productionAuthorsQuery"] = _describe_object((data.get("repository") or {}).get("object"))
        except ScanError as error:
            result["productionAuthorsQuery"] = {"error": str(error)}
        try:
            data = client.query(DIAGNOSE_QUERY, {"owner": owner, "repo": repo, "head": sha, "expression": sha})
            repository = data.get("repository") or {}
            result.update({"byOid": _describe_object(repository.get("byOid")),
                           "byExpression": _describe_object(repository.get("byExpression"))})
        except ScanError as error:
            result["comparisonQueryError"] = str(error)
        results.append(result)
    return results


def _fetch_authors(client, owner, repo, sha, connection, *, use_expression=False):
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
        query = EXPRESSION_AUTHORS_QUERY if use_expression else AUTHORS_QUERY
        variables = {"owner": owner, "repo": repo, "expression" if use_expression else "head": sha, "after": after}
        data = client.query(query, variables)
        connection = _commit_object(data, sha).get("authors")
    if not authors or len(seen) != expected:
        raise ScanError(f"Incomplete authors for {sha}: {len(seen)} unique edges, totalCount={expected}.")
    return authors


def _recover_authors(client, owner, repo, sha):
    """Return None only after two explicit null objects in valid repositories."""
    for use_expression in (False, True):
        query = EXPRESSION_AUTHORS_QUERY if use_expression else AUTHORS_QUERY
        variables = {"owner": owner, "repo": repo, "expression" if use_expression else "head": sha, "after": None}
        data = client.query(query, variables)
        repository = data.get("repository")
        if not isinstance(repository, dict) or "object" not in repository:
            raise ScanError(f"Invalid repository response while resolving authors for {sha}.")
        if repository["object"] is None:
            continue
        obj = _commit_object(data, sha)
        return _fetch_authors(client, owner, repo, sha, obj.get("authors"), use_expression=use_expression)
    return None


def read_reachable_shas(owner, repo, sha, *, timeout=300):
    """Independently enumerate the pinned commit's complete Git ancestry."""
    if not all(re.fullmatch(r"[A-Za-z0-9_.-]+", value) for value in (owner, repo)):
        raise ScanError("Invalid repository identity for Git verification.")
    if not re.fullmatch(r"[0-9a-f]{40}|[0-9a-f]{64}", sha):
        raise ScanError("Invalid pinned SHA for Git verification.")
    deadline = time.monotonic() + timeout
    env = os.environ.copy()
    env["GIT_TERMINAL_PROMPT"] = "0"
    for key in ("GIT_DIR", "GIT_WORK_TREE", "GIT_INDEX_FILE", "GIT_OBJECT_DIRECTORY", "GIT_ALTERNATE_OBJECT_DIRECTORIES"):
        env.pop(key, None)
    with tempfile.TemporaryDirectory(prefix="hermes-ancestry-") as folder:
        def run(*arguments):
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                raise ScanError("Git reachability verification exceeded its runtime budget.")
            try:
                result = subprocess.run(["git", "--no-replace-objects", "-C", folder, *arguments],
                                        capture_output=True, text=True, check=True, timeout=remaining, env=env)
            except (OSError, subprocess.SubprocessError) as error:
                raise ScanError(f"Git reachability verification failed ({type(error).__name__}); no snapshot published.") from error
            return result.stdout.strip()
        run("init", "--bare", "--quiet")
        run("-c", "gc.auto=0", "fetch", "--quiet", "--filter=tree:0", "--no-tags", "--no-recurse-submodules",
            f"https://github.com/{owner}/{repo}.git", sha)
        if run("rev-parse", "--is-shallow-repository") != "false":
            raise ScanError("Git verification repository is shallow; complete ancestry is required.")
        rows = run("rev-list", "--missing=error", sha, "--").splitlines()
    reachable = set(rows)
    if sha not in reachable or len(rows) != len(reachable) or any(not re.fullmatch(r"[0-9a-f]{40}|[0-9a-f]{64}", row) for row in rows):
        raise ScanError("Git returned an invalid reachable commit set.")
    return reachable


def fetch_history(client, owner="NousResearch", repo="hermes-agent", progress=_progress, *, target_login="KoNit-K", reachable_shas_provider=None, checkpoint_path=None):
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
    history_unique = len(commits)
    checkpoint_details = {}

    def checkpoint(phase, **updates):
        checkpoint_details.update(updates)
        _write_checkpoint(checkpoint_path, {"schemaVersion": 1, "kind": "incomplete-scan", "complete": False,
            "capturedAt": datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z"),
            "phase": phase, "targetUser": data.get("user"), "source": {
                "repository": repository["nameWithOwner"], "repositoryUrl": repository["url"],
                "defaultBranch": branch["name"], "headSha": sha, "historyTotalCount": expected,
                "historyPages": pages, "duplicateCommitRows": duplicates,
                "graphqlHistoryUniqueCommits": history_unique, "uniqueCommits": len(commits),
                "historyPaginationComplete": True, "paginationComplete": False,
                "queryCount": getattr(client, "query_count", None), "queryCost": getattr(client, "query_cost", None)},
            "commits": list(commits.values()), **checkpoint_details})

    checkpoint("history-scanned")
    progress("Verifying the complete reachable SHA set with Git")
    if reachable_shas_provider is None:
        reachable = read_reachable_shas(owner, repo, sha, timeout=min(300, client.check_deadline()))
    else:
        reachable = set(reachable_shas_provider(owner, repo, sha))
    extra = set(commits) - reachable
    missing = sorted(reachable - set(commits))
    checkpoint("git-compared", gitReachableCommitShas=sorted(reachable),
               originalMissingCommitShas=missing, missingCommitShas=missing,
               extraCommitShas=sorted(extra), recoveredCommitShas=[])
    if sha not in reachable or len(reachable) != expected:
        raise ScanError(f"Git ancestry count {len(reachable)} does not match history.totalCount={expected}, or the pinned SHA is missing; no snapshot published.")
    if extra:
        raise ScanError(f"GraphQL returned {len(extra)} commits outside the pinned Git ancestry: {', '.join(sorted(extra)[:10])}; no snapshot published.")
    if missing:
        progress(f"GraphQL history omitted {len(missing)} reachable commits; fetching authors directly by SHA")
    recovered_shas, unresolved_shas = [], []
    for oid in missing:
        progress(f"Recovering omitted commit {oid}")
        authors = _recover_authors(client, owner, repo, oid)
        if authors is None:
            unresolved_shas.append(oid)
            progress(f"Author attribution unresolved for {oid}: both GitHub object lookups returned null")
        else:
            commits[oid] = {"oid": oid, "authors": authors}
            recovered_shas.append(oid)
        checkpoint("recovering", missingCommitShas=sorted(reachable - set(commits) - set(unresolved_shas)),
                   recoveredCommitShas=list(recovered_shas), unresolvedCommitShas=list(unresolved_shas))
    if set(commits) & set(unresolved_shas) or set(commits) | set(unresolved_shas) != reachable:
        raise ScanError("Resolved and unresolved SHA sets do not form the exact pinned Git ancestry; no snapshot published.")
    progress(f"Git verified {len(reachable)} reachable commits; resolved={len(commits)}, unresolved={len(unresolved_shas)}, recovered={len(recovered_shas)}, duplicate history rows={duplicates}")
    return {"targetUser": data.get("user"), "commits": list(commits.values()), "reachableCommitShas": sorted(reachable), "source": {
        "repository": repository["nameWithOwner"], "repositoryUrl": repository["url"],
        "defaultBranch": branch["name"], "headSha": sha, "historyTotalCount": expected,
        "uniqueCommits": len(reachable), "historyPages": pages, "duplicateCommitRows": duplicates,
        "graphqlHistoryUniqueCommits": history_unique, "gitReachableCommits": len(reachable),
        "gitReachabilityVerified": True, "recoveredCommitShas": sorted(recovered_shas),
        "resolvedCommits": len(commits), "unresolvedCommits": len(unresolved_shas),
        "unresolvedCommitShas": sorted(unresolved_shas), "authorAttributionComplete": not unresolved_shas,
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


def apply_uncertainty_bounds(contributors, unresolved_count):
    """Bound complete totals and competition ranks without assigning unknowns."""
    if type(unresolved_count) is not int or unresolved_count < 0:
        raise ScanError("Unresolved commit count must be a nonnegative integer.")
    known_counts = sorted(row["total_commits"] for row in contributors)
    bounded = []
    for contributor in contributors:
        row = dict(contributor)
        known, upper = row["total_commits"], row["total_commits"] + unresolved_count
        best = 1 + len(known_counts) - bisect_right(known_counts, upper)
        # Unknown accounts can exceed the target only if its known count is < U.
        worst = None if known < unresolved_count else (
            1 + len(known_counts) - bisect_right(known_counts, known - unresolved_count) - (unresolved_count > 0))
        row.update({"total_commits_min": known, "total_commits_max": upper,
                    "rank_min": best, "rank_max": worst,
                    "rank_is_exact": worst is not None and best == worst})
        bounded.append(row)
    return bounded


def build_snapshot(history, target_login="KoNit-K", generated_at=None):
    commits = {row["oid"]: row for row in history["commits"]}
    source = dict(history["source"])
    unresolved_shas = source.get("unresolvedCommitShas", [])
    if (not isinstance(unresolved_shas, list) or any(not isinstance(sha, str) for sha in unresolved_shas)
            or len(unresolved_shas) != len(set(unresolved_shas)) or set(unresolved_shas) & set(commits)):
        raise ScanError("Unresolved commit SHAs must be unique and separate from resolved records.")
    unresolved_count, total_count = len(unresolved_shas), len(commits) + len(unresolved_shas)
    reachable = history.get("reachableCommitShas")
    if (not isinstance(reachable, (list, tuple, set, frozenset))
            or any(not isinstance(sha, str) for sha in reachable)
            or len(reachable) != len(set(reachable))
            or (set(commits) | set(unresolved_shas)) != set(reachable)):
        raise ScanError("Resolved and unresolved SHA records do not exactly partition the verified Git set.")
    if (source.get("paginationComplete") is not True or source.get("historyTotalCount") != total_count
            or source.get("gitReachabilityVerified") is not True or source.get("gitReachableCommits") != total_count
            or source.get("unresolvedCommits", unresolved_count) != unresolved_count):
        raise ScanError("Cannot build a snapshot from incomplete history.")
    contributors = apply_uncertainty_bounds(aggregate_contributors(history["commits"]), unresolved_count)
    linked = sum(any(a["user"] is not None for a in c["authors"]) for c in commits.values())
    source.update({"uniqueCommits": total_count, "resolvedCommits": len(commits),
                   "unresolvedCommits": unresolved_count, "unresolvedCommitShas": sorted(unresolved_shas),
                   "authorAttributionComplete": unresolved_count == 0, "linkedCommits": linked,
                   "unlinkedCommits": len(commits) - linked,
                   "commitsWithUnlinkedAuthors": sum(any(a["user"] is None for a in c["authors"]) for c in commits.values()),
                   "unlinkedAuthorAttributions": sum(a["user"] is None for c in commits.values() for a in c["authors"]),
                   "linkedAccountAttributions": sum(c["total_commits"] for c in contributors)})
    target_user = history.get("targetUser") or {}
    target_id = target_user.get("id")
    matches = [c for c in contributors if c["id"] == target_id] if target_id else [c for c in contributors if c["login"].casefold() == target_login.casefold()]
    target = dict(matches[0]) if matches else {"id": target_id, "login": target_user.get("login", target_login),
             "rank": None, "primary_author_commits": 0, "coauthored_commits": 0, "total_commits": 0,
             "total_commits_min": 0, "total_commits_max": unresolved_count,
             "rank_min": None, "rank_max": None, "rank_is_exact": False}
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
            "method": {"name": "custom-primary-plus-coauthor-commit-ranking", "version": 2,
                       "api": API_URL, "authors": "GitHub Commit.authors; first entry is primary",
                       "scope": "All commits reachable from the pinned default-branch head; no history filters",
                       "completeness": "Resolved SHA set and explicitly unresolved SHA set form a disjoint, exact partition of independent Git rev-list",
                       "paginationCompleteMeaning": "All GraphQL history pages and available author connections were fully read; this does not mean all commit author objects were available",
                       "unresolvedCommitRule": "A missing commit is unresolved only when both oid and full-SHA expression lookups return explicit null objects in valid repositories; other errors fail the run",
                       "includesMergeCommits": True, "includesEmptyCommits": True,
                       "linkedBotsIncluded": True, "unlinkedAuthorsIncluded": False,
                       "identity": "GitHub user.id", "deduplication": "One count per (commit SHA, user.id); primary takes precedence",
                       "coauthoredCommits": "Coauthor-only commits; excludes commits also credited as primary",
                       "ranking": "rank is the competition rank of verified known totals, not necessarily the complete rank; display ties by login.casefold(), then user.id",
                       "bounds": "For U unresolved commits, every account has known <= total <= known+U. rank_min=1+count(other known > own known+U); rank_max=1+count(other known+U > own known), or null when own known<U because unseen accounts may outrank it",
                       "unknownsAreNotZero": True,
                       "officialInsightsRanking": False, "attributionCache": False,
                       "unlinkedAuthorNote": "GitActor.user=null may include bot identities. No account is inferred from names or email addresses.",
                       "attributionTiming": "Commit set is pinned; GitHub account associations are observed during this run and may change later.",
                       "documentation": ["https://docs.github.com/en/graphql/reference/commits#commit", "https://docs.github.com/en/graphql/reference/git#gitactor", "https://git-scm.com/docs/git-rev-list"]},
            "source": source, "target": target, "contributors": contributors}


def _rank_message(contributor):
    lower, upper = contributor.get("rank_min"), contributor.get("rank_max")
    if lower is None or upper is None:
        return "unverified"
    return f"#{lower}" if lower == upper else f"#{lower}–{upper}"


def _total_range(contributor):
    lower, upper = contributor["total_commits_min"], contributor["total_commits_max"]
    return f"{lower:,}" if lower == upper else f"{lower:,}–{upper:,}"


def render_markdown(snapshot):
    source, target = snapshot["source"], snapshot["target"]
    repo_url, sha = source["repositoryUrl"], source["headSha"]
    rows = snapshot["contributors"][:100]
    unresolved = source["unresolvedCommits"]
    lines = ["# Hermes Agent contribution audit", "", "This is a **custom primary-plus-coauthor ranking**, not GitHub Insights or the REST contributors ranking.", "",
             f"Generated: {snapshot['generatedAt']}", "",
             f"Source: [{source['repository']}]({repo_url}), default branch `{source['defaultBranch']}`, pinned commit [`{sha}`]({repo_url}/commit/{sha}).", "",
             (f"**Author attribution is incomplete for {unresolved} commits.** Verified totals are lower bounds; unknown contributions have not been assigned to anyone or treated as zero. Complete-count and rank bounds are shown below."
              if unresolved else "Author connections were available for every reachable commit. Counts and ranks are exact under the linked-account method below."), "",
             "## Method", "",
             "- Scan the complete unfiltered history of the pinned default-branch head, including merge and empty commits.",
             "- Read every available GitHub `Commit.authors` connection completely, including nested pagination. The first author is primary; the others are coauthors.",
             "- Independently enumerate the exact reachable commit set with Git. Resolved author records and explicitly unresolved SHAs must form a disjoint, complete partition of that set.",
             "- Classify a missing commit as unresolved only when both object-by-oid and full-SHA expression lookups return explicit null objects in valid repository responses. Other errors still fail the run.",
             "- Group linked accounts by stable GitHub user ID. Count each account once per commit SHA; primary authorship takes precedence over coauthorship.",
             "- Include every linked account, including linked bots. Exclude unlinked authors without guessing identities from names or emails; those unlinked entries may include bots.",
             "- Keep verified totals and their competition ranks (1, 2, 2, 4) for sorting. Display complete-rank bounds; ties in verified totals use case-folded login, then stable user ID.",
             "- Resolve account associations afresh on each run. The commit set is pinned; account associations are observed during the scan and can change later.", "",
             "References: [GitHub Commit.authors and history](https://docs.github.com/en/graphql/reference/commits#commit) · [GitActor.user](https://docs.github.com/en/graphql/reference/git#gitactor) · [generator source](../scripts/update_hermes_contributions.py) · [complete JSON](hermes-contributions.json).", "",
             "## Completeness and attribution", "",
             f"- Completed history pages: {source['historyPages']}; declared history total: {source['historyTotalCount']:,}; independent Git ancestry: {source['gitReachableCommits']:,} commits.",
             f"- Resolved author records: {source['resolvedCommits']:,}; unresolved commit objects: {unresolved:,}. Their disjoint SHA sets exactly cover all {source['uniqueCommits']:,} reachable commits.",
             f"- Initial GraphQL history: {source['graphqlHistoryUniqueCommits']:,} unique commits; duplicate history rows: {source['duplicateCommitRows']:,}; resolved by direct SHA queries: {len(source['recoveredCommitShas']):,}.",
             f"- Among resolved commits only: at least one linked account on {source['linkedCommits']:,}; no linked account on {source['unlinkedCommits']:,}. Unresolved commit objects are not included in either figure.",
             f"- Among resolved commits only: any unlinked author on {source['commitsWithUnlinkedAuthors']:,}; unlinked author entries: {source['unlinkedAuthorAttributions']:,}.",
             f"- Linked account-commit credits: {source['linkedAccountAttributions']:,}; accounts: {len(snapshot['contributors']):,}. A commit credited to multiple accounts contributes once to each account.",
             f"- GraphQL requests: {source.get('queryCount')}; reported query cost: {source.get('queryCost')}; remaining rate-limit points: {source.get('rateLimitRemaining')}.", "",
             "## Uncertainty bounds", "",
             f"There are **U = {unresolved}** unresolved commit objects. Each account's complete total lies between its verified total and that total plus U. An unresolved commit can credit multiple accounts, so it is not allocated as one exclusive credit.", "",
             "The best possible rank is 1 plus the number of other known totals strictly above the account's upper total. The worst possible rank is 1 plus the number of other upper totals strictly above its known total. When the known total is below U, previously unseen accounts may also exceed it; the available evidence provides no finite worst-rank guarantee, shown as `unverified` and `rank_max: null`.", "",
             "A rank is exact only when its lower and upper bounds coincide. Unknown authorship is never interpreted as zero contribution. The JSON `rank` field ranks known credits only; `rank_min`, `rank_max`, and `rank_is_exact` govern the displayed complete rank.", "",
             "Unresolved commit SHAs: " + (", ".join(f"[`{oid}`]({repo_url}/commit/{oid})" for oid in source["unresolvedCommitShas"]) if unresolved else "none") + ".", "",
             f"## {target['login']}", "",
             f"Verified commits: **{target['total_commits']:,}** · verified primary: **{target['primary_author_commits']:,}** · verified coauthor-only: **{target['coauthored_commits']:,}**.", "",
             f"Complete total: **{_total_range(target)}** · complete custom rank: **{_rank_message(target)}** · rank determined: **{'yes' if target['rank_is_exact'] else 'no'}**. Primary/coauthor SHA evidence is retained in the [complete JSON](hermes-contributions.json).", "",
             f"## {'All contributors' if len(snapshot['contributors']) <= 100 else 'First 100 contributor rows'}", "",
             "Rows are ordered by verified totals and include positions 5–20 where present. Row position and the known-credit rank are not substituted for an uncertain complete rank.", "",
             "| Known-credit position | Complete rank | Account | Verified primary | Verified coauthor-only | Complete total |",
             "| ---: | ---: | --- | ---: | ---: | ---: |"]
    lines.extend(f"| {i} | {_rank_message(c)} | [{c['login']}](https://github.com/{c['login']}) | {c['primary_author_commits']:,} | {c['coauthored_commits']:,} | {_total_range(c)} |" for i, c in enumerate(rows, 1))
    return "\n".join(lines) + "\n"


def write_outputs(snapshot, output_dir):
    """Stage all files before replacing; roll back an ordinary replacement error."""
    target = snapshot["target"]
    if target.get("found") is not True or type(target.get("rank")) is not int or target["rank"] < 1:
        raise ScanError("Target account could not be ranked; retaining the previous snapshot and badges.")
    badge = lambda label, message, color: {"schemaVersion": 1, "label": label, "message": message, "color": color, "cacheSeconds": 3600}
    suffix = "+" if snapshot["source"]["unresolvedCommits"] else ""
    payloads = {"hermes-contributions.json": snapshot,
                "hermes-primary-commits.json": badge("PRIMARY", str(target["primary_author_commits"]) + suffix, "38BDF8"),
                "hermes-coauthored-commits.json": badge("CO-AUTHORED", str(target["coauthored_commits"]) + suffix, "D946EF"),
                "hermes-commits.json": badge("COMMITS", str(target["total_commits"]) + suffix, "8B5CF6"),
                "hermes-contributor-rank.json": badge("COMMIT RANK", _rank_message(target), "22c55e")}
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
    parser.add_argument("--checkpoint-path", type=Path, help="Retain incomplete full-scan records at this path for diagnostics.")
    parser.add_argument("--diagnose-only", nargs="+", metavar="SHA", help="Probe specified full SHAs without scanning history or writing badges.")
    args = parser.parse_args(argv)
    try:
        owner, repo = args.repository.split("/")
        if not owner or not repo:
            raise ValueError("Repository must be OWNER/REPO")
        client = GitHubGraphQLClient((os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN") or "").strip(), max_runtime_seconds=args.max_runtime_seconds)
        if args.diagnose_only:
            print(json.dumps({"repository": args.repository, "diagnostics": diagnose_commits(client, owner, repo, args.diagnose_only)}, ensure_ascii=False, indent=2))
            return 0
        history = fetch_history(client, owner, repo, target_login=args.target, checkpoint_path=args.checkpoint_path)
        snapshot = build_snapshot(history, target_login=args.target)
        client.check_deadline()
        write_outputs(snapshot, args.output_dir)
        target = snapshot["target"]
        _progress(f"Published {len(snapshot['contributors'])} accounts; {target['login']}: {target['total_commits']} verified commits, complete custom rank {_rank_message(target)}; unresolved commits={snapshot['source']['unresolvedCommits']}.")
        return 0
    except (ScanError, OSError, ValueError, KeyError, TypeError) as error:
        _progress(f"ERROR: {error}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
