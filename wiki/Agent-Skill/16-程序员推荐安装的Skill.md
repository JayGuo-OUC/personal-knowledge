---
title: 程序员推荐安装的 Skill（Vue3+TS+Element Plus / Spring Cloud+Java+MyBatis）
type: entry
created: 2026-09-08
updated: 2026-09-08
tags: [AI, Agent, Skill, Cursor, 安装, Vue3, TypeScript, ElementPlus, SpringCloud, Java, MyBatis, 推荐]
sources: [skills.sh, github.com/PatternsDev/skills, github.com/mattpocock/skills, github.com/piomin/claude-ai-spring-boot, github.com/mindrally/skills, github.com/smithery/ai, github.com/sammcj/agentic-coding, github.com/vercel-labs/skills, github.com/anthropics/skills]
---

# 程序员推荐安装的 Skill（按本司技术栈定制）

## 摘要

去哪下载见 [[15-Skill市场与下载渠道]]，安装语法见 [[10-Cursor安装与使用教程]]。本文按**本司技术栈**裁剪：**前端 Vue3 + TS + Element Plus，后端 Spring Cloud + Java + MyBatis**。已删除与栈无关的技能（React/Next、Rust、Azure 等），并为无成熟公共技能的 **Element Plus / MyBatis** 给出自建模板。每个 Skill 都标注了**触发关键词 / 调用方式**，安装命令统一用 **skills.sh 的 `npx skills add` 体系**。核心决策：**团队规范 / 合规 / 项目技术栈 → 项目级进 git；个人效率工具 → 全局**。

## 正文

### 第一步：先装「元技能」find-skills

- `find-skills`（vercel-labs/skills，**1.3M+ 安装**，全生态第一）：用自然语言搜并安装其它 Skill 的元技能
- 装好它之后，「想装什么直接说」即可，不必每次手动查市场
- 安装（全局）：`npx skills add vercel-labs/skills --skill find-skills -g`
- 它是你后续所有安装的入口，建议**全局**安装（个人通用）

### 前端（Vue3 + TypeScript + Element Plus）

| 推荐 Skill | 触发关键词 / 调用方式 | 安装（skills.sh 方式） | 建议层级 |
|-----------|----------------------|------------------------|----------|
| `vue-composition-api`（PatternsDev） | "用 Composition API 写"、"setup 语法糖"、"组合式函数" | `npx skills add PatternsDev/skills --skill vue-composition-api` | 项目级 |
| `vue-performance`（PatternsDev） | "Vue 性能优化"、"虚拟滚动"、"计算属性优化" | `npx skills add PatternsDev/skills --skill vue-performance` | 项目级 |
| `frontend-design`（anthropics） | "UI 审美"、"设计稿实现"、"避免 AI 模板味" | `npx skills add anthropics/skills --skill frontend-design` | 全局（个人偏好） |
| `grill-me`（mattpocock） | "审查 TS 类型安全"、"抓 any 滥用"、"类型审查" | `npx skills add mattpocock/skills --skill grill-me` | 全局 |
| `vite-bundle-optimization`（PatternsDev，可选） | "Vite 打包优化"、"减小体积" | `npx skills add PatternsDev/skills --skill vite-bundle-optimization` | 项目级 |
| `element-plus`（自建，见下文） | "用 el- 组件"、"表单校验"、"el-table 分页" | 自建 SKILL.md 放进项目级目录 | **项目级 + 进 git** |

> Element Plus 目前**没有成熟公共 Skill**，建议按文末模板自建并随项目进 git（团队统一组件用法）。

### 后端（Spring Cloud + Java + MyBatis）

| 推荐 Skill | 触发关键词 / 调用方式 | 安装（skills.sh 方式） | 建议层级 |
|-----------|----------------------|------------------------|----------|
| `java`（mindrally） | "Java 专家"、"Spring Boot 写法"、"Java 17 特性" | `npx skills add mindrally/skills --skill java` | 项目级 |
| `spring-boot-engineer`（piomin） | "写 Spring Boot 3 代码"、"Controller/Service"、"依赖注入" | `npx skills add piomin/claude-ai-spring-boot --skill spring-boot-engineer` | 项目级 |
| `java-architect`（piomin） | "微服务架构"、"Spring Cloud 设计"、"技术选型" | `npx skills add piomin/claude-ai-spring-boot --skill java-architect` | 项目级 |
| `java-code-review`（piomin） | "审查 Java 代码"、"空安全/并发/性能审查" | `npx skills add piomin/claude-ai-spring-boot --skill java-code-review` | 项目级（团队评审门禁） |
| `api-contract-review`（piomin） | "REST API 契约检查"、"接口版本兼容" | `npx skills add piomin/claude-ai-spring-boot --skill api-contract-review` | 项目级 |
| `spring-boot-development`（smithery/ai） | "建 Spring Boot 应用"、"REST API/微服务" | `npx skills add smithery/ai --skill spring-boot-development` | 项目级 |
| `mysql-best-practices` / `sql-optimization-patterns` | "MySQL 规范"、"SQL 调优"、"索引优化"（MyBatis 写 SQL 必看） | `npx skills find mysql-best-practices` 定位后 `npx skills add <repo> --skill ...` | 项目级 |
| `mybatis`（自建，见下文） | "建 Mapper"、"写动态 SQL"、"分页/ResultMap" | 自建 SKILL.md 放进项目级目录 | **项目级 + 进 git** |

> `piomin/claude-ai-spring-boot` 还含 `jpa-patterns`、`clean-code`、`design-patterns` 等子技能；**用 MyBatis 而非 JPA，故 `jpa-patterns` 可不装**。MyBatis 暂无成熟公共 Skill，按文末模板自建。

### 测试 / 评审（跨端通用）

| 推荐 Skill | 触发关键词 / 调用方式 | 安装（skills.sh 方式） | 建议层级 |
|-----------|----------------------|------------------------|----------|
| `tdd`（mattpocock） | "用 TDD 写"、"先写测试再实现"、"red-green-refactor" | `npx skills add mattpocock/skills --skill tdd` | 全局 |
| `code-review`（sammcj/agentic-coding） | "做代码评审"、"review my changes"、"严格自审" | `npx skills add sammcj/agentic-coding --skill code-review` | 全局（个人）/ 项目级（团队强制门禁） |

### 工程效能（Cursor 内置，无需安装）

| 推荐 Skill | 触发关键词 / 调用方式 | 建议层级 |
|-----------|----------------------|----------|
| `onboard` / `new-repo` / `create-skill` / `create-rule` | `/onboard`、`/new-repo`、`/create-skill`、`/create-rule`；"项目上手引导"、"把这个流程做成技能" | `onboard/new-repo` 项目级；`create-skill/rule` 全局 |

### 文档写作（通用）

| 推荐 Skill | 触发关键词 / 调用方式 | 安装（skills.sh 方式） | 建议层级 |
|-----------|----------------------|------------------------|----------|
| README / API doc / docstring 生成 | "生成 README"、"写 API 文档"、"补 docstring" | 用 `npx skills find readme` / `api-docs` 取准确仓库 | 全局 |

### 团队治理（贵司合规，强制项目级）

| 推荐 Skill | 触发关键词 / 调用方式 | 安装 | 建议层级 |
|-----------|----------------------|------|----------|
| `ai-coding-policy` / `ai-code-review` / `ai-coding-audit` / `cursor-setup` / `code-agent-best-practices`（贵司） | 见各技能 description，如"AI 编程能做什么/不能做什么"、"提交前评审"、"合规审计" | 从贵司私有仓库 / 白名单安装，如 `npx skills add <贵司git>/ai-coding-skills --skill ai-code-review` | **项目级 + 进 git（强制）** |

> 安装量数据见 [[15-Skill市场与下载渠道]]；Cursor 内置技能见 [[09-Cursor中的Skill全景]]。

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
| 把自己的流程固化成技能 | `npx skills init my-skill` |

> 项目级默认落到 `.cursor/skills/`（或 `.agents/skills/`），全局落到 `~/.cursor/skills/`（或 `~/.agents/skills/`）。Cursor 会递归扫描并自动加载。

### 全局 vs 项目级：决策框架

| 维度 | 用户级（全局 `-g` → `~/.cursor/skills/`） | 项目级（默认 → `.cursor/skills/` 进 git） |
|------|------------------------------------------|------------------------------------------|
| 作用范围 | 你本地**所有项目**通用 | **仅本项目**，队友 clone 即得 |
| 适合内容 | 个人效率工具、私人偏好 | 团队规范、技术栈、合规要求 |
| 同步到 Cloud / SSH worker | ❌ **不会同步**（Cursor 限制） | ✅ 仓库里就有 |
| 版本 / 审计 | 个人维护，难统一 | 进 git，可评审、可回滚、可审计 |
| 典型例子 | `find-skills`、`grill-me`、`tdd`、个人前端偏好 | `vue-composition-api`、`spring-boot-engineer`、`element-plus`、`mybatis`、评审门禁 |

> **两种口径的叠加**（skills.sh 官方建议 + 贵司合规）：
> - skills.sh 官方：通用型（code review、tdd）→ **全局**；领域型（框架）→ **项目级**
> - 贵司强合规：**凡团队标准 / 治理 / 栈专属（vue、spring、element-plus、mybatis）→ 一律项目级 + 进 git**
> - 一句话：**个人习惯放全局，团队规矩进项目。**

> ⚠️ **关键限制（来自 [[09-Cursor中的Skill全景]]）**：Cursor **不会**把 `~/.cursor/skills/` 同步到 Cloud Agents、远程 SSH、self-hosted worker。这些环境只能用**仓库里的项目级技能**。推论：**团队规范必须放项目级并进 git。**

### 栈专属技能（Element Plus / MyBatis）建议自建

这两个目前没有成熟公共 Skill，按官方示例自建并随项目进 git 最稳。模板（放进 `.cursor/skills/<name>/SKILL.md`）：

```markdown
---
name: mybatis
description: MyBatis / MyBatis-Plus 开发规范。当用户创建 Mapper、编写动态 SQL、定义 ResultMap 或做分页时自动激活。
---
# MyBatis 开发指南
## 核心规则
1. 参数用 @Param 显式命名，XML 中用 ${param} 防歧义
2. 批量用 <foreach>，避免循环单条
3. 结果映射优先 resultMap；开启 mapUnderscoreToCamelCase 做下划线转驼峰
4. 分页用 PageHelper 或 MyBatis-Plus Page，禁止内存分页
5. 防 SQL 注入：${} 仅用于排序/表名白名单，值一律用 #{}
```

```markdown
---
name: element-plus
description: Element Plus 组件使用规范（Vue3 + TS）。当用户使用 el- 组件、表单校验、el-table 或 el-dialog 时自动激活。
---
# Element Plus 指南
## 核心规则
1. 表单用 <el-form> + rules + el-form-item，校验用 async-validator
2. 表格用 <el-table> + 作用域插槽，分页用 <el-pagination> 配合 v-model
3. 弹窗用 <el-dialog> 配 v-model，避免多弹窗同时
4. 图标用 @element-plus/icons-vue 按需引入
5. 主题用 SCSS 变量覆盖，勿改 node_modules
```

### 落地建议（结合贵司强合规背景）

1. **治理 / 合规类 + 栈专属技能 → 一律项目级 + 进 git**
   - 包括：`ai-coding-policy`、`ai-code-review`、`ai-coding-audit`、`cursor-setup`、`code-agent-best-practices`，以及自建的 `element-plus`、`mybatis`、`vue-composition-api`、`spring-boot-engineer`
   - 理由：可审计、可评审、可同步到 worker、队友 clone 即得
2. **个人效率工具 → 全局（`-g`）**
   - `find-skills`、`grill-me`、`tdd`、个人前端设计偏好、文档生成
3. **安装前先预览**：`npx skills add owner/repo --list`，确认内容再 `--skill` 安装

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
- [[02-Agent-Skills开放标准与生态全景]]

## 来源

- https://skills.sh （排行榜、安装量、CLI 文档）
- https://github.com/PatternsDev/skills （vue-composition-api、vue-performance、vite-bundle-optimization）
- https://github.com/mattpocock/skills （grill-me、tdd）
- https://github.com/piomin/claude-ai-spring-boot （spring-boot-engineer、java-architect、java-code-review、api-contract-review）
- https://github.com/mindrally/skills （java）
- https://github.com/smithery/ai （spring-boot-development）
- https://github.com/sammcj/agentic-coding （code-review）
- https://github.com/vercel-labs/skills （find-skills）
- https://github.com/anthropics/skills （frontend-design）
- 贵司治理技能：`~/.workbuddy/skills/` 下 `ai-coding-*` / `cursor-setup` / `code-agent-best-practices` 系列
