# Hermes Agent contribution audit

This is a **custom primary-plus-coauthor ranking**, not GitHub Insights or the REST contributors ranking.

Generated: 2026-11-09T13:22:49Z

Source: [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent), default branch `main`, pinned commit [`34acabf0e681e9432059d1a060c78cc043becc0f`](https://github.com/NousResearch/hermes-agent/commit/34acabf0e681e9432059d1a060c78cc043becc0f).

**Author attribution is incomplete for 3 commits.** Verified totals are lower bounds; unknown contributions have not been assigned to anyone or treated as zero. Complete-count and rank bounds are shown below.

## Method

- Scan the complete unfiltered history of the pinned default-branch head, including merge and empty commits.
- Read every available GitHub `Commit.authors` connection completely, including nested pagination. The first author is primary; the others are coauthors.
- Independently enumerate the exact reachable commit set with Git. Resolved author records and explicitly unresolved SHAs must form a disjoint, complete partition of that set.
- Classify a missing commit as unresolved only when both object-by-oid and full-SHA expression lookups return explicit null objects in valid repository responses. Other errors still fail the run.
- Group linked accounts by stable GitHub user ID. Count each account once per commit SHA; primary authorship takes precedence over coauthorship.
- Include every linked account, including linked bots. Exclude unlinked authors without guessing identities from names or emails; those unlinked entries may include bots.
- Keep verified totals and their competition ranks (1, 2, 2, 4) for sorting. Display complete-rank bounds; ties in verified totals use case-folded login, then stable user ID.
- Resolve account associations afresh on each run. The commit set is pinned; account associations are observed during the scan and can change later.

References: [GitHub Commit.authors and history](https://docs.github.com/en/graphql/reference/commits#commit) · [GitActor.user](https://docs.github.com/en/graphql/reference/git#gitactor) · [generator source](../scripts/update_hermes_contributions.py) · [complete JSON](hermes-contributions.json).

## Completeness and attribution

- Completed history pages: 650; declared history total: 64,988; independent Git ancestry: 64,988 commits.
- Resolved author records: 64,985; unresolved commit objects: 3. Their disjoint SHA sets exactly cover all 64,988 reachable commits.
- Initial GraphQL history: 64,985 unique commits; duplicate history rows: 3; resolved by direct SHA queries: 0.
- Among resolved commits only: at least one linked account on 63,478; no linked account on 1,507. Unresolved commit objects are not included in either figure.
- Among resolved commits only: any unlinked author on 1,989; unlinked author entries: 2,012.
- Linked account-commit credits: 68,491; accounts: 4,717. A commit credited to multiple accounts contributes once to each account.
- GraphQL requests: 657; reported query cost: 657; remaining rate-limit points: 4504.

## Uncertainty bounds

There are **U = 3** unresolved commit objects. Each account's complete total lies between its verified total and that total plus U. An unresolved commit can credit multiple accounts, so it is not allocated as one exclusive credit.

The best possible rank is 1 plus the number of other known totals strictly above the account's upper total. The worst possible rank is 1 plus the number of other upper totals strictly above its known total. When the known total is below U, previously unseen accounts may also exceed it; the available evidence provides no finite worst-rank guarantee, shown as `unverified` and `rank_max: null`.

A rank is exact only when its lower and upper bounds coincide. Unknown authorship is never interpreted as zero contribution. The JSON `rank` field ranks known credits only; `rank_min`, `rank_max`, and `rank_is_exact` govern the displayed complete rank.

Unresolved commit SHAs: [`722acd66f62f7617a0df3b5af919d257a35fc258`](https://github.com/NousResearch/hermes-agent/commit/722acd66f62f7617a0df3b5af919d257a35fc258), [`8239ec483323d7f447a7fe708d58b77ed405916f`](https://github.com/NousResearch/hermes-agent/commit/8239ec483323d7f447a7fe708d58b77ed405916f), [`aa0beef6848bd9cdcf1a7015cebc8dfc6170cf5b`](https://github.com/NousResearch/hermes-agent/commit/aa0beef6848bd9cdcf1a7015cebc8dfc6170cf5b).

## KoNit-K

Verified commits: **403** · verified primary: **307** · verified coauthor-only: **96**.

Complete total: **403–406** · complete custom rank: **#17–18** · rank determined: **no**. Primary/coauthor SHA evidence is retained in the [complete JSON](hermes-contributions.json).

## First 100 contributor rows

Rows are ordered by verified totals and include positions 5–20 where present. Row position and the known-credit rank are not substituted for an uncertain complete rank.

| Known-credit position | Complete rank | Account | Verified primary | Verified coauthor-only | Complete total |
| ---: | ---: | --- | ---: | ---: | ---: |
| 1 | #1 | [teknium1](https://github.com/teknium1) | 26,970 | 82 | 27,052–27,055 |
| 2 | #2 | [kshitijk4poor](https://github.com/kshitijk4poor) | 5,631 | 55 | 5,686–5,689 |
| 3 | #3 | [OutThisLife](https://github.com/OutThisLife) | 4,580 | 31 | 4,611–4,614 |
| 4 | #4 | [ethernet8023](https://github.com/ethernet8023) | 2,367 | 4 | 2,371–2,374 |
| 5 | #5 | [claude](https://github.com/claude) | 13 | 1,130 | 1,143–1,146 |
| 6 | #6 | [unsupportedpastels](https://github.com/unsupportedpastels) | 1,049 | 15 | 1,064–1,067 |
| 7 | #7 | [alt-glitch](https://github.com/alt-glitch) | 1,048 | 9 | 1,057–1,060 |
| 8 | #8 | [liuhao1024](https://github.com/liuhao1024) | 601 | 125 | 726–729 |
| 9 | #9 | [benbarclay](https://github.com/benbarclay) | 616 | 18 | 634–637 |
| 10 | #10 | [jquesnelle](https://github.com/jquesnelle) | 513 | 7 | 520–523 |
| 11 | #11 | [austinpickett](https://github.com/austinpickett) | 480 | 12 | 492–495 |
| 12 | #12 | [c2h5oh](https://github.com/c2h5oh) | 464 | 0 | 464–467 |
| 13 | #13 | [github-actions[bot]](https://github.com/github-actions[bot]) | 10 | 438 | 448–451 |
| 14 | #14 | [helix4u](https://github.com/helix4u) | 405 | 22 | 427–430 |
| 15 | #15 | [fangliquanflq](https://github.com/fangliquanflq) | 365 | 56 | 421–424 |
| 16 | #16 | [JoaoMarcos44](https://github.com/JoaoMarcos44) | 327 | 89 | 416–419 |
| 17 | #17–18 | [KoNit-K](https://github.com/KoNit-K) | 307 | 96 | 403–406 |
| 18 | #17–18 | [hermes-seaeye[bot]](https://github.com/hermes-seaeye[bot]) | 401 | 1 | 402–405 |
| 19 | #19 | [xxxigm](https://github.com/xxxigm) | 313 | 38 | 351–354 |
| 20 | #20 | [yoniebans](https://github.com/yoniebans) | 297 | 4 | 301–304 |
| 21 | #20–21 | [jonpol01](https://github.com/jonpol01) | 267 | 31 | 298–301 |
| 22 | #22 | [erosika](https://github.com/erosika) | 256 | 6 | 262–265 |
| 23 | #23 | [dokterdok](https://github.com/dokterdok) | 237 | 19 | 256–259 |
| 24 | #24 | [0xbyt4](https://github.com/0xbyt4) | 203 | 12 | 215–218 |
| 25 | #24–25 | [BearHuddleston](https://github.com/BearHuddleston) | 125 | 87 | 212–215 |
| 26 | #26–27 | [HexLab98](https://github.com/HexLab98) | 193 | 13 | 206–209 |
| 27 | #26–27 | [Adolanium](https://github.com/Adolanium) | 198 | 7 | 205–208 |
| 28 | #28 | [cursoragent](https://github.com/cursoragent) | 23 | 165 | 188–191 |
| 29 | #29 | [victor-kyriazakos](https://github.com/victor-kyriazakos) | 173 | 7 | 180–183 |
| 30 | #30–31 | [afourniernv](https://github.com/afourniernv) | 171 | 0 | 171–174 |
| 31 | #30–31 | [kokhlo](https://github.com/kokhlo) | 131 | 40 | 171–174 |
| 32 | #32 | [briandevans](https://github.com/briandevans) | 155 | 10 | 165–168 |
| 33 | #33 | [Finn763](https://github.com/Finn763) | 122 | 35 | 157–160 |
| 34 | #34 | [dskwe](https://github.com/dskwe) | 126 | 27 | 153–156 |
| 35 | #35 | [itpartypattaya](https://github.com/itpartypattaya) | 142 | 0 | 142–145 |
| 36 | #36–37 | [LeonSGP43](https://github.com/LeonSGP43) | 108 | 29 | 137–140 |
| 37 | #36–37 | [chelsealong](https://github.com/chelsealong) | 121 | 15 | 136–139 |
| 38 | #38 | [DavidMetcalfe](https://github.com/DavidMetcalfe) | 113 | 17 | 130–133 |
| 39 | #39 | [webtecnica](https://github.com/webtecnica) | 87 | 38 | 125–128 |
| 40 | #40 | [Tranquil-Flow](https://github.com/Tranquil-Flow) | 89 | 21 | 110–113 |
| 41 | #41 | [SHL0MS](https://github.com/SHL0MS) | 95 | 11 | 106–109 |
| 42 | #42 | [686f6c61](https://github.com/686f6c61) | 80 | 20 | 100–103 |
| 43 | #43–44 | [Wenfengcheng](https://github.com/Wenfengcheng) | 81 | 10 | 91–94 |
| 44 | #43–44 | [ygd58](https://github.com/ygd58) | 57 | 33 | 90–93 |
| 45 | #45–46 | [shannonsands](https://github.com/shannonsands) | 82 | 0 | 82–85 |
| 46 | #45–48 | [apoapostolov](https://github.com/apoapostolov) | 79 | 1 | 80–83 |
| 47 | #46–48 | [PRATHAMESH75](https://github.com/PRATHAMESH75) | 70 | 8 | 78–81 |
| 48 | #46–48 | [TakeshiTGAL](https://github.com/TakeshiTGAL) | 78 | 0 | 78–81 |
| 49 | #49–52 | [Bartok9](https://github.com/Bartok9) | 61 | 13 | 74–77 |
| 50 | #49–53 | [beardthelion](https://github.com/beardthelion) | 69 | 4 | 73–76 |
| 51 | #49–53 | [konsisumer](https://github.com/konsisumer) | 63 | 10 | 73–76 |
| 52 | #49–53 | [100yenadmin](https://github.com/100yenadmin) | 66 | 6 | 72–75 |
| 53 | #49–53 | [ehz0ah](https://github.com/ehz0ah) | 63 | 8 | 71–74 |
| 54 | #54 | [aydnOktay](https://github.com/aydnOktay) | 45 | 21 | 66–69 |
| 55 | #55–56 | [Halldrix](https://github.com/Halldrix) | 54 | 8 | 62–65 |
| 56 | #55–57 | [Sahil-SS9](https://github.com/Sahil-SS9) | 53 | 7 | 60–63 |
| 57 | #56–58 | [kvnloo](https://github.com/kvnloo) | 42 | 16 | 58–61 |
| 58 | #57–61 | [salch-cred](https://github.com/salch-cred) | 40 | 16 | 56–59 |
| 59 | #58–66 | [AhmetArif0](https://github.com/AhmetArif0) | 52 | 2 | 54–57 |
| 60 | #58–66 | [capthvnsen](https://github.com/capthvnsen) | 54 | 0 | 54–57 |
| 61 | #58–66 | [dyiapanis](https://github.com/dyiapanis) | 54 | 0 | 54–57 |
| 62 | #58–68 | [Froraut](https://github.com/Froraut) | 35 | 18 | 53–56 |
| 63 | #58–68 | [Xipong](https://github.com/Xipong) | 48 | 5 | 53–56 |
| 64 | #59–68 | [bbednarski9](https://github.com/bbednarski9) | 52 | 0 | 52–55 |
| 65 | #59–68 | [frizikk](https://github.com/frizikk) | 46 | 6 | 52–55 |
| 66 | #59–68 | [necoweb3](https://github.com/necoweb3) | 48 | 4 | 52–55 |
| 67 | #59–71 | [entropidelic](https://github.com/entropidelic) | 51 | 0 | 51–54 |
| 68 | #59–71 | [olric3015](https://github.com/olric3015) | 51 | 0 | 51–54 |
| 69 | #64–74 | [EloquentBrush0x](https://github.com/EloquentBrush0x) | 49 | 0 | 49–52 |
| 70 | #64–74 | [pierrenode](https://github.com/pierrenode) | 38 | 11 | 49–52 |
| 71 | #64–74 | [sprmn24](https://github.com/sprmn24) | 42 | 7 | 49–52 |
| 72 | #69–78 | [embwl0x](https://github.com/embwl0x) | 42 | 5 | 47–50 |
| 73 | #69–78 | [itsflownium](https://github.com/itsflownium) | 39 | 8 | 47–50 |
| 74 | #69–78 | [rewbs](https://github.com/rewbs) | 46 | 1 | 47–50 |
| 75 | #69–79 | [rob-maron](https://github.com/rob-maron) | 45 | 1 | 46–49 |
| 76 | #69–79 | [whyyagswhy](https://github.com/whyyagswhy) | 35 | 11 | 46–49 |
| 77 | #72–80 | [srojk34](https://github.com/srojk34) | 43 | 2 | 45–48 |
| 78 | #72–80 | [Teknium](https://github.com/Teknium) | 18 | 27 | 45–48 |
| 79 | #72–80 | [Frowtek](https://github.com/Frowtek) | 41 | 3 | 44–47 |
| 80 | #75–81 | [nftpoetrist](https://github.com/nftpoetrist) | 36 | 7 | 43–46 |
| 81 | #79–84 | [wesleysimplicio](https://github.com/wesleysimplicio) | 40 | 1 | 41–44 |
| 82 | #80–86 | [jackulau](https://github.com/jackulau) | 36 | 4 | 40–43 |
| 83 | #81–88 | [mnajafian-nv](https://github.com/mnajafian-nv) | 38 | 1 | 39–42 |
| 84 | #81–88 | [Rafa-Ross](https://github.com/Rafa-Ross) | 19 | 20 | 39–42 |
| 85 | #81–91 | [andrexibiza](https://github.com/andrexibiza) | 23 | 15 | 38–41 |
| 86 | #81–91 | [Drexuxux](https://github.com/Drexuxux) | 36 | 2 | 38–41 |
| 87 | #82–94 | [adybag14-cyber](https://github.com/adybag14-cyber) | 36 | 1 | 37–40 |
| 88 | #82–94 | [ayushnangia](https://github.com/ayushnangia) | 36 | 1 | 37–40 |
| 89 | #83–98 | [Christopher-Schulze](https://github.com/Christopher-Schulze) | 31 | 5 | 36–39 |
| 90 | #83–98 | [ooiuuii](https://github.com/ooiuuii) | 32 | 4 | 36–39 |
| 91 | #83–98 | [r266-tech](https://github.com/r266-tech) | 33 | 3 | 36–39 |
| 92 | #85–101 | [Kyzcreig](https://github.com/Kyzcreig) | 22 | 13 | 35–38 |
| 93 | #85–101 | [MohamadKanso](https://github.com/MohamadKanso) | 21 | 14 | 35–38 |
| 94 | #85–101 | [nousbot-eng](https://github.com/nousbot-eng) | 35 | 0 | 35–38 |
| 95 | #87–103 | [anpicasso](https://github.com/anpicasso) | 26 | 8 | 34–37 |
| 96 | #87–103 | [Dusk1e](https://github.com/Dusk1e) | 30 | 4 | 34–37 |
| 97 | #87–103 | [Enough1122](https://github.com/Enough1122) | 26 | 8 | 34–37 |
| 98 | #87–103 | [GottZ](https://github.com/GottZ) | 32 | 2 | 34–37 |
| 99 | #89–106 | [IAvecilla](https://github.com/IAvecilla) | 31 | 2 | 33–36 |
| 100 | #89–106 | [izumi0uu](https://github.com/izumi0uu) | 24 | 9 | 33–36 |
