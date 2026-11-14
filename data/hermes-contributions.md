# Hermes Agent contribution audit

This is a **custom primary-plus-coauthor ranking**, not GitHub Insights or the REST contributors ranking.

Generated: 2026-11-14T11:52:01Z

Source: [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent), default branch `main`, pinned commit [`d3d4ee4c7c0e0e29dbd8562aa836303dbc468877`](https://github.com/NousResearch/hermes-agent/commit/d3d4ee4c7c0e0e29dbd8562aa836303dbc468877).

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

- Completed history pages: 718; declared history total: 71,794; independent Git ancestry: 71,794 commits.
- Resolved author records: 71,791; unresolved commit objects: 3. Their disjoint SHA sets exactly cover all 71,794 reachable commits.
- Initial GraphQL history: 71,791 unique commits; duplicate history rows: 3; resolved by direct SHA queries: 0.
- Among resolved commits only: at least one linked account on 70,076; no linked account on 1,715. Unresolved commit objects are not included in either figure.
- Among resolved commits only: any unlinked author on 2,218; unlinked author entries: 2,241.
- Linked account-commit credits: 75,682; accounts: 5,458. A commit credited to multiple accounts contributes once to each account.
- GraphQL requests: 725; reported query cost: 725; remaining rate-limit points: 4640.

## Uncertainty bounds

There are **U = 3** unresolved commit objects. Each account's complete total lies between its verified total and that total plus U. An unresolved commit can credit multiple accounts, so it is not allocated as one exclusive credit.

The best possible rank is 1 plus the number of other known totals strictly above the account's upper total. The worst possible rank is 1 plus the number of other upper totals strictly above its known total. When the known total is below U, previously unseen accounts may also exceed it; the available evidence provides no finite worst-rank guarantee, shown as `unverified` and `rank_max: null`.

A rank is exact only when its lower and upper bounds coincide. Unknown authorship is never interpreted as zero contribution. The JSON `rank` field ranks known credits only; `rank_min`, `rank_max`, and `rank_is_exact` govern the displayed complete rank.

Unresolved commit SHAs: [`722acd66f62f7617a0df3b5af919d257a35fc258`](https://github.com/NousResearch/hermes-agent/commit/722acd66f62f7617a0df3b5af919d257a35fc258), [`8239ec483323d7f447a7fe708d58b77ed405916f`](https://github.com/NousResearch/hermes-agent/commit/8239ec483323d7f447a7fe708d58b77ed405916f), [`aa0beef6848bd9cdcf1a7015cebc8dfc6170cf5b`](https://github.com/NousResearch/hermes-agent/commit/aa0beef6848bd9cdcf1a7015cebc8dfc6170cf5b).

## KoNit-K

Verified commits: **408** · verified primary: **312** · verified coauthor-only: **96**.

Complete total: **408–411** · complete custom rank: **#18** · rank determined: **yes**. Primary/coauthor SHA evidence is retained in the [complete JSON](hermes-contributions.json).

## First 100 contributor rows

Rows are ordered by verified totals and include positions 5–20 where present. Row position and the known-credit rank are not substituted for an uncertain complete rank.

| Known-credit position | Complete rank | Account | Verified primary | Verified coauthor-only | Complete total |
| ---: | ---: | --- | ---: | ---: | ---: |
| 1 | #1 | [teknium1](https://github.com/teknium1) | 28,970 | 86 | 29,056–29,059 |
| 2 | #2 | [kshitijk4poor](https://github.com/kshitijk4poor) | 5,749 | 56 | 5,805–5,808 |
| 3 | #3 | [OutThisLife](https://github.com/OutThisLife) | 4,580 | 31 | 4,611–4,614 |
| 4 | #4 | [ethernet8023](https://github.com/ethernet8023) | 2,367 | 4 | 2,371–2,374 |
| 5 | #5 | [claude](https://github.com/claude) | 28 | 1,411 | 1,439–1,442 |
| 6 | #6 | [alt-glitch](https://github.com/alt-glitch) | 1,216 | 9 | 1,225–1,228 |
| 7 | #7 | [unsupportedpastels](https://github.com/unsupportedpastels) | 1,168 | 27 | 1,195–1,198 |
| 8 | #8 | [c2h5oh](https://github.com/c2h5oh) | 1,117 | 0 | 1,117–1,120 |
| 9 | #9 | [liuhao1024](https://github.com/liuhao1024) | 639 | 136 | 775–778 |
| 10 | #10 | [benbarclay](https://github.com/benbarclay) | 663 | 18 | 681–684 |
| 11 | #11 | [jquesnelle](https://github.com/jquesnelle) | 528 | 7 | 535–538 |
| 12 | #12 | [austinpickett](https://github.com/austinpickett) | 490 | 12 | 502–505 |
| 13 | #13 | [BearHuddleston](https://github.com/BearHuddleston) | 224 | 249 | 473–476 |
| 14 | #14 | [github-actions[bot]](https://github.com/github-actions[bot]) | 12 | 438 | 450–453 |
| 15 | #15 | [helix4u](https://github.com/helix4u) | 410 | 22 | 432–435 |
| 16 | #15–16 | [fangliquanflq](https://github.com/fangliquanflq) | 369 | 60 | 429–432 |
| 17 | #17 | [JoaoMarcos44](https://github.com/JoaoMarcos44) | 329 | 90 | 419–422 |
| 18 | #18 | [KoNit-K](https://github.com/KoNit-K) | 312 | 96 | 408–411 |
| 19 | #19 | [hermes-seaeye[bot]](https://github.com/hermes-seaeye[bot]) | 401 | 1 | 402–405 |
| 20 | #20 | [xxxigm](https://github.com/xxxigm) | 315 | 38 | 353–356 |
| 21 | #21 | [yoniebans](https://github.com/yoniebans) | 311 | 5 | 316–319 |
| 22 | #22 | [jonpol01](https://github.com/jonpol01) | 278 | 32 | 310–313 |
| 23 | #23 | [erosika](https://github.com/erosika) | 262 | 6 | 268–271 |
| 24 | #24 | [dokterdok](https://github.com/dokterdok) | 238 | 19 | 257–260 |
| 25 | #25–26 | [Adolanium](https://github.com/Adolanium) | 230 | 8 | 238–241 |
| 26 | #25–26 | [victor-kyriazakos](https://github.com/victor-kyriazakos) | 229 | 8 | 237–240 |
| 27 | #27 | [0xbyt4](https://github.com/0xbyt4) | 203 | 12 | 215–218 |
| 28 | #28 | [cursoragent](https://github.com/cursoragent) | 39 | 171 | 210–213 |
| 29 | #29 | [HexLab98](https://github.com/HexLab98) | 193 | 13 | 206–209 |
| 30 | #30 | [kokhlo](https://github.com/kokhlo) | 133 | 41 | 174–177 |
| 31 | #30–31 | [afourniernv](https://github.com/afourniernv) | 171 | 0 | 171–174 |
| 32 | #31–32 | [briandevans](https://github.com/briandevans) | 157 | 11 | 168–171 |
| 33 | #33 | [dskwe](https://github.com/dskwe) | 133 | 29 | 162–165 |
| 34 | #34 | [Finn763](https://github.com/Finn763) | 122 | 35 | 157–160 |
| 35 | #35 | [kvnloo](https://github.com/kvnloo) | 123 | 29 | 152–155 |
| 36 | #36 | [itpartypattaya](https://github.com/itpartypattaya) | 143 | 0 | 143–146 |
| 37 | #37–38 | [LeonSGP43](https://github.com/LeonSGP43) | 108 | 30 | 138–141 |
| 38 | #37–38 | [chelsealong](https://github.com/chelsealong) | 121 | 15 | 136–139 |
| 39 | #39–40 | [DavidMetcalfe](https://github.com/DavidMetcalfe) | 113 | 17 | 130–133 |
| 40 | #39–40 | [webtecnica](https://github.com/webtecnica) | 89 | 40 | 129–132 |
| 41 | #41 | [Tranquil-Flow](https://github.com/Tranquil-Flow) | 90 | 22 | 112–115 |
| 42 | #41–42 | [SHL0MS](https://github.com/SHL0MS) | 98 | 11 | 109–112 |
| 43 | #43 | [686f6c61](https://github.com/686f6c61) | 82 | 20 | 102–105 |
| 44 | #44–46 | [Wenfengcheng](https://github.com/Wenfengcheng) | 82 | 10 | 92–95 |
| 45 | #44–46 | [TakeshiTGAL](https://github.com/TakeshiTGAL) | 91 | 0 | 91–94 |
| 46 | #44–46 | [ygd58](https://github.com/ygd58) | 57 | 34 | 91–94 |
| 47 | #47–49 | [shannonsands](https://github.com/shannonsands) | 82 | 0 | 82–85 |
| 48 | #47–51 | [apoapostolov](https://github.com/apoapostolov) | 80 | 1 | 81–84 |
| 49 | #47–52 | [100yenadmin](https://github.com/100yenadmin) | 74 | 6 | 80–83 |
| 50 | #47–52 | [PRATHAMESH75](https://github.com/PRATHAMESH75) | 71 | 8 | 79–82 |
| 51 | #47–52 | [salch-cred](https://github.com/salch-cred) | 63 | 16 | 79–82 |
| 52 | #48–53 | [beardthelion](https://github.com/beardthelion) | 72 | 6 | 78–81 |
| 53 | #50–54 | [Bartok9](https://github.com/Bartok9) | 63 | 13 | 76–79 |
| 54 | #52–55 | [dyiapanis](https://github.com/dyiapanis) | 75 | 0 | 75–78 |
| 55 | #53–57 | [konsisumer](https://github.com/konsisumer) | 63 | 10 | 73–76 |
| 56 | #54–57 | [gzaentz](https://github.com/gzaentz) | 72 | 0 | 72–75 |
| 57 | #55–58 | [ehz0ah](https://github.com/ehz0ah) | 63 | 8 | 71–74 |
| 58 | #56–58 | [Sahil-SS9](https://github.com/Sahil-SS9) | 61 | 8 | 69–72 |
| 59 | #58–59 | [aydnOktay](https://github.com/aydnOktay) | 45 | 21 | 66–69 |
| 60 | #60–63 | [Halldrix](https://github.com/Halldrix) | 54 | 8 | 62–65 |
| 61 | #60–63 | [capthvnsen](https://github.com/capthvnsen) | 61 | 0 | 61–64 |
| 62 | #60–63 | [Froraut](https://github.com/Froraut) | 39 | 22 | 61–64 |
| 63 | #60–63 | [itsflownium](https://github.com/itsflownium) | 53 | 8 | 61–64 |
| 64 | #64–69 | [AhmetArif0](https://github.com/AhmetArif0) | 52 | 2 | 54–57 |
| 65 | #64–69 | [mojomast](https://github.com/mojomast) | 51 | 3 | 54–57 |
| 66 | #64–69 | [necoweb3](https://github.com/necoweb3) | 48 | 6 | 54–57 |
| 67 | #64–72 | [Xipong](https://github.com/Xipong) | 48 | 5 | 53–56 |
| 68 | #64–72 | [bbednarski9](https://github.com/bbednarski9) | 52 | 0 | 52–55 |
| 69 | #64–72 | [frizikk](https://github.com/frizikk) | 46 | 6 | 52–55 |
| 70 | #64–75 | [Christopher-Schulze](https://github.com/Christopher-Schulze) | 44 | 7 | 51–54 |
| 71 | #64–75 | [entropidelic](https://github.com/entropidelic) | 51 | 0 | 51–54 |
| 72 | #64–75 | [olric3015](https://github.com/olric3015) | 51 | 0 | 51–54 |
| 73 | #68–77 | [EloquentBrush0x](https://github.com/EloquentBrush0x) | 49 | 0 | 49–52 |
| 74 | #68–77 | [pierrenode](https://github.com/pierrenode) | 38 | 11 | 49–52 |
| 75 | #68–77 | [sprmn24](https://github.com/sprmn24) | 42 | 7 | 49–52 |
| 76 | #73–81 | [embwl0x](https://github.com/embwl0x) | 42 | 5 | 47–50 |
| 77 | #73–81 | [rewbs](https://github.com/rewbs) | 46 | 1 | 47–50 |
| 78 | #73–83 | [rob-maron](https://github.com/rob-maron) | 45 | 1 | 46–49 |
| 79 | #73–83 | [whyyagswhy](https://github.com/whyyagswhy) | 35 | 11 | 46–49 |
| 80 | #76–83 | [srojk34](https://github.com/srojk34) | 43 | 2 | 45–48 |
| 81 | #76–83 | [Teknium](https://github.com/Teknium) | 18 | 27 | 45–48 |
| 82 | #76–83 | [Frowtek](https://github.com/Frowtek) | 41 | 3 | 44–47 |
| 83 | #76–83 | [nftpoetrist](https://github.com/nftpoetrist) | 37 | 7 | 44–47 |
| 84 | #82–90 | [ooiuuii](https://github.com/ooiuuii) | 37 | 4 | 41–44 |
| 85 | #82–90 | [wesleysimplicio](https://github.com/wesleysimplicio) | 40 | 1 | 41–44 |
| 86 | #84–92 | [jackulau](https://github.com/jackulau) | 36 | 4 | 40–43 |
| 87 | #84–92 | [tuancookiez-hub](https://github.com/tuancookiez-hub) | 36 | 4 | 40–43 |
| 88 | #84–95 | [GottZ](https://github.com/GottZ) | 37 | 2 | 39–42 |
| 89 | #84–95 | [mnajafian-nv](https://github.com/mnajafian-nv) | 38 | 1 | 39–42 |
| 90 | #84–95 | [Rafa-Ross](https://github.com/Rafa-Ross) | 19 | 20 | 39–42 |
| 91 | #84–100 | [andrexibiza](https://github.com/andrexibiza) | 23 | 15 | 38–41 |
| 92 | #84–100 | [Drexuxux](https://github.com/Drexuxux) | 36 | 2 | 38–41 |
| 93 | #86–103 | [adybag14-cyber](https://github.com/adybag14-cyber) | 36 | 1 | 37–40 |
| 94 | #86–103 | [ayushnangia](https://github.com/ayushnangia) | 36 | 1 | 37–40 |
| 95 | #86–103 | [Enough1122](https://github.com/Enough1122) | 27 | 10 | 37–40 |
| 96 | #88–108 | [calvinnwq](https://github.com/calvinnwq) | 36 | 0 | 36–39 |
| 97 | #88–108 | [IAvecilla](https://github.com/IAvecilla) | 34 | 2 | 36–39 |
| 98 | #88–108 | [lEWFkRAD](https://github.com/lEWFkRAD) | 33 | 3 | 36–39 |
| 99 | #88–108 | [r266-tech](https://github.com/r266-tech) | 33 | 3 | 36–39 |
| 100 | #88–108 | [vdimarco](https://github.com/vdimarco) | 36 | 0 | 36–39 |
