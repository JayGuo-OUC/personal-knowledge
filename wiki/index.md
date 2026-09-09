---
title: 知识库总索引
type: index
created: 2026-08-26
updated: 2026-09-09
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
- [[Agent-Skill-index]] — AI Agent Skill（概念 / 开放标准 / SKILL.md 结构 / 渐进式披露 / 作用原理 / 与 Rules·MCP·Subagent 对比 / Cursor 安装使用 / 安全合规 / 技术栈选型 / 文档与通用技能 / Cursor 内置技能 / 真实代码试用），共 20 篇 + 配套 Cursor 技能包

## 统计（2026-09-08 更新）

- 主题数：5
- wiki 页面数：77（JDK&Spring 6 / 云原生 20 / git 12 / 珍大户 16 / Agent-Skill 21 / 根级 index+log 2）
- 本次新增：15 个页面（「AI Agent Skill」主题，14 篇条目 + MOC 索引）；另在根目录 `skills/` 产出 `cursor-agent-skills/` 技能包（6 个 Cursor Agent Skill + 1 个 Python 合规扫描脚本 + 1 份六维评审清单），已安装至 `~/.cursor/skills/`

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
- 2026-09-09 新建 **20-Skill后端试用**（在 `E:\guojian\01project\sjz\sjz-back` 套用已装 21 个 Skill 的静态分析试用报告：命中 2 处 SQL 注入 `${id}`、16 处多写无事务、24 文件 `SELECT *`、3 处深分页、30/38 处日志与栈打印反模式，附证据链与修复建议）。并修正 16 篇（删 skills.sh 未收录项、订正安装量、补测试模块）。
