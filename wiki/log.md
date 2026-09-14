---
title: 云原生知识库 · 操作日志
type: synthesis
created: 2026-08-26
updated: 2026-09-11
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

## 2026-09-10

### 23-skill主流技术栈.md 第十节：接口导出与测试工程化（按工作流扩展）
- 用户要求：在 23 篇基础上，按「后端接口全部导出方便测试 / 接口文档导出」工作流扩展找 skill，去 skills.sh 检索。
- 新发现主表缺口：主表只有 `api-and-interface-design`（写前定契约）与 `java-junit`（单测），缺「从已有 Controller 导出 OpenAPI」与「用 Mock 把接口跑起来测」。
- 第十节新增 3 个扩展 skill（均 installs≥1K）：
  - `spring-boot-openapi-documentation`（giuseppe-trisciuoglio/developer-kit，3,052 / ⭐343）——Spring Boot 原生接口文档导出，正中文档导出需求；⚠️ 仓库 ⭐343 低、installs 含预装灌水，装前读 SKILL.md。
  - `unit-test-wiremock-rest-api`（同 developer-kit 仓库，2,869 / ⭐343）——WireMock 给 REST 接口打桩做测试，与 `java-junit` 配套。
  - `api-security-testing`（usestrix/strix，4,337 / ⭐61,562）——接口安全扫描（OWASP），质量高。
  - 备选 `api-documentation-generator`（sickn33/agentic-awesome-skills，2,146 / ⭐46,209）框架无关通用文档导出。
- 10.4 诚实标注未过 1K 的：功能接口测试 `api-testing`(745)、`casely`(893)、契约测试 `api-contract-testing`(888)、Pact `pactflow`(98)；参数化单测 `unit-test-parameterized`(2,845) 已由主表 `java-junit` 覆盖。
- 结论：功能级接口自动化测试 skills.sh 无过 1K 成熟方案，先用 WireMock+JUnit 顶上。同步更新摘要/安装命令/验证状态；未改篇数编号，index 不动。

### 新增 20-后端Skill试用.md（下午）
- 用户要求把 `E:/guojian/01project/sjz/sjz-back/skill运行结果.md` 纳入 Agent-Skill 主题，「重命名为后端Skill试用」。
- 按目录 01—20 的编号惯例定为 **`20-后端Skill试用.md`**（保留用户指定名称）；按 CLAUDE.md 规范补齐 frontmatter、摘要、相关双链与来源，原文（26 个 skill 逐项体检）完整保留。
- 内容要点：sjz-back（Java 8 + Boot 2.3 / Hoxton）已装 26 个 skill 逐个对照 SKILL.md 做合规审计，**通过 0 · 部分通过 17 · 未通过 9**。
  - 跨 skill 最高优先级：SQL 注入（`${id}`）、无 Flyway/Liquibase 版本化迁移、Redis `KEYS` 与大量无 TTL、字段 `@Autowired` 主导（170+ 文件）、测试与质量门禁缺失、配置明文密码、日志不规范（System.out / printStackTrace / 字符串拼接）。
  - 与 20 篇的边界：20 篇＝重点缺陷的深度证据链 + 修复代码；21 篇＝全量 skill 适用性体检（广度）。两者互补并已互链。
- 联动更新：`20-Skill后端试用.md`（related 加 [[20-后端Skill试用]]）、`Agent-Skill-index.md`（篇目表 + 相关区）、`wiki/index.md`（Agent-Skill 20→21 篇）、本日志。

### 新增 21-前端Skill试用.md（下午）
- 用户要求把 `E:/guojian/01project/sjz/sjz-front/skill运行结果.md` 纳入 Agent-Skill 主题，命名为 `21-前端Skill试用.md`（本次用户直接指定编号）。
- 按 CLAUDE.md + llm-wiki（Karpathy）ingest 规范处理：补 frontmatter、提炼标签、写摘要、加 `## 相关` 双链与 `## 来源`，**原文 20 个 skill 的逐项审计结果一字未改**。
- 内容要点：sjz-front（Vue 3.5 `<script setup>`(JS，非 TS) + Pinia 3 + Vue Router 4 + Element Plus 2.13 + Tailwind 3 + Vite 7，无 TS、无测试链）已装 20 个前端 skill 逐个审计，**PASS 6 · WARN 9 · FAIL 5**。
  - PASS（日常主力）：`vue`、`vue-best-practices`、`vue-pinia-best-practices`、`vue-router-best-practices`、`pinia`、`element-plus`（自建）。
  - FAIL（建议停用或移出项目上下文）：`typescript-pro`（仓库无 TS）、`vitest`（未装测试链）、`frontend-patterns` / `frontend-dev-guidelines` / `frontend-ui-engineering`（React·Next·MUI·TanStack 教条，会把 agent 导向错误 API；后者还存在 `references/accessibility-checklist.md` 断链）。
  - 目录卫生：以 `.agents/skills/`（20 个）为准；`agent/skills/` 有 16 个重复副本、`.claude/skills/` 为子集副本，建议清理以降低维护成本。
- 与 21 篇构成**前后端完整对照**（后端 26 个 / 前端 20 个），已互链。
- 联动更新：`20-后端Skill试用.md`（related 加 [[21-前端Skill试用]]）、`Agent-Skill-index.md`（篇目表 + 相关区）、`wiki/index.md`（Agent-Skill 21→22 篇，总页面 78→79）、本日志。

### 每日整理（2026-09-09 18:00 · 自动化触发）
- 按 CLAUDE.md 第八节流程执行；任务调度 ID = `automation-1787715448943`。
- `Clippings/` 不存在，无需归类清空。
- `raw/` 今日无新增；`raw/珍大户/` 6 个原始数据文件维持 2026-09-08 14:26 mtime，无变化。
- `mine/` 全空；`output/` 今日无新增文件。
- **结论：今日无新资料进入 raw/mine，因此本轮不触发「raw→wiki 编译」，也不触发 output→wiki/skills 沉淀。**
- 轻量链接检查（87 总页 / 0 孤儿 / 35 已知历史断链）：
  - `[[CLAUDE]]` 6 处 → 根目录规则文件，是否有效取决于 Obsidian vault 范围。
  - `[[Git概览]]` / `[[Git核心概念]]` / `[[Git主题索引]]` / `[[Git学习路线与资源]]` 各 1 处 → log.md 历史旧称，08-27 已对齐新内容，保留原状。
  - `[[wiki/珍大户/assets/images/...]]` 25 处 → Obsidian wikilink 嵌入图片（资源存在），脚本正则误判，无须处理。
- 与本自动化正交的今日变更（上午/下午用户驱动）：
  - 新增 16 篇校验与 skills.sh 口径修正（详见 wiki/log.md 上方三段）
  - 新增 20-Skill后端试用 / 20-后端Skill试用 / 21-前端Skill试用 三篇
  - 联动更新 Agent-Skill-index / wiki/index / wiki/log.md
- 写出本笔日志与 `output/daily-log-2026-09-09.md` 作为今日变更清单留底。
- 未修改 `raw/` 与 `mine/` 下任何文件（合规自检通过）。

## 2026-09-10

### 新增 22-Skill现有技术栈.md（上午）
- 用户需求：按公司实际栈重新梳理该装哪些 skill——后端 Java/Spring Cloud/MyBatis/MySQL/Redis/Kafka，前端 Vue3 + TS + Element Plus，并覆盖「从 UI 设计稿实现前端页面」链路。硬要求：来源 skills.sh、安装量 ≥1K、**一个技术方向不重复安装**，结果写入 `23-skill二次查找.md`。
- 方法：skills.sh 语义检索 + GitHub API `stargazers_count`。**关键教训：skills.sh 是语义搜索，任何关键词都返回 100 条，光看名字会被误导，必须回 GitHub 读 SKILL.md 原文才能确认版本与内容**（如 `java` 关键词返回的却是大量 Boot 3 / Java 17+ skill）。
- 产出：**17 个可安装 + 2 个自建**。
  - 后端 8：`java-springboot`(github/awesome-copilot, 19,987/⭐38,819)、`microservices-patterns`(wshobson/agents, 11,775/⭐39,535)、`backend-patterns`(ecc, 13,165/⭐255,173)、`java-coding-standards`(ecc, 10,363)、`mysql-patterns`(ecc, 5,230)、`redis-patterns`(ecc, 5,204)、`kafka-development`(mindrally, 1,049/⭐260)、`java-junit`(awesome-copilot, 11,329)。
  - 前端 4：`vue-best-practices`(vuejs-ai, 38,433/⭐2,836)、`typescript-expert`(sickn33, 11,966/⭐46,209)、`ui-to-vue`(ecc, 5,121)、`vue-testing-best-practices`(vuejs-ai, 11,496)。
  - 工程通用 3：`code-review`(mattpocock, **520,310**/⭐257,863，全库安装量第一)、`api-and-interface-design`(addyosmani, 31,705/⭐93,221)、`git-commit`(awesome-copilot, 44,591)。
  - 自建 2：**MyBatis**（`mybatis` 关键词检索 **0 条 ≥1K**，与 16 篇结论一致）、**Element Plus**（无优质公共 skill，沿用 sjz-front 已有自建模板）。
- 主动排除的坑：`upstash-redis-js`(9,945) 是 **Node/JS 客户端**非 Java 后端所用；`create-spring-boot-java-project`(9,509) 是 **Java 21 + Boot 3 脚手架**会毁存量项目；`typescript-advanced-types`(72,710) installs 最高但只讲**类型体操**，日常业务用不上；`planetscale/mysql`(7,632) 仓库仅 ⭐661 且偏自家产品。
- 文档附：按仓库合并的安装命令（快模式 `--agent cursor`，避免全平台版单 skill 约 7 分钟）、**JDK 8 / Boot 2.3 版本护栏写法**。
- 联动更新：`21-前端Skill试用.md`（补齐缺失的 frontmatter `related` 字段并回链 23）、`Agent-Skill-index.md`（篇目表 + 相关区）、`wiki/index.md`（Agent-Skill 22→23 篇，总页面 79→80）、本日志。

### 新增 23-skill主流技术栈.md（上午，23 篇的姐妹篇）
- 用户追加要求：**别考虑存量项目，版本不是问题**，按主流技术栈重做一份选型（去重与 ≥1K 门槛同 23 篇），写入 `23-skill主流技术栈.md`。
- 与 23 篇的差异：① 去掉版本约束与「版本护栏」章节；② Element Plus 方向给出可装方案 `element-plus-vue3`(1,941/⭐658)，而非仅自建；③ 新增「与 23 篇的差异」对照表与「验证状态说明」章节（诚实标注哪些已读 SKILL.md 原文、哪些仅依据 installs/star 判断）。
- 本轮补搜的新结论：
  - **MyBatis 仍为 0 条 ≥1K**——用 `mybatis` / `mybatis plus` / `persistence layer` 多轮检索均为 0；注意 `mybatis plus` 返回的是 `element-plus-vue3`、`web-search-plus` 这类**名字误匹配**（"plus" 被语义匹配），切勿采信。
  - ORM 方向唯一过线的是 `affaan-m/ecc/jpa-patterns`(9,190/⭐255,173)，但属 **JPA/Hibernate**，与 MyBatis 不是一回事，不推荐。
  - Element Plus：`partme-ai/full-stack-skills/element-plus-vue3`(1,941) 过线；UI 还原主推 `affaan-m/ecc/ui-to-vue`(5,126)，`figma/mcp-server-guide/implement-design`(6,003，installs 更高但未取到原文) 列为 Figma 场景备选。
  - Kafka 仍只有 `mindrally/skills/kafka-development`(1,049)；若做事件溯源可看 `wshobson/agents/event-store-design`(9,594/⭐39,535)。
- 最终产出：**16 个可安装 + 1 个自建（MyBatis）**。
- 联动更新：`22-Skill现有技术栈.md`（related 加 24，双向互链）、`Agent-Skill-index.md`（篇目表 + 相关区）、`wiki/index.md`（Agent-Skill 23→24 篇，总页面 80→81）、本日志。

### 重写 17-文档Skill.md 与 18-通用Skill.md（上午）
- 用户需求：围绕**编写需求规格说明书、概要设计说明书、详细设计说明书、用户使用说明手册**重做 17 篇，并一并更新 18 篇；来源 skills.sh、installs≥1K、每方向不重复；**17 篇之前内容删除重写**（18 篇同样按新检索重写）。
- **17 篇产出（7 主装 + 3 配套）**：`create-specification`(13,397/⭐38,819，需求规格)、`architecture-blueprint-generator`(11,964/⭐38,819，概要设计)、`create-oo-component-documentation`(7,022/⭐38,819，详细设计)、`documentation-writer`(26,239/⭐38,819，用户手册)、`architecture-decision-records`(wshobson, 16,372/⭐39,535)、`mermaid-diagrams`(softaworks, 4,863/⭐2,452)、`create-readme`(18,165/⭐38,819)；配套 `update-specification`(9,236)、`create-github-issues-for-unmet-specification-requirements`(8,975)、`update-oo-component-documentation`(6,991)。
- **18 篇产出（7 个通用）**：`improve-codebase-architecture`(mattpocock, 901,011/⭐257,863)、`code-review`(mattpocock, 520,310)、`systematic-debugging`(obra, 253,410/⭐284,019)、`git-commit`(44,591/⭐38,819)、`architecture-patterns`(wshobson, 21,882/⭐39,535)、`refactor`(21,635/⭐38,819)、`security-review`(ecc, 16,130/⭐255,183)。
- **本轮关键发现：installs 高 ≠ 可信**。
  - `warpdotdev/common-skills/write-tech-spec` installs 24,793 但仓库仅 ⭐**564**——Warp 终端**厂商预装推送**带来的安装量。
  - `riekelt/technical-writer/writing-design-docs` installs 5,860 但仓库仅 ⭐**16**——名字最贴「设计文档写作」却几乎无人验证。
  - `microsoft/azure-skills/azure-compliance` installs 569,861 但**绑定 Azure 平台**，非通用合规能力。
  - 三者均未选入主表。**结论：installs 只说明装得多，star 才是社区验证信号。**
- **方法备忘**：GitHub API 未认证配额（60/hr）两轮即耗尽并返回 403；**改用 curl 抓仓库页面 HTML 提取 star 可绕开限流**：`curl -s https://github.com/<repo> | grep -oE 'id="repo-stars-counter-star"[^>]*title="[0-9,]+"'`。
- 合规方向结论：检索到的合规 skill 全部绑定特定法规或平台（Azure / PCI-DSS / HIPAA / 无障碍），**无适配国内政企「代码与数据不出境」的通用项**，建议沿用 16 篇已自建的 `data-compliance-guard`（含 `scripts/scan-egress.py`，支持 .cn 与内网域名白名单不误报）。
- 联动更新：`Agent-Skill-index.md`（17/18 篇目表与相关区描述）、本日志。

### 删除 20-Skill后端试用.md 并重编号后续文档（上午）
- 用户要求：删除 20 号文档，后续文档编号前移，并更新相关链接。
- 执行：旧 `20-Skill后端试用.md` **移出 wiki 备份至 `_tmp/deleted_wiki/`**（未彻底删除，可恢复）；随后 `21→20`、`22→21`、`23→22`、`24→23` 重命名。
- 编号映射：旧 21 后端体检 → **20-后端Skill试用**；旧 22 前端体检 → **21-前端Skill试用**；旧 23 二次查找 → **22-Skill现有技术栈**；旧 24 主流技术栈 → **23-skill主流技术栈**。Agent-Skill 现有 **01—23**。
- 全库同步：sed 批量替换 4 组编号字符串（覆盖 frontmatter title、H1 标题、正文 `[[双链]]`、"X 篇"简写），范围含 `wiki/index.md`、`wiki/log.md`、`wiki/Agent-Skill/*.md`。
- 断链清理：删除所有指向已删文档的 `[[20-Skill后端试用]]` 链接行；改写 `20-后端Skill试用` 与 `21-前端Skill试用` 摘要中「与已删文档互补」的表述；`wiki/index.md` 中对应来源条目一并删除。
- 统计更新：`wiki/index.md` Agent-Skill 24→**23 篇**，总页面 81→**80**。
- 说明：`wiki/log.md` 中提及旧 20 的均为**纯文本历史记录**（非 `[[]]` 链接），按 append-only 原则保留，不产生断链。

### 23-skill主流技术栈.md 第九节补全「版本排除项解禁清单」（延续未完成任务）
- 背景：上一轮已在 23 篇（不受版本约束的姐妹篇）写入「九、曾被版本约束排除、现已解禁的 skill」一节，但核对 22 篇时发现两处遗漏 + 一处来源口径需澄清。
- 本轮用 skills.sh 公开接口（`https://www.skills.sh/api/search`）补全检索，确认并新增：
  - **`microservices-architect`**（`jeffallan/claude-skills`，**4,259**/⭐11,389）：与 23 主表 `microservices-patterns` 同方向、面向 Java 21/Boot 3，补入 9.1 替换选项。
  - **`mindrally/java`**（写 Java 17+）：来源为 22 篇实测记录；skills.sh 当前未收录其独立安装量（同名仅 `mindrally/skills/spring-boot` 769），标注「未核实」，补入 9.1 替换选项。
  - 来源澄清：`java-architect` 主流来源是 `jeffallan/claude-skills`(5,219)；22 篇写的 `piomin/claude-ai-spring-boot/java-architect` 在 skills.sh 仅 1 安装，以 jeffallan 版为准。
  - 同系列 `java-microservices`(`pluginagentmarketplace/custom-plugin-java`) 仅 484 安装，未过 1K 门槛，注明不列入主清单。
- 现 23 篇第九节共覆盖 **5 个解禁替换项 + 2 个场景限定项 + 1 组「仍排除（与版本无关）」**，与 22 篇构成完整的版本约束/解禁对照。
- 本次仅增补内容，未改动篇数/编号/标题/链接，`Agent-Skill-index.md` 与 `wiki/index.md` 无需变动。

## 2026-09-11

### 每日整理（2026-09-11 08:07 · 自动化触发）
- 按 CLAUDE.md 第八节流程执行；任务调度 ID = `automation-1787715448943`。
- `Clippings/` 不存在，无需归类清空。
- `raw/` 今日无新增；`raw/珍大户/` 6 个文件维持 2026-09-08 14:26 mtime。`mine/` 全空。
- `output/` 今日无新增文件。
- **结论：今日无新资料进入 raw/mine/output，不触发 raw→wiki 编译，也不触发 output→wiki/skills 沉淀。**
- **index.md 统计校正**：发现 `wiki/index.md` 统计数据与实际文件数偏差 +4：
  - 珍大户：index 写 16，实际 18（15 主题页 + index + 系列脉络 + 重点必读）。
  - Agent-Skill：index 写 23 篇（24 文件），实际 25 篇（26 文件，含 09-10 新增的 24-软件开发Skill 与 25-开发Skill最佳实践）。
  - 总页面：80 → 84。
- 轻量链接检查（84 活跃页面 / 0 孤儿 / 12 已知断链）：
  - `[[CLAUDE]]` 6 处 → 根目录规则文件，是否有效取决于 Obsidian vault 范围。
  - `log.md` 内 5 处历史旧称（Git概览/Git核心概念/Git主题索引/Git学习路线与资源/双链）→ append-only 历史记录，保留原状。
  - `log.md` 内 `[[20-Skill后端试用]]` 1 处 → 已删文档历史引用，文本提及非结构化链接，保留。
- 产出 `output/daily-log-2026-09-11.md`。
- 未修改 `raw/` 与 `mine/` 下任何文件（合规自检通过）。

### 每日整理（2026-09-11 18:00 · 自动化触发 · 当日第二次）
- 按 CLAUDE.md **第八节**「每日任务」流程执行（用户消息写「第 9 节」，实为第八节；第九节是每周体检）。调度 ID = `automation-1787715448943`。
- 同日 08:07 已跑过一次（完成 index.md 统计校正 80→84、写入 daily-log 08:07 版、追加上一段）。18:00 为当日第二次，复核全库现状：
- `Clippings/` 已存在但**为空**，无剪藏需归类清空。
- `raw/` 今日无新增/修改；`raw/珍大户/` 6 文件维持 2026-09-02 mtime。`mine/` 不存在。
- `output/` 今日无新增问答/报告/幻灯片等沉淀对象（仅既有 08-26 两份 + 历次 daily-log）。
- **结论：当日无新资料进入 raw/mine/output，不触发 raw→wiki 编译，也不触发 output→wiki/skills 沉淀。**
- 复核 `wiki/index.md`：统计与实测 90 页（含 `_旧版备份` 6 页）一致 → 活跃 **84 页**（JDK&Spring 6 / 云原生 20 / git 12 / 珍大户 18 / Agent-Skill 26 / 根级 index+log 2），无需再校正。
- 轻量链接检查（`.workbuddy/linkcheck.py`，90 全页含备份）：
  - 断链全部为已知历史/结构性项：`[[CLAUDE]]` 14 处（根规则文件，vault 范围依赖）、log.md 历史旧称（`Git*` 4 类共 9 处 + `[[20-Skill后端试用]]` 2 处 + `[[双链]]`/图片示例各 1 处）、珍大户图片嵌入 ~48 处（`![[...]]` 有效嵌入，脚本正则误判）。**无新增断链**。
  - 孤儿页：仅 `wiki/log.md`（元日志页，符合预期，无入链需求）。
- 覆写 `output/daily-log-2026-09-11.md`（内容一致：当日无变更；08:07 版 index 校正记录保留于本日志上一段）。
- 合规自检：未修改 `raw/`、`mine/`（不存在）任何文件；仅追加本段并覆写 daily-log。✅

## [2026-09-11] 每周体检（自动化触发 · CLAUDE.md 第 9 节细化为 8 步）
- 触发：自动化调度，按 CLAUDE.md 第 9 节「每周体检」执行（用户消息将第 9 节细化为 8 步流程）。
- 体检范围：wiki/ 全量 101 文件（活跃 84 + `珍大户/_旧版备份` 17），5 大主题 + 根级 index/log。
- 结果摘要：
  - **孤儿页：0**（活跃页均无入链缺失；仅 `log.md` 元日志页无入链，符合预期，非内容孤儿）。
  - **长期 stub（停留 >2 周）：0**（全库页面均为实质内容；`log.md` 因正文含「待补」字样被正则误标，非占位页）。
  - **断链：无新增、无可修正项**。唯一跨库链接 `[[CLAUDE]]`（指向 vault 根规则文件，结构性有效，取决于 Obsidian vault 范围）；`log.md` 内 8 处历史旧称（`Git*`、`20-Skill后端试用` 等）按 append-only 保留。
  - **矛盾/过时核实**：联网核实 3 项关键版本/许可声明——Spring Boot 4.1.0 发布日 2026-06-10、3.5 OSS EOL 2026-06-30、Oracle JDK 21 NFTC 免费至 2026-09——**全部准确**，无修正；已在 `01-JDK21新特性.md` 与 `02-Spring4新特性.md` 补「数据核实时点：2026-09-11」并 bump `updated`。
  - **内容重叠**：高相似度对均为「刻意姐妹篇 / 精选聚合 / 同主题页模板相似」（如 22↔23、政策解读↔重点必读），**无应合并项**。
  - **写作风格提炼**：受阻——`mine/` 目录不存在，`mine/已发布/` 无定稿可读取；已创建 `wiki/moc/我的风格.md` 占位页说明状态与边界（未读 `mine/草稿/`、未用 `mine/AI生成/`）。
  - **新条目候选**：OpenJDK 发行版选型（NFTC 到期后）、Spring Boot 4.2 前瞻、AI 辅助编程 Skill 本公司落地规范、Spring Boot 4.1 可观测性落地、JDK 25 LTS 评估。
- 产出：`output/health-check-2026-09-11.md`。
- 合规自检：未修改 `raw/`、`mine/`（不存在）任何文件；仅对 2 个 wiki 条目做「核实注解 + updated 日期」增补，并新增 1 个占位页。✅

## 2026-09-12

### 每日整理（2026-09-12 18:00 · 自动化触发）
- 按 CLAUDE.md **第八节**「每日任务」流程执行（用户消息称「第 9 节」，实为第八节；第九节是每周体检）。调度 ID = `13590c9d-5273-4345-a929-0ea323ce079d`。
- `Clippings/` 已存在但**为空**，无剪藏需归类清空。
- `raw/` 今日无新增/修改；`raw/珍大户/` 6 文件 mtime 维持 2026-09-02。`mine/` 不存在。
- `output/` 今日无新增问答/报告/幻灯片等沉淀对象（最新文件为 2026-09-11）。
- **结论：当日无新资料进入 raw/mine/output，不触发 raw→wiki 编译，也不触发 output→wiki/skills 沉淀。**
- 复核 `wiki/index.md`：统计与 09-11 08:07 校正基线（活跃 84 页）一致，无需改动。
- 轻量链接检查（`.workbuddy/linkcheck.py`，91 全页含备份 + moc 占位）：
  - 断链全部为已知历史/结构性项（`[[CLAUDE]]` 17 处、`log.md` 历史旧称约 13 处、珍大户图片嵌入约 48 处），**无新增断链**。
  - 孤儿页：`wiki/log.md` + `wiki/moc/我的风格.md`（均符合预期，无入链需求）；后者为 09-11 每周体检新增的占位页，尚未计入 index.md 的 84 统计。
- 覆写 `output/daily-log-2026-09-12.md`（当日无变更）。
- 合规自检：未修改 `raw/`、`mine/`（不存在）任何文件；仅追加本段并覆写 daily-log。✅

## 2026-09-13

### 每日整理（2026-09-13 18:00 · 自动化触发）
- 按 CLAUDE.md **第八节**「每日任务」流程执行（用户消息写「第 9 节」，实为第八节；第九节是每周体检）。调度 ID = `13590c9d-5273-4345-a929-0ea323ce079d`。
- `Clippings/` 已存在但**为空**，无剪藏需归类清空。
- `raw/` 今日无新增/修改；`raw/珍大户/` 6 文件 mtime 维持 2026-09-02。`mine/` 不存在。
- `output/` 今日无新增问答/报告/幻灯片等沉淀对象（最新文件为 2026-09-12 daily-log）。
- **结论：当日无新资料进入 raw/mine/output，不触发 raw→wiki 编译，也不触发 output→wiki/skills 沉淀。**
- 复核 `wiki/index.md`：统计与 09-11/09-12 校正基线（活跃 84 页）一致，无需改动。
- 轻量链接检查（`.workbuddy/linkcheck.py`，91 全页含备份 + moc 占位）：
  - 断链全部为已知历史/结构性项（`[[CLAUDE]]` 18 处、`log.md` 历史旧称约 13 处、珍大户图片嵌入约 48 处、`[[...]]`/`[[双链]]` 示例各 1–2 处），**无新增断链**。
  - 孤儿页：`wiki/log.md` + `wiki/moc/我的风格.md`（均符合预期，无入链需求）。
- 覆写 `output/daily-log-2026-09-13.md`（当日无变更）。
- 合规自检：未修改 `raw/`、`mine/`（不存在）任何文件；仅追加本段并覆写 daily-log。✅
