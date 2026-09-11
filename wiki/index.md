---
title: 知识库总索引
type: index
created: 2026-08-26
updated: 2026-09-11
tags: [索引]
sources: []
---

# 知识库总索引（Index）

> 问答第一步先查本页。库的规则见 [[CLAUDE]]。

## 主题

- [[JDK&Spring-index]] — JDK & Spring 架构升级（JDK 21 / Spring Boot 4 特性、版本对比、迁移路径、升级论证），共 5 篇
- [[云原生-index]] — 云原生（容器 / Kubernetes / 微服务 / 可观测性 / DevOps 等），共 19 篇
- [[git-index]] — Git（版本控制 / 分支 / 远程协作 / 变基 / 工作流等），共 11 篇
- [[珍大户-index]] — 珍大户的经济圈（政策解读 / 年度大预测 / 房产与城市 / 股票与投资 / 行业分析等 15 个主题），857 条官方精华 + 19 条目录补录
- [[Agent-Skill-index]] — AI Agent Skill（概念 / 开放标准 / SKILL.md 结构 / 渐进式披露 / 作用原理 / 与 Rules·MCP·Subagent 对比 / Cursor 安装使用 / 安全合规 / 技术栈选型 / 文档与通用技能 / Cursor 内置技能 / 真实代码试用 / 软件开发 Skill / 开发最佳实践），共 25 篇 + 配套 Cursor 技能包

## 统计（2026-09-11 更新）

- 主题数：5
- wiki 页面数：84（JDK&Spring 6 / 云原生 20 / git 12 / 珍大户 18 / Agent-Skill 26 / 根级 index+log 2）
- 本次校正：index 统计与实际文件数偏差修正（珍大户 16→18 计入系列脉络+重点必读；Agent-Skill 23→25 补录 24-软件开发Skill 与 25-开发Skill最佳实践）

## 相关

- [[CLAUDE]]
- [[JDK&Spring-index]]
- [[云原生-index]]
- [[git-index]]
- [[珍大户-index]]
- [[Agent-Skill-index]]

## 来源

- 初始化自上一轮构建的云原生知识库；本索引按 CLAUDE.md 规范重建。
- 2026-09-02 新增「JDK & Spring 架构升级」主题，服务于公司后端从 JDK 8 + Spring Boot 2.3 升级至 JDK 21 + Spring Boot 4 的选型决策。
- 2026-09-02 新增「珍大户的经济圈」主题，**857 条官方精华**（平台 `digested` 标记）正文约 143 万字，时间跨度 2018-08 至 2026-09，另补录 19 条官方目录 4—5 心条目，落位于 `wiki/珍大户/`。原始数据见 `raw/珍大户/`。
- 2026-09-03 新增「AI Agent Skill」主题（`wiki/Agent-Skill/`），14 篇条目 + MOC 索引。核心来源为 Agent Skills 开放标准规范（agentskills.io）、Cursor 官方文档（Skills）、Anthropic《The Complete Guide to Building Skills for Claude》，并实测本机 Cursor 内置 24 个技能。配套产出：根目录 `skills/cursor-agent-skills/` 六件套（已安装至 `~/.cursor/skills/`），面向政府/工业/水务强合规场景。
- 2026-09-08 补充「AI Agent Skill」主题 4 篇：15 Skill 市场与下载渠道 / 16 程序员推荐安装的 Skill / 17 文档 Skill / 18 通用 Skill；并新增 **19 Cursor 内置 Skill 一览**（实测本机 `~/.cursor/skills-cursor/` 25 个 + 官方文档 Built-in 表 19 个，去重后 26 个，标注哪些只能 `/` 手动调用）。同日按「宿主仓库 ⭐≥1K」门槛重写 16 篇，淘汰未达标的外置技能。
- 2026-09-08 为 15—18 篇全部外置技能标注宿主 GitHub 仓库 Star 数（GitHub API 实时抓取）。
- 2026-09-09 新增 **20-后端Skill试用**（同一 `sjz-back` 项目上把已装 **26 个 skill 逐个跑一遍**的适用性体检：通过 0 · 部分通过 17 · 未通过 9；最高优先级为 SQL 注入 `${id}`、无 Flyway/Liquibase 版本化迁移、Redis `KEYS` 与大量无 TTL、字段 `@Autowired` 注入主导（170+ 文件）、测试与质量门禁缺失、配置明文口令、日志不规范）。与 20 篇互补：**20 篇＝重点缺陷的深度证据链 + 修复代码，21 篇＝全量 skill 适用性体检（广度）**。
- 2026-09-09 新增 **21-前端Skill试用**（`sjz-front`（Vue 3.5 + Vite 7 + Element Plus + Pinia，JS 非 TS、无测试链）上已装 **20 个前端 skill 逐个审计**：PASS 6 · WARN 9 · FAIL 5。PASS 主力为 `vue` / `vue-best-practices` / `vue-pinia-best-practices` / `vue-router-best-practices` / `pinia` / `element-plus`；FAIL 5 个多为 React·Next·MUI·TanStack 或 TS 专用栈（`frontend-patterns`、`frontend-dev-guidelines`、`frontend-ui-engineering`、`typescript-pro`、`vitest`），建议停用。与 21 篇构成**前后端完整对照**。）
- 2026-09-10 新增 **22-Skill现有技术栈**（按公司实际栈重做的选型：后端 Java/SpringCloud/MyBatis/MySQL/Redis/Kafka + 前端 Vue3/TS/ElementPlus + UI 还原链路；门槛 installs≥1K、**每技术方向仅一个**。产出 **17 个可安装 + 2 个自建**（MyBatis、Element Plus 在 ≥1K 门槛下确无公共 skill）；附按仓库合并的安装命令与 **JDK8/Boot2.3 版本护栏写法**。核心结论：生态主流 skill 全面向 Java 17+/Boot 3.x，存量项目须加护栏才能安全使用。）
- 2026-09-10 新增 **23-skill主流技术栈**（**不受版本约束**的主流栈选型，23 篇的姐妹篇：后端 Java/SpringCloud/MyBatis/MySQL/Redis/Kafka + 前端 Vue3/TS/ElementPlus + UI 还原。产出 **16 个可安装 + 1 个自建（MyBatis）**；补搜确认 **MyBatis 在 ≥1K 下确为 0 条**、ORM 过线的仅 `jpa-patterns`(9,190) 但属 JPA 不适用。文档附安装命令、与 23 篇的差异对照表，以及**验证状态标注**（哪些已读原文、哪些仅依据 installs/star）。）
