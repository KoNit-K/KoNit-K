# Hermes Agent contribution audit

This is a **custom primary-plus-coauthor ranking**, not GitHub Insights or the REST contributors ranking.

Generated: 2026-11-16T13:15:37Z

Source: [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent), default branch `main`, pinned commit [`f8acc26834bf1275c34d09ccc3e51250bcd1e26b`](https://github.com/NousResearch/hermes-agent/commit/f8acc26834bf1275c34d09ccc3e51250bcd1e26b).

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

- Completed history pages: 733; declared history total: 73,297; independent Git ancestry: 73,297 commits.
- Resolved author records: 73,294; unresolved commit objects: 3. Their disjoint SHA sets exactly cover all 73,297 reachable commits.
- Initial GraphQL history: 73,294 unique commits; duplicate history rows: 3; resolved by direct SHA queries: 0.
- Among resolved commits only: at least one linked account on 71,551; no linked account on 1,743. Unresolved commit objects are not included in either figure.
- Among resolved commits only: any unlinked author on 2,253; unlinked author entries: 2,276.
- Linked account-commit credits: 77,458; accounts: 5,523. A commit credited to multiple accounts contributes once to each account.
- GraphQL requests: 740; reported query cost: 740; remaining rate-limit points: 4623.

## Uncertainty bounds

There are **U = 3** unresolved commit objects. Each account's complete total lies between its verified total and that total plus U. An unresolved commit can credit multiple accounts, so it is not allocated as one exclusive credit.

The best possible rank is 1 plus the number of other known totals strictly above the account's upper total. The worst possible rank is 1 plus the number of other upper totals strictly above its known total. When the known total is below U, previously unseen accounts may also exceed it; the available evidence provides no finite worst-rank guarantee, shown as `unverified` and `rank_max: null`.

A rank is exact only when its lower and upper bounds coincide. Unknown authorship is never interpreted as zero contribution. The JSON `rank` field ranks known credits only; `rank_min`, `rank_max`, and `rank_is_exact` govern the displayed complete rank.

Unresolved commit SHAs: [`722acd66f62f7617a0df3b5af919d257a35fc258`](https://github.com/NousResearch/hermes-agent/commit/722acd66f62f7617a0df3b5af919d257a35fc258), [`8239ec483323d7f447a7fe708d58b77ed405916f`](https://github.com/NousResearch/hermes-agent/commit/8239ec483323d7f447a7fe708d58b77ed405916f), [`aa0beef6848bd9cdcf1a7015cebc8dfc6170cf5b`](https://github.com/NousResearch/hermes-agent/commit/aa0beef6848bd9cdcf1a7015cebc8dfc6170cf5b).

## KoNit-K

Verified commits: **412** · verified primary: **315** · verified coauthor-only: **97**.

Complete total: **412–415** · complete custom rank: **#18** · rank determined: **yes**. Primary/coauthor SHA evidence is retained in the [complete JSON](hermes-contributions.json).

## First 100 contributor rows

Rows are ordered by verified totals and include positions 5–20 where present. Row position and the known-credit rank are not substituted for an uncertain complete rank.

| Known-credit position | Complete rank | Account | Verified primary | Verified coauthor-only | Complete total |
| ---: | ---: | --- | ---: | ---: | ---: |
| 1 | #1 | [teknium1](https://github.com/teknium1) | 29,180 | 89 | 29,269–29,272 |
| 2 | #2 | [kshitijk4poor](https://github.com/kshitijk4poor) | 5,755 | 56 | 5,811–5,814 |
| 3 | #3 | [OutThisLife](https://github.com/OutThisLife) | 4,581 | 31 | 4,612–4,615 |
| 4 | #4 | [ethernet8023](https://github.com/ethernet8023) | 2,367 | 4 | 2,371–2,374 |
| 5 | #5 | [c2h5oh](https://github.com/c2h5oh) | 1,779 | 0 | 1,779–1,782 |
| 6 | #6 | [claude](https://github.com/claude) | 28 | 1,443 | 1,471–1,474 |
| 7 | #7 | [alt-glitch](https://github.com/alt-glitch) | 1,267 | 9 | 1,276–1,279 |
| 8 | #8 | [unsupportedpastels](https://github.com/unsupportedpastels) | 1,179 | 33 | 1,212–1,215 |
| 9 | #9 | [liuhao1024](https://github.com/liuhao1024) | 658 | 143 | 801–804 |
| 10 | #10 | [BearHuddleston](https://github.com/BearHuddleston) | 226 | 473 | 699–702 |
| 11 | #11 | [benbarclay](https://github.com/benbarclay) | 663 | 18 | 681–684 |
| 12 | #12 | [jquesnelle](https://github.com/jquesnelle) | 528 | 7 | 535–538 |
| 13 | #13 | [austinpickett](https://github.com/austinpickett) | 491 | 12 | 503–506 |
| 14 | #14 | [github-actions[bot]](https://github.com/github-actions[bot]) | 12 | 438 | 450–453 |
| 15 | #15 | [helix4u](https://github.com/helix4u) | 418 | 22 | 440–443 |
| 16 | #16 | [fangliquanflq](https://github.com/fangliquanflq) | 370 | 61 | 431–434 |
| 17 | #17 | [JoaoMarcos44](https://github.com/JoaoMarcos44) | 329 | 92 | 421–424 |
| 18 | #18 | [KoNit-K](https://github.com/KoNit-K) | 315 | 97 | 412–415 |
| 19 | #19 | [hermes-seaeye[bot]](https://github.com/hermes-seaeye[bot]) | 401 | 1 | 402–405 |
| 20 | #20 | [yoniebans](https://github.com/yoniebans) | 354 | 5 | 359–362 |
| 21 | #21 | [xxxigm](https://github.com/xxxigm) | 315 | 38 | 353–356 |
| 22 | #22 | [jonpol01](https://github.com/jonpol01) | 283 | 32 | 315–318 |
| 23 | #23 | [erosika](https://github.com/erosika) | 262 | 6 | 268–271 |
| 24 | #24 | [Adolanium](https://github.com/Adolanium) | 251 | 9 | 260–263 |
| 25 | #24–25 | [dokterdok](https://github.com/dokterdok) | 238 | 19 | 257–260 |
| 26 | #26 | [victor-kyriazakos](https://github.com/victor-kyriazakos) | 229 | 8 | 237–240 |
| 27 | #27 | [0xbyt4](https://github.com/0xbyt4) | 203 | 12 | 215–218 |
| 28 | #28 | [cursoragent](https://github.com/cursoragent) | 39 | 171 | 210–213 |
| 29 | #29 | [HexLab98](https://github.com/HexLab98) | 193 | 13 | 206–209 |
| 30 | #30–31 | [kvnloo](https://github.com/kvnloo) | 147 | 29 | 176–179 |
| 31 | #30–31 | [kokhlo](https://github.com/kokhlo) | 134 | 41 | 175–178 |
| 32 | #32 | [afourniernv](https://github.com/afourniernv) | 171 | 0 | 171–174 |
| 33 | #32–33 | [briandevans](https://github.com/briandevans) | 157 | 11 | 168–171 |
| 34 | #34 | [dskwe](https://github.com/dskwe) | 135 | 29 | 164–167 |
| 35 | #35 | [Finn763](https://github.com/Finn763) | 123 | 35 | 158–161 |
| 36 | #36 | [itpartypattaya](https://github.com/itpartypattaya) | 145 | 0 | 145–148 |
| 37 | #37–38 | [LeonSGP43](https://github.com/LeonSGP43) | 108 | 30 | 138–141 |
| 38 | #37–38 | [chelsealong](https://github.com/chelsealong) | 121 | 15 | 136–139 |
| 39 | #39–40 | [DavidMetcalfe](https://github.com/DavidMetcalfe) | 114 | 17 | 131–134 |
| 40 | #39–40 | [webtecnica](https://github.com/webtecnica) | 89 | 41 | 130–133 |
| 41 | #41 | [Tranquil-Flow](https://github.com/Tranquil-Flow) | 90 | 22 | 112–115 |
| 42 | #41–42 | [SHL0MS](https://github.com/SHL0MS) | 98 | 11 | 109–112 |
| 43 | #43 | [686f6c61](https://github.com/686f6c61) | 84 | 20 | 104–107 |
| 44 | #44–46 | [TakeshiTGAL](https://github.com/TakeshiTGAL) | 93 | 0 | 93–96 |
| 45 | #44–46 | [Wenfengcheng](https://github.com/Wenfengcheng) | 82 | 10 | 92–95 |
| 46 | #44–46 | [ygd58](https://github.com/ygd58) | 57 | 35 | 92–95 |
| 47 | #47–50 | [beardthelion](https://github.com/beardthelion) | 75 | 9 | 84–87 |
| 48 | #47–50 | [salch-cred](https://github.com/salch-cred) | 68 | 16 | 84–87 |
| 49 | #47–52 | [100yenadmin](https://github.com/100yenadmin) | 76 | 6 | 82–85 |
| 50 | #47–52 | [shannonsands](https://github.com/shannonsands) | 82 | 0 | 82–85 |
| 51 | #47–52 | [apoapostolov](https://github.com/apoapostolov) | 80 | 1 | 81–84 |
| 52 | #49–52 | [PRATHAMESH75](https://github.com/PRATHAMESH75) | 72 | 8 | 80–83 |
| 53 | #52–54 | [Bartok9](https://github.com/Bartok9) | 63 | 14 | 77–80 |
| 54 | #53–55 | [dyiapanis](https://github.com/dyiapanis) | 75 | 0 | 75–78 |
| 55 | #54–58 | [konsisumer](https://github.com/konsisumer) | 63 | 10 | 73–76 |
| 56 | #54–58 | [gzaentz](https://github.com/gzaentz) | 72 | 0 | 72–75 |
| 57 | #54–58 | [Sahil-SS9](https://github.com/Sahil-SS9) | 64 | 8 | 72–75 |
| 58 | #55–58 | [ehz0ah](https://github.com/ehz0ah) | 63 | 8 | 71–74 |
| 59 | #59 | [aydnOktay](https://github.com/aydnOktay) | 45 | 21 | 66–69 |
| 60 | #60–63 | [Halldrix](https://github.com/Halldrix) | 54 | 8 | 62–65 |
| 61 | #60–63 | [capthvnsen](https://github.com/capthvnsen) | 61 | 0 | 61–64 |
| 62 | #60–63 | [Froraut](https://github.com/Froraut) | 39 | 22 | 61–64 |
| 63 | #60–63 | [itsflownium](https://github.com/itsflownium) | 53 | 8 | 61–64 |
| 64 | #64–71 | [AhmetArif0](https://github.com/AhmetArif0) | 52 | 2 | 54–57 |
| 65 | #64–71 | [mojomast](https://github.com/mojomast) | 51 | 3 | 54–57 |
| 66 | #64–71 | [necoweb3](https://github.com/necoweb3) | 48 | 6 | 54–57 |
| 67 | #64–73 | [EloquentBrush0x](https://github.com/EloquentBrush0x) | 53 | 0 | 53–56 |
| 68 | #64–73 | [Xipong](https://github.com/Xipong) | 48 | 5 | 53–56 |
| 69 | #64–74 | [bbednarski9](https://github.com/bbednarski9) | 52 | 0 | 52–55 |
| 70 | #64–74 | [Christopher-Schulze](https://github.com/Christopher-Schulze) | 45 | 7 | 52–55 |
| 71 | #64–74 | [frizikk](https://github.com/frizikk) | 46 | 6 | 52–55 |
| 72 | #64–75 | [entropidelic](https://github.com/entropidelic) | 51 | 0 | 51–54 |
| 73 | #64–75 | [olric3015](https://github.com/olric3015) | 51 | 0 | 51–54 |
| 74 | #67–76 | [pierrenode](https://github.com/pierrenode) | 39 | 11 | 50–53 |
| 75 | #69–77 | [sprmn24](https://github.com/sprmn24) | 42 | 7 | 49–52 |
| 76 | #72–79 | [embwl0x](https://github.com/embwl0x) | 43 | 5 | 48–51 |
| 77 | #74–81 | [rewbs](https://github.com/rewbs) | 46 | 1 | 47–50 |
| 78 | #75–83 | [rob-maron](https://github.com/rob-maron) | 45 | 1 | 46–49 |
| 79 | #75–83 | [whyyagswhy](https://github.com/whyyagswhy) | 35 | 11 | 46–49 |
| 80 | #76–84 | [srojk34](https://github.com/srojk34) | 43 | 2 | 45–48 |
| 81 | #76–84 | [Teknium](https://github.com/Teknium) | 18 | 27 | 45–48 |
| 82 | #77–86 | [Frowtek](https://github.com/Frowtek) | 41 | 3 | 44–47 |
| 83 | #77–86 | [nftpoetrist](https://github.com/nftpoetrist) | 37 | 7 | 44–47 |
| 84 | #78–87 | [anpicasso](https://github.com/anpicasso) | 35 | 8 | 43–46 |
| 85 | #80–89 | [ooiuuii](https://github.com/ooiuuii) | 37 | 5 | 42–45 |
| 86 | #80–89 | [tuancookiez-hub](https://github.com/tuancookiez-hub) | 38 | 4 | 42–45 |
| 87 | #82–92 | [wesleysimplicio](https://github.com/wesleysimplicio) | 40 | 1 | 41–44 |
| 88 | #84–96 | [jackulau](https://github.com/jackulau) | 36 | 4 | 40–43 |
| 89 | #84–96 | [jarrett-del](https://github.com/jarrett-del) | 40 | 0 | 40–43 |
| 90 | #85–100 | [GottZ](https://github.com/GottZ) | 37 | 2 | 39–42 |
| 91 | #85–100 | [mnajafian-nv](https://github.com/mnajafian-nv) | 38 | 1 | 39–42 |
| 92 | #85–100 | [Rafa-Ross](https://github.com/Rafa-Ross) | 19 | 20 | 39–42 |
| 93 | #87–104 | [abundantbeing](https://github.com/abundantbeing) | 36 | 2 | 38–41 |
| 94 | #87–104 | [andrexibiza](https://github.com/andrexibiza) | 23 | 15 | 38–41 |
| 95 | #87–104 | [Drexuxux](https://github.com/Drexuxux) | 36 | 2 | 38–41 |
| 96 | #87–104 | [kouyichi](https://github.com/kouyichi) | 34 | 4 | 38–41 |
| 97 | #88–109 | [adybag14-cyber](https://github.com/adybag14-cyber) | 36 | 1 | 37–40 |
| 98 | #88–109 | [ayushnangia](https://github.com/ayushnangia) | 36 | 1 | 37–40 |
| 99 | #88–109 | [calvinnwq](https://github.com/calvinnwq) | 37 | 0 | 37–40 |
| 100 | #88–109 | [Enough1122](https://github.com/Enough1122) | 27 | 10 | 37–40 |
