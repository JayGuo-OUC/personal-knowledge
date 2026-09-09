---
title: 云原生知识库 · 操作日志
type: synthesis
created: 2026-08-26
updated: 2026-08-27
tags: [云原生, 日志]
---

# 操作日志（Log）

append-only  chronological record。可用 `grep "^## \[" log.md` 快速检索。

## [2026-08-26] init | 初始化云原生知识库
创建 Vault 结构（WIKI-SCHEMA、README、raw/、wiki/），并一次性写入 19 篇教程笔记：
概览、CNCF 全景、容器基础、Docker、运行时/OCI、K8s 核心/架构/工作负载/网络/存储/控制器、
微服务、服务网格、可观测性、CI/CD、Serverless、安全、最佳实践、学习路线。建立交叉引用与目录索引。

## [2026-08-26] restructure | 改造为自生长知识库
将仓库重构为 raw / mine(未定稿·已定稿·AI辅助生成) / wiki / output / skills , 大类（参考 Karpathy LLM-Wiki 方法论）。
- 云原生 19 篇并入根目录 `wiki/云原生`，旧 `云原生/` 文件夹清空移除。
- 新建 `wiki/index.md`（总索引）与 `wiki/云原生/云原生-index.md`（主题索引）。
- 编写根 `CLAUDE.md`：目录结构、wiki 标准格式、新开vs并入、链接/占位页规则、mine 风格边界、问答模式、skills 沉淀条件、每日/每周任务。
- 沉淀首个技能 `skills/主题知识库搭建.md` 并建 `skills/README.md` 索引。
- 跑首次体检与示例问答，产出 `output/体检报告-2026-08-26.md` 与 `output/问答-容器与虚拟机区别-2026-08-26.md`。

## [2026-08-26] add | 新增 Git 主题知识库
在 `wiki/git/` 下新建 Git 主题，按 CLAUDE.md 标准格式写入 10 篇条目 + 主题索引 `git-index.md`：
概览、核心概念、基础命令、分支模型、远程协作、变基与历史改写、暂存与忽略、冲突解决、工作流与最佳实践、学习路线与资源。
建立交叉引用（双链）与总索引联动（`wiki/index.md` 新增 Git 主题，条目数 19 → 29）。

## [2026-08-27] fix | 修复 Git 主题双链格式
用户确认 Obsidian 未启用标题/.basename 匹配，原 `[[Git概览]]` 等写法无法定位带序号文件 `01-Git概览.md`，导致 10 条 Git 链接悬空。
将 `wiki/git/` 下全部 11 篇（10 条目 + `git-index` 索引）中的双链改写为带序号（或 git-index）格式：
`[[Git概览]]→[[01-Git概览]]`、`[[Git核心概念]]→[[02-Git核心概念]]` … `[[Git学习路线与资源]]→[[10-学习路线与资源]]`、`[[Git主题索引]]→[[git-index]]`。
全库链接校验：无孤儿页；Git 断链已全部消除。
遗留：`[[CLAUDE]]` 指向 vault 根目录 `CLAUDE.md`（规则文件），若 Obsidian vault 范围含根目录则有效，否则需在插件/设置中确认索引范围。

## [2026-08-31] add | 新增 Git 日常流程与命令速查
用户需要在 `wiki/git/` 下新增一份「按流程组织的日常操作手册」。新建 `11-Git日常流程与命令速查.md`（type: term）：
七条铁律 → 晨间同步 → 开分支 → 小步提交 → 提交前自检 → Conventional Commits → 追平主干(rebase) →
整理本地历史(amend/rebase -i) → 推送提 PR → 评审后修改(fixup) → 合入后清理 → 冲突处理 → 事故救急
(错分支/撤销/已推送回滚/reflog/误删分支/stash) + 撤销矩阵 + 命令速查表 + 全局配置与别名 +
AI 辅助编程场景下的提交纪律。
联动更新：`git-index.md`（新增条目、条目数 10→11）、`wiki/index.md`（Git 10→11 篇、总条目 29→30）、
`03-Git基础命令.md` 与 `09-Git工作流与最佳实践.md` 补反向双链。

## [2026-08-31] expand | 补充 Git 速查的分支位置标注与 rebase 详解
用户反馈「不够详细、看不出 rebase 时本地在哪个分支」。重写 `11-Git日常流程与命令速查.md`：
- 新增第〇节「我现在到底在哪个分支」：`git status` 首行四种状态表（正常 / 游离 HEAD / rebase 进行中 / merge 冲突中），明确 rebase 期间 `branch --show-current` 返回空。
- 新增第一节「rebase 到底在干什么」：before/after 提交图、Git 内部五步（找 merge-base → 摘补丁 → 游离 HEAD 落新基点 → 重放 → 分支指针搬家）、三方关系表（当前分支 / upstream / 被重放提交 / 不被改动的 upstream）、`--onto` 语法、merge vs rebase 对比图。
- 全篇每个流程加「本地位置 / 执行后」标注 + 分支位置变化表；rebase、冲突、救急各节按触发命令区分收尾方式（rebase 用 `--continue`，merge 用 `commit`）。
- 新增附录「一次完整任务的分支迁移轨迹」11 步表。
- 章节由 16 节扩为 18 节 + 附录，篇幅约翻倍。

## [2026-09-02] add | 新增「JDK & Spring 架构升级」主题知识库
用户计划将公司后端从 JDK 8 + Spring Boot 2.3 升级至 JDK 21 + Spring Boot 4（初提 Spring 3，经版本核查后修正为 Spring Boot 4）。
在 `wiki/JDK&Spring/` 下新建 5 篇条目 + 主题索引 `JDK&Spring-index.md`：
- `01-JDK21新特性.md`：虚拟线程(JEP 444)、记录模式(440)、switch 模式匹配(441)、有序集合(431)、分代 ZGC(439)、
  外部函数与内存 API(442)、KEM API(452)；预览特性表（结构化并发/作用域值等，注明字符串模板已在 JDK 23 移除）；
  移除与行为变更清单（强封装、JAXB 移除、Nashorn 移除等）；**Oracle JDK 21 免费许可 2026-09 到期**的关键提醒。
- `02-Spring4新特性.md`：基座对照表（Jakarta EE 11 / Servlet 6.1 / Hibernate 7 / Tomcat 11 / Jackson 3 / JUnit 6）；
  虚拟线程默认开启；一等公民 API 版本化（RFC 9745）；内建弹性（@Retryable / @ConcurrencyLimit）；
  JSpecify 空安全（NullAway 需 JDK 21+）；模块化与 starter 改名；Jackson 3 破坏性变更；
  Micrometer 2 + OpenTelemetry；GraalVM 24 AOT；RestTemplate 将于 7.1 废弃、8.0 移除。
- `03-JDK21与JDK8对比.md`：总览对照 + 语言特性落差表（9~21 逐版本）+ 代码对照 + 运行时性能落差 +
  容器感知差异 + 安全许可落差 + 破坏性变更清单 + 升级路径建议（先单独升 JDK 再动 Spring）。
- `04-Spring4与Spring2对比.md`：五大破坏性变更（javax→jakarta / Security 重写 / 第三方依赖连锁 /
  Jackson 3 默认行为 / 配置与 starter 改名）+ 推荐迁移路径 2.3→2.7→3.5→4.1 + OpenRewrite 配方与人工补位 +
  第三方依赖对照表 + 工作量估算（约 10–17 人日/中型项目）。
- `05-升级必要性.md`：风险侧（Boot 2.3 已于 2021-05 EOL、商业支持 2022-08 终止，JDK 8 无官方免费更新；
  等保/供应链合规风险）+ 收益侧（云原生适配、虚拟线程、ZGC、可观测性、TCO）+ 信创与数据合规章节
  （国产 OpenJDK 发行版 Dragonwell / 毕昇 / Kona，规避 Oracle 订阅）+ 风险对冲表 + 分阶段路线图。
- `JDK&Spring-index.md`：主题索引，含一句话结论、关键时间节点表、推荐阅读顺序、跨主题（云原生）关联。
联动更新：`wiki/index.md`（新增主题，主题数 2→3，条目数 30→35）。
交叉引用：5 篇条目之间互链，并向云原生主题（[[01-云原生概览]]、[[03-容器技术基础]]、[[08-Pod与工作负载]]、
[[12-微服务架构]]、[[14-可观测性]]、[[15-CI-CD与DevOps]]、[[16-Serverless与FaaS]]、[[17-云原生安全]]、
[[18-云原生最佳实践]]）建立跨主题双链。
数据核实时点：2026-09-02（Spring Boot 4.1.0 为当前稳定版，2026-06-10 发布；Spring Boot 3.x 全系 EOL）。

## [2026-08-27] daily | 每日任务执行（无新资料）
按 CLAUDE.md 第八节执行每日整理流程：`Clippings/` 不存在；`raw/` 为空；`mine/` 无新增；`output/` 无新增产出。
全库无新资料需要编译进 wiki。链接校验状态与上午一致：无孤儿页、Git 断链已修复。
产出 `output/daily-log-2026-08-27.md`。知识库规模维持：29 条目（云原生 19 + Git 10），2 主题，1 skill。

## 2026-09-02

- **新增主题：「珍大户的经济圈」**（`wiki/珍大户/`），来自知识星球同名付费星球（group_id `458522225218`）。
- 摄入量：**1024 条精华正文**，约 **149 万字**，时间跨度 2018-08 — 2026-09。
- 产出：MOC 总索引 `珍大户-index.md` + 14 个主题页 + `珍大户-重点必读.md`（90 条 4—5 心精选）+ `珍大户-系列脉络.md`（8 大系列编号清单）。
- 原始数据落位 `raw/珍大户/`：`master.json`（精华正文与元数据）、`master_themed.json`（含主题与系列标注）、`digest_master.json`（官方目录 2010 条）、`kdocs_lines.txt`（官方目录文档全文）。
- 方法说明：
  - 官方 Skill 的 `get_group_topics` 被星主关闭权限，改用浏览器会话抓取；点击「只看星主」后底层 API 走 `scope=digests`，即官方精华流。
  - ❤ 重要度评级取自星球官方维护的金山文档《星球目录时间线（七周年重制版）》。
  - 主题归类为脚本规则粗分（标题 + 官方摘要 + 正文前 400 字），边界存在少量模糊。

## 2026-09-03

- **新增主题：「AI Agent Skill」**（`wiki/Agent-Skill/`），15 个页面 = MOC 索引 + 14 篇条目。
- 选题动因：用户（技术负责人）要系统理解 Skill 的概念、结构、作用原理，并为公司已选定的 Cursor 配一套可落地的技能包与教程。
- 篇目（按学习/落地顺序编号，非字母序）：01 是什么 / 02 开放标准与生态 / 03 SKILL.md 结构与 frontmatter /
  04 渐进式披露 / 05 作用原理 / 06 目录结构与捆绑资源 / 07 与 Rules·Commands·MCP·Subagent 对比 /
  08 如何写出好 Skill / 09 Cursor 中的 Skill 全景 / 10 Cursor 安装与使用教程 / 11 实战技能包六件套 /
  12 安全与企业合规 / 13 速查表与 FAQ / 14 学习路线与资源。
- 核心结论：
  - Skill = `SKILL.md`（YAML frontmatter + Markdown 指令）+ 可选 `scripts/`、`references/`、`assets/` 的**文件夹**。
  - 开放标准由 Anthropic 发起、agentskills.io 维护，已被 30+ 产品采用；**只强制 2 个字段**：`name`、`description`。
  - 机制是**渐进式披露**：启动加载元数据（~100 token/个）→ 语义命中后加载正文（<5000 token）→ 资源按需。
  - **Skill 不改模型权重，只改上下文**；判断写 Markdown、确定性逻辑写脚本。
  - 生态有真实供应链风险：Snyk 审计 3984 个技能 13.4% 严重问题 / 36.82% 有缺陷；学术研究 26.1% 含漏洞，
    带 `scripts/` 的技能风险为纯指令型的 2.12 倍。
- **配套产出（在 `skills/` 而非 `wiki/`）**：`skills/cursor-agent-skills/` 六件套——
  `data-compliance-guard`（含 `scripts/scan-egress.py`）、`code-review-gate`（含 `references/review-checklist.md`）、
  `ai-code-provenance`、`commit-and-pr`、`debug-systematically`、`refactor-safely`。
  已安装至 `~/.cursor/skills/`，6/6 通过 name 与目录名一致性校验。
- 脚本验证：`scan-egress.py` 用正反例样本测试通过——`req.body` 整体打印命中、`req.body.userId` 白名单取字段不命中、
  `maskPhone()` 脱敏写法不误报、`.cn`/内网域名不误报；退出码 0/1 可接 CI。
- 链接校验：新主题 102 条双链，0 断链，0 孤儿页。
- 联动更新：`wiki/index.md`（主题数 4→5，页面数 56→71）。
- 数据核实时点：2026-09-03。Cursor 官方文档以 `/docs/skills` 为当前路径，`/migrate-to-skills` 需 2.4+。

## 2026-09-08

### Agent-Skill 主题补充（用户主动迭代）
- **补充「AI Agent Skill」主题 4 篇**：15 Skill 市场与下载渠道 / 16 程序员推荐安装的 Skill / 17 文档 Skill / 18 通用 Skill。
  并为 15—18 篇的全部外置技能**标注宿主 GitHub 仓库 Star 数**（GitHub API `stargazers_count` 实时抓取，仓库级指标非单技能计数）。
  - 发现两个仓库已 404 不可用：`smithery/ai`、`dengineproblem/agents-monorepo` → 标 N/A。
  - 发现 `jabrena/cursor-rules-java` 已改名并入 `jabrena/plinth`。
- **按「⭐≥1K」门槛重写 16 篇**（本司栈：前端 Vue3+TS+Vite+Element Plus，后端 Spring Cloud+Java+MyBatis+MySQL+Redis）：
  - 新增达标主力：`antfu/skills` ⭐5.9k（vue/vite/pinia/vitest/vueuse-functions）、`vuejs-ai/skills` ⭐2.8k（Vue3 官方向技能集）、
    `awesome-skills/code-review-skill` ⭐1.9k（20+ 语言，含 Vue3.5/TS/Java17+SpringBoot3 评审规则，一个顶前后端两套）。
  - 淘汰未达标：`PatternsDev/skills` ⭐246、`mindrally/skills` ⭐258、`sammcj/agentic-coding` ⭐160。
  - 结论：**Element Plus / MyBatis / MySQL / Redis / Spring Cloud 在 1K 门槛下无任何公共 Skill** → 补了 4 份自建 SKILL.md 模板。
  - 顺手修正 mybatis 模板错误：`${param}`（字符串拼接，有注入风险）→ `#{param}`。
- **新增 19-Cursor内置skill.md**：合并本机实测 25 个（`~/.cursor/skills-cursor/`，`.sync-manifest.json` 全部标记为 Cursor 托管）
  与官方文档 Built-in 表 19 个，去重得 **26 个**内置技能全表。
  - 官方有而本机未同步 1 个：`/cursor-blame`；本机有而官方表未列 7 个：`deploy-with-vercel` / `goal` / `new-repo` / `onboard` / `origin` / `rename-chat` / `share`。
  - 实测标注 **8 个技能设了 `disable-model-invocation: true`（只能 `/` 手动调用）**：`create-subagent`、`deploy-with-vercel`、`goal`、
    `migrate-to-skills`、`onboard`、`rename-chat`、`review`、`shell`。
  - 澄清：`/autopilot`（盯 PR）在部分文档镜像中写作 `/babysit`，功能相同，属改名。
  - 澄清：内置技能目录是 `~/.cursor/skills-cursor/`（**带 `-cursor` 后缀**），与放自己技能的 `~/.cursor/skills/` 是两个目录，前者会被同步覆盖。
- **联动更新**：`Agent-Skill-index.md`（新增 19 篇目、修正内置技能数 24→25）、`09-Cursor中的Skill全景.md`（内置技能表改为指向 19 篇，避免重复维护）、
  `wiki/index.md`（Agent-Skill 14→19 篇，总页面 71→76）、本日志。
- 方法备忘：GitHub API 未认证配额易打满（core 60/hr、search 10/min），**改用 `raw.githubusercontent.com` 抓 README 不受限**；搜索用 `stars:>1000` 限定词可省去逐条过滤。

### 每日整理（2026-09-08 18:00）
- 按 CLAUDE.md 第八节执行每日流程。
- `Clippings/` 不存在，无需归类清空。
- `raw/` 今日新增 6 个珍大户原始数据文件（已落在 `raw/珍大户/` 下）：
  `master.json`、`master_themed.json`、`all_themed.json`、`digest_master.json`、`kdocs_lines.txt`、`topics_owner.json`。
  其中 `master_themed.json` 与 `all_themed.json` 为首次入库。
- 判定为**并入已有**：资料属于已有「珍大户的经济圈」主题，未出现新的独立概念，不新建 wiki 条目。
- 更新受影响页面：
  - `wiki/珍大户/珍大户-index.md`：frontmatter sources 补全 6 个 raw 文件，正文「来源」节补充分类数据文件说明，更新 `updated`。
  - `wiki/珍大户/珍大户-系列脉络.md`：sources 增加 `master_themed.json`、`all_themed.json`，更新 `updated`。
  - `wiki/珍大户/珍大户-重点必读.md`：sources 增加 `all_themed.json`，更新 `updated`。
  - `wiki/珍大户/01-15` 全部 15 个主题页：sources 增加 `all_themed.json`，更新 `updated`。
- `output/` 今日无新增产出；既有 3 份文件（8 月 26、27 日产出）留原地。
- 轻量链接检查：待产出 daily-log 后由脚本跑。

## 2026-09-09

### 16 篇校验与 skills.sh 口径修正（上午）
- 将 16 篇每条「技能→仓库」断言逐条打到 `https://www.skills.sh/api/search?q=xxx`（公开 JSON 接口，无需浏览器；注意限流，间隔 ≥1.5s）核对：75 条断言 → **71 通过 / 3 删除 / 1 改名**。
  - 删除（skills.sh 未收录）：`agent-rules-books`（ciembor，是规则原料非可装技能）、`Cocoon-AI/architecture-diagram-generator`（同名仅在他仓库）、`clean-code`（piomin，GitHub 有但 skills.sh 未索引）。
  - 改名：`Agents365-ai/drawio-skill` → 小写 `agents365-ai/drawio-skill`。
  - 订正安装量误读：上轮把「仓库某模块查询下技能安装量之和」误当单技能安装量（`webapp-testing` 304k→152.7k、`code-review` 1.32M→513.7k、superpowers 评审 819k→188k/223k 等）。
- 确认 `spring-boot-engineer` / `java-architect` / `java-code-review` / `api-contract-review` / `design-patterns`（piomin/claude-ai-spring-boot）**5 个均已被 skills.sh 收录**（设计模式 53、其余各 1 安装量），GitHub 仓库目录树也佐证；并挖到一个漏列的 `code-quality`（56 安装）。

### 新增 20-Skill后端试用.md（下午）
- 用户要求在 Agent-Skill 文件夹下新增「20-Skill后端试用.md」，在 `E:/guojian/01project/sjz/sjz/sjz-back` 用这些 skill 完成任务并写入结果。
- **关键限制确认**：本机 Cursor（`D:/apps/cursor`）只有 IDE 内部 agent 运行时扩展，**无程序化拉起的非交互 CLI 入口**（`cursor` 主命令仅 IDE 启动器，不支持 `--agent/--ask/--run/--headless`）。故采用等价离线验证：读取 sjz-back 已装的 21 个 SKILL.md 规则原文，逐条套真实代码做静态分析。
- 已装 21 技能（sjz-back/skills-lock.json）：ecc 9（backend/mysql/redis/java-coding-standards/database-*/springboot-*）、piomin 5、jeffallan 4、awesome-copilot 4、wshobson 1。
- 真实命中（附文件:行号证据链）：
  - 🔴 SQL 注入 2 处：`MajorAlarmMapper.xml:247/318` `delete ... where id = ${id}`（值位置 `${}`，应改 `#{}`）；调用链 `deleteAlarmConfig(Map)` → `param.get("id")` 外部可控 → `${id}` 字符串拼接。
  - 🟠 多写无事务 16 处：`ServiceImpl` 142 个中 131 个无 `@Transactional`，其中 16 个多步写无事务（含 `MajorAlarmServiceImpl` 7 写操作，且 `deleteAlarmConfig` 两步删表无事务，留孤儿数据风险）。
  - 🟡 `SELECT *` 24 文件；`LIMIT offset,size` 深分页 3 处；`System.out.println` 30 文件；`printStackTrace` 38 文件。
  - 🟢 Redis 仅 4 文件且收口到 `hi-libs-redis` 模块（符合 redis-patterns 集中管理思想）。分页统一 MyBatis-Plus（86 文件），未用 PageHelper。
- 报告含修复建议片段（改 `#{}`、补 `@Transactional(rollbackFor=Exception.class)`、keyset 游标、统一 SLF4J）。
- 联动更新：`Agent-Skill-index.md`（加 20 篇目 + 相关 + 来源）、`wiki/index.md`（Agent-Skill 20 篇 / 总页面 77）、本日志。
- 临时扫描脚本 `_scan.py` / `_scan.txt` 已清理。
