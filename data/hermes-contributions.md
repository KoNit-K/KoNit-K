# Hermes Agent contribution audit

This is a **custom primary-plus-coauthor ranking**, not GitHub Insights or the REST contributors ranking.

Generated: 2026-11-11T12:12:34Z

Source: [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent), default branch `main`, pinned commit [`79fb37f8a9e74ad09f63227ebc069c98e84855ea`](https://github.com/NousResearch/hermes-agent/commit/79fb37f8a9e74ad09f63227ebc069c98e84855ea).

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

- Completed history pages: 672; declared history total: 67,162; independent Git ancestry: 67,162 commits.
- Resolved author records: 67,159; unresolved commit objects: 3. Their disjoint SHA sets exactly cover all 67,162 reachable commits.
- Initial GraphQL history: 67,159 unique commits; duplicate history rows: 3; resolved by direct SHA queries: 0.
- Among resolved commits only: at least one linked account on 65,568; no linked account on 1,591. Unresolved commit objects are not included in either figure.
- Among resolved commits only: any unlinked author on 2,087; unlinked author entries: 2,110.
- Linked account-commit credits: 70,725; accounts: 4,987. A commit credited to multiple accounts contributes once to each account.
- GraphQL requests: 679; reported query cost: 679; remaining rate-limit points: 4484.

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
| 1 | #1 | [teknium1](https://github.com/teknium1) | 27,656 | 82 | 27,738–27,741 |
| 2 | #2 | [kshitijk4poor](https://github.com/kshitijk4poor) | 5,685 | 55 | 5,740–5,743 |
| 3 | #3 | [OutThisLife](https://github.com/OutThisLife) | 4,580 | 31 | 4,611–4,614 |
| 4 | #4 | [ethernet8023](https://github.com/ethernet8023) | 2,367 | 4 | 2,371–2,374 |
| 5 | #5 | [claude](https://github.com/claude) | 26 | 1,233 | 1,259–1,262 |
| 6 | #6 | [unsupportedpastels](https://github.com/unsupportedpastels) | 1,093 | 15 | 1,108–1,111 |
| 7 | #7 | [alt-glitch](https://github.com/alt-glitch) | 1,082 | 9 | 1,091–1,094 |
| 8 | #8 | [liuhao1024](https://github.com/liuhao1024) | 607 | 129 | 736–739 |
| 9 | #9 | [benbarclay](https://github.com/benbarclay) | 622 | 18 | 640–643 |
| 10 | #10 | [jquesnelle](https://github.com/jquesnelle) | 517 | 7 | 524–527 |
| 11 | #11 | [c2h5oh](https://github.com/c2h5oh) | 513 | 0 | 513–516 |
| 12 | #12 | [austinpickett](https://github.com/austinpickett) | 490 | 12 | 502–505 |
| 13 | #13 | [github-actions[bot]](https://github.com/github-actions[bot]) | 12 | 438 | 450–453 |
| 14 | #14 | [helix4u](https://github.com/helix4u) | 406 | 22 | 428–431 |
| 15 | #15 | [fangliquanflq](https://github.com/fangliquanflq) | 365 | 56 | 421–424 |
| 16 | #16 | [JoaoMarcos44](https://github.com/JoaoMarcos44) | 328 | 89 | 417–420 |
| 17 | #17–18 | [KoNit-K](https://github.com/KoNit-K) | 307 | 96 | 403–406 |
| 18 | #17–18 | [hermes-seaeye[bot]](https://github.com/hermes-seaeye[bot]) | 401 | 1 | 402–405 |
| 19 | #19 | [xxxigm](https://github.com/xxxigm) | 315 | 38 | 353–356 |
| 20 | #20–21 | [yoniebans](https://github.com/yoniebans) | 297 | 4 | 301–304 |
| 21 | #20–21 | [jonpol01](https://github.com/jonpol01) | 268 | 32 | 300–303 |
| 22 | #22 | [BearHuddleston](https://github.com/BearHuddleston) | 179 | 94 | 273–276 |
| 23 | #23 | [erosika](https://github.com/erosika) | 256 | 6 | 262–265 |
| 24 | #24 | [dokterdok](https://github.com/dokterdok) | 237 | 19 | 256–259 |
| 25 | #25 | [0xbyt4](https://github.com/0xbyt4) | 203 | 12 | 215–218 |
| 26 | #25–26 | [Adolanium](https://github.com/Adolanium) | 205 | 7 | 212–215 |
| 27 | #27 | [HexLab98](https://github.com/HexLab98) | 193 | 13 | 206–209 |
| 28 | #28 | [cursoragent](https://github.com/cursoragent) | 29 | 165 | 194–197 |
| 29 | #29 | [victor-kyriazakos](https://github.com/victor-kyriazakos) | 173 | 7 | 180–183 |
| 30 | #30–31 | [kokhlo](https://github.com/kokhlo) | 131 | 41 | 172–175 |
| 31 | #30–31 | [afourniernv](https://github.com/afourniernv) | 171 | 0 | 171–174 |
| 32 | #32 | [briandevans](https://github.com/briandevans) | 155 | 10 | 165–168 |
| 33 | #33–34 | [dskwe](https://github.com/dskwe) | 130 | 27 | 157–160 |
| 34 | #33–34 | [Finn763](https://github.com/Finn763) | 122 | 35 | 157–160 |
| 35 | #35 | [itpartypattaya](https://github.com/itpartypattaya) | 143 | 0 | 143–146 |
| 36 | #36–37 | [LeonSGP43](https://github.com/LeonSGP43) | 108 | 29 | 137–140 |
| 37 | #36–37 | [chelsealong](https://github.com/chelsealong) | 121 | 15 | 136–139 |
| 38 | #38–39 | [DavidMetcalfe](https://github.com/DavidMetcalfe) | 113 | 17 | 130–133 |
| 39 | #38–39 | [webtecnica](https://github.com/webtecnica) | 89 | 39 | 128–131 |
| 40 | #40 | [Tranquil-Flow](https://github.com/Tranquil-Flow) | 90 | 21 | 111–114 |
| 41 | #41 | [SHL0MS](https://github.com/SHL0MS) | 95 | 11 | 106–109 |
| 42 | #42 | [686f6c61](https://github.com/686f6c61) | 81 | 20 | 101–104 |
| 43 | #43–44 | [Wenfengcheng](https://github.com/Wenfengcheng) | 82 | 10 | 92–95 |
| 44 | #43–44 | [ygd58](https://github.com/ygd58) | 57 | 34 | 91–94 |
| 45 | #45–46 | [TakeshiTGAL](https://github.com/TakeshiTGAL) | 83 | 0 | 83–86 |
| 46 | #45–47 | [shannonsands](https://github.com/shannonsands) | 82 | 0 | 82–85 |
| 47 | #45–48 | [apoapostolov](https://github.com/apoapostolov) | 79 | 1 | 80–83 |
| 48 | #47–50 | [PRATHAMESH75](https://github.com/PRATHAMESH75) | 70 | 8 | 78–81 |
| 49 | #47–51 | [100yenadmin](https://github.com/100yenadmin) | 71 | 6 | 77–80 |
| 50 | #48–51 | [Bartok9](https://github.com/Bartok9) | 63 | 13 | 76–79 |
| 51 | #48–52 | [beardthelion](https://github.com/beardthelion) | 69 | 6 | 75–78 |
| 52 | #50–54 | [konsisumer](https://github.com/konsisumer) | 63 | 10 | 73–76 |
| 53 | #51–55 | [kvnloo](https://github.com/kvnloo) | 53 | 19 | 72–75 |
| 54 | #52–55 | [ehz0ah](https://github.com/ehz0ah) | 63 | 8 | 71–74 |
| 55 | #52–55 | [dyiapanis](https://github.com/dyiapanis) | 70 | 0 | 70–73 |
| 56 | #56–57 | [aydnOktay](https://github.com/aydnOktay) | 45 | 21 | 66–69 |
| 57 | #56–57 | [salch-cred](https://github.com/salch-cred) | 49 | 16 | 65–68 |
| 58 | #57–59 | [Halldrix](https://github.com/Halldrix) | 54 | 8 | 62–65 |
| 59 | #58–59 | [Sahil-SS9](https://github.com/Sahil-SS9) | 53 | 8 | 61–64 |
| 60 | #60–67 | [AhmetArif0](https://github.com/AhmetArif0) | 52 | 2 | 54–57 |
| 61 | #60–67 | [capthvnsen](https://github.com/capthvnsen) | 54 | 0 | 54–57 |
| 62 | #60–67 | [Froraut](https://github.com/Froraut) | 35 | 19 | 54–57 |
| 63 | #60–67 | [necoweb3](https://github.com/necoweb3) | 48 | 6 | 54–57 |
| 64 | #60–69 | [itsflownium](https://github.com/itsflownium) | 45 | 8 | 53–56 |
| 65 | #60–69 | [Xipong](https://github.com/Xipong) | 48 | 5 | 53–56 |
| 66 | #60–69 | [bbednarski9](https://github.com/bbednarski9) | 52 | 0 | 52–55 |
| 67 | #60–69 | [frizikk](https://github.com/frizikk) | 46 | 6 | 52–55 |
| 68 | #60–72 | [entropidelic](https://github.com/entropidelic) | 51 | 0 | 51–54 |
| 69 | #60–72 | [olric3015](https://github.com/olric3015) | 51 | 0 | 51–54 |
| 70 | #66–74 | [EloquentBrush0x](https://github.com/EloquentBrush0x) | 49 | 0 | 49–52 |
| 71 | #66–74 | [pierrenode](https://github.com/pierrenode) | 38 | 11 | 49–52 |
| 72 | #66–74 | [sprmn24](https://github.com/sprmn24) | 42 | 7 | 49–52 |
| 73 | #70–78 | [embwl0x](https://github.com/embwl0x) | 42 | 5 | 47–50 |
| 74 | #70–78 | [rewbs](https://github.com/rewbs) | 46 | 1 | 47–50 |
| 75 | #70–79 | [rob-maron](https://github.com/rob-maron) | 45 | 1 | 46–49 |
| 76 | #70–79 | [whyyagswhy](https://github.com/whyyagswhy) | 35 | 11 | 46–49 |
| 77 | #73–80 | [srojk34](https://github.com/srojk34) | 43 | 2 | 45–48 |
| 78 | #73–80 | [Teknium](https://github.com/Teknium) | 18 | 27 | 45–48 |
| 79 | #73–81 | [Frowtek](https://github.com/Frowtek) | 41 | 3 | 44–47 |
| 80 | #75–82 | [nftpoetrist](https://github.com/nftpoetrist) | 36 | 7 | 43–46 |
| 81 | #77–83 | [mojomast](https://github.com/mojomast) | 39 | 3 | 42–45 |
| 82 | #79–85 | [wesleysimplicio](https://github.com/wesleysimplicio) | 40 | 1 | 41–44 |
| 83 | #80–88 | [jackulau](https://github.com/jackulau) | 36 | 4 | 40–43 |
| 84 | #81–91 | [mnajafian-nv](https://github.com/mnajafian-nv) | 38 | 1 | 39–42 |
| 85 | #81–91 | [Rafa-Ross](https://github.com/Rafa-Ross) | 19 | 20 | 39–42 |
| 86 | #82–96 | [andrexibiza](https://github.com/andrexibiza) | 23 | 15 | 38–41 |
| 87 | #82–96 | [Drexuxux](https://github.com/Drexuxux) | 36 | 2 | 38–41 |
| 88 | #82–96 | [GottZ](https://github.com/GottZ) | 36 | 2 | 38–41 |
| 89 | #83–100 | [adybag14-cyber](https://github.com/adybag14-cyber) | 36 | 1 | 37–40 |
| 90 | #83–100 | [ayushnangia](https://github.com/ayushnangia) | 36 | 1 | 37–40 |
| 91 | #83–100 | [ooiuuii](https://github.com/ooiuuii) | 33 | 4 | 37–40 |
| 92 | #84–103 | [calvinnwq](https://github.com/calvinnwq) | 36 | 0 | 36–39 |
| 93 | #84–103 | [Christopher-Schulze](https://github.com/Christopher-Schulze) | 31 | 5 | 36–39 |
| 94 | #84–103 | [lEWFkRAD](https://github.com/lEWFkRAD) | 33 | 3 | 36–39 |
| 95 | #84–103 | [r266-tech](https://github.com/r266-tech) | 33 | 3 | 36–39 |
| 96 | #84–103 | [vdimarco](https://github.com/vdimarco) | 36 | 0 | 36–39 |
| 97 | #86–105 | [Enough1122](https://github.com/Enough1122) | 26 | 9 | 35–38 |
| 98 | #86–105 | [Kyzcreig](https://github.com/Kyzcreig) | 22 | 13 | 35–38 |
| 99 | #86–105 | [MohamadKanso](https://github.com/MohamadKanso) | 21 | 14 | 35–38 |
| 100 | #86–105 | [nousbot-eng](https://github.com/nousbot-eng) | 35 | 0 | 35–38 |
