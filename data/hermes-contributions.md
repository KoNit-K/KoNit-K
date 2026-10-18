# Hermes Agent contribution audit

This is a **custom primary-plus-coauthor ranking**, not GitHub Insights or the REST contributors ranking.

Generated: 2026-10-18T13:10:19Z

Source: [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent), default branch `main`, pinned commit [`9e01b44dd23978f9ff40b7837467f3a9f1582130`](https://github.com/NousResearch/hermes-agent/commit/9e01b44dd23978f9ff40b7837467f3a9f1582130).

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

- Completed history pages: 562; declared history total: 56,144; independent Git ancestry: 56,144 commits.
- Resolved author records: 56,141; unresolved commit objects: 3. Their disjoint SHA sets exactly cover all 56,144 reachable commits.
- Initial GraphQL history: 56,141 unique commits; duplicate history rows: 3; resolved by direct SHA queries: 0.
- Among resolved commits only: at least one linked account on 54,840; no linked account on 1,301. Unresolved commit objects are not included in either figure.
- Among resolved commits only: any unlinked author on 1,739; unlinked author entries: 1,760.
- Linked account-commit credits: 59,386; accounts: 4,147. A commit credited to multiple accounts contributes once to each account.
- GraphQL requests: 569; reported query cost: 569; remaining rate-limit points: 4779.

## Uncertainty bounds

There are **U = 3** unresolved commit objects. Each account's complete total lies between its verified total and that total plus U. An unresolved commit can credit multiple accounts, so it is not allocated as one exclusive credit.

The best possible rank is 1 plus the number of other known totals strictly above the account's upper total. The worst possible rank is 1 plus the number of other upper totals strictly above its known total. When the known total is below U, previously unseen accounts may also exceed it; the available evidence provides no finite worst-rank guarantee, shown as `unverified` and `rank_max: null`.

A rank is exact only when its lower and upper bounds coincide. Unknown authorship is never interpreted as zero contribution. The JSON `rank` field ranks known credits only; `rank_min`, `rank_max`, and `rank_is_exact` govern the displayed complete rank.

Unresolved commit SHAs: [`722acd66f62f7617a0df3b5af919d257a35fc258`](https://github.com/NousResearch/hermes-agent/commit/722acd66f62f7617a0df3b5af919d257a35fc258), [`8239ec483323d7f447a7fe708d58b77ed405916f`](https://github.com/NousResearch/hermes-agent/commit/8239ec483323d7f447a7fe708d58b77ed405916f), [`aa0beef6848bd9cdcf1a7015cebc8dfc6170cf5b`](https://github.com/NousResearch/hermes-agent/commit/aa0beef6848bd9cdcf1a7015cebc8dfc6170cf5b).

## KoNit-K

Verified commits: **382** · verified primary: **288** · verified coauthor-only: **94**.

Complete total: **382–385** · complete custom rank: **#16** · rank determined: **yes**. Primary/coauthor SHA evidence is retained in the [complete JSON](hermes-contributions.json).

## First 100 contributor rows

Rows are ordered by verified totals and include positions 5–20 where present. Row position and the known-credit rank are not substituted for an uncertain complete rank.

| Known-credit position | Complete rank | Account | Verified primary | Verified coauthor-only | Complete total |
| ---: | ---: | --- | ---: | ---: | ---: |
| 1 | #1 | [teknium1](https://github.com/teknium1) | 23,162 | 75 | 23,237–23,240 |
| 2 | #2 | [kshitijk4poor](https://github.com/kshitijk4poor) | 5,089 | 54 | 5,143–5,146 |
| 3 | #3 | [OutThisLife](https://github.com/OutThisLife) | 4,560 | 30 | 4,590–4,593 |
| 4 | #4 | [ethernet8023](https://github.com/ethernet8023) | 2,286 | 4 | 2,290–2,293 |
| 5 | #5 | [claude](https://github.com/claude) | 5 | 893 | 898–901 |
| 6 | #6 | [alt-glitch](https://github.com/alt-glitch) | 839 | 7 | 846–849 |
| 7 | #7 | [liuhao1024](https://github.com/liuhao1024) | 570 | 112 | 682–685 |
| 8 | #8 | [benbarclay](https://github.com/benbarclay) | 533 | 17 | 550–553 |
| 9 | #9 | [unsupportedpastels](https://github.com/unsupportedpastels) | 525 | 7 | 532–535 |
| 10 | #10 | [github-actions[bot]](https://github.com/github-actions[bot]) | 10 | 438 | 448–451 |
| 11 | #11 | [austinpickett](https://github.com/austinpickett) | 422 | 11 | 433–436 |
| 12 | #12–13 | [JoaoMarcos44](https://github.com/JoaoMarcos44) | 327 | 89 | 416–419 |
| 13 | #12–13 | [fangliquanflq](https://github.com/fangliquanflq) | 360 | 54 | 414–417 |
| 14 | #14–15 | [helix4u](https://github.com/helix4u) | 382 | 20 | 402–405 |
| 15 | #14–15 | [hermes-seaeye[bot]](https://github.com/hermes-seaeye[bot]) | 401 | 1 | 402–405 |
| 16 | #16 | [KoNit-K](https://github.com/KoNit-K) | 288 | 94 | 382–385 |
| 17 | #17 | [jquesnelle](https://github.com/jquesnelle) | 336 | 3 | 339–342 |
| 18 | #18 | [xxxigm](https://github.com/xxxigm) | 296 | 36 | 332–335 |
| 19 | #19 | [jonpol01](https://github.com/jonpol01) | 253 | 28 | 281–284 |
| 20 | #20 | [erosika](https://github.com/erosika) | 256 | 6 | 262–265 |
| 21 | #21 | [0xbyt4](https://github.com/0xbyt4) | 201 | 12 | 213–216 |
| 22 | #22 | [HexLab98](https://github.com/HexLab98) | 193 | 13 | 206–209 |
| 23 | #23 | [yoniebans](https://github.com/yoniebans) | 198 | 2 | 200–203 |
| 24 | #24 | [cursoragent](https://github.com/cursoragent) | 15 | 161 | 176–179 |
| 25 | #25 | [afourniernv](https://github.com/afourniernv) | 171 | 0 | 171–174 |
| 26 | #26 | [kokhlo](https://github.com/kokhlo) | 127 | 39 | 166–169 |
| 27 | #26–27 | [briandevans](https://github.com/briandevans) | 153 | 10 | 163–166 |
| 28 | #28 | [Finn763](https://github.com/Finn763) | 122 | 35 | 157–160 |
| 29 | #28–29 | [victor-kyriazakos](https://github.com/victor-kyriazakos) | 147 | 7 | 154–157 |
| 30 | #30 | [dskwe](https://github.com/dskwe) | 114 | 25 | 139–142 |
| 31 | #30–32 | [LeonSGP43](https://github.com/LeonSGP43) | 108 | 28 | 136–139 |
| 32 | #31–33 | [chelsealong](https://github.com/chelsealong) | 120 | 14 | 134–137 |
| 33 | #32–33 | [Adolanium](https://github.com/Adolanium) | 126 | 6 | 132–135 |
| 34 | #33–34 | [DavidMetcalfe](https://github.com/DavidMetcalfe) | 113 | 16 | 129–132 |
| 35 | #35–36 | [dokterdok](https://github.com/dokterdok) | 106 | 17 | 123–126 |
| 36 | #35–36 | [webtecnica](https://github.com/webtecnica) | 85 | 38 | 123–126 |
| 37 | #37–38 | [c2h5oh](https://github.com/c2h5oh) | 110 | 0 | 110–113 |
| 38 | #37–38 | [Tranquil-Flow](https://github.com/Tranquil-Flow) | 88 | 20 | 108–111 |
| 39 | #39 | [SHL0MS](https://github.com/SHL0MS) | 87 | 11 | 98–101 |
| 40 | #40 | [686f6c61](https://github.com/686f6c61) | 71 | 20 | 91–94 |
| 41 | #40–42 | [Wenfengcheng](https://github.com/Wenfengcheng) | 78 | 10 | 88–91 |
| 42 | #40–42 | [ygd58](https://github.com/ygd58) | 55 | 33 | 88–91 |
| 43 | #43–44 | [shannonsands](https://github.com/shannonsands) | 81 | 0 | 81–84 |
| 44 | #43–44 | [itpartypattaya](https://github.com/itpartypattaya) | 80 | 0 | 80–83 |
| 45 | #45–47 | [PRATHAMESH75](https://github.com/PRATHAMESH75) | 67 | 8 | 75–78 |
| 46 | #45–48 | [Bartok9](https://github.com/Bartok9) | 61 | 13 | 74–77 |
| 47 | #45–48 | [konsisumer](https://github.com/konsisumer) | 63 | 10 | 73–76 |
| 48 | #45–49 | [beardthelion](https://github.com/beardthelion) | 68 | 4 | 72–75 |
| 49 | #47–49 | [ehz0ah](https://github.com/ehz0ah) | 63 | 7 | 70–73 |
| 50 | #50 | [aydnOktay](https://github.com/aydnOktay) | 44 | 21 | 65–68 |
| 51 | #51–52 | [Halldrix](https://github.com/Halldrix) | 54 | 7 | 61–64 |
| 52 | #51–52 | [apoapostolov](https://github.com/apoapostolov) | 58 | 1 | 59–62 |
| 53 | #53–60 | [AhmetArif0](https://github.com/AhmetArif0) | 52 | 2 | 54–57 |
| 54 | #53–60 | [kvnloo](https://github.com/kvnloo) | 37 | 16 | 53–56 |
| 55 | #53–60 | [Xipong](https://github.com/Xipong) | 48 | 5 | 53–56 |
| 56 | #53–60 | [100yenadmin](https://github.com/100yenadmin) | 46 | 6 | 52–55 |
| 57 | #53–60 | [bbednarski9](https://github.com/bbednarski9) | 52 | 0 | 52–55 |
| 58 | #53–60 | [frizikk](https://github.com/frizikk) | 46 | 6 | 52–55 |
| 59 | #53–60 | [kyssta-exe](https://github.com/kyssta-exe) | 37 | 15 | 52–55 |
| 60 | #53–60 | [necoweb3](https://github.com/necoweb3) | 48 | 4 | 52–55 |
| 61 | #56–66 | [capthvnsen](https://github.com/capthvnsen) | 49 | 0 | 49–52 |
| 62 | #56–66 | [EloquentBrush0x](https://github.com/EloquentBrush0x) | 49 | 0 | 49–52 |
| 63 | #56–66 | [salch-cred](https://github.com/salch-cred) | 34 | 15 | 49–52 |
| 64 | #56–66 | [sprmn24](https://github.com/sprmn24) | 42 | 7 | 49–52 |
| 65 | #61–70 | [entropidelic](https://github.com/entropidelic) | 48 | 0 | 48–51 |
| 66 | #61–70 | [pierrenode](https://github.com/pierrenode) | 38 | 10 | 48–51 |
| 67 | #61–74 | [embwl0x](https://github.com/embwl0x) | 42 | 4 | 46–49 |
| 68 | #61–74 | [rewbs](https://github.com/rewbs) | 45 | 1 | 46–49 |
| 69 | #61–74 | [TakeshiTGAL](https://github.com/TakeshiTGAL) | 46 | 0 | 46–49 |
| 70 | #61–74 | [whyyagswhy](https://github.com/whyyagswhy) | 35 | 11 | 46–49 |
| 71 | #65–75 | [srojk34](https://github.com/srojk34) | 43 | 2 | 45–48 |
| 72 | #65–75 | [Teknium](https://github.com/Teknium) | 18 | 27 | 45–48 |
| 73 | #67–75 | [Froraut](https://github.com/Froraut) | 28 | 16 | 44–47 |
| 74 | #67–75 | [Frowtek](https://github.com/Frowtek) | 41 | 3 | 44–47 |
| 75 | #67–76 | [nftpoetrist](https://github.com/nftpoetrist) | 36 | 7 | 43–46 |
| 76 | #73–80 | [wesleysimplicio](https://github.com/wesleysimplicio) | 40 | 1 | 41–44 |
| 77 | #75–83 | [jackulau](https://github.com/jackulau) | 36 | 4 | 40–43 |
| 78 | #75–83 | [rob-maron](https://github.com/rob-maron) | 39 | 1 | 40–43 |
| 79 | #75–83 | [Sahil-SS9](https://github.com/Sahil-SS9) | 36 | 4 | 40–43 |
| 80 | #76–86 | [Rafa-Ross](https://github.com/Rafa-Ross) | 19 | 20 | 39–42 |
| 81 | #76–88 | [andrexibiza](https://github.com/andrexibiza) | 23 | 15 | 38–41 |
| 82 | #76–88 | [Drexuxux](https://github.com/Drexuxux) | 36 | 2 | 38–41 |
| 83 | #76–88 | [mnajafian-nv](https://github.com/mnajafian-nv) | 37 | 1 | 38–41 |
| 84 | #77–91 | [adybag14-cyber](https://github.com/adybag14-cyber) | 36 | 1 | 37–40 |
| 85 | #77–91 | [ayushnangia](https://github.com/ayushnangia) | 36 | 1 | 37–40 |
| 86 | #77–91 | [itsflownium](https://github.com/itsflownium) | 32 | 5 | 37–40 |
| 87 | #80–94 | [Christopher-Schulze](https://github.com/Christopher-Schulze) | 31 | 5 | 36–39 |
| 88 | #80–94 | [ooiuuii](https://github.com/ooiuuii) | 32 | 4 | 36–39 |
| 89 | #81–96 | [Kyzcreig](https://github.com/Kyzcreig) | 22 | 13 | 35–38 |
| 90 | #81–96 | [nousbot-eng](https://github.com/nousbot-eng) | 35 | 0 | 35–38 |
| 91 | #81–96 | [olric3015](https://github.com/olric3015) | 35 | 0 | 35–38 |
| 92 | #84–98 | [Dusk1e](https://github.com/Dusk1e) | 30 | 4 | 34–37 |
| 93 | #84–98 | [Enough1122](https://github.com/Enough1122) | 26 | 8 | 34–37 |
| 94 | #84–98 | [MohamadKanso](https://github.com/MohamadKanso) | 21 | 13 | 34–37 |
| 95 | #87–99 | [izumi0uu](https://github.com/izumi0uu) | 24 | 9 | 33–36 |
| 96 | #87–99 | [zapabob](https://github.com/zapabob) | 21 | 12 | 33–36 |
| 97 | #89–104 | [anpicasso](https://github.com/anpicasso) | 24 | 8 | 32–35 |
| 98 | #89–104 | [HenkDz](https://github.com/HenkDz) | 29 | 3 | 32–35 |
| 99 | #92–108 | [pefontana](https://github.com/pefontana) | 30 | 1 | 31–34 |
| 100 | #95–109 | [memosr](https://github.com/memosr) | 19 | 11 | 30–33 |
