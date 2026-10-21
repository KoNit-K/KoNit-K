# Hermes Agent contribution audit

This is a **custom primary-plus-coauthor ranking**, not GitHub Insights or the REST contributors ranking.

Generated: 2026-10-21T09:39:52Z

Source: [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent), default branch `main`, pinned commit [`369cc6b07f26f4454f56555f1001ea9eb7d8d948`](https://github.com/NousResearch/hermes-agent/commit/369cc6b07f26f4454f56555f1001ea9eb7d8d948).

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

- Completed history pages: 575; declared history total: 57,432; independent Git ancestry: 57,432 commits.
- Resolved author records: 57,429; unresolved commit objects: 3. Their disjoint SHA sets exactly cover all 57,432 reachable commits.
- Initial GraphQL history: 57,429 unique commits; duplicate history rows: 3; resolved by direct SHA queries: 0.
- Among resolved commits only: at least one linked account on 56,073; no linked account on 1,356. Unresolved commit objects are not included in either figure.
- Among resolved commits only: any unlinked author on 1,805; unlinked author entries: 1,828.
- Linked account-commit credits: 60,657; accounts: 4,201. A commit credited to multiple accounts contributes once to each account.
- GraphQL requests: 582; reported query cost: 582; remaining rate-limit points: 4488.

## Uncertainty bounds

There are **U = 3** unresolved commit objects. Each account's complete total lies between its verified total and that total plus U. An unresolved commit can credit multiple accounts, so it is not allocated as one exclusive credit.

The best possible rank is 1 plus the number of other known totals strictly above the account's upper total. The worst possible rank is 1 plus the number of other upper totals strictly above its known total. When the known total is below U, previously unseen accounts may also exceed it; the available evidence provides no finite worst-rank guarantee, shown as `unverified` and `rank_max: null`.

A rank is exact only when its lower and upper bounds coincide. Unknown authorship is never interpreted as zero contribution. The JSON `rank` field ranks known credits only; `rank_min`, `rank_max`, and `rank_is_exact` govern the displayed complete rank.

Unresolved commit SHAs: [`722acd66f62f7617a0df3b5af919d257a35fc258`](https://github.com/NousResearch/hermes-agent/commit/722acd66f62f7617a0df3b5af919d257a35fc258), [`8239ec483323d7f447a7fe708d58b77ed405916f`](https://github.com/NousResearch/hermes-agent/commit/8239ec483323d7f447a7fe708d58b77ed405916f), [`aa0beef6848bd9cdcf1a7015cebc8dfc6170cf5b`](https://github.com/NousResearch/hermes-agent/commit/aa0beef6848bd9cdcf1a7015cebc8dfc6170cf5b).

## KoNit-K

Verified commits: **390** · verified primary: **295** · verified coauthor-only: **95**.

Complete total: **390–393** · complete custom rank: **#16** · rank determined: **yes**. Primary/coauthor SHA evidence is retained in the [complete JSON](hermes-contributions.json).

## First 100 contributor rows

Rows are ordered by verified totals and include positions 5–20 where present. Row position and the known-credit rank are not substituted for an uncertain complete rank.

| Known-credit position | Complete rank | Account | Verified primary | Verified coauthor-only | Complete total |
| ---: | ---: | --- | ---: | ---: | ---: |
| 1 | #1 | [teknium1](https://github.com/teknium1) | 23,779 | 77 | 23,856–23,859 |
| 2 | #2 | [kshitijk4poor](https://github.com/kshitijk4poor) | 5,215 | 54 | 5,269–5,272 |
| 3 | #3 | [OutThisLife](https://github.com/OutThisLife) | 4,576 | 30 | 4,606–4,609 |
| 4 | #4 | [ethernet8023](https://github.com/ethernet8023) | 2,319 | 4 | 2,323–2,326 |
| 5 | #5 | [claude](https://github.com/claude) | 5 | 921 | 926–929 |
| 6 | #6 | [alt-glitch](https://github.com/alt-glitch) | 845 | 7 | 852–855 |
| 7 | #7 | [liuhao1024](https://github.com/liuhao1024) | 576 | 112 | 688–691 |
| 8 | #8 | [benbarclay](https://github.com/benbarclay) | 542 | 17 | 559–562 |
| 9 | #9 | [unsupportedpastels](https://github.com/unsupportedpastels) | 534 | 8 | 542–545 |
| 10 | #10 | [austinpickett](https://github.com/austinpickett) | 456 | 12 | 468–471 |
| 11 | #11 | [github-actions[bot]](https://github.com/github-actions[bot]) | 10 | 438 | 448–451 |
| 12 | #12–13 | [JoaoMarcos44](https://github.com/JoaoMarcos44) | 327 | 89 | 416–419 |
| 13 | #12–13 | [fangliquanflq](https://github.com/fangliquanflq) | 360 | 54 | 414–417 |
| 14 | #14–15 | [helix4u](https://github.com/helix4u) | 383 | 20 | 403–406 |
| 15 | #14–15 | [hermes-seaeye[bot]](https://github.com/hermes-seaeye[bot]) | 401 | 1 | 402–405 |
| 16 | #16 | [KoNit-K](https://github.com/KoNit-K) | 295 | 95 | 390–393 |
| 17 | #17 | [jquesnelle](https://github.com/jquesnelle) | 338 | 3 | 341–344 |
| 18 | #18 | [xxxigm](https://github.com/xxxigm) | 298 | 36 | 334–337 |
| 19 | #19 | [jonpol01](https://github.com/jonpol01) | 255 | 28 | 283–286 |
| 20 | #20 | [erosika](https://github.com/erosika) | 256 | 6 | 262–265 |
| 21 | #21 | [yoniebans](https://github.com/yoniebans) | 250 | 2 | 252–255 |
| 22 | #22 | [0xbyt4](https://github.com/0xbyt4) | 201 | 12 | 213–216 |
| 23 | #23 | [HexLab98](https://github.com/HexLab98) | 193 | 13 | 206–209 |
| 24 | #24 | [cursoragent](https://github.com/cursoragent) | 15 | 164 | 179–182 |
| 25 | #25 | [afourniernv](https://github.com/afourniernv) | 171 | 0 | 171–174 |
| 26 | #25–27 | [dokterdok](https://github.com/dokterdok) | 149 | 19 | 168–171 |
| 27 | #26–27 | [kokhlo](https://github.com/kokhlo) | 127 | 39 | 166–169 |
| 28 | #27–28 | [briandevans](https://github.com/briandevans) | 153 | 10 | 163–166 |
| 29 | #29–30 | [Finn763](https://github.com/Finn763) | 122 | 35 | 157–160 |
| 30 | #29–30 | [victor-kyriazakos](https://github.com/victor-kyriazakos) | 149 | 7 | 156–159 |
| 31 | #31–32 | [Adolanium](https://github.com/Adolanium) | 137 | 6 | 143–146 |
| 32 | #31–32 | [dskwe](https://github.com/dskwe) | 116 | 25 | 141–144 |
| 33 | #33–34 | [LeonSGP43](https://github.com/LeonSGP43) | 108 | 28 | 136–139 |
| 34 | #33–34 | [chelsealong](https://github.com/chelsealong) | 120 | 14 | 134–137 |
| 35 | #35 | [DavidMetcalfe](https://github.com/DavidMetcalfe) | 113 | 16 | 129–132 |
| 36 | #36 | [webtecnica](https://github.com/webtecnica) | 85 | 38 | 123–126 |
| 37 | #36–37 | [c2h5oh](https://github.com/c2h5oh) | 120 | 0 | 120–123 |
| 38 | #38 | [Tranquil-Flow](https://github.com/Tranquil-Flow) | 88 | 20 | 108–111 |
| 39 | #39 | [SHL0MS](https://github.com/SHL0MS) | 87 | 11 | 98–101 |
| 40 | #40 | [686f6c61](https://github.com/686f6c61) | 74 | 20 | 94–97 |
| 41 | #40–41 | [Wenfengcheng](https://github.com/Wenfengcheng) | 81 | 10 | 91–94 |
| 42 | #41–42 | [ygd58](https://github.com/ygd58) | 55 | 33 | 88–91 |
| 43 | #42–43 | [itpartypattaya](https://github.com/itpartypattaya) | 85 | 0 | 85–88 |
| 44 | #44 | [shannonsands](https://github.com/shannonsands) | 81 | 0 | 81–84 |
| 45 | #45–46 | [PRATHAMESH75](https://github.com/PRATHAMESH75) | 68 | 8 | 76–79 |
| 46 | #45–48 | [Bartok9](https://github.com/Bartok9) | 61 | 13 | 74–77 |
| 47 | #45–49 | [konsisumer](https://github.com/konsisumer) | 63 | 10 | 73–76 |
| 48 | #46–49 | [beardthelion](https://github.com/beardthelion) | 68 | 4 | 72–75 |
| 49 | #46–49 | [ehz0ah](https://github.com/ehz0ah) | 63 | 8 | 71–74 |
| 50 | #50 | [aydnOktay](https://github.com/aydnOktay) | 45 | 21 | 66–69 |
| 51 | #51–52 | [Halldrix](https://github.com/Halldrix) | 54 | 7 | 61–64 |
| 52 | #51–53 | [apoapostolov](https://github.com/apoapostolov) | 59 | 1 | 60–63 |
| 53 | #51–53 | [100yenadmin](https://github.com/100yenadmin) | 52 | 6 | 58–61 |
| 54 | #54–62 | [AhmetArif0](https://github.com/AhmetArif0) | 52 | 2 | 54–57 |
| 55 | #54–63 | [kvnloo](https://github.com/kvnloo) | 37 | 16 | 53–56 |
| 56 | #54–63 | [salch-cred](https://github.com/salch-cred) | 37 | 16 | 53–56 |
| 57 | #54–63 | [Xipong](https://github.com/Xipong) | 48 | 5 | 53–56 |
| 58 | #54–63 | [bbednarski9](https://github.com/bbednarski9) | 52 | 0 | 52–55 |
| 59 | #54–63 | [capthvnsen](https://github.com/capthvnsen) | 52 | 0 | 52–55 |
| 60 | #54–63 | [frizikk](https://github.com/frizikk) | 46 | 6 | 52–55 |
| 61 | #54–63 | [necoweb3](https://github.com/necoweb3) | 48 | 4 | 52–55 |
| 62 | #54–63 | [TakeshiTGAL](https://github.com/TakeshiTGAL) | 52 | 0 | 52–55 |
| 63 | #54–65 | [entropidelic](https://github.com/entropidelic) | 51 | 0 | 51–54 |
| 64 | #58–66 | [EloquentBrush0x](https://github.com/EloquentBrush0x) | 49 | 0 | 49–52 |
| 65 | #58–66 | [sprmn24](https://github.com/sprmn24) | 42 | 7 | 49–52 |
| 66 | #63–69 | [pierrenode](https://github.com/pierrenode) | 38 | 10 | 48–51 |
| 67 | #64–73 | [embwl0x](https://github.com/embwl0x) | 42 | 4 | 46–49 |
| 68 | #64–73 | [rewbs](https://github.com/rewbs) | 45 | 1 | 46–49 |
| 69 | #64–73 | [whyyagswhy](https://github.com/whyyagswhy) | 35 | 11 | 46–49 |
| 70 | #66–74 | [srojk34](https://github.com/srojk34) | 43 | 2 | 45–48 |
| 71 | #66–74 | [Teknium](https://github.com/Teknium) | 18 | 27 | 45–48 |
| 72 | #67–74 | [Froraut](https://github.com/Froraut) | 28 | 16 | 44–47 |
| 73 | #67–74 | [Frowtek](https://github.com/Frowtek) | 41 | 3 | 44–47 |
| 74 | #67–76 | [nftpoetrist](https://github.com/nftpoetrist) | 36 | 7 | 43–46 |
| 75 | #72–80 | [Sahil-SS9](https://github.com/Sahil-SS9) | 37 | 4 | 41–44 |
| 76 | #72–80 | [wesleysimplicio](https://github.com/wesleysimplicio) | 40 | 1 | 41–44 |
| 77 | #74–83 | [jackulau](https://github.com/jackulau) | 36 | 4 | 40–43 |
| 78 | #74–83 | [rob-maron](https://github.com/rob-maron) | 39 | 1 | 40–43 |
| 79 | #75–86 | [olric3015](https://github.com/olric3015) | 39 | 0 | 39–42 |
| 80 | #75–86 | [Rafa-Ross](https://github.com/Rafa-Ross) | 19 | 20 | 39–42 |
| 81 | #75–88 | [andrexibiza](https://github.com/andrexibiza) | 23 | 15 | 38–41 |
| 82 | #75–88 | [Drexuxux](https://github.com/Drexuxux) | 36 | 2 | 38–41 |
| 83 | #75–88 | [mnajafian-nv](https://github.com/mnajafian-nv) | 37 | 1 | 38–41 |
| 84 | #77–91 | [adybag14-cyber](https://github.com/adybag14-cyber) | 36 | 1 | 37–40 |
| 85 | #77–91 | [ayushnangia](https://github.com/ayushnangia) | 36 | 1 | 37–40 |
| 86 | #77–91 | [itsflownium](https://github.com/itsflownium) | 32 | 5 | 37–40 |
| 87 | #79–93 | [Christopher-Schulze](https://github.com/Christopher-Schulze) | 31 | 5 | 36–39 |
| 88 | #79–93 | [ooiuuii](https://github.com/ooiuuii) | 32 | 4 | 36–39 |
| 89 | #81–95 | [Kyzcreig](https://github.com/Kyzcreig) | 22 | 13 | 35–38 |
| 90 | #81–95 | [MohamadKanso](https://github.com/MohamadKanso) | 21 | 14 | 35–38 |
| 91 | #81–95 | [nousbot-eng](https://github.com/nousbot-eng) | 35 | 0 | 35–38 |
| 92 | #84–97 | [Dusk1e](https://github.com/Dusk1e) | 30 | 4 | 34–37 |
| 93 | #84–97 | [Enough1122](https://github.com/Enough1122) | 26 | 8 | 34–37 |
| 94 | #87–99 | [izumi0uu](https://github.com/izumi0uu) | 24 | 9 | 33–36 |
| 95 | #87–99 | [zapabob](https://github.com/zapabob) | 21 | 12 | 33–36 |
| 96 | #89–104 | [anpicasso](https://github.com/anpicasso) | 24 | 8 | 32–35 |
| 97 | #89–104 | [HenkDz](https://github.com/HenkDz) | 29 | 3 | 32–35 |
| 98 | #92–108 | [notwitcheer](https://github.com/notwitcheer) | 30 | 1 | 31–34 |
| 99 | #92–108 | [pefontana](https://github.com/pefontana) | 30 | 1 | 31–34 |
| 100 | #94–109 | [memosr](https://github.com/memosr) | 19 | 11 | 30–33 |
