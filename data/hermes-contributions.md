# Hermes Agent contribution audit

This is a **custom primary-plus-coauthor ranking**, not GitHub Insights or the REST contributors ranking.

Generated: 2026-11-04T12:34:53Z

Source: [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent), default branch `main`, pinned commit [`71736c9f32597bbca9d89cede5aa136e55946b2f`](https://github.com/NousResearch/hermes-agent/commit/71736c9f32597bbca9d89cede5aa136e55946b2f).

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

- Completed history pages: 620; declared history total: 61,939; independent Git ancestry: 61,939 commits.
- Resolved author records: 61,936; unresolved commit objects: 3. Their disjoint SHA sets exactly cover all 61,939 reachable commits.
- Initial GraphQL history: 61,936 unique commits; duplicate history rows: 3; resolved by direct SHA queries: 0.
- Among resolved commits only: at least one linked account on 60,532; no linked account on 1,404. Unresolved commit objects are not included in either figure.
- Among resolved commits only: any unlinked author on 1,869; unlinked author entries: 1,892.
- Linked account-commit credits: 65,294; accounts: 4,429. A commit credited to multiple accounts contributes once to each account.
- GraphQL requests: 627; reported query cost: 627; remaining rate-limit points: 4512.

## Uncertainty bounds

There are **U = 3** unresolved commit objects. Each account's complete total lies between its verified total and that total plus U. An unresolved commit can credit multiple accounts, so it is not allocated as one exclusive credit.

The best possible rank is 1 plus the number of other known totals strictly above the account's upper total. The worst possible rank is 1 plus the number of other upper totals strictly above its known total. When the known total is below U, previously unseen accounts may also exceed it; the available evidence provides no finite worst-rank guarantee, shown as `unverified` and `rank_max: null`.

A rank is exact only when its lower and upper bounds coincide. Unknown authorship is never interpreted as zero contribution. The JSON `rank` field ranks known credits only; `rank_min`, `rank_max`, and `rank_is_exact` govern the displayed complete rank.

Unresolved commit SHAs: [`722acd66f62f7617a0df3b5af919d257a35fc258`](https://github.com/NousResearch/hermes-agent/commit/722acd66f62f7617a0df3b5af919d257a35fc258), [`8239ec483323d7f447a7fe708d58b77ed405916f`](https://github.com/NousResearch/hermes-agent/commit/8239ec483323d7f447a7fe708d58b77ed405916f), [`aa0beef6848bd9cdcf1a7015cebc8dfc6170cf5b`](https://github.com/NousResearch/hermes-agent/commit/aa0beef6848bd9cdcf1a7015cebc8dfc6170cf5b).

## KoNit-K

Verified commits: **395** · verified primary: **299** · verified coauthor-only: **96**.

Complete total: **395–398** · complete custom rank: **#17** · rank determined: **yes**. Primary/coauthor SHA evidence is retained in the [complete JSON](hermes-contributions.json).

## First 100 contributor rows

Rows are ordered by verified totals and include positions 5–20 where present. Row position and the known-credit rank are not substituted for an uncertain complete rank.

| Known-credit position | Complete rank | Account | Verified primary | Verified coauthor-only | Complete total |
| ---: | ---: | --- | ---: | ---: | ---: |
| 1 | #1 | [teknium1](https://github.com/teknium1) | 25,836 | 79 | 25,915–25,918 |
| 2 | #2 | [kshitijk4poor](https://github.com/kshitijk4poor) | 5,522 | 55 | 5,577–5,580 |
| 3 | #3 | [OutThisLife](https://github.com/OutThisLife) | 4,578 | 31 | 4,609–4,612 |
| 4 | #4 | [ethernet8023](https://github.com/ethernet8023) | 2,367 | 4 | 2,371–2,374 |
| 5 | #5 | [claude](https://github.com/claude) | 8 | 1,000 | 1,008–1,011 |
| 6 | #6 | [alt-glitch](https://github.com/alt-glitch) | 894 | 7 | 901–904 |
| 7 | #7 | [unsupportedpastels](https://github.com/unsupportedpastels) | 876 | 14 | 890–893 |
| 8 | #8 | [liuhao1024](https://github.com/liuhao1024) | 586 | 118 | 704–707 |
| 9 | #9 | [benbarclay](https://github.com/benbarclay) | 609 | 18 | 627–630 |
| 10 | #10 | [jquesnelle](https://github.com/jquesnelle) | 513 | 7 | 520–523 |
| 11 | #11 | [austinpickett](https://github.com/austinpickett) | 477 | 12 | 489–492 |
| 12 | #12 | [github-actions[bot]](https://github.com/github-actions[bot]) | 10 | 438 | 448–451 |
| 13 | #13–14 | [fangliquanflq](https://github.com/fangliquanflq) | 364 | 56 | 420–423 |
| 14 | #13–15 | [helix4u](https://github.com/helix4u) | 398 | 20 | 418–421 |
| 15 | #14–15 | [JoaoMarcos44](https://github.com/JoaoMarcos44) | 327 | 89 | 416–419 |
| 16 | #16 | [hermes-seaeye[bot]](https://github.com/hermes-seaeye[bot]) | 401 | 1 | 402–405 |
| 17 | #17 | [KoNit-K](https://github.com/KoNit-K) | 299 | 96 | 395–398 |
| 18 | #18 | [c2h5oh](https://github.com/c2h5oh) | 356 | 0 | 356–359 |
| 19 | #19 | [xxxigm](https://github.com/xxxigm) | 309 | 38 | 347–350 |
| 20 | #20 | [jonpol01](https://github.com/jonpol01) | 262 | 31 | 293–296 |
| 21 | #21 | [yoniebans](https://github.com/yoniebans) | 283 | 4 | 287–290 |
| 22 | #22 | [erosika](https://github.com/erosika) | 256 | 6 | 262–265 |
| 23 | #23 | [0xbyt4](https://github.com/0xbyt4) | 201 | 12 | 213–216 |
| 24 | #24 | [HexLab98](https://github.com/HexLab98) | 193 | 13 | 206–209 |
| 25 | #25 | [Adolanium](https://github.com/Adolanium) | 189 | 7 | 196–199 |
| 26 | #26 | [dokterdok](https://github.com/dokterdok) | 171 | 19 | 190–193 |
| 27 | #27 | [cursoragent](https://github.com/cursoragent) | 15 | 165 | 180–183 |
| 28 | #28 | [victor-kyriazakos](https://github.com/victor-kyriazakos) | 169 | 7 | 176–179 |
| 29 | #29–30 | [afourniernv](https://github.com/afourniernv) | 171 | 0 | 171–174 |
| 30 | #29–30 | [kokhlo](https://github.com/kokhlo) | 129 | 40 | 169–172 |
| 31 | #31 | [briandevans](https://github.com/briandevans) | 153 | 10 | 163–166 |
| 32 | #32 | [Finn763](https://github.com/Finn763) | 122 | 35 | 157–160 |
| 33 | #33 | [dskwe](https://github.com/dskwe) | 126 | 25 | 151–154 |
| 34 | #34–36 | [itpartypattaya](https://github.com/itpartypattaya) | 137 | 0 | 137–140 |
| 35 | #34–36 | [LeonSGP43](https://github.com/LeonSGP43) | 108 | 29 | 137–140 |
| 36 | #34–36 | [chelsealong](https://github.com/chelsealong) | 121 | 15 | 136–139 |
| 37 | #37 | [DavidMetcalfe](https://github.com/DavidMetcalfe) | 113 | 17 | 130–133 |
| 38 | #38 | [webtecnica](https://github.com/webtecnica) | 86 | 38 | 124–127 |
| 39 | #39–40 | [Tranquil-Flow](https://github.com/Tranquil-Flow) | 88 | 20 | 108–111 |
| 40 | #39–40 | [SHL0MS](https://github.com/SHL0MS) | 95 | 11 | 106–109 |
| 41 | #41 | [686f6c61](https://github.com/686f6c61) | 79 | 20 | 99–102 |
| 42 | #42–43 | [Wenfengcheng](https://github.com/Wenfengcheng) | 81 | 10 | 91–94 |
| 43 | #42–43 | [ygd58](https://github.com/ygd58) | 56 | 33 | 89–92 |
| 44 | #44 | [shannonsands](https://github.com/shannonsands) | 82 | 0 | 82–85 |
| 45 | #45 | [PRATHAMESH75](https://github.com/PRATHAMESH75) | 70 | 8 | 78–81 |
| 46 | #46–48 | [Bartok9](https://github.com/Bartok9) | 61 | 13 | 74–77 |
| 47 | #46–50 | [konsisumer](https://github.com/konsisumer) | 63 | 10 | 73–76 |
| 48 | #46–50 | [beardthelion](https://github.com/beardthelion) | 68 | 4 | 72–75 |
| 49 | #46–51 | [apoapostolov](https://github.com/apoapostolov) | 70 | 1 | 71–74 |
| 50 | #46–51 | [ehz0ah](https://github.com/ehz0ah) | 63 | 8 | 71–74 |
| 51 | #48–52 | [TakeshiTGAL](https://github.com/TakeshiTGAL) | 69 | 0 | 69–72 |
| 52 | #49–53 | [BearHuddleston](https://github.com/BearHuddleston) | 63 | 5 | 68–71 |
| 53 | #51–53 | [aydnOktay](https://github.com/aydnOktay) | 45 | 21 | 66–69 |
| 54 | #54–55 | [100yenadmin](https://github.com/100yenadmin) | 56 | 6 | 62–65 |
| 55 | #54–55 | [Halldrix](https://github.com/Halldrix) | 54 | 8 | 62–65 |
| 56 | #56 | [kvnloo](https://github.com/kvnloo) | 42 | 16 | 58–61 |
| 57 | #57–64 | [AhmetArif0](https://github.com/AhmetArif0) | 52 | 2 | 54–57 |
| 58 | #57–64 | [capthvnsen](https://github.com/capthvnsen) | 54 | 0 | 54–57 |
| 59 | #57–66 | [salch-cred](https://github.com/salch-cred) | 37 | 16 | 53–56 |
| 60 | #57–66 | [Xipong](https://github.com/Xipong) | 48 | 5 | 53–56 |
| 61 | #57–66 | [bbednarski9](https://github.com/bbednarski9) | 52 | 0 | 52–55 |
| 62 | #57–66 | [frizikk](https://github.com/frizikk) | 46 | 6 | 52–55 |
| 63 | #57–66 | [Froraut](https://github.com/Froraut) | 35 | 17 | 52–55 |
| 64 | #57–66 | [necoweb3](https://github.com/necoweb3) | 48 | 4 | 52–55 |
| 65 | #57–69 | [entropidelic](https://github.com/entropidelic) | 51 | 0 | 51–54 |
| 66 | #57–69 | [olric3015](https://github.com/olric3015) | 51 | 0 | 51–54 |
| 67 | #61–73 | [EloquentBrush0x](https://github.com/EloquentBrush0x) | 49 | 0 | 49–52 |
| 68 | #61–73 | [pierrenode](https://github.com/pierrenode) | 38 | 11 | 49–52 |
| 69 | #61–73 | [sprmn24](https://github.com/sprmn24) | 42 | 7 | 49–52 |
| 70 | #67–78 | [embwl0x](https://github.com/embwl0x) | 42 | 5 | 47–50 |
| 71 | #67–78 | [itsflownium](https://github.com/itsflownium) | 39 | 8 | 47–50 |
| 72 | #67–78 | [rewbs](https://github.com/rewbs) | 46 | 1 | 47–50 |
| 73 | #67–78 | [Sahil-SS9](https://github.com/Sahil-SS9) | 43 | 4 | 47–50 |
| 74 | #67–79 | [rob-maron](https://github.com/rob-maron) | 45 | 1 | 46–49 |
| 75 | #67–79 | [whyyagswhy](https://github.com/whyyagswhy) | 35 | 11 | 46–49 |
| 76 | #70–80 | [dyiapanis](https://github.com/dyiapanis) | 45 | 0 | 45–48 |
| 77 | #70–80 | [srojk34](https://github.com/srojk34) | 43 | 2 | 45–48 |
| 78 | #70–80 | [Teknium](https://github.com/Teknium) | 18 | 27 | 45–48 |
| 79 | #70–80 | [Frowtek](https://github.com/Frowtek) | 41 | 3 | 44–47 |
| 80 | #74–81 | [nftpoetrist](https://github.com/nftpoetrist) | 36 | 7 | 43–46 |
| 81 | #79–84 | [wesleysimplicio](https://github.com/wesleysimplicio) | 40 | 1 | 41–44 |
| 82 | #80–86 | [jackulau](https://github.com/jackulau) | 36 | 4 | 40–43 |
| 83 | #81–88 | [mnajafian-nv](https://github.com/mnajafian-nv) | 38 | 1 | 39–42 |
| 84 | #81–88 | [Rafa-Ross](https://github.com/Rafa-Ross) | 19 | 20 | 39–42 |
| 85 | #81–90 | [andrexibiza](https://github.com/andrexibiza) | 23 | 15 | 38–41 |
| 86 | #81–90 | [Drexuxux](https://github.com/Drexuxux) | 36 | 2 | 38–41 |
| 87 | #82–93 | [adybag14-cyber](https://github.com/adybag14-cyber) | 36 | 1 | 37–40 |
| 88 | #82–93 | [ayushnangia](https://github.com/ayushnangia) | 36 | 1 | 37–40 |
| 89 | #83–96 | [Christopher-Schulze](https://github.com/Christopher-Schulze) | 31 | 5 | 36–39 |
| 90 | #83–96 | [ooiuuii](https://github.com/ooiuuii) | 32 | 4 | 36–39 |
| 91 | #85–98 | [Kyzcreig](https://github.com/Kyzcreig) | 22 | 13 | 35–38 |
| 92 | #85–98 | [MohamadKanso](https://github.com/MohamadKanso) | 21 | 14 | 35–38 |
| 93 | #85–98 | [nousbot-eng](https://github.com/nousbot-eng) | 35 | 0 | 35–38 |
| 94 | #87–99 | [anpicasso](https://github.com/anpicasso) | 26 | 8 | 34–37 |
| 95 | #87–99 | [Dusk1e](https://github.com/Dusk1e) | 30 | 4 | 34–37 |
| 96 | #87–99 | [Enough1122](https://github.com/Enough1122) | 26 | 8 | 34–37 |
| 97 | #89–103 | [izumi0uu](https://github.com/izumi0uu) | 24 | 9 | 33–36 |
| 98 | #89–103 | [zapabob](https://github.com/zapabob) | 21 | 12 | 33–36 |
| 99 | #91–109 | [HenkDz](https://github.com/HenkDz) | 29 | 3 | 32–35 |
| 100 | #94–112 | [IAvecilla](https://github.com/IAvecilla) | 29 | 2 | 31–34 |
