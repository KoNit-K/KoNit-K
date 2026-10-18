# Hermes contribution statistics

For requests about Hermes Agent historical commit totals, KoNit-K's commit badges,
or contributor ranks 5–20, first read
[`docs/hermes-commit-history-prompt.md`](docs/hermes-commit-history-prompt.md).
That file is the reusable task prompt and defines this profile's counting method.

Use `data/hermes-contributions.json` for a dated, audited snapshot. Count each
account once per commit SHA across primary and GitHub-recognized coauthorship,
and apply the same method to every linked account. Inspect author-attribution
completeness and the count/rank bounds before presenting a number as exact.

The updater is `scripts/update_hermes_contributions.py`; the scheduled workflow is
`.github/workflows/hermes-contributor-rank.yml`. Do not replace the inclusive
counts with primary-author-only REST statistics or raw message-search counts.
