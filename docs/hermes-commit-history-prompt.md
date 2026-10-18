# Hermes commit 历史统计：给后续 agent 的固定提示词

将下面提示词交给后续 agent，即可复用当前主页的统计口径。适用于查询 KoNit-K 的历史 commit 数、Hermes Agent 第 5–20 名、共同作者贡献和排名变化。

---

请查询 `NousResearch/hermes-agent` 的历史提交贡献，默认展示第 5–20 名，并单独列出 `KoNit-K`。使用与 `KoNit-K/KoNit-K` 主页 **COMMITS / COMMIT RANK** 徽章一致的口径：

**账号的总贡献 = 主作者提交 SHA 集合与 GitHub 识别的共同作者提交 SHA 集合的并集大小。**

## 统计规则

1. 统计默认分支固定头提交所能到达的全部历史；不设时间、路径、作者筛选，包含合并提交和空提交。
2. 用 GitHub GraphQL `Commit.authors` 获取作者。第一项是 Git 主作者，其余项是 GitHub 识别的 `Co-authored-by` 共同作者。提交执行者 `committer` 不自动计入作者贡献。
3. 按 `authors.user.id` 关联账号，同一个账号在同一个 SHA 上只计一次。主作者又重复出现在共同署名中，归入主作者，不再计共同作者。
4. 分别报告 `primary_author_commits`、`coauthored_commits`（仅共同作者）、`total_commits`。前两项相加等于总数。
5. 对所有已关联账号使用上述规则，包括已关联的机器人和只有共同作者记录的账号。`user: null` 不猜身份，单独记录未关联条目。
6. 按总数降序计算竞争排名：`rank = 1 + 总数严格更高的账号数量`，同分并列，例如 `1, 2, 2, 4`。同分展示顺序按账号名和稳定 ID 排列。
7. 作者归属全部可读时，默认“第 5–20 名”指 `5 <= rank <= 20`，包括边界上的所有同分账号；如因此超过 16 行，解释同分原因。如果用户明确要求第 5–20 行，才取排序列表位置 5–20，并把列名写为“位置”。
8. 某些 Git 可达提交可能无法从 GitHub 读取作者。保留这些 SHA 为未知，不将其当作无作者或零贡献。设未知 SHA 数为 `U`，每个已知账号的总数范围统一为 `[已核实总数, 已核实总数 + U]`；一个未知提交可以给多个账号署名，但对同一账号最多计一次。
9. 存在未知归属时，使用 `rank_min` / `rank_max`，只有二者相等才称为确定名次。第 5–20 名候选取排名区间与 `[5,20]` 相交的账号，并明确标注边界不确定的条目，不把按已核实数排序的 `rank` 当作完整确定排名。低于 `U` 个已核实提交的尾部账号，可能被尚未出现的账号超过，`rank_max` 可以为 `null`。

## 优先复用已验证结果

- 仓库：`https://github.com/KoNit-K/KoNit-K`
- 完整统计：`https://raw.githubusercontent.com/KoNit-K/KoNit-K/main/data/hermes-contributions.json`
- 可读报告：`https://github.com/KoNit-K/KoNit-K/blob/main/data/hermes-contributions.md`
- 生成脚本：`scripts/update_hermes_contributions.py`
- 更新工作流：`.github/workflows/hermes-contributor-rank.yml`

先读取完整 JSON，检查 `source.paginationComplete == true`、`source.gitReachabilityVerified == true`，以及 `source.historyTotalCount == source.gitReachableCommits == source.uniqueCommits == source.resolvedCommits + source.unresolvedCommits`，并读取 `generatedAt`、`source.defaultBranch`、`source.headSha`。Git 集合完整核验不等于所有作者均可读取；还必须检查 `source.authorAttributionComplete` 和 `source.unresolvedCommitShas`。明确告诉用户这是哪个时间和上游快照的结果，不把旧快照称为“现在实时值”。

从 `contributors` 中按上述排名范围筛选。KoNit-K 的明细在 `target`，其 `primary_commit_shas` 与 `coauthored_commit_shas` 可用于逐条对账。`total_commits`、主作者数和共同作者数均为已核实值；总数范围使用 `total_commits_min` / `total_commits_max`。存在未知归属时，主页 COMMITS 的 `+` 表示已核实下界，不能把它改写为精确总数。

如果需要重新计算，优先运行已有 GitHub Actions 工作流并等待成功；有已授权 GitHub 令牌的环境也可运行：

```sh
python3 scripts/update_hermes_contributions.py
```

令牌通过 `GH_TOKEN` 或 `GITHUB_TOKEN` 环境变量提供。不要显示、复制到文件或索取用户在聊天中粘贴令牌。

## 全量重新计算要求

先固定默认分支头 SHA，然后对这个固定提交完整读取 `history` 分页和每个提交的 `authors` 分页。使用 `git fetch --filter=tree:0` 只取提交元数据，再用 `git rev-list` 得到固定 SHA 的精确可达全集；不使用浅克隆或 `--first-parent`。逐个 SHA 对账，而不只比较总数：分页遗漏的提交按固定 SHA 补查作者，出现不属于该历史的提交则失败。对完整 SHA 的 `object(oid: ...)` 和 `object(expression: ...)` 都明确返回 `null`、且仓库身份有效的提交，记录为未知归属，不能构造空作者记录。已解析 SHA 与未知 SHA 必须不相交，其并集必须与 Git 历史完全相等，记录 `recoveredCommitShas` 和 `unresolvedCommitShas` 等证据。

不要只扫前 100 个贡献者，不要截断搜索结果，也不要在遇到某个旧提交时提前结束。账号关联每轮重新解析。运行环境需要 Python 3 和 Git；GitHub Actions 已提供两者。

任意作者分页不完整、游标不前进、GraphQL 返回错误（包括 HTTP 200 中的部分错误）、Git 集合无法完整对账、目标账号无法解析或最终找不到目标时，都应让更新失败并保留上次成功结果。两个徽章和统计报告必须来自同一个经过集合核验的快照，一次提交发布。有明确未知归属时，必须一起发布下界标记、数量范围和排名范围，不能声称作者覆盖完整。

脚本的 `--checkpoint-path PATH` 会保留未完成扫描证据，便于排查失败，不直接作为徽章数据。Actions 会保留最近运行的此类证据；`--diagnose-only SHA...` 和手动工作流 `Diagnose Hermes commit objects` 可做指定 SHA 的短查询诊断。正常每日运行仍重新读取归属，不使用旧归属缓存。

排名区间采用竞争排名：最好名次为 `1 + 其他账号已核实数严格大于本账号总数上界的数量`；最坏名次为 `1 + 其他账号总数上界严格大于本账号已核实数的数量`。本账号已核实数小于 `U` 时，还可能有未知新账号排在前面，最坏名次保留未知。主作者与共同作者的未知增量合计最多 `U`，不要各加 `U` 后再把总数上界加成 `2U`。

## 数字变化的核查

- 不直接把普通 REST `/contributors` 的缓存数与文本搜索命中数相加；不同来源可能遗漏、重复或包含未被 GitHub 识别的署名。
- 不把包含 `Co-authored-by` 字样的每一行都当作实际账号贡献，也不把本地 `git interpret-trailers` 的结果当作 GitHub 识别结果的替代品。
- 不只给 KoNit-K 加共同作者数，却拿其他人的主作者数比较排名。
- 比较两次结果的上游 SHA、时间、统计规则、账号 ID 和具体提交集合。明确区分新增提交、主分支历史变化、账号归属变化与尚未验证的推测。
- 账号曾被限制不能直接证明 GitHub 删除了贡献；需要具体提交和归属证据。
- 这是当前主页定义的主作者与共同作者合计排名，不声称等于 GitHub Insights 或普通 REST contributors 的官方显示。

## 输出格式

先写数据时间、仓库、分支和固定 SHA，再给表格：

| 排名或排名范围 | GitHub 账号 | 已核实主作者提交 | 已核实仅共同作者提交 | 去重总数或总数范围 |
| ---: | --- | ---: | ---: | ---: |

随后单列 KoNit-K 的同口径明细，并提供对应统计报告、完整 JSON 和必要的具体提交链接。对于无法验证的差异，明确写“尚未确认”，不编造原因或排名。

官方字段说明：[Commit.authors / history](https://docs.github.com/en/graphql/reference/commits#commit)、[GitActor.user](https://docs.github.com/en/graphql/reference/git#gitactor)。
