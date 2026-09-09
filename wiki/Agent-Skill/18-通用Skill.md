---
title: 通用优质 Skill 总览（技术负责人 / 架构师工作相关）
type: entry
created: 2026-09-08
updated: 2026-09-08
tags: [AI, Agent, Skill, Cursor, 通用, 架构, 代码质量, 提交规范, 版本管理, 合规, 推荐]
sources: [skills.sh, github.com/vercel-labs/skills, github.com/wshobson/agents, github.com/vercel/ai, github.com/jabrena/cursor-rules-java, github.com/sammcj/agentic-coding, github.com/mattpocock/skills, github.com/tigrisdata/skills, github.com/eva813/skills-base, github.com/laurigates/claude-plugins]
---

# 通用优质 Skill 总览（技术负责人 / 架构师工作相关）

## 摘要

作为**技术负责人 / 架构师**（公司做政府、工业、水务等强合规业务，前端 Vue3 + TS + Element Plus，后端 Spring Cloud + Java + MyBatis），日常最值得装的优秀 Skill 不止写代码。本文按**工作场景**分 6 类，每类标注**触发关键词 / 调用方式**，安装命令统一用 **skills.sh 的 `npx skills add` 体系**。文档类、技术栈类分别在 [[17-文档Skill]]、[[16-程序员推荐安装的Skill]] 详述，本文是"通用且必装"的总览与入口。核心决策：**团队规范 / 合规 / 架构决策 / 文档模板 → 项目级进 git；个人效率工具 → 全局**。

## 正文

### 第一步：先装「元技能」find-skills

- `find-skills`（vercel-labs/skills，**1.4M+ 安装**，⭐30.6k，全生态第一）：用自然语言搜并安装其它 Skill 的元技能

> ⭐ 说明：表格中 ⭐ 数值为该技能**宿主 GitHub 仓库**的 Star 数（一个仓库常含多个 Skill，故为仓库级指标，并非单技能独立计数）。`smithery/ai` 与 `dengineproblem/agents-monorepo` 当前 GitHub 返回 404（仓库已不可访问），标 N/A。
- 想装什么直接说即可，不必每次手动查市场
- 安装（全局）：`npx skills add vercel-labs/skills --skill find-skills -g`
- 它是后续所有安装的入口，建议**全局**安装（个人通用）

### 一、架构与设计决策（架构师核心）

| 推荐 Skill | 触发关键词 / 调用方式 | 安装（skills.sh 方式） | 建议层级 |
|-----------|----------------------|------------------------|----------|
| `architecture-decision-records`（wshobson/agents · ⭐39.5k，15.3k 安装） | "记架构决策"、"出 ADR"、"技术选型留痕"、"MADR 模板"、"设计评审" | `npx skills add wshobson/agents --skill architecture-decision-records` | **项目级 + 进 git** |
| `adr-skill`（vercel/ai · ⭐26.6k） | "把决策写成可执行 ADR"、"技术决策含实施方案"、"为什么这么选" | `npx skills add vercel/ai --skill adr-skill` | **项目级 + 进 git** |
| `034-architecture-diagrams`（jabrena/cursor-rules-java → jabrena/plinth · ⭐437） | "画 C4 模型"、"UML 类/序列/状态机图"、"ER 图" | `npx skills add jabrena/cursor-rules-java --skill 034-architecture-diagrams` | **项目级 + 进 git** |

> 技术负责人的核心产出之一是**技术决策留痕**与**架构图**。ADR 类技能把"为什么选 Spring Cloud / 为什么用 MyBatis 而非 JPA"固化成可审计记录；`034-architecture-diagrams` 用 C4 + PlantUML 一键出图，写进概要/详细设计（联动 [[17-文档Skill]]）。

### 二、代码质量与评审

| 推荐 Skill | 触发关键词 / 调用方式 | 安装（skills.sh 方式） | 建议层级 |
|-----------|----------------------|------------------------|----------|
| `code-review`（sammcj/agentic-coding · ⭐160） | "做代码评审"、"review my changes"、"严格自审" | `npx skills add sammcj/agentic-coding --skill code-review` | 全局（个人）/ 项目级（团队强制门禁） |
| `tdd`（mattpocock/skills · ⭐256k） | "用 TDD 写"、"先写测试再实现"、"red-green-refactor" | `npx skills add mattpocock/skills --skill tdd` | 全局 |
| `grill-me`（mattpocock/skills · ⭐256k） | "审查 TS 类型安全"、"抓 any 滥用"、"类型审查" | `npx skills add mattpocock/skills --skill grill-me` | 全局 |

> 代码质量是团队红线。详见 [[16-程序员推荐安装的Skill]] 的测试/评审小节与贵司 `ai-code-review` 门禁。

### 三、提交规范与版本管理

| 推荐 Skill | 触发关键词 / 调用方式 | 安装（skills.sh 方式） | 建议层级 |
|-----------|----------------------|------------------------|----------|
| `conventional-commits`（tigrisdata/skills · ⭐3） | "按约定式提交"、"生成 CHANGELOG"、"语义化版本" | `npx skills add tigrisdata/skills --skill conventional-commits` | 全局 |
| `git-conventional-commits`（eva813/skills-base · ⭐2） | "规范 git 提交"、"feat/fix/docs 分类"、"提交信息校验" | `npx skills add eva813/skills-base --skill git-conventional-commits` | 全局 |
| `git-commit-workflow`（laurigates/claude-plugins · ⭐58） | "提交前上下文收集"、"显式暂存"、"关联 issue" | `npx skills add laurigates/claude-plugins --skill git-commit-workflow` | 全局 |

> 统一的提交规范 = 自动 CHANGELOG + 语义化发版 + 可审计变更。个人效率类，建议**全局**。

### 四、需求与文档（详见 [[17-文档Skill]]）

| 推荐 Skill | 触发关键词 / 调用方式 | 安装（skills.sh 方式） | 建议层级 |
|-----------|----------------------|------------------------|----------|
| `work-define`（juanca202/sdd-devkit · ⭐0） | "写需求规格说明书"、"拆解用户故事"、"补验收标准" | `npx skills add juanca202/sdd-devkit --skill work-define` | **项目级 + 进 git** |
| `design-define`（juanca202/sdd-devkit · ⭐0） | "写详细设计"、"数据模型/API/流程图规范" | `npx skills add juanca202/sdd-devkit --skill design-define` | **项目级 + 进 git** |
| `openapi-documentation`（dengineproblem/agents-monorepo · ⭐N/A，GitHub 404） | "写接口契约"、"OpenAPI 3.0 规范" | `npx skills add dengineproblem/agents-monorepo --skill openapi-documentation` | **项目级 + 进 git** |

> 三类工程文档（需求/概要/详细）的完整 Skill 清单见 [[17-文档Skill]]，此处仅列代表项。

### 五、安全合规（详见 [[12-Skill安全与企业合规]] + 贵司治理系列）

| 推荐 Skill | 触发关键词 / 调用方式 | 安装 | 建议层级 |
|-----------|----------------------|------|----------|
| `ai-coding-policy` / `ai-code-review` / `ai-coding-audit` / `cursor-setup` / `code-agent-best-practices`（贵司） | 见各技能 description，如"AI 编程能做什么/不能做什么"、"提交前评审"、"合规审计" | 从贵司私有仓库 / 白名单安装，如 `npx skills add <贵司git>/ai-coding-skills --skill ai-code-review` | **项目级 + 进 git（强制）** |

> 政府/工业/水务强合规，代码不出境是红线。详见 [[12-Skill安全与企业合规]] 与 [[16-程序员推荐安装的Skill]] 的落地建议。

### 六、技术栈专项（详见 [[16-程序员推荐安装的Skill]]）

- **前端**：`vue-composition-api`、`vue-performance`（PatternsDev/skills · ⭐246）、`frontend-design`（anthropics/skills · ⭐175k）、`grill-me`（mattpocock/skills · ⭐256k，TS）、`element-plus`（自建进 git）
- **后端**：`java`（mindrally/skills · ⭐258）、`spring-boot-engineer` / `java-architect` / `java-code-review` / `api-contract-review`（piomin/claude-ai-spring-boot · ⭐1.3k）、`spring-boot-development`（smithery/ai · ⭐N/A，仓库 GitHub 404）、`mysql-best-practices` / `sql-optimization-patterns`、`mybatis`（自建进 git）
- 完整触发词与安装命令见 [[16-程序员推荐安装的Skill]]。

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
| 把流程固化成技能 | `npx skills init my-skill` |

> 项目级默认落到 `.cursor/skills/`（或 `.agents/skills/`），全局落到 `~/.cursor/skills/`（或 `~/.agents/skills/`）。Cursor 会递归扫描并自动加载。

### 全局 vs 项目级：决策框架

| 维度 | 用户级（全局 `-g` → `~/.cursor/skills/`） | 项目级（默认 → `.cursor/skills/` 进 git） |
|------|------------------------------------------|------------------------------------------|
| 作用范围 | 你本地**所有项目**通用 | **仅本项目**，队友 clone 即得 |
| 适合内容 | 个人效率工具、私人偏好 | 团队规范、架构决策、文档模板、合规要求 |
| 同步到 Cloud / SSH worker | ❌ **不会同步**（Cursor 限制） | ✅ 仓库里就有 |
| 版本 / 审计 | 个人维护，难统一 | 进 git，可评审、可回滚、可审计 |
| 典型例子 | `find-skills`、`grill-me`、`tdd`、`conventional-commits`、个人提交偏好 | `architecture-decision-records`、`adr-skill`、`034-architecture-diagrams`、`work-define`、`code-review`（团队门禁）、贵司 `ai-coding-*` |

> **两种口径的叠加**（skills.sh 官方 + 贵司合规）：
> - skills.sh 官方：通用型（code review、tdd）→ **全局**；领域型（框架）→ **项目级**
> - 贵司强合规：**凡团队标准 / 治理 / 架构决策 / 文档模板 → 一律项目级 + 进 git**
> - 一句话：**个人习惯放全局，团队规矩进项目。**

> ⚠️ **关键限制（来自 [[09-Cursor中的Skill全景]]）**：Cursor **不会**把 `~/.cursor/skills/` 同步到 Cloud Agents、远程 SSH、self-hosted worker。团队规范必须放项目级并进 git。

### 落地建议（结合贵司强合规背景）

1. **治理 / 合规 / 架构决策 / 文档模板类 → 一律项目级 + 进 git**
   - 包括：贵司 `ai-coding-*` 系列、`architecture-decision-records`、`adr-skill`、`034-architecture-diagrams`、`work-define`、`design-define`、`openapi-documentation`
   - 理由：可审计、可评审、可同步到 worker、队友 clone 即得
2. **个人效率工具 → 全局（`-g`）**
   - `find-skills`、`grill-me`、`tdd`、`conventional-commits`、`git-conventional-commits`、`git-commit-workflow`
3. **安装前先预览**：`npx skills add owner/repo --list`，确认内容再 `--skill` 安装
4. **技术栈专项**走 [[16-程序员推荐安装的Skill]]，**文档专项**走 [[17-文档Skill]]，本文作总入口

### 风险提示

- 从 [[12-Skill安全与企业合规]] 与 [[15-Skill市场与下载渠道]] 已知：**市场 ≠ 可信**（Snyk 审计 3984 个技能，13.4% 含严重问题；学术界扫 42447 个，26.1% 含漏洞）
- 项目级技能**进 git 前必须做代码评审**；带 `scripts/` 的技能出事概率是纯指令型的 **2.12 倍**
- 企业：只从白名单市场下载，建立技能审批流程后再进项目级目录

## 相关

- [[09-Cursor中的Skill全景]]
- [[10-Cursor安装与使用教程]]
- [[11-实战技能包六件套]]
- [[12-Skill安全与企业合规]]
- [[15-Skill市场与下载渠道]]
- [[16-程序员推荐安装的Skill]]
- [[17-文档Skill]]
- [[02-Agent-Skills开放标准与生态全景]]

## 来源

- https://skills.sh （排行榜、安装量、CLI 文档）
- https://github.com/vercel-labs/skills （find-skills 元技能）
- https://github.com/wshobson/agents （architecture-decision-records：ADR 模板，15.3k 安装）
- https://github.com/vercel/ai （adr-skill：可执行 ADR 规范）
- https://github.com/jabrena/cursor-rules-java （034-architecture-diagrams：UML + C4 + ER）
- https://github.com/sammcj/agentic-coding （code-review）
- https://github.com/mattpocock/skills （tdd、grill-me）
- https://github.com/tigrisdata/skills （conventional-commits）
- https://github.com/eva813/skills-base （git-conventional-commits）
- https://github.com/laurigates/claude-plugins （git-commit-workflow）
- 文档类见 [[17-文档Skill]] 来源；技术栈类见 [[16-程序员推荐安装的Skill]] 来源
