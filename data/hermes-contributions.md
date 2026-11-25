# Hermes Agent contribution audit

This is a **custom primary-plus-coauthor ranking**, not GitHub Insights or the REST contributors ranking.

Generated: 2026-11-25T15:00:13Z

Source: [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent), default branch `main`, pinned commit [`f681186ea35e212c575a13d056ef241bfabe6190`](https://github.com/NousResearch/hermes-agent/commit/f681186ea35e212c575a13d056ef241bfabe6190).

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

- Completed history pages: 767; declared history total: 76,678; independent Git ancestry: 76,678 commits.
- Resolved author records: 76,675; unresolved commit objects: 3. Their disjoint SHA sets exactly cover all 76,678 reachable commits.
- Initial GraphQL history: 76,675 unique commits; duplicate history rows: 3; resolved by direct SHA queries: 0.
- Among resolved commits only: at least one linked account on 75,143; no linked account on 1,532. Unresolved commit objects are not included in either figure.
- Among resolved commits only: any unlinked author on 2,027; unlinked author entries: 2,050.
- Linked account-commit credits: 81,296; accounts: 5,736. A commit credited to multiple accounts contributes once to each account.
- GraphQL requests: 774; reported query cost: 774; remaining rate-limit points: 4423.

## Uncertainty bounds

There are **U = 3** unresolved commit objects. Each account's complete total lies between its verified total and that total plus U. An unresolved commit can credit multiple accounts, so it is not allocated as one exclusive credit.

The best possible rank is 1 plus the number of other known totals strictly above the account's upper total. The worst possible rank is 1 plus the number of other upper totals strictly above its known total. When the known total is below U, previously unseen accounts may also exceed it; the available evidence provides no finite worst-rank guarantee, shown as `unverified` and `rank_max: null`.

A rank is exact only when its lower and upper bounds coincide. Unknown authorship is never interpreted as zero contribution. The JSON `rank` field ranks known credits only; `rank_min`, `rank_max`, and `rank_is_exact` govern the displayed complete rank.

Unresolved commit SHAs: [`722acd66f62f7617a0df3b5af919d257a35fc258`](https://github.com/NousResearch/hermes-agent/commit/722acd66f62f7617a0df3b5af919d257a35fc258), [`8239ec483323d7f447a7fe708d58b77ed405916f`](https://github.com/NousResearch/hermes-agent/commit/8239ec483323d7f447a7fe708d58b77ed405916f), [`aa0beef6848bd9cdcf1a7015cebc8dfc6170cf5b`](https://github.com/NousResearch/hermes-agent/commit/aa0beef6848bd9cdcf1a7015cebc8dfc6170cf5b).

## KoNit-K

Verified commits: **414** · verified primary: **317** · verified coauthor-only: **97**.

Complete total: **414–417** · complete custom rank: **#19** · rank determined: **yes**. Primary/coauthor SHA evidence is retained in the [complete JSON](hermes-contributions.json).

## First 100 contributor rows

Rows are ordered by verified totals and include positions 5–20 where present. Row position and the known-credit rank are not substituted for an uncertain complete rank.

| Known-credit position | Complete rank | Account | Verified primary | Verified coauthor-only | Complete total |
| ---: | ---: | --- | ---: | ---: | ---: |
| 1 | #1 | [teknium1](https://github.com/teknium1) | 30,017 | 95 | 30,112–30,115 |
| 2 | #2 | [kshitijk4poor](https://github.com/kshitijk4poor) | 5,901 | 64 | 5,965–5,968 |
| 3 | #3 | [OutThisLife](https://github.com/OutThisLife) | 4,582 | 31 | 4,613–4,616 |
| 4 | #4 | [ethernet8023](https://github.com/ethernet8023) | 2,385 | 4 | 2,389–2,392 |
| 5 | #5 | [c2h5oh](https://github.com/c2h5oh) | 1,916 | 0 | 1,916–1,919 |
| 6 | #6 | [claude](https://github.com/claude) | 31 | 1,556 | 1,587–1,590 |
| 7 | #7 | [unsupportedpastels](https://github.com/unsupportedpastels) | 1,467 | 45 | 1,512–1,515 |
| 8 | #8 | [alt-glitch](https://github.com/alt-glitch) | 1,313 | 9 | 1,322–1,325 |
| 9 | #9 | [BearHuddleston](https://github.com/BearHuddleston) | 484 | 551 | 1,035–1,038 |
| 10 | #10 | [liuhao1024](https://github.com/liuhao1024) | 661 | 144 | 805–808 |
| 11 | #11 | [benbarclay](https://github.com/benbarclay) | 666 | 18 | 684–687 |
| 12 | #12 | [yoniebans](https://github.com/yoniebans) | 659 | 5 | 664–667 |
| 13 | #13 | [jquesnelle](https://github.com/jquesnelle) | 575 | 7 | 582–585 |
| 14 | #14 | [austinpickett](https://github.com/austinpickett) | 503 | 13 | 516–519 |
| 15 | #15 | [github-actions[bot]](https://github.com/github-actions[bot]) | 12 | 438 | 450–453 |
| 16 | #16 | [helix4u](https://github.com/helix4u) | 420 | 22 | 442–445 |
| 17 | #17 | [fangliquanflq](https://github.com/fangliquanflq) | 370 | 62 | 432–435 |
| 18 | #18 | [JoaoMarcos44](https://github.com/JoaoMarcos44) | 329 | 92 | 421–424 |
| 19 | #19 | [KoNit-K](https://github.com/KoNit-K) | 317 | 97 | 414–417 |
| 20 | #20 | [hermes-seaeye[bot]](https://github.com/hermes-seaeye[bot]) | 401 | 1 | 402–405 |
| 21 | #21 | [xxxigm](https://github.com/xxxigm) | 320 | 38 | 358–361 |
| 22 | #22 | [jonpol01](https://github.com/jonpol01) | 283 | 32 | 315–318 |
| 23 | #23–24 | [erosika](https://github.com/erosika) | 264 | 6 | 270–273 |
| 24 | #23–24 | [Adolanium](https://github.com/Adolanium) | 260 | 9 | 269–272 |
| 25 | #25–26 | [victor-kyriazakos](https://github.com/victor-kyriazakos) | 251 | 8 | 259–262 |
| 26 | #25–26 | [dokterdok](https://github.com/dokterdok) | 238 | 19 | 257–260 |
| 27 | #27 | [0xbyt4](https://github.com/0xbyt4) | 203 | 12 | 215–218 |
| 28 | #27–30 | [100yenadmin](https://github.com/100yenadmin) | 206 | 6 | 212–215 |
| 29 | #27–30 | [kvnloo](https://github.com/kvnloo) | 179 | 33 | 212–215 |
| 30 | #28–30 | [cursoragent](https://github.com/cursoragent) | 40 | 171 | 211–214 |
| 31 | #31 | [HexLab98](https://github.com/HexLab98) | 193 | 13 | 206–209 |
| 32 | #32 | [afourniernv](https://github.com/afourniernv) | 179 | 0 | 179–182 |
| 33 | #33 | [kokhlo](https://github.com/kokhlo) | 134 | 41 | 175–178 |
| 34 | #34–35 | [briandevans](https://github.com/briandevans) | 157 | 11 | 168–171 |
| 35 | #34–35 | [dskwe](https://github.com/dskwe) | 137 | 29 | 166–169 |
| 36 | #36 | [itpartypattaya](https://github.com/itpartypattaya) | 161 | 0 | 161–164 |
| 37 | #36–37 | [Finn763](https://github.com/Finn763) | 123 | 35 | 158–161 |
| 38 | #38–39 | [LeonSGP43](https://github.com/LeonSGP43) | 108 | 30 | 138–141 |
| 39 | #38–39 | [chelsealong](https://github.com/chelsealong) | 121 | 15 | 136–139 |
| 40 | #40–41 | [DavidMetcalfe](https://github.com/DavidMetcalfe) | 114 | 17 | 131–134 |
| 41 | #40–41 | [webtecnica](https://github.com/webtecnica) | 89 | 41 | 130–133 |
| 42 | #42 | [Tranquil-Flow](https://github.com/Tranquil-Flow) | 93 | 22 | 115–118 |
| 43 | #43 | [SHL0MS](https://github.com/SHL0MS) | 98 | 13 | 111–114 |
| 44 | #44–45 | [686f6c61](https://github.com/686f6c61) | 84 | 20 | 104–107 |
| 45 | #44–45 | [TakeshiTGAL](https://github.com/TakeshiTGAL) | 103 | 0 | 103–106 |
| 46 | #46–47 | [Wenfengcheng](https://github.com/Wenfengcheng) | 82 | 10 | 92–95 |
| 47 | #46–47 | [ygd58](https://github.com/ygd58) | 57 | 35 | 92–95 |
| 48 | #48–51 | [apoapostolov](https://github.com/apoapostolov) | 85 | 1 | 86–89 |
| 49 | #48–51 | [ghgoodreau](https://github.com/ghgoodreau) | 85 | 0 | 85–88 |
| 50 | #48–52 | [beardthelion](https://github.com/beardthelion) | 75 | 9 | 84–87 |
| 51 | #48–52 | [salch-cred](https://github.com/salch-cred) | 68 | 16 | 84–87 |
| 52 | #49–54 | [shannonsands](https://github.com/shannonsands) | 82 | 0 | 82–85 |
| 53 | #52–54 | [calvinnwq](https://github.com/calvinnwq) | 80 | 0 | 80–83 |
| 54 | #52–54 | [PRATHAMESH75](https://github.com/PRATHAMESH75) | 72 | 8 | 80–83 |
| 55 | #53–56 | [Bartok9](https://github.com/Bartok9) | 63 | 14 | 77–80 |
| 56 | #55–56 | [dyiapanis](https://github.com/dyiapanis) | 76 | 0 | 76–79 |
| 57 | #56–60 | [konsisumer](https://github.com/konsisumer) | 63 | 10 | 73–76 |
| 58 | #56–60 | [Sahil-SS9](https://github.com/Sahil-SS9) | 65 | 8 | 73–76 |
| 59 | #57–60 | [gzaentz](https://github.com/gzaentz) | 72 | 0 | 72–75 |
| 60 | #57–60 | [ehz0ah](https://github.com/ehz0ah) | 63 | 8 | 71–74 |
| 61 | #61 | [aydnOktay](https://github.com/aydnOktay) | 45 | 21 | 66–69 |
| 62 | #62–65 | [Froraut](https://github.com/Froraut) | 39 | 23 | 62–65 |
| 63 | #62–65 | [Halldrix](https://github.com/Halldrix) | 54 | 8 | 62–65 |
| 64 | #62–65 | [capthvnsen](https://github.com/capthvnsen) | 61 | 0 | 61–64 |
| 65 | #62–65 | [itsflownium](https://github.com/itsflownium) | 53 | 8 | 61–64 |
| 66 | #66–67 | [33hodl](https://github.com/33hodl) | 57 | 0 | 57–60 |
| 67 | #66–71 | [anpicasso](https://github.com/anpicasso) | 48 | 8 | 56–59 |
| 68 | #66–76 | [AhmetArif0](https://github.com/AhmetArif0) | 52 | 2 | 54–57 |
| 69 | #66–76 | [mojomast](https://github.com/mojomast) | 51 | 3 | 54–57 |
| 70 | #66–76 | [necoweb3](https://github.com/necoweb3) | 48 | 6 | 54–57 |
| 71 | #66–76 | [Xipong](https://github.com/Xipong) | 48 | 6 | 54–57 |
| 72 | #67–78 | [EloquentBrush0x](https://github.com/EloquentBrush0x) | 53 | 0 | 53–56 |
| 73 | #67–78 | [jarrett-del](https://github.com/jarrett-del) | 53 | 0 | 53–56 |
| 74 | #68–79 | [bbednarski9](https://github.com/bbednarski9) | 52 | 0 | 52–55 |
| 75 | #68–79 | [Christopher-Schulze](https://github.com/Christopher-Schulze) | 45 | 7 | 52–55 |
| 76 | #68–79 | [frizikk](https://github.com/frizikk) | 46 | 6 | 52–55 |
| 77 | #68–80 | [entropidelic](https://github.com/entropidelic) | 51 | 0 | 51–54 |
| 78 | #68–80 | [olric3015](https://github.com/olric3015) | 51 | 0 | 51–54 |
| 79 | #72–81 | [pierrenode](https://github.com/pierrenode) | 39 | 11 | 50–53 |
| 80 | #74–84 | [sprmn24](https://github.com/sprmn24) | 42 | 7 | 49–52 |
| 81 | #77–85 | [embwl0x](https://github.com/embwl0x) | 43 | 5 | 48–51 |
| 82 | #79–88 | [nftpoetrist](https://github.com/nftpoetrist) | 40 | 7 | 47–50 |
| 83 | #79–88 | [rewbs](https://github.com/rewbs) | 46 | 1 | 47–50 |
| 84 | #79–88 | [whyyagswhy](https://github.com/whyyagswhy) | 35 | 12 | 47–50 |
| 85 | #80–89 | [rob-maron](https://github.com/rob-maron) | 45 | 1 | 46–49 |
| 86 | #81–89 | [srojk34](https://github.com/srojk34) | 43 | 2 | 45–48 |
| 87 | #81–89 | [Teknium](https://github.com/Teknium) | 18 | 27 | 45–48 |
| 88 | #81–89 | [YAN-XBT](https://github.com/YAN-XBT) | 45 | 0 | 45–48 |
| 89 | #82–92 | [Frowtek](https://github.com/Frowtek) | 41 | 3 | 44–47 |
| 90 | #86–96 | [kouyichi](https://github.com/kouyichi) | 38 | 4 | 42–45 |
| 91 | #86–96 | [ooiuuii](https://github.com/ooiuuii) | 37 | 5 | 42–45 |
| 92 | #86–96 | [tuancookiez-hub](https://github.com/tuancookiez-hub) | 38 | 4 | 42–45 |
| 93 | #89–98 | [abundantbeing](https://github.com/abundantbeing) | 39 | 2 | 41–44 |
| 94 | #89–98 | [wesleysimplicio](https://github.com/wesleysimplicio) | 40 | 1 | 41–44 |
| 95 | #90–101 | [GottZ](https://github.com/GottZ) | 38 | 2 | 40–43 |
| 96 | #90–101 | [jackulau](https://github.com/jackulau) | 36 | 4 | 40–43 |
| 97 | #90–105 | [mnajafian-nv](https://github.com/mnajafian-nv) | 38 | 1 | 39–42 |
| 98 | #90–105 | [Rafa-Ross](https://github.com/Rafa-Ross) | 19 | 20 | 39–42 |
| 99 | #93–110 | [andrexibiza](https://github.com/andrexibiza) | 23 | 15 | 38–41 |
| 100 | #93–110 | [Drexuxux](https://github.com/Drexuxux) | 36 | 2 | 38–41 |
