# Hermes Agent contribution audit

This is a **custom primary-plus-coauthor ranking**, not GitHub Insights or the REST contributors ranking.

Generated: 2026-11-06T12:31:32Z

Source: [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent), default branch `main`, pinned commit [`90d6b98fd86d20981ee06ddd5b7d93e4320f26a4`](https://github.com/NousResearch/hermes-agent/commit/90d6b98fd86d20981ee06ddd5b7d93e4320f26a4).

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

- Completed history pages: 629; declared history total: 62,833; independent Git ancestry: 62,833 commits.
- Resolved author records: 62,830; unresolved commit objects: 3. Their disjoint SHA sets exactly cover all 62,833 reachable commits.
- Initial GraphQL history: 62,830 unique commits; duplicate history rows: 3; resolved by direct SHA queries: 0.
- Among resolved commits only: at least one linked account on 61,415; no linked account on 1,415. Unresolved commit objects are not included in either figure.
- Among resolved commits only: any unlinked author on 1,886; unlinked author entries: 1,909.
- Linked account-commit credits: 66,210; accounts: 4,492. A commit credited to multiple accounts contributes once to each account.
- GraphQL requests: 636; reported query cost: 636; remaining rate-limit points: 4499.

## Uncertainty bounds

There are **U = 3** unresolved commit objects. Each account's complete total lies between its verified total and that total plus U. An unresolved commit can credit multiple accounts, so it is not allocated as one exclusive credit.

The best possible rank is 1 plus the number of other known totals strictly above the account's upper total. The worst possible rank is 1 plus the number of other upper totals strictly above its known total. When the known total is below U, previously unseen accounts may also exceed it; the available evidence provides no finite worst-rank guarantee, shown as `unverified` and `rank_max: null`.

A rank is exact only when its lower and upper bounds coincide. Unknown authorship is never interpreted as zero contribution. The JSON `rank` field ranks known credits only; `rank_min`, `rank_max`, and `rank_is_exact` govern the displayed complete rank.

Unresolved commit SHAs: [`722acd66f62f7617a0df3b5af919d257a35fc258`](https://github.com/NousResearch/hermes-agent/commit/722acd66f62f7617a0df3b5af919d257a35fc258), [`8239ec483323d7f447a7fe708d58b77ed405916f`](https://github.com/NousResearch/hermes-agent/commit/8239ec483323d7f447a7fe708d58b77ed405916f), [`aa0beef6848bd9cdcf1a7015cebc8dfc6170cf5b`](https://github.com/NousResearch/hermes-agent/commit/aa0beef6848bd9cdcf1a7015cebc8dfc6170cf5b).

## KoNit-K

Verified commits: **397** · verified primary: **301** · verified coauthor-only: **96**.

Complete total: **397–400** · complete custom rank: **#17** · rank determined: **yes**. Primary/coauthor SHA evidence is retained in the [complete JSON](hermes-contributions.json).

## First 100 contributor rows

Rows are ordered by verified totals and include positions 5–20 where present. Row position and the known-credit rank are not substituted for an uncertain complete rank.

| Known-credit position | Complete rank | Account | Verified primary | Verified coauthor-only | Complete total |
| ---: | ---: | --- | ---: | ---: | ---: |
| 1 | #1 | [teknium1](https://github.com/teknium1) | 26,223 | 79 | 26,302–26,305 |
| 2 | #2 | [kshitijk4poor](https://github.com/kshitijk4poor) | 5,533 | 55 | 5,588–5,591 |
| 3 | #3 | [OutThisLife](https://github.com/OutThisLife) | 4,579 | 31 | 4,610–4,613 |
| 4 | #4 | [ethernet8023](https://github.com/ethernet8023) | 2,367 | 4 | 2,371–2,374 |
| 5 | #5 | [claude](https://github.com/claude) | 13 | 1,020 | 1,033–1,036 |
| 6 | #6 | [unsupportedpastels](https://github.com/unsupportedpastels) | 959 | 14 | 973–976 |
| 7 | #7 | [alt-glitch](https://github.com/alt-glitch) | 894 | 7 | 901–904 |
| 8 | #8 | [liuhao1024](https://github.com/liuhao1024) | 590 | 119 | 709–712 |
| 9 | #9 | [benbarclay](https://github.com/benbarclay) | 616 | 18 | 634–637 |
| 10 | #10 | [jquesnelle](https://github.com/jquesnelle) | 513 | 7 | 520–523 |
| 11 | #11 | [austinpickett](https://github.com/austinpickett) | 480 | 12 | 492–495 |
| 12 | #12 | [github-actions[bot]](https://github.com/github-actions[bot]) | 10 | 438 | 448–451 |
| 13 | #13–14 | [fangliquanflq](https://github.com/fangliquanflq) | 364 | 56 | 420–423 |
| 14 | #13–14 | [helix4u](https://github.com/helix4u) | 398 | 22 | 420–423 |
| 15 | #15 | [JoaoMarcos44](https://github.com/JoaoMarcos44) | 327 | 89 | 416–419 |
| 16 | #16 | [hermes-seaeye[bot]](https://github.com/hermes-seaeye[bot]) | 401 | 1 | 402–405 |
| 17 | #17 | [KoNit-K](https://github.com/KoNit-K) | 301 | 96 | 397–400 |
| 18 | #18 | [c2h5oh](https://github.com/c2h5oh) | 392 | 0 | 392–395 |
| 19 | #19 | [xxxigm](https://github.com/xxxigm) | 311 | 38 | 349–352 |
| 20 | #20 | [yoniebans](https://github.com/yoniebans) | 297 | 4 | 301–304 |
| 21 | #21 | [jonpol01](https://github.com/jonpol01) | 262 | 31 | 293–296 |
| 22 | #22 | [erosika](https://github.com/erosika) | 256 | 6 | 262–265 |
| 23 | #23 | [0xbyt4](https://github.com/0xbyt4) | 201 | 12 | 213–216 |
| 24 | #23–24 | [dokterdok](https://github.com/dokterdok) | 191 | 19 | 210–213 |
| 25 | #25 | [HexLab98](https://github.com/HexLab98) | 193 | 13 | 206–209 |
| 26 | #26 | [Adolanium](https://github.com/Adolanium) | 193 | 7 | 200–203 |
| 27 | #27–28 | [cursoragent](https://github.com/cursoragent) | 15 | 165 | 180–183 |
| 28 | #27–28 | [victor-kyriazakos](https://github.com/victor-kyriazakos) | 173 | 7 | 180–183 |
| 29 | #29–30 | [afourniernv](https://github.com/afourniernv) | 171 | 0 | 171–174 |
| 30 | #29–30 | [kokhlo](https://github.com/kokhlo) | 129 | 40 | 169–172 |
| 31 | #31 | [briandevans](https://github.com/briandevans) | 155 | 10 | 165–168 |
| 32 | #32 | [Finn763](https://github.com/Finn763) | 122 | 35 | 157–160 |
| 33 | #33 | [dskwe](https://github.com/dskwe) | 126 | 25 | 151–154 |
| 34 | #34 | [itpartypattaya](https://github.com/itpartypattaya) | 140 | 0 | 140–143 |
| 35 | #34–36 | [LeonSGP43](https://github.com/LeonSGP43) | 108 | 29 | 137–140 |
| 36 | #35–36 | [chelsealong](https://github.com/chelsealong) | 121 | 15 | 136–139 |
| 37 | #37 | [DavidMetcalfe](https://github.com/DavidMetcalfe) | 113 | 17 | 130–133 |
| 38 | #38 | [webtecnica](https://github.com/webtecnica) | 86 | 38 | 124–127 |
| 39 | #39–40 | [Tranquil-Flow](https://github.com/Tranquil-Flow) | 88 | 20 | 108–111 |
| 40 | #39–40 | [SHL0MS](https://github.com/SHL0MS) | 95 | 11 | 106–109 |
| 41 | #41 | [686f6c61](https://github.com/686f6c61) | 80 | 20 | 100–103 |
| 42 | #42 | [BearHuddleston](https://github.com/BearHuddleston) | 85 | 11 | 96–99 |
| 43 | #43–44 | [Wenfengcheng](https://github.com/Wenfengcheng) | 81 | 10 | 91–94 |
| 44 | #43–44 | [ygd58](https://github.com/ygd58) | 56 | 33 | 89–92 |
| 45 | #45 | [shannonsands](https://github.com/shannonsands) | 82 | 0 | 82–85 |
| 46 | #46–47 | [PRATHAMESH75](https://github.com/PRATHAMESH75) | 70 | 8 | 78–81 |
| 47 | #46–48 | [apoapostolov](https://github.com/apoapostolov) | 75 | 1 | 76–79 |
| 48 | #47–51 | [Bartok9](https://github.com/Bartok9) | 61 | 13 | 74–77 |
| 49 | #47–52 | [konsisumer](https://github.com/konsisumer) | 63 | 10 | 73–76 |
| 50 | #48–52 | [beardthelion](https://github.com/beardthelion) | 68 | 4 | 72–75 |
| 51 | #48–52 | [TakeshiTGAL](https://github.com/TakeshiTGAL) | 72 | 0 | 72–75 |
| 52 | #48–52 | [ehz0ah](https://github.com/ehz0ah) | 63 | 8 | 71–74 |
| 53 | #53–54 | [aydnOktay](https://github.com/aydnOktay) | 45 | 21 | 66–69 |
| 54 | #53–55 | [100yenadmin](https://github.com/100yenadmin) | 58 | 6 | 64–67 |
| 55 | #54–55 | [Halldrix](https://github.com/Halldrix) | 54 | 8 | 62–65 |
| 56 | #56 | [kvnloo](https://github.com/kvnloo) | 42 | 16 | 58–61 |
| 57 | #57–64 | [AhmetArif0](https://github.com/AhmetArif0) | 52 | 2 | 54–57 |
| 58 | #57–64 | [capthvnsen](https://github.com/capthvnsen) | 54 | 0 | 54–57 |
| 59 | #57–67 | [salch-cred](https://github.com/salch-cred) | 37 | 16 | 53–56 |
| 60 | #57–67 | [Xipong](https://github.com/Xipong) | 48 | 5 | 53–56 |
| 61 | #57–67 | [bbednarski9](https://github.com/bbednarski9) | 52 | 0 | 52–55 |
| 62 | #57–67 | [frizikk](https://github.com/frizikk) | 46 | 6 | 52–55 |
| 63 | #57–67 | [Froraut](https://github.com/Froraut) | 35 | 17 | 52–55 |
| 64 | #57–67 | [necoweb3](https://github.com/necoweb3) | 48 | 4 | 52–55 |
| 65 | #57–70 | [dyiapanis](https://github.com/dyiapanis) | 51 | 0 | 51–54 |
| 66 | #57–70 | [entropidelic](https://github.com/entropidelic) | 51 | 0 | 51–54 |
| 67 | #57–70 | [olric3015](https://github.com/olric3015) | 51 | 0 | 51–54 |
| 68 | #61–74 | [EloquentBrush0x](https://github.com/EloquentBrush0x) | 49 | 0 | 49–52 |
| 69 | #61–74 | [pierrenode](https://github.com/pierrenode) | 38 | 11 | 49–52 |
| 70 | #61–74 | [sprmn24](https://github.com/sprmn24) | 42 | 7 | 49–52 |
| 71 | #68–78 | [embwl0x](https://github.com/embwl0x) | 42 | 5 | 47–50 |
| 72 | #68–78 | [itsflownium](https://github.com/itsflownium) | 39 | 8 | 47–50 |
| 73 | #68–78 | [rewbs](https://github.com/rewbs) | 46 | 1 | 47–50 |
| 74 | #68–78 | [Sahil-SS9](https://github.com/Sahil-SS9) | 43 | 4 | 47–50 |
| 75 | #68–79 | [rob-maron](https://github.com/rob-maron) | 45 | 1 | 46–49 |
| 76 | #68–79 | [whyyagswhy](https://github.com/whyyagswhy) | 35 | 11 | 46–49 |
| 77 | #71–80 | [srojk34](https://github.com/srojk34) | 43 | 2 | 45–48 |
| 78 | #71–80 | [Teknium](https://github.com/Teknium) | 18 | 27 | 45–48 |
| 79 | #71–80 | [Frowtek](https://github.com/Frowtek) | 41 | 3 | 44–47 |
| 80 | #75–81 | [nftpoetrist](https://github.com/nftpoetrist) | 36 | 7 | 43–46 |
| 81 | #79–84 | [wesleysimplicio](https://github.com/wesleysimplicio) | 40 | 1 | 41–44 |
| 82 | #80–86 | [jackulau](https://github.com/jackulau) | 36 | 4 | 40–43 |
| 83 | #81–88 | [mnajafian-nv](https://github.com/mnajafian-nv) | 38 | 1 | 39–42 |
| 84 | #81–88 | [Rafa-Ross](https://github.com/Rafa-Ross) | 19 | 20 | 39–42 |
| 85 | #81–90 | [andrexibiza](https://github.com/andrexibiza) | 23 | 15 | 38–41 |
| 86 | #81–90 | [Drexuxux](https://github.com/Drexuxux) | 36 | 2 | 38–41 |
| 87 | #82–93 | [adybag14-cyber](https://github.com/adybag14-cyber) | 36 | 1 | 37–40 |
| 88 | #82–93 | [ayushnangia](https://github.com/ayushnangia) | 36 | 1 | 37–40 |
| 89 | #83–98 | [Christopher-Schulze](https://github.com/Christopher-Schulze) | 31 | 5 | 36–39 |
| 90 | #83–98 | [ooiuuii](https://github.com/ooiuuii) | 32 | 4 | 36–39 |
| 91 | #85–101 | [Kyzcreig](https://github.com/Kyzcreig) | 22 | 13 | 35–38 |
| 92 | #85–101 | [MohamadKanso](https://github.com/MohamadKanso) | 21 | 14 | 35–38 |
| 93 | #85–101 | [nousbot-eng](https://github.com/nousbot-eng) | 35 | 0 | 35–38 |
| 94 | #87–103 | [anpicasso](https://github.com/anpicasso) | 26 | 8 | 34–37 |
| 95 | #87–103 | [Dusk1e](https://github.com/Dusk1e) | 30 | 4 | 34–37 |
| 96 | #87–103 | [Enough1122](https://github.com/Enough1122) | 26 | 8 | 34–37 |
| 97 | #87–103 | [GottZ](https://github.com/GottZ) | 32 | 2 | 34–37 |
| 98 | #87–103 | [r266-tech](https://github.com/r266-tech) | 31 | 3 | 34–37 |
| 99 | #89–105 | [IAvecilla](https://github.com/IAvecilla) | 31 | 2 | 33–36 |
| 100 | #89–105 | [izumi0uu](https://github.com/izumi0uu) | 24 | 9 | 33–36 |
