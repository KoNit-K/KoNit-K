# Hermes Agent contribution audit

This is a **custom primary-plus-coauthor ranking**, not GitHub Insights or the REST contributors ranking.

Generated: 2026-11-28T13:37:54Z

Source: [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent), default branch `main`, pinned commit [`3ef8bf4f68c91dce2870eba5625426b32ac6ba58`](https://github.com/NousResearch/hermes-agent/commit/3ef8bf4f68c91dce2870eba5625426b32ac6ba58).

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

- Completed history pages: 776; declared history total: 77,546; independent Git ancestry: 77,546 commits.
- Resolved author records: 77,543; unresolved commit objects: 3. Their disjoint SHA sets exactly cover all 77,546 reachable commits.
- Initial GraphQL history: 77,543 unique commits; duplicate history rows: 3; resolved by direct SHA queries: 0.
- Among resolved commits only: at least one linked account on 75,997; no linked account on 1,546. Unresolved commit objects are not included in either figure.
- Among resolved commits only: any unlinked author on 2,048; unlinked author entries: 2,071.
- Linked account-commit credits: 82,186; accounts: 5,781. A commit credited to multiple accounts contributes once to each account.
- GraphQL requests: 783; reported query cost: 783; remaining rate-limit points: 4410.

## Uncertainty bounds

There are **U = 3** unresolved commit objects. Each account's complete total lies between its verified total and that total plus U. An unresolved commit can credit multiple accounts, so it is not allocated as one exclusive credit.

The best possible rank is 1 plus the number of other known totals strictly above the account's upper total. The worst possible rank is 1 plus the number of other upper totals strictly above its known total. When the known total is below U, previously unseen accounts may also exceed it; the available evidence provides no finite worst-rank guarantee, shown as `unverified` and `rank_max: null`.

A rank is exact only when its lower and upper bounds coincide. Unknown authorship is never interpreted as zero contribution. The JSON `rank` field ranks known credits only; `rank_min`, `rank_max`, and `rank_is_exact` govern the displayed complete rank.

Unresolved commit SHAs: [`722acd66f62f7617a0df3b5af919d257a35fc258`](https://github.com/NousResearch/hermes-agent/commit/722acd66f62f7617a0df3b5af919d257a35fc258), [`8239ec483323d7f447a7fe708d58b77ed405916f`](https://github.com/NousResearch/hermes-agent/commit/8239ec483323d7f447a7fe708d58b77ed405916f), [`aa0beef6848bd9cdcf1a7015cebc8dfc6170cf5b`](https://github.com/NousResearch/hermes-agent/commit/aa0beef6848bd9cdcf1a7015cebc8dfc6170cf5b).

## KoNit-K

Verified commits: **415** · verified primary: **318** · verified coauthor-only: **97**.

Complete total: **415–418** · complete custom rank: **#19** · rank determined: **yes**. Primary/coauthor SHA evidence is retained in the [complete JSON](hermes-contributions.json).

## First 100 contributor rows

Rows are ordered by verified totals and include positions 5–20 where present. Row position and the known-credit rank are not substituted for an uncertain complete rank.

| Known-credit position | Complete rank | Account | Verified primary | Verified coauthor-only | Complete total |
| ---: | ---: | --- | ---: | ---: | ---: |
| 1 | #1 | [teknium1](https://github.com/teknium1) | 30,214 | 95 | 30,309–30,312 |
| 2 | #2 | [kshitijk4poor](https://github.com/kshitijk4poor) | 5,918 | 67 | 5,985–5,988 |
| 3 | #3 | [OutThisLife](https://github.com/OutThisLife) | 4,582 | 31 | 4,613–4,616 |
| 4 | #4 | [ethernet8023](https://github.com/ethernet8023) | 2,404 | 4 | 2,408–2,411 |
| 5 | #5 | [c2h5oh](https://github.com/c2h5oh) | 1,925 | 0 | 1,925–1,928 |
| 6 | #6 | [claude](https://github.com/claude) | 32 | 1,578 | 1,610–1,613 |
| 7 | #7 | [unsupportedpastels](https://github.com/unsupportedpastels) | 1,549 | 48 | 1,597–1,600 |
| 8 | #8 | [alt-glitch](https://github.com/alt-glitch) | 1,313 | 9 | 1,322–1,325 |
| 9 | #9 | [BearHuddleston](https://github.com/BearHuddleston) | 712 | 560 | 1,272–1,275 |
| 10 | #10 | [liuhao1024](https://github.com/liuhao1024) | 661 | 144 | 805–808 |
| 11 | #11 | [yoniebans](https://github.com/yoniebans) | 700 | 5 | 705–708 |
| 12 | #12 | [benbarclay](https://github.com/benbarclay) | 666 | 18 | 684–687 |
| 13 | #13 | [jquesnelle](https://github.com/jquesnelle) | 578 | 7 | 585–588 |
| 14 | #14 | [austinpickett](https://github.com/austinpickett) | 503 | 13 | 516–519 |
| 15 | #15 | [github-actions[bot]](https://github.com/github-actions[bot]) | 12 | 438 | 450–453 |
| 16 | #16 | [helix4u](https://github.com/helix4u) | 421 | 22 | 443–446 |
| 17 | #17 | [fangliquanflq](https://github.com/fangliquanflq) | 370 | 62 | 432–435 |
| 18 | #18 | [JoaoMarcos44](https://github.com/JoaoMarcos44) | 329 | 92 | 421–424 |
| 19 | #19 | [KoNit-K](https://github.com/KoNit-K) | 318 | 97 | 415–418 |
| 20 | #20 | [hermes-seaeye[bot]](https://github.com/hermes-seaeye[bot]) | 401 | 1 | 402–405 |
| 21 | #21 | [xxxigm](https://github.com/xxxigm) | 320 | 38 | 358–361 |
| 22 | #22 | [jonpol01](https://github.com/jonpol01) | 284 | 32 | 316–319 |
| 23 | #23 | [victor-kyriazakos](https://github.com/victor-kyriazakos) | 271 | 8 | 279–282 |
| 24 | #24–25 | [erosika](https://github.com/erosika) | 265 | 6 | 271–274 |
| 25 | #24–25 | [Adolanium](https://github.com/Adolanium) | 260 | 9 | 269–272 |
| 26 | #26 | [dokterdok](https://github.com/dokterdok) | 238 | 19 | 257–260 |
| 27 | #27 | [kvnloo](https://github.com/kvnloo) | 192 | 34 | 226–229 |
| 28 | #28–29 | [0xbyt4](https://github.com/0xbyt4) | 203 | 12 | 215–218 |
| 29 | #28–29 | [100yenadmin](https://github.com/100yenadmin) | 208 | 6 | 214–217 |
| 30 | #29–30 | [cursoragent](https://github.com/cursoragent) | 40 | 171 | 211–214 |
| 31 | #31 | [HexLab98](https://github.com/HexLab98) | 193 | 13 | 206–209 |
| 32 | #32 | [afourniernv](https://github.com/afourniernv) | 179 | 0 | 179–182 |
| 33 | #33 | [kokhlo](https://github.com/kokhlo) | 134 | 41 | 175–178 |
| 34 | #34–35 | [itpartypattaya](https://github.com/itpartypattaya) | 169 | 0 | 169–172 |
| 35 | #34–36 | [briandevans](https://github.com/briandevans) | 157 | 11 | 168–171 |
| 36 | #34–36 | [dskwe](https://github.com/dskwe) | 137 | 29 | 166–169 |
| 37 | #37 | [Finn763](https://github.com/Finn763) | 123 | 35 | 158–161 |
| 38 | #38–39 | [LeonSGP43](https://github.com/LeonSGP43) | 108 | 30 | 138–141 |
| 39 | #38–39 | [chelsealong](https://github.com/chelsealong) | 121 | 15 | 136–139 |
| 40 | #40–41 | [DavidMetcalfe](https://github.com/DavidMetcalfe) | 114 | 17 | 131–134 |
| 41 | #40–41 | [webtecnica](https://github.com/webtecnica) | 89 | 41 | 130–133 |
| 42 | #42 | [Tranquil-Flow](https://github.com/Tranquil-Flow) | 93 | 22 | 115–118 |
| 43 | #43 | [SHL0MS](https://github.com/SHL0MS) | 98 | 13 | 111–114 |
| 44 | #44–45 | [TakeshiTGAL](https://github.com/TakeshiTGAL) | 106 | 0 | 106–109 |
| 45 | #44–45 | [686f6c61](https://github.com/686f6c61) | 84 | 20 | 104–107 |
| 46 | #46–47 | [Wenfengcheng](https://github.com/Wenfengcheng) | 82 | 10 | 92–95 |
| 47 | #46–47 | [ygd58](https://github.com/ygd58) | 57 | 35 | 92–95 |
| 48 | #48–51 | [apoapostolov](https://github.com/apoapostolov) | 85 | 1 | 86–89 |
| 49 | #48–51 | [ghgoodreau](https://github.com/ghgoodreau) | 85 | 0 | 85–88 |
| 50 | #48–52 | [beardthelion](https://github.com/beardthelion) | 75 | 9 | 84–87 |
| 51 | #48–52 | [salch-cred](https://github.com/salch-cred) | 68 | 16 | 84–87 |
| 52 | #49–54 | [shannonsands](https://github.com/shannonsands) | 82 | 0 | 82–85 |
| 53 | #52–55 | [calvinnwq](https://github.com/calvinnwq) | 80 | 0 | 80–83 |
| 54 | #52–55 | [PRATHAMESH75](https://github.com/PRATHAMESH75) | 72 | 8 | 80–83 |
| 55 | #52–56 | [dyiapanis](https://github.com/dyiapanis) | 79 | 0 | 79–82 |
| 56 | #53–57 | [Bartok9](https://github.com/Bartok9) | 63 | 14 | 77–80 |
| 57 | #55–57 | [Sahil-SS9](https://github.com/Sahil-SS9) | 68 | 8 | 76–79 |
| 58 | #57–60 | [konsisumer](https://github.com/konsisumer) | 63 | 10 | 73–76 |
| 59 | #58–60 | [gzaentz](https://github.com/gzaentz) | 72 | 0 | 72–75 |
| 60 | #58–60 | [ehz0ah](https://github.com/ehz0ah) | 63 | 8 | 71–74 |
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
| 77 | #68–81 | [entropidelic](https://github.com/entropidelic) | 51 | 0 | 51–54 |
| 78 | #68–81 | [olric3015](https://github.com/olric3015) | 51 | 0 | 51–54 |
| 79 | #72–82 | [pierrenode](https://github.com/pierrenode) | 39 | 11 | 50–53 |
| 80 | #74–84 | [nftpoetrist](https://github.com/nftpoetrist) | 42 | 7 | 49–52 |
| 81 | #74–84 | [sprmn24](https://github.com/sprmn24) | 42 | 7 | 49–52 |
| 82 | #77–85 | [embwl0x](https://github.com/embwl0x) | 43 | 5 | 48–51 |
| 83 | #79–89 | [rewbs](https://github.com/rewbs) | 46 | 1 | 47–50 |
| 84 | #79–89 | [whyyagswhy](https://github.com/whyyagswhy) | 35 | 12 | 47–50 |
| 85 | #80–90 | [rob-maron](https://github.com/rob-maron) | 45 | 1 | 46–49 |
| 86 | #82–90 | [IAvecilla](https://github.com/IAvecilla) | 43 | 2 | 45–48 |
| 87 | #82–90 | [srojk34](https://github.com/srojk34) | 43 | 2 | 45–48 |
| 88 | #82–90 | [Teknium](https://github.com/Teknium) | 18 | 27 | 45–48 |
| 89 | #82–90 | [YAN-XBT](https://github.com/YAN-XBT) | 45 | 0 | 45–48 |
| 90 | #83–93 | [Frowtek](https://github.com/Frowtek) | 41 | 3 | 44–47 |
| 91 | #86–98 | [kouyichi](https://github.com/kouyichi) | 38 | 4 | 42–45 |
| 92 | #86–98 | [ooiuuii](https://github.com/ooiuuii) | 37 | 5 | 42–45 |
| 93 | #86–98 | [tuancookiez-hub](https://github.com/tuancookiez-hub) | 38 | 4 | 42–45 |
| 94 | #90–100 | [abundantbeing](https://github.com/abundantbeing) | 39 | 2 | 41–44 |
| 95 | #90–100 | [soyelmismo](https://github.com/soyelmismo) | 41 | 0 | 41–44 |
| 96 | #90–100 | [wesleysimplicio](https://github.com/wesleysimplicio) | 40 | 1 | 41–44 |
| 97 | #91–103 | [GottZ](https://github.com/GottZ) | 38 | 2 | 40–43 |
| 98 | #91–103 | [jackulau](https://github.com/jackulau) | 36 | 4 | 40–43 |
| 99 | #91–106 | [mnajafian-nv](https://github.com/mnajafian-nv) | 38 | 1 | 39–42 |
| 100 | #91–106 | [Rafa-Ross](https://github.com/Rafa-Ross) | 19 | 20 | 39–42 |
