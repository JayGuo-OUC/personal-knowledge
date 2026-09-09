---
title: 写文档必备的 Skill（需求规格说明书 / 概要设计 / 详细设计）
type: entry
created: 2026-09-08
updated: 2026-09-08
tags: [AI, Agent, Skill, Cursor, 文档, 需求规格说明书, 概要设计, 详细设计, UML, C4, ADR, OpenAPI, 技术写作]
sources: [skills.sh, github.com/juanca202/sdd-devkit, github.com/jabrena/cursor-rules-java, github.com/markdown-viewer/skills, github.com/wshobson/agents, github.com/vercel/ai, github.com/jabrena/plinth, github.com/dengineproblem/agents-monorepo, github.com/aiskillstore/marketplace]
---

# 写文档必备的 Skill（需求规格说明书 / 概要设计 / 详细设计）

## 摘要

你们日常要产出**需求规格说明书、概要设计、详细设计**三类工程文档。本文按**文档类型**拆分，列出每种文档该装哪些 Skill，每个都标注**触发关键词 / 调用方式**，安装命令统一用 **skills.sh 的 `npx skills add` 体系**。所有文档类技能产出的是 Markdown / PlantUML，建议**项目级 + 进 git**（团队模板统一、可追溯、可同步到 worker）。元技能 `find-skills` 仍作入口。技术栈专项（Vue/Spring/Java/MyBatis）见 [[16-程序员推荐安装的Skill]]；通用优质技能总览见 [[18-通用Skill]]。

## 正文

### 第一步：先装「元技能」find-skills

- `find-skills`（vercel-labs/skills，**1.4M+ 安装**，⭐30.6k，全生态第一）：用自然语言搜并安装其它 Skill 的元技能

> ⭐ 说明：表格中 ⭐ 数值为该技能**宿主 GitHub 仓库**的 Star 数（一个仓库常含多个 Skill，故为仓库级指标，并非单技能独立计数）。`smithery/ai` 与 `dengineproblem/agents-monorepo` 当前 GitHub 返回 404（仓库已不可访问），标 N/A。
- 想装什么直接说（"找个写需求规格说明书的技能"）即可，不必每次手动查市场
- 安装（全局）：`npx skills add vercel-labs/skills --skill find-skills -g`
- 它是后续所有安装的入口，建议**全局**安装（个人通用）

### 一、需求规格说明书（SRS）

| 推荐 Skill | 触发关键词 / 调用方式 | 安装（skills.sh 方式） | 建议层级 |
|-----------|----------------------|------------------------|----------|
| `work-define`（juanca202/sdd-devkit · ⭐0） | "写需求规格说明书"、"拆解用户故事"、"补验收标准"、"功能需求清单" | `npx skills add juanca202/sdd-devkit --skill work-define` | **项目级 + 进 git** |
| `031-architecture-adr-functional-requirements`（jabrena/plinth · ⭐437） | "为功能需求/REST API 出 ADR"、"需求决策记录" | `npx skills add jabrena/plinth --skill 031-architecture-adr-functional-requirements` | **项目级 + 进 git** |
| `uml`（markdown-viewer/skills · ⭐3.3k）— 用例图 | "画用例图"、"功能交互图"、"角色与用例" | `npx skills add markdown-viewer/skills --skill uml` | **项目级 + 进 git** |

> `work-define` 会把需求拆成带标识（US-XX）的用户故事 + 验收标准，正好对应 SRS 的功能需求与验收准则章节；`uml` 的 use case 图用于功能建模。

### 二、概要设计

| 推荐 Skill | 触发关键词 / 调用方式 | 安装（skills.sh 方式） | 建议层级 |
|-----------|----------------------|------------------------|----------|
| `architecture-decision-records`（wshobson/agents · ⭐39.5k，15.3k 安装） | "记架构决策"、"出 ADR"、"技术选型留痕"、"MADR 模板" | `npx skills add wshobson/agents --skill architecture-decision-records` | **项目级 + 进 git** |
| `adr-skill`（vercel/ai · ⭐26.6k） | "把决策写成可执行 ADR"、"技术决策含实施方案" | `npx skills add vercel/ai --skill adr-skill` | **项目级 + 进 git** |
| `034-architecture-diagrams`（jabrena/cursor-rules-java → jabrena/plinth · ⭐437） | "画 C4 模型"、"上下文/容器/组件图"、"ER 图（库表设计）" | `npx skills add jabrena/cursor-rules-java --skill 034-architecture-diagrams` | **项目级 + 进 git** |
| `uml`（markdown-viewer/skills · ⭐3.3k）— 组件图/部署图 | "画组件图"、"部署架构图" | `npx skills add markdown-viewer/skills --skill uml` | **项目级 + 进 git** |

> 概要设计 = 模块划分 + 技术选型 + 部署架构。`architecture-decision-records` / `adr-skill` 管"为什么这么选"（ADR 章节），`034-architecture-diagrams` 用 C4（Context→Container→Component）画分层架构与 ER 图，天然对应概要设计模板。

### 三、详细设计

| 推荐 Skill | 触发关键词 / 调用方式 | 安装（skills.sh 方式） | 建议层级 |
|-----------|----------------------|------------------------|----------|
| `034-architecture-diagrams`（jabrena/plinth · ⭐437） | "画类图"、"序列图"、"状态机图"、"ER 图" | `npx skills add jabrena/cursor-rules-java --skill 034-architecture-diagrams` | **项目级 + 进 git** |
| `uml`（markdown-viewer/skills · ⭐3.3k） | "UML 类图/时序图/状态图"、"PlantUML 语法" | `npx skills add markdown-viewer/skills --skill uml` | **项目级 + 进 git** |
| `design-define`（juanca202/sdd-devkit · ⭐0） | "写详细设计文档"、"数据模型/API/流程图规范"、"技术规格书" | `npx skills add juanca202/sdd-devkit --skill design-define` | **项目级 + 进 git** |
| `openapi-documentation`（dengineproblem/agents-monorepo · ⭐N/A，GitHub 404） | "写接口契约"、"OpenAPI 3.0 规范"、"Swagger 文档" | `npx skills add dengineproblem/agents-monorepo --skill openapi-documentation` | **项目级 + 进 git** |
| `api-documentation-generator`（aiskillstore/marketplace · ⭐418） | "从代码生成 OpenAPI"、"自动出接口文档" | `npx skills add aiskillstore/marketplace --skill api-documentation-generator` | **项目级 + 进 git** |

> 详细设计 = 类/对象设计 + 接口契约 + 关键流程。用 `034-architecture-diagrams` + `uml` 出类图/时序图/状态机，`design-define` 把数据模型、API、流程标准化成带 `MD-XX/API-XX/FL-XX` 标识的技术规格，`openapi-documentation` 把 REST 接口写成可执行契约（对应你们 Spring Cloud 的微服务接口）。

### 安装命令（skills.sh 统一体系）

| 目的 | 命令 |
|------|------|
| 预览仓库内有哪些技能（先看清再装） | `npx skills add owner/repo --list` |
| 装单个技能（**项目级，默认**） | `npx skills add owner/repo --skill skill-name` |
| 装到**全局**（跨项目可用） | `npx skills add owner/repo --skill skill-name -g` |
| 指定装到某个 Agent | `npx skills add owner/repo --skill skill-name -a cursor`（或 `-a claude-code`） |
| 装整个仓库全部技能 | `npx skills add owner/repo --all` |
| 按关键词搜社区技能 | `npx skills find <关键词>` |
| 查看已装（全局加 `-g`） | `npx skills list` / `npx skills list -g` |
| 更新（单个 / 全部） | `npx skills update <name>` / `npx skills update` |
| 删除 | `npx skills remove <name>` |
| 把自己的文档模板固化成技能 | `npx skills init my-doc-skill` |

> 项目级默认落到 `.cursor/skills/`（或 `.agents/skills/`），全局落到 `~/.cursor/skills/`（或 `~/.agents/skills/`）。Cursor 会递归扫描并自动加载。

### 全局 vs 项目级：决策框架（文档场景）

| 维度 | 用户级（全局 `-g`） | 项目级（默认 → `.cursor/skills/` 进 git） |
|------|-------------------|------------------------------------------|
| 作用范围 | 你本地所有项目 | 仅本项目，队友 clone 即得 |
| 适合内容 | 个人偏好的写作风格 | **团队文档模板、SRS/设计章节规范、画图约定** |
| 同步到 Cloud / SSH worker | ❌ 不会同步 | ✅ 仓库里就有 |
| 版本 / 审计 | 个人维护，难统一 | 进 git，可评审、可回滚、可审计 |
| 典型例子 | `find-skills` | `work-define`、`design-define`、`034-architecture-diagrams`、`architecture-decision-records`、`openapi-documentation` |

> **结论（结合贵司强合规）**：文档类技能本质是"团队模板与规范"，务必**项目级 + 进 git**——队友拿到即用、审计可查、也能跑在 Cloud/SSH worker 上。

> ⚠️ **关键限制（来自 [[09-Cursor中的Skill全景]]）**：Cursor **不会**把 `~/.cursor/skills/` 同步到 Cloud Agents、远程 SSH、self-hosted worker。团队文档规范必须放项目级并进 git。

### 落地建议（结合贵司强合规背景）

1. **文档/设计类技能 → 一律项目级 + 进 git**
   - 包括：`work-define`、`design-define`、`034-architecture-diagrams`、`uml`、`architecture-decision-records`、`adr-skill`、`031-architecture-adr-functional-requirements`、`openapi-documentation`、`api-documentation-generator`
   - 理由：模板统一、可审计、可评审、可同步到 worker、队友 clone 即得
2. **元技能 `find-skills` → 全局（`-g`）**，作为个人入口
3. **装前先预览**：`npx skills add owner/repo --list`，确认内容再 `--skill` 安装；产出物（`.md` / `.puml`）统一放进 `docs/` 对应子目录
4. **合规衔接**：文档模板里嵌入 [[12-Skill安全与企业合规]] 的数据分级（L0–L3）要求，涉密章节单列

### 风险提示

- 从 [[12-Skill安全与企业合规]] 与 [[15-Skill市场与下载渠道]] 已知：**市场 ≠ 可信**（Snyk 审计 3984 个技能，13.4% 含严重问题；学术界扫 42447 个，26.1% 含漏洞）
- 项目级文档技能**进 git 前必须做代码评审**；带 `scripts/` 的技能出事概率是纯指令型的 **2.12 倍**
- 企业：只从白名单市场下载，建立技能审批流程后再进项目级目录；文档产出物也需走内部评审与密级标识

## 相关

- [[09-Cursor中的Skill全景]]
- [[10-Cursor安装与使用教程]]
- [[12-Skill安全与企业合规]]
- [[15-Skill市场与下载渠道]]
- [[16-程序员推荐安装的Skill]]
- [[18-通用Skill]]
- [[02-Agent-Skills开放标准与生态全景]]

## 来源

- https://skills.sh （排行榜、安装量、CLI 文档）
- https://github.com/juanca202/sdd-devkit （work-define 需求/功能文档、design-define 技术设计文档）
- https://github.com/jabrena/cursor-rules-java （034-architecture-diagrams：UML 类/序列/状态机 + C4 + ER，PlantUML）
- https://github.com/markdown-viewer/skills （uml：UML 图生成器）
- https://github.com/wshobson/agents （architecture-decision-records：ADR 模板，15.3k 安装）
- https://github.com/vercel/ai （adr-skill：可执行 ADR 规范）
- https://github.com/jabrena/plinth （031-architecture-adr-functional-requirements：功能需求/REST API 的 ADR）
- https://github.com/dengineproblem/agents-monorepo （openapi-documentation：OpenAPI 3.0/Swagger 规范）
- https://github.com/aiskillstore/marketplace （api-documentation-generator：从代码生成 OpenAPI）
- https://github.com/vercel-labs/skills （find-skills 元技能）
