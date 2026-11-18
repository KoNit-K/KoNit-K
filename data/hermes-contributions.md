# Hermes Agent contribution audit

This is a **custom primary-plus-coauthor ranking**, not GitHub Insights or the REST contributors ranking.

Generated: 2026-11-18T13:31:54Z

Source: [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent), default branch `main`, pinned commit [`0922303631b7ee4ae9a1c3512eab8002da153888`](https://github.com/NousResearch/hermes-agent/commit/0922303631b7ee4ae9a1c3512eab8002da153888).

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

- Completed history pages: 744; declared history total: 74,350; independent Git ancestry: 74,350 commits.
- Resolved author records: 74,347; unresolved commit objects: 3. Their disjoint SHA sets exactly cover all 74,350 reachable commits.
- Initial GraphQL history: 74,347 unique commits; duplicate history rows: 3; resolved by direct SHA queries: 0.
- Among resolved commits only: at least one linked account on 72,735; no linked account on 1,612. Unresolved commit objects are not included in either figure.
- Among resolved commits only: any unlinked author on 2,108; unlinked author entries: 2,131.
- Linked account-commit credits: 78,705; accounts: 5,572. A commit credited to multiple accounts contributes once to each account.
- GraphQL requests: 751; reported query cost: 751; remaining rate-limit points: 4430.

## Uncertainty bounds

There are **U = 3** unresolved commit objects. Each account's complete total lies between its verified total and that total plus U. An unresolved commit can credit multiple accounts, so it is not allocated as one exclusive credit.

The best possible rank is 1 plus the number of other known totals strictly above the account's upper total. The worst possible rank is 1 plus the number of other upper totals strictly above its known total. When the known total is below U, previously unseen accounts may also exceed it; the available evidence provides no finite worst-rank guarantee, shown as `unverified` and `rank_max: null`.

A rank is exact only when its lower and upper bounds coincide. Unknown authorship is never interpreted as zero contribution. The JSON `rank` field ranks known credits only; `rank_min`, `rank_max`, and `rank_is_exact` govern the displayed complete rank.

Unresolved commit SHAs: [`722acd66f62f7617a0df3b5af919d257a35fc258`](https://github.com/NousResearch/hermes-agent/commit/722acd66f62f7617a0df3b5af919d257a35fc258), [`8239ec483323d7f447a7fe708d58b77ed405916f`](https://github.com/NousResearch/hermes-agent/commit/8239ec483323d7f447a7fe708d58b77ed405916f), [`aa0beef6848bd9cdcf1a7015cebc8dfc6170cf5b`](https://github.com/NousResearch/hermes-agent/commit/aa0beef6848bd9cdcf1a7015cebc8dfc6170cf5b).

## KoNit-K

Verified commits: **413** · verified primary: **316** · verified coauthor-only: **97**.

Complete total: **413–416** · complete custom rank: **#19** · rank determined: **yes**. Primary/coauthor SHA evidence is retained in the [complete JSON](hermes-contributions.json).

## First 100 contributor rows

Rows are ordered by verified totals and include positions 5–20 where present. Row position and the known-credit rank are not substituted for an uncertain complete rank.

| Known-credit position | Complete rank | Account | Verified primary | Verified coauthor-only | Complete total |
| ---: | ---: | --- | ---: | ---: | ---: |
| 1 | #1 | [teknium1](https://github.com/teknium1) | 29,579 | 95 | 29,674–29,677 |
| 2 | #2 | [kshitijk4poor](https://github.com/kshitijk4poor) | 5,774 | 63 | 5,837–5,840 |
| 3 | #3 | [OutThisLife](https://github.com/OutThisLife) | 4,581 | 31 | 4,612–4,615 |
| 4 | #4 | [ethernet8023](https://github.com/ethernet8023) | 2,367 | 4 | 2,371–2,374 |
| 5 | #5 | [c2h5oh](https://github.com/c2h5oh) | 1,796 | 0 | 1,796–1,799 |
| 6 | #6 | [claude](https://github.com/claude) | 28 | 1,475 | 1,503–1,506 |
| 7 | #7 | [alt-glitch](https://github.com/alt-glitch) | 1,313 | 9 | 1,322–1,325 |
| 8 | #8 | [unsupportedpastels](https://github.com/unsupportedpastels) | 1,182 | 36 | 1,218–1,221 |
| 9 | #9 | [liuhao1024](https://github.com/liuhao1024) | 658 | 143 | 801–804 |
| 10 | #10 | [BearHuddleston](https://github.com/BearHuddleston) | 242 | 482 | 724–727 |
| 11 | #11 | [benbarclay](https://github.com/benbarclay) | 663 | 18 | 681–684 |
| 12 | #12 | [yoniebans](https://github.com/yoniebans) | 649 | 5 | 654–657 |
| 13 | #13 | [jquesnelle](https://github.com/jquesnelle) | 529 | 7 | 536–539 |
| 14 | #14 | [austinpickett](https://github.com/austinpickett) | 502 | 12 | 514–517 |
| 15 | #15 | [github-actions[bot]](https://github.com/github-actions[bot]) | 12 | 438 | 450–453 |
| 16 | #16 | [helix4u](https://github.com/helix4u) | 418 | 22 | 440–443 |
| 17 | #17 | [fangliquanflq](https://github.com/fangliquanflq) | 370 | 61 | 431–434 |
| 18 | #18 | [JoaoMarcos44](https://github.com/JoaoMarcos44) | 329 | 92 | 421–424 |
| 19 | #19 | [KoNit-K](https://github.com/KoNit-K) | 316 | 97 | 413–416 |
| 20 | #20 | [hermes-seaeye[bot]](https://github.com/hermes-seaeye[bot]) | 401 | 1 | 402–405 |
| 21 | #21 | [xxxigm](https://github.com/xxxigm) | 315 | 38 | 353–356 |
| 22 | #22 | [jonpol01](https://github.com/jonpol01) | 283 | 32 | 315–318 |
| 23 | #23 | [erosika](https://github.com/erosika) | 262 | 6 | 268–271 |
| 24 | #24 | [Adolanium](https://github.com/Adolanium) | 252 | 9 | 261–264 |
| 25 | #25 | [dokterdok](https://github.com/dokterdok) | 238 | 19 | 257–260 |
| 26 | #26 | [victor-kyriazakos](https://github.com/victor-kyriazakos) | 229 | 8 | 237–240 |
| 27 | #27 | [0xbyt4](https://github.com/0xbyt4) | 203 | 12 | 215–218 |
| 28 | #28 | [cursoragent](https://github.com/cursoragent) | 39 | 171 | 210–213 |
| 29 | #29 | [HexLab98](https://github.com/HexLab98) | 193 | 13 | 206–209 |
| 30 | #30 | [kvnloo](https://github.com/kvnloo) | 164 | 31 | 195–198 |
| 31 | #31 | [afourniernv](https://github.com/afourniernv) | 179 | 0 | 179–182 |
| 32 | #32 | [kokhlo](https://github.com/kokhlo) | 134 | 41 | 175–178 |
| 33 | #33 | [briandevans](https://github.com/briandevans) | 157 | 11 | 168–171 |
| 34 | #34 | [dskwe](https://github.com/dskwe) | 135 | 29 | 164–167 |
| 35 | #35 | [Finn763](https://github.com/Finn763) | 123 | 35 | 158–161 |
| 36 | #36 | [itpartypattaya](https://github.com/itpartypattaya) | 148 | 0 | 148–151 |
| 37 | #37–38 | [LeonSGP43](https://github.com/LeonSGP43) | 108 | 30 | 138–141 |
| 38 | #37–38 | [chelsealong](https://github.com/chelsealong) | 121 | 15 | 136–139 |
| 39 | #39–40 | [DavidMetcalfe](https://github.com/DavidMetcalfe) | 114 | 17 | 131–134 |
| 40 | #39–40 | [webtecnica](https://github.com/webtecnica) | 89 | 41 | 130–133 |
| 41 | #41 | [Tranquil-Flow](https://github.com/Tranquil-Flow) | 93 | 22 | 115–118 |
| 42 | #42 | [SHL0MS](https://github.com/SHL0MS) | 98 | 13 | 111–114 |
| 43 | #43 | [686f6c61](https://github.com/686f6c61) | 84 | 20 | 104–107 |
| 44 | #44–45 | [100yenadmin](https://github.com/100yenadmin) | 89 | 6 | 95–98 |
| 45 | #44–45 | [TakeshiTGAL](https://github.com/TakeshiTGAL) | 95 | 0 | 95–98 |
| 46 | #44–47 | [Wenfengcheng](https://github.com/Wenfengcheng) | 82 | 10 | 92–95 |
| 47 | #44–47 | [ygd58](https://github.com/ygd58) | 57 | 35 | 92–95 |
| 48 | #48–51 | [beardthelion](https://github.com/beardthelion) | 75 | 9 | 84–87 |
| 49 | #48–51 | [salch-cred](https://github.com/salch-cred) | 68 | 16 | 84–87 |
| 50 | #48–51 | [apoapostolov](https://github.com/apoapostolov) | 82 | 1 | 83–86 |
| 51 | #48–52 | [shannonsands](https://github.com/shannonsands) | 82 | 0 | 82–85 |
| 52 | #50–52 | [PRATHAMESH75](https://github.com/PRATHAMESH75) | 72 | 8 | 80–83 |
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
| 64 | #64–67 | [33hodl](https://github.com/33hodl) | 56 | 0 | 56–59 |
| 65 | #64–72 | [AhmetArif0](https://github.com/AhmetArif0) | 52 | 2 | 54–57 |
| 66 | #64–72 | [mojomast](https://github.com/mojomast) | 51 | 3 | 54–57 |
| 67 | #64–72 | [necoweb3](https://github.com/necoweb3) | 48 | 6 | 54–57 |
| 68 | #64–75 | [EloquentBrush0x](https://github.com/EloquentBrush0x) | 53 | 0 | 53–56 |
| 69 | #64–75 | [Xipong](https://github.com/Xipong) | 48 | 5 | 53–56 |
| 70 | #65–76 | [bbednarski9](https://github.com/bbednarski9) | 52 | 0 | 52–55 |
| 71 | #65–76 | [Christopher-Schulze](https://github.com/Christopher-Schulze) | 45 | 7 | 52–55 |
| 72 | #65–76 | [frizikk](https://github.com/frizikk) | 46 | 6 | 52–55 |
| 73 | #65–77 | [entropidelic](https://github.com/entropidelic) | 51 | 0 | 51–54 |
| 74 | #65–77 | [jarrett-del](https://github.com/jarrett-del) | 51 | 0 | 51–54 |
| 75 | #65–77 | [olric3015](https://github.com/olric3015) | 51 | 0 | 51–54 |
| 76 | #68–78 | [pierrenode](https://github.com/pierrenode) | 39 | 11 | 50–53 |
| 77 | #70–79 | [sprmn24](https://github.com/sprmn24) | 42 | 7 | 49–52 |
| 78 | #73–81 | [embwl0x](https://github.com/embwl0x) | 43 | 5 | 48–51 |
| 79 | #76–84 | [rewbs](https://github.com/rewbs) | 46 | 1 | 47–50 |
| 80 | #77–86 | [rob-maron](https://github.com/rob-maron) | 45 | 1 | 46–49 |
| 81 | #77–86 | [whyyagswhy](https://github.com/whyyagswhy) | 35 | 11 | 46–49 |
| 82 | #78–86 | [anpicasso](https://github.com/anpicasso) | 37 | 8 | 45–48 |
| 83 | #78–86 | [srojk34](https://github.com/srojk34) | 43 | 2 | 45–48 |
| 84 | #78–86 | [Teknium](https://github.com/Teknium) | 18 | 27 | 45–48 |
| 85 | #79–88 | [Frowtek](https://github.com/Frowtek) | 41 | 3 | 44–47 |
| 86 | #79–88 | [nftpoetrist](https://github.com/nftpoetrist) | 37 | 7 | 44–47 |
| 87 | #82–91 | [ooiuuii](https://github.com/ooiuuii) | 37 | 5 | 42–45 |
| 88 | #82–91 | [tuancookiez-hub](https://github.com/tuancookiez-hub) | 38 | 4 | 42–45 |
| 89 | #85–93 | [wesleysimplicio](https://github.com/wesleysimplicio) | 40 | 1 | 41–44 |
| 90 | #87–98 | [GottZ](https://github.com/GottZ) | 38 | 2 | 40–43 |
| 91 | #87–98 | [jackulau](https://github.com/jackulau) | 36 | 4 | 40–43 |
| 92 | #87–101 | [mnajafian-nv](https://github.com/mnajafian-nv) | 38 | 1 | 39–42 |
| 93 | #87–101 | [Rafa-Ross](https://github.com/Rafa-Ross) | 19 | 20 | 39–42 |
| 94 | #89–106 | [abundantbeing](https://github.com/abundantbeing) | 36 | 2 | 38–41 |
| 95 | #89–106 | [andrexibiza](https://github.com/andrexibiza) | 23 | 15 | 38–41 |
| 96 | #89–106 | [calvinnwq](https://github.com/calvinnwq) | 38 | 0 | 38–41 |
| 97 | #89–106 | [Drexuxux](https://github.com/Drexuxux) | 36 | 2 | 38–41 |
| 98 | #89–106 | [kouyichi](https://github.com/kouyichi) | 34 | 4 | 38–41 |
| 99 | #90–111 | [adybag14-cyber](https://github.com/adybag14-cyber) | 36 | 1 | 37–40 |
| 100 | #90–111 | [ayushnangia](https://github.com/ayushnangia) | 36 | 1 | 37–40 |
