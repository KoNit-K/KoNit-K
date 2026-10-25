# Hermes Agent contribution audit

This is a **custom primary-plus-coauthor ranking**, not GitHub Insights or the REST contributors ranking.

Generated: 2026-10-25T09:26:12Z

Source: [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent), default branch `main`, pinned commit [`4ea8d23cc9f527332ccb1d55359b27741b6ea51b`](https://github.com/NousResearch/hermes-agent/commit/4ea8d23cc9f527332ccb1d55359b27741b6ea51b).

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

- Completed history pages: 586; declared history total: 58,529; independent Git ancestry: 58,529 commits.
- Resolved author records: 58,526; unresolved commit objects: 3. Their disjoint SHA sets exactly cover all 58,529 reachable commits.
- Initial GraphQL history: 58,526 unique commits; duplicate history rows: 3; resolved by direct SHA queries: 0.
- Among resolved commits only: at least one linked account on 57,167; no linked account on 1,359. Unresolved commit objects are not included in either figure.
- Among resolved commits only: any unlinked author on 1,811; unlinked author entries: 1,834.
- Linked account-commit credits: 61,795; accounts: 4,269. A commit credited to multiple accounts contributes once to each account.
- GraphQL requests: 593; reported query cost: 593; remaining rate-limit points: 4554.

## Uncertainty bounds

There are **U = 3** unresolved commit objects. Each account's complete total lies between its verified total and that total plus U. An unresolved commit can credit multiple accounts, so it is not allocated as one exclusive credit.

The best possible rank is 1 plus the number of other known totals strictly above the account's upper total. The worst possible rank is 1 plus the number of other upper totals strictly above its known total. When the known total is below U, previously unseen accounts may also exceed it; the available evidence provides no finite worst-rank guarantee, shown as `unverified` and `rank_max: null`.

A rank is exact only when its lower and upper bounds coincide. Unknown authorship is never interpreted as zero contribution. The JSON `rank` field ranks known credits only; `rank_min`, `rank_max`, and `rank_is_exact` govern the displayed complete rank.

Unresolved commit SHAs: [`722acd66f62f7617a0df3b5af919d257a35fc258`](https://github.com/NousResearch/hermes-agent/commit/722acd66f62f7617a0df3b5af919d257a35fc258), [`8239ec483323d7f447a7fe708d58b77ed405916f`](https://github.com/NousResearch/hermes-agent/commit/8239ec483323d7f447a7fe708d58b77ed405916f), [`aa0beef6848bd9cdcf1a7015cebc8dfc6170cf5b`](https://github.com/NousResearch/hermes-agent/commit/aa0beef6848bd9cdcf1a7015cebc8dfc6170cf5b).

## KoNit-K

Verified commits: **391** · verified primary: **295** · verified coauthor-only: **96**.

Complete total: **391–394** · complete custom rank: **#16** · rank determined: **yes**. Primary/coauthor SHA evidence is retained in the [complete JSON](hermes-contributions.json).

## First 100 contributor rows

Rows are ordered by verified totals and include positions 5–20 where present. Row position and the known-credit rank are not substituted for an uncertain complete rank.

| Known-credit position | Complete rank | Account | Verified primary | Verified coauthor-only | Complete total |
| ---: | ---: | --- | ---: | ---: | ---: |
| 1 | #1 | [teknium1](https://github.com/teknium1) | 24,337 | 78 | 24,415–24,418 |
| 2 | #2 | [kshitijk4poor](https://github.com/kshitijk4poor) | 5,216 | 54 | 5,270–5,273 |
| 3 | #3 | [OutThisLife](https://github.com/OutThisLife) | 4,578 | 31 | 4,609–4,612 |
| 4 | #4 | [ethernet8023](https://github.com/ethernet8023) | 2,356 | 4 | 2,360–2,363 |
| 5 | #5 | [claude](https://github.com/claude) | 6 | 940 | 946–949 |
| 6 | #6 | [alt-glitch](https://github.com/alt-glitch) | 891 | 7 | 898–901 |
| 7 | #7 | [liuhao1024](https://github.com/liuhao1024) | 578 | 114 | 692–695 |
| 8 | #8 | [benbarclay](https://github.com/benbarclay) | 545 | 17 | 562–565 |
| 9 | #9 | [unsupportedpastels](https://github.com/unsupportedpastels) | 537 | 12 | 549–552 |
| 10 | #10 | [austinpickett](https://github.com/austinpickett) | 460 | 12 | 472–475 |
| 11 | #11 | [github-actions[bot]](https://github.com/github-actions[bot]) | 10 | 438 | 448–451 |
| 12 | #12–13 | [fangliquanflq](https://github.com/fangliquanflq) | 363 | 55 | 418–421 |
| 13 | #12–13 | [JoaoMarcos44](https://github.com/JoaoMarcos44) | 327 | 89 | 416–419 |
| 14 | #14 | [helix4u](https://github.com/helix4u) | 385 | 20 | 405–408 |
| 15 | #14–15 | [hermes-seaeye[bot]](https://github.com/hermes-seaeye[bot]) | 401 | 1 | 402–405 |
| 16 | #16 | [KoNit-K](https://github.com/KoNit-K) | 295 | 96 | 391–394 |
| 17 | #17 | [jquesnelle](https://github.com/jquesnelle) | 355 | 3 | 358–361 |
| 18 | #18 | [xxxigm](https://github.com/xxxigm) | 298 | 36 | 334–337 |
| 19 | #19 | [jonpol01](https://github.com/jonpol01) | 256 | 29 | 285–288 |
| 20 | #20 | [yoniebans](https://github.com/yoniebans) | 276 | 2 | 278–281 |
| 21 | #21 | [erosika](https://github.com/erosika) | 256 | 6 | 262–265 |
| 22 | #22 | [c2h5oh](https://github.com/c2h5oh) | 225 | 0 | 225–228 |
| 23 | #23 | [0xbyt4](https://github.com/0xbyt4) | 201 | 12 | 213–216 |
| 24 | #24 | [HexLab98](https://github.com/HexLab98) | 193 | 13 | 206–209 |
| 25 | #25 | [cursoragent](https://github.com/cursoragent) | 15 | 165 | 180–183 |
| 26 | #26 | [afourniernv](https://github.com/afourniernv) | 171 | 0 | 171–174 |
| 27 | #26–28 | [dokterdok](https://github.com/dokterdok) | 149 | 19 | 168–171 |
| 28 | #27–28 | [kokhlo](https://github.com/kokhlo) | 127 | 39 | 166–169 |
| 29 | #28–29 | [briandevans](https://github.com/briandevans) | 153 | 10 | 163–166 |
| 30 | #30–32 | [Finn763](https://github.com/Finn763) | 122 | 35 | 157–160 |
| 31 | #30–32 | [Adolanium](https://github.com/Adolanium) | 150 | 6 | 156–159 |
| 32 | #30–32 | [victor-kyriazakos](https://github.com/victor-kyriazakos) | 149 | 7 | 156–159 |
| 33 | #33 | [dskwe](https://github.com/dskwe) | 118 | 25 | 143–146 |
| 34 | #34–35 | [LeonSGP43](https://github.com/LeonSGP43) | 108 | 28 | 136–139 |
| 35 | #34–35 | [chelsealong](https://github.com/chelsealong) | 120 | 15 | 135–138 |
| 36 | #36 | [DavidMetcalfe](https://github.com/DavidMetcalfe) | 113 | 17 | 130–133 |
| 37 | #37 | [webtecnica](https://github.com/webtecnica) | 85 | 38 | 123–126 |
| 38 | #38 | [Tranquil-Flow](https://github.com/Tranquil-Flow) | 88 | 20 | 108–111 |
| 39 | #39–40 | [SHL0MS](https://github.com/SHL0MS) | 87 | 11 | 98–101 |
| 40 | #39–41 | [itpartypattaya](https://github.com/itpartypattaya) | 96 | 0 | 96–99 |
| 41 | #39–41 | [686f6c61](https://github.com/686f6c61) | 75 | 20 | 95–98 |
| 42 | #42 | [Wenfengcheng](https://github.com/Wenfengcheng) | 81 | 10 | 91–94 |
| 43 | #42–43 | [ygd58](https://github.com/ygd58) | 55 | 33 | 88–91 |
| 44 | #44 | [shannonsands](https://github.com/shannonsands) | 81 | 0 | 81–84 |
| 45 | #45–46 | [PRATHAMESH75](https://github.com/PRATHAMESH75) | 68 | 8 | 76–79 |
| 46 | #45–48 | [Bartok9](https://github.com/Bartok9) | 61 | 13 | 74–77 |
| 47 | #45–49 | [konsisumer](https://github.com/konsisumer) | 63 | 10 | 73–76 |
| 48 | #46–49 | [beardthelion](https://github.com/beardthelion) | 68 | 4 | 72–75 |
| 49 | #46–49 | [ehz0ah](https://github.com/ehz0ah) | 63 | 8 | 71–74 |
| 50 | #50–51 | [apoapostolov](https://github.com/apoapostolov) | 65 | 1 | 66–69 |
| 51 | #50–51 | [aydnOktay](https://github.com/aydnOktay) | 45 | 21 | 66–69 |
| 52 | #52–53 | [Halldrix](https://github.com/Halldrix) | 54 | 7 | 61–64 |
| 53 | #52–54 | [100yenadmin](https://github.com/100yenadmin) | 53 | 6 | 59–62 |
| 54 | #53–54 | [TakeshiTGAL](https://github.com/TakeshiTGAL) | 57 | 0 | 57–60 |
| 55 | #54–62 | [AhmetArif0](https://github.com/AhmetArif0) | 52 | 2 | 54–57 |
| 56 | #54–62 | [capthvnsen](https://github.com/capthvnsen) | 54 | 0 | 54–57 |
| 57 | #55–63 | [kvnloo](https://github.com/kvnloo) | 37 | 16 | 53–56 |
| 58 | #55–63 | [salch-cred](https://github.com/salch-cred) | 37 | 16 | 53–56 |
| 59 | #55–63 | [Xipong](https://github.com/Xipong) | 48 | 5 | 53–56 |
| 60 | #55–63 | [bbednarski9](https://github.com/bbednarski9) | 52 | 0 | 52–55 |
| 61 | #55–63 | [frizikk](https://github.com/frizikk) | 46 | 6 | 52–55 |
| 62 | #55–63 | [necoweb3](https://github.com/necoweb3) | 48 | 4 | 52–55 |
| 63 | #55–65 | [entropidelic](https://github.com/entropidelic) | 51 | 0 | 51–54 |
| 64 | #60–66 | [EloquentBrush0x](https://github.com/EloquentBrush0x) | 49 | 0 | 49–52 |
| 65 | #60–66 | [sprmn24](https://github.com/sprmn24) | 42 | 7 | 49–52 |
| 66 | #63–69 | [pierrenode](https://github.com/pierrenode) | 38 | 10 | 48–51 |
| 67 | #64–75 | [embwl0x](https://github.com/embwl0x) | 42 | 4 | 46–49 |
| 68 | #64–75 | [rewbs](https://github.com/rewbs) | 45 | 1 | 46–49 |
| 69 | #64–75 | [whyyagswhy](https://github.com/whyyagswhy) | 35 | 11 | 46–49 |
| 70 | #66–76 | [olric3015](https://github.com/olric3015) | 45 | 0 | 45–48 |
| 71 | #66–76 | [rob-maron](https://github.com/rob-maron) | 44 | 1 | 45–48 |
| 72 | #66–76 | [srojk34](https://github.com/srojk34) | 43 | 2 | 45–48 |
| 73 | #66–76 | [Teknium](https://github.com/Teknium) | 18 | 27 | 45–48 |
| 74 | #67–77 | [Froraut](https://github.com/Froraut) | 28 | 16 | 44–47 |
| 75 | #67–77 | [Frowtek](https://github.com/Frowtek) | 41 | 3 | 44–47 |
| 76 | #67–78 | [nftpoetrist](https://github.com/nftpoetrist) | 36 | 7 | 43–46 |
| 77 | #70–79 | [Sahil-SS9](https://github.com/Sahil-SS9) | 38 | 4 | 42–45 |
| 78 | #74–80 | [wesleysimplicio](https://github.com/wesleysimplicio) | 40 | 1 | 41–44 |
| 79 | #76–83 | [jackulau](https://github.com/jackulau) | 36 | 4 | 40–43 |
| 80 | #77–86 | [Rafa-Ross](https://github.com/Rafa-Ross) | 19 | 20 | 39–42 |
| 81 | #78–88 | [andrexibiza](https://github.com/andrexibiza) | 23 | 15 | 38–41 |
| 82 | #78–88 | [Drexuxux](https://github.com/Drexuxux) | 36 | 2 | 38–41 |
| 83 | #78–88 | [mnajafian-nv](https://github.com/mnajafian-nv) | 37 | 1 | 38–41 |
| 84 | #79–91 | [adybag14-cyber](https://github.com/adybag14-cyber) | 36 | 1 | 37–40 |
| 85 | #79–91 | [ayushnangia](https://github.com/ayushnangia) | 36 | 1 | 37–40 |
| 86 | #79–91 | [itsflownium](https://github.com/itsflownium) | 32 | 5 | 37–40 |
| 87 | #80–94 | [Christopher-Schulze](https://github.com/Christopher-Schulze) | 31 | 5 | 36–39 |
| 88 | #80–94 | [ooiuuii](https://github.com/ooiuuii) | 32 | 4 | 36–39 |
| 89 | #81–96 | [Kyzcreig](https://github.com/Kyzcreig) | 22 | 13 | 35–38 |
| 90 | #81–96 | [MohamadKanso](https://github.com/MohamadKanso) | 21 | 14 | 35–38 |
| 91 | #81–96 | [nousbot-eng](https://github.com/nousbot-eng) | 35 | 0 | 35–38 |
| 92 | #84–97 | [anpicasso](https://github.com/anpicasso) | 26 | 8 | 34–37 |
| 93 | #84–97 | [Dusk1e](https://github.com/Dusk1e) | 30 | 4 | 34–37 |
| 94 | #84–97 | [Enough1122](https://github.com/Enough1122) | 26 | 8 | 34–37 |
| 95 | #87–99 | [izumi0uu](https://github.com/izumi0uu) | 24 | 9 | 33–36 |
| 96 | #87–99 | [zapabob](https://github.com/zapabob) | 21 | 12 | 33–36 |
| 97 | #89–105 | [HenkDz](https://github.com/HenkDz) | 29 | 3 | 32–35 |
| 98 | #92–108 | [notwitcheer](https://github.com/notwitcheer) | 30 | 1 | 31–34 |
| 99 | #92–108 | [pefontana](https://github.com/pefontana) | 30 | 1 | 31–34 |
| 100 | #95–109 | [memosr](https://github.com/memosr) | 19 | 11 | 30–33 |
