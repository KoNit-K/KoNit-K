# Hermes Agent contribution audit

This is a **custom primary-plus-coauthor ranking**, not GitHub Insights or the REST contributors ranking.

Generated: 2026-10-28T10:54:11Z

Source: [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent), default branch `main`, pinned commit [`8acb7f65801fa7548b223244dee57465adfda8ec`](https://github.com/NousResearch/hermes-agent/commit/8acb7f65801fa7548b223244dee57465adfda8ec).

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

- Completed history pages: 602; declared history total: 60,107; independent Git ancestry: 60,107 commits.
- Resolved author records: 60,104; unresolved commit objects: 3. Their disjoint SHA sets exactly cover all 60,107 reachable commits.
- Initial GraphQL history: 60,104 unique commits; duplicate history rows: 3; resolved by direct SHA queries: 0.
- Among resolved commits only: at least one linked account on 58,728; no linked account on 1,376. Unresolved commit objects are not included in either figure.
- Among resolved commits only: any unlinked author on 1,837; unlinked author entries: 1,860.
- Linked account-commit credits: 63,422; accounts: 4,321. A commit credited to multiple accounts contributes once to each account.
- GraphQL requests: 609; reported query cost: 609; remaining rate-limit points: 4664.

## Uncertainty bounds

There are **U = 3** unresolved commit objects. Each account's complete total lies between its verified total and that total plus U. An unresolved commit can credit multiple accounts, so it is not allocated as one exclusive credit.

The best possible rank is 1 plus the number of other known totals strictly above the account's upper total. The worst possible rank is 1 plus the number of other upper totals strictly above its known total. When the known total is below U, previously unseen accounts may also exceed it; the available evidence provides no finite worst-rank guarantee, shown as `unverified` and `rank_max: null`.

A rank is exact only when its lower and upper bounds coincide. Unknown authorship is never interpreted as zero contribution. The JSON `rank` field ranks known credits only; `rank_min`, `rank_max`, and `rank_is_exact` govern the displayed complete rank.

Unresolved commit SHAs: [`722acd66f62f7617a0df3b5af919d257a35fc258`](https://github.com/NousResearch/hermes-agent/commit/722acd66f62f7617a0df3b5af919d257a35fc258), [`8239ec483323d7f447a7fe708d58b77ed405916f`](https://github.com/NousResearch/hermes-agent/commit/8239ec483323d7f447a7fe708d58b77ed405916f), [`aa0beef6848bd9cdcf1a7015cebc8dfc6170cf5b`](https://github.com/NousResearch/hermes-agent/commit/aa0beef6848bd9cdcf1a7015cebc8dfc6170cf5b).

## KoNit-K

Verified commits: **393** · verified primary: **297** · verified coauthor-only: **96**.

Complete total: **393–396** · complete custom rank: **#17** · rank determined: **yes**. Primary/coauthor SHA evidence is retained in the [complete JSON](hermes-contributions.json).

## First 100 contributor rows

Rows are ordered by verified totals and include positions 5–20 where present. Row position and the known-credit rank are not substituted for an uncertain complete rank.

| Known-credit position | Complete rank | Account | Verified primary | Verified coauthor-only | Complete total |
| ---: | ---: | --- | ---: | ---: | ---: |
| 1 | #1 | [teknium1](https://github.com/teknium1) | 25,031 | 78 | 25,109–25,112 |
| 2 | #2 | [kshitijk4poor](https://github.com/kshitijk4poor) | 5,279 | 54 | 5,333–5,336 |
| 3 | #3 | [OutThisLife](https://github.com/OutThisLife) | 4,578 | 31 | 4,609–4,612 |
| 4 | #4 | [ethernet8023](https://github.com/ethernet8023) | 2,356 | 4 | 2,360–2,363 |
| 5 | #5 | [claude](https://github.com/claude) | 6 | 965 | 971–974 |
| 6 | #6 | [alt-glitch](https://github.com/alt-glitch) | 894 | 7 | 901–904 |
| 7 | #7 | [unsupportedpastels](https://github.com/unsupportedpastels) | 810 | 14 | 824–827 |
| 8 | #8 | [liuhao1024](https://github.com/liuhao1024) | 582 | 116 | 698–701 |
| 9 | #9 | [benbarclay](https://github.com/benbarclay) | 588 | 18 | 606–609 |
| 10 | #10 | [jquesnelle](https://github.com/jquesnelle) | 506 | 7 | 513–516 |
| 11 | #11 | [austinpickett](https://github.com/austinpickett) | 474 | 12 | 486–489 |
| 12 | #12 | [github-actions[bot]](https://github.com/github-actions[bot]) | 10 | 438 | 448–451 |
| 13 | #13–14 | [fangliquanflq](https://github.com/fangliquanflq) | 363 | 55 | 418–421 |
| 14 | #13–14 | [JoaoMarcos44](https://github.com/JoaoMarcos44) | 327 | 89 | 416–419 |
| 15 | #15 | [helix4u](https://github.com/helix4u) | 390 | 20 | 410–413 |
| 16 | #16 | [hermes-seaeye[bot]](https://github.com/hermes-seaeye[bot]) | 401 | 1 | 402–405 |
| 17 | #17 | [KoNit-K](https://github.com/KoNit-K) | 297 | 96 | 393–396 |
| 18 | #18 | [xxxigm](https://github.com/xxxigm) | 304 | 38 | 342–345 |
| 19 | #19 | [c2h5oh](https://github.com/c2h5oh) | 321 | 0 | 321–324 |
| 20 | #20 | [jonpol01](https://github.com/jonpol01) | 261 | 31 | 292–295 |
| 21 | #21 | [yoniebans](https://github.com/yoniebans) | 276 | 4 | 280–283 |
| 22 | #22 | [erosika](https://github.com/erosika) | 256 | 6 | 262–265 |
| 23 | #23 | [0xbyt4](https://github.com/0xbyt4) | 201 | 12 | 213–216 |
| 24 | #24 | [HexLab98](https://github.com/HexLab98) | 193 | 13 | 206–209 |
| 25 | #25 | [dokterdok](https://github.com/dokterdok) | 168 | 19 | 187–190 |
| 26 | #25–26 | [Adolanium](https://github.com/Adolanium) | 178 | 6 | 184–187 |
| 27 | #27 | [cursoragent](https://github.com/cursoragent) | 15 | 165 | 180–183 |
| 28 | #28 | [afourniernv](https://github.com/afourniernv) | 171 | 0 | 171–174 |
| 29 | #29 | [kokhlo](https://github.com/kokhlo) | 127 | 40 | 167–170 |
| 30 | #30 | [briandevans](https://github.com/briandevans) | 153 | 10 | 163–166 |
| 31 | #31–32 | [Finn763](https://github.com/Finn763) | 122 | 35 | 157–160 |
| 32 | #31–32 | [victor-kyriazakos](https://github.com/victor-kyriazakos) | 149 | 7 | 156–159 |
| 33 | #33 | [dskwe](https://github.com/dskwe) | 121 | 25 | 146–149 |
| 34 | #34–35 | [chelsealong](https://github.com/chelsealong) | 121 | 15 | 136–139 |
| 35 | #34–35 | [LeonSGP43](https://github.com/LeonSGP43) | 108 | 28 | 136–139 |
| 36 | #36 | [DavidMetcalfe](https://github.com/DavidMetcalfe) | 113 | 17 | 130–133 |
| 37 | #37 | [webtecnica](https://github.com/webtecnica) | 86 | 38 | 124–127 |
| 38 | #38–39 | [Tranquil-Flow](https://github.com/Tranquil-Flow) | 88 | 20 | 108–111 |
| 39 | #38–39 | [SHL0MS](https://github.com/SHL0MS) | 95 | 11 | 106–109 |
| 40 | #40 | [itpartypattaya](https://github.com/itpartypattaya) | 102 | 0 | 102–105 |
| 41 | #41 | [686f6c61](https://github.com/686f6c61) | 78 | 20 | 98–101 |
| 42 | #42 | [Wenfengcheng](https://github.com/Wenfengcheng) | 81 | 10 | 91–94 |
| 43 | #42–43 | [ygd58](https://github.com/ygd58) | 55 | 33 | 88–91 |
| 44 | #44 | [shannonsands](https://github.com/shannonsands) | 81 | 0 | 81–84 |
| 45 | #45 | [PRATHAMESH75](https://github.com/PRATHAMESH75) | 69 | 8 | 77–80 |
| 46 | #45–48 | [Bartok9](https://github.com/Bartok9) | 61 | 13 | 74–77 |
| 47 | #46–49 | [konsisumer](https://github.com/konsisumer) | 63 | 10 | 73–76 |
| 48 | #46–49 | [beardthelion](https://github.com/beardthelion) | 68 | 4 | 72–75 |
| 49 | #46–49 | [ehz0ah](https://github.com/ehz0ah) | 63 | 8 | 71–74 |
| 50 | #50–51 | [apoapostolov](https://github.com/apoapostolov) | 65 | 1 | 66–69 |
| 51 | #50–51 | [aydnOktay](https://github.com/aydnOktay) | 45 | 21 | 66–69 |
| 52 | #52–54 | [Halldrix](https://github.com/Halldrix) | 54 | 8 | 62–65 |
| 53 | #52–54 | [100yenadmin](https://github.com/100yenadmin) | 55 | 6 | 61–64 |
| 54 | #52–54 | [TakeshiTGAL](https://github.com/TakeshiTGAL) | 60 | 0 | 60–63 |
| 55 | #54–55 | [kvnloo](https://github.com/kvnloo) | 41 | 16 | 57–60 |
| 56 | #55–62 | [AhmetArif0](https://github.com/AhmetArif0) | 52 | 2 | 54–57 |
| 57 | #55–62 | [capthvnsen](https://github.com/capthvnsen) | 54 | 0 | 54–57 |
| 58 | #56–63 | [salch-cred](https://github.com/salch-cred) | 37 | 16 | 53–56 |
| 59 | #56–63 | [Xipong](https://github.com/Xipong) | 48 | 5 | 53–56 |
| 60 | #56–63 | [bbednarski9](https://github.com/bbednarski9) | 52 | 0 | 52–55 |
| 61 | #56–63 | [frizikk](https://github.com/frizikk) | 46 | 6 | 52–55 |
| 62 | #56–63 | [necoweb3](https://github.com/necoweb3) | 48 | 4 | 52–55 |
| 63 | #56–66 | [entropidelic](https://github.com/entropidelic) | 51 | 0 | 51–54 |
| 64 | #60–68 | [EloquentBrush0x](https://github.com/EloquentBrush0x) | 49 | 0 | 49–52 |
| 65 | #60–68 | [pierrenode](https://github.com/pierrenode) | 38 | 11 | 49–52 |
| 66 | #60–68 | [sprmn24](https://github.com/sprmn24) | 42 | 7 | 49–52 |
| 67 | #64–74 | [olric3015](https://github.com/olric3015) | 47 | 0 | 47–50 |
| 68 | #64–74 | [rewbs](https://github.com/rewbs) | 46 | 1 | 47–50 |
| 69 | #64–76 | [embwl0x](https://github.com/embwl0x) | 42 | 4 | 46–49 |
| 70 | #64–76 | [rob-maron](https://github.com/rob-maron) | 45 | 1 | 46–49 |
| 71 | #64–76 | [Sahil-SS9](https://github.com/Sahil-SS9) | 42 | 4 | 46–49 |
| 72 | #64–76 | [whyyagswhy](https://github.com/whyyagswhy) | 35 | 11 | 46–49 |
| 73 | #67–77 | [srojk34](https://github.com/srojk34) | 43 | 2 | 45–48 |
| 74 | #67–77 | [Teknium](https://github.com/Teknium) | 18 | 27 | 45–48 |
| 75 | #67–77 | [Froraut](https://github.com/Froraut) | 28 | 16 | 44–47 |
| 76 | #67–77 | [Frowtek](https://github.com/Frowtek) | 41 | 3 | 44–47 |
| 77 | #69–78 | [nftpoetrist](https://github.com/nftpoetrist) | 36 | 7 | 43–46 |
| 78 | #75–80 | [wesleysimplicio](https://github.com/wesleysimplicio) | 40 | 1 | 41–44 |
| 79 | #77–84 | [jackulau](https://github.com/jackulau) | 36 | 4 | 40–43 |
| 80 | #78–86 | [Rafa-Ross](https://github.com/Rafa-Ross) | 19 | 20 | 39–42 |
| 81 | #78–88 | [andrexibiza](https://github.com/andrexibiza) | 23 | 15 | 38–41 |
| 82 | #78–88 | [Drexuxux](https://github.com/Drexuxux) | 36 | 2 | 38–41 |
| 83 | #78–88 | [itsflownium](https://github.com/itsflownium) | 32 | 6 | 38–41 |
| 84 | #78–88 | [mnajafian-nv](https://github.com/mnajafian-nv) | 37 | 1 | 38–41 |
| 85 | #79–91 | [adybag14-cyber](https://github.com/adybag14-cyber) | 36 | 1 | 37–40 |
| 86 | #79–91 | [ayushnangia](https://github.com/ayushnangia) | 36 | 1 | 37–40 |
| 87 | #80–94 | [Christopher-Schulze](https://github.com/Christopher-Schulze) | 31 | 5 | 36–39 |
| 88 | #80–94 | [ooiuuii](https://github.com/ooiuuii) | 32 | 4 | 36–39 |
| 89 | #81–96 | [Kyzcreig](https://github.com/Kyzcreig) | 22 | 13 | 35–38 |
| 90 | #81–96 | [MohamadKanso](https://github.com/MohamadKanso) | 21 | 14 | 35–38 |
| 91 | #81–96 | [nousbot-eng](https://github.com/nousbot-eng) | 35 | 0 | 35–38 |
| 92 | #85–98 | [anpicasso](https://github.com/anpicasso) | 26 | 8 | 34–37 |
| 93 | #85–98 | [Dusk1e](https://github.com/Dusk1e) | 30 | 4 | 34–37 |
| 94 | #85–98 | [Enough1122](https://github.com/Enough1122) | 26 | 8 | 34–37 |
| 95 | #87–100 | [izumi0uu](https://github.com/izumi0uu) | 24 | 9 | 33–36 |
| 96 | #87–100 | [zapabob](https://github.com/zapabob) | 21 | 12 | 33–36 |
| 97 | #89–107 | [BearHuddleston](https://github.com/BearHuddleston) | 31 | 1 | 32–35 |
| 98 | #89–107 | [HenkDz](https://github.com/HenkDz) | 29 | 3 | 32–35 |
| 99 | #92–110 | [notwitcheer](https://github.com/notwitcheer) | 30 | 1 | 31–34 |
| 100 | #92–110 | [pefontana](https://github.com/pefontana) | 30 | 1 | 31–34 |
