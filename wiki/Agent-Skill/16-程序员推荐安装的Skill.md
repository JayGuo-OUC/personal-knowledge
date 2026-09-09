---
title: 程序员推荐安装的 Skill（Vue3+TS+Vite+Element Plus / Spring Cloud+Java+MyBatis）
type: entry
created: 2026-09-08
updated: 2026-09-09
tags: [AI, Agent, Skill, Cursor, 安装, Vue3, TypeScript, Vite, ElementPlus, SpringCloud, Java, MyBatis, MySQL, Redis, 测试, 架构, 规范, 推荐]
sources: [skills.sh, github.com/affaan-m/ecc, github.com/obra/superpowers, github.com/mattpocock/skills, github.com/anthropics/skills, github.com/addyosmani/agent-skills, github.com/github/awesome-copilot, github.com/tt-a1i/archify, github.com/antfu/skills, github.com/vuejs-ai/skills, github.com/piomin/claude-ai-spring-boot]
---

# 程序员推荐安装的 Skill（按本司技术栈定制）

## 摘要

去哪下载见 [[15-Skill市场与下载渠道]]，安装语法见 [[10-Cursor安装与使用教程]]。本文按**本司技术栈**分模块裁剪：**前端 Vue3 + TS + Vite + Element Plus，后端 Spring Cloud + Java + MyBatis + MySQL + Redis**，并新增**测试**模块。

**本轮数据源 = [skills.sh](https://www.skills.sh/)（官方技能目录，取安装量）+ GitHub API（取 Star）**，双指标交叉：⭐ 看仓库热度与可信度，安装量看实际流行度。**选型原则：同一场景下优先 Star 最高的仓库**，未达 ⭐1K 的一律不列入。核心决策：**团队规范 / 合规 / 项目技术栈 → 项目级进 git；个人效率工具 → 全局**。

> ⭐ 说明：⭐ 为该技能**宿主 GitHub 仓库**的 Star 数（一个仓库常含多个 Skill，是仓库级指标，非单技能独立计数）。「安装量」为 skills.sh 全站累计安装数（标注「仓库合计」的是该仓库全部技能之和）。

### ✅ 逐条校验记录（2026-09-09）

本文列出的**每一条「技能 → 仓库」对应关系，已逐条打到 skills.sh 检索接口核对**（`https://www.skills.sh/api/search?q=`），共 **75 条断言**。

**结论：71 条命中并保留；3 条未被 skills.sh 收录 → 已从本文删除；1 条修正仓库名。**

| 校验结果 | 条目 | 处理 |
|---------|------|------|
| ❌ 未收录 → **已删除** | `clean-code`（piomin/claude-ai-spring-boot） | GitHub 仓库里确实有（`main` 分支嵌套 `skills/` 目录），但 skills.sh 无此技能 ID |
| ❌ 未收录 → **已删除** | `agent-rules-books`（ciembor/agent-rules-books） | skills.sh 查无此技能；它本就不是可安装技能，而是规则原料 |
| ❌ 未收录 → **已删除** | `Cocoon-AI/architecture-diagram-generator` | skills.sh 无此 ID（同名技能在别的仓库），原「排雷」提示一并移除 |
| ⚠️ 仓库名大小写 | `drawio-skill` 归属 `Agents365-ai/...` | skills.sh 规范名为小写 **`agents365-ai/drawio-skill`**，已改正 |
| ✅ 通过 | 其余 71 条 | — |

> 校验同时订正了几处**安装量标错**的地方（上一轮把「仓库合计」误当成了单个技能的安装量）：`webapp-testing` 304k→**152.7k**、mattpocock `code-review` 1.32M→**513.7k**、superpowers 评审 819k→**188k / 223k**。
>
> **不在校验范围内的**（本文保留但不声称来自 skills.sh）：Element Plus / MyBatis 的自建模板、Cursor 内置技能（`/onboard` 等，见 [[19-cursor内置skill]]）、贵司私有治理技能。

### 本轮更新的关键变化

| 变化 | 内容 |
|------|------|
| 🆕 **数据源换了** | 从 GitHub 搜索改为 **skills.sh 官方目录**，能按模块捞到实际在装的技能 + 真实安装量 |
| 🔥 **冒出两个 25 万星级巨头** | **`affaan-m/ecc` ⭐253k**（一个仓库覆盖 Java/SpringBoot/MySQL/Redis/前端/架构/测试）与 **`obra/superpowers` ⭐283k**（TDD + 评审方法论） |
| ✅ **MySQL / Redis 缺口被补上** | 上轮判定「1K 门槛下无公共 Skill」，本轮在 ecc(⭐253k) 里找到 `mysql-patterns`、`redis-patterns` → **不必全自建了** |
| 🆕 **新增「测试」模块** | 独立成节，覆盖 TDD / 单测 / E2E / 前端组件测试 / 后端测试 |
| ❌ **降级/剔除** | `redis/agent-skills` 虽是 Redis 官方，但仅 ⭐142；`planetscale/database-skills` ⭐661；`currents-dev` Playwright ⭐373 —— 均未达 1K，改用 ecc 的同名技能 |

### 第一步：先装「元技能」find-skills

- `find-skills`（vercel-labs/skills ⭐30.6k，**3.3M 安装**，全生态第一）：用自然语言搜并安装其它 Skill 的元技能
- 装好它之后，「想装什么直接说」即可，不必每次手动查市场
- 安装（全局）：`npx skills add vercel-labs/skills --skill find-skills -g`

### 一、前端（Vue3 + TypeScript + Vite + Element Plus）

| 推荐 Skill | ⭐ / 安装量 | 触发关键词 / 调用方式 | 安装（skills.sh 方式） | 层级 |
|-----------|------------|----------------------|------------------------|------|
| `grill-me`（mattpocock/skills） | ⭐256k / 1.09M | "审查 TS 类型安全"、"抓 any 滥用"、"类型审查" | `npx skills add mattpocock/skills --skill grill-me` | 全局 |
| `frontend-patterns`（affaan-m/ecc） | ⭐253k / 13.0k | "前端写法规范"、"组件模式"、"状态与数据流" | `npx skills add affaan-m/ecc --skill frontend-patterns` | 项目级 |
| `ui-to-vue`（affaan-m/ecc） | ⭐253k / 5.1k | "把 UI 设计转成 Vue 组件"、"设计稿落地" | `npx skills add affaan-m/ecc --skill ui-to-vue` | 项目级 |
| `vite-patterns`（affaan-m/ecc） | ⭐253k / 5.2k | "Vite 配置与优化"、"构建/分包"、"插件写法" | `npx skills add affaan-m/ecc --skill vite-patterns` | 项目级 |
| `frontend-design`（anthropics/skills） | ⭐175k / 868k | "UI 审美"、"设计稿实现"、"避免 AI 模板味" | `npx skills add anthropics/skills --skill frontend-design` | 全局 |
| `frontend-ui-engineering`（addyosmani/agent-skills） | ⭐92.9k / 35.1k | "前端工程化"、"UI 实现质量"、"交互与可访问性" | `npx skills add addyosmani/agent-skills --skill frontend-ui-engineering` | 项目级 |
| `design-taste-frontend`（leonxlnx/taste-skill） | ⭐85.3k / 458k | "别生成廉价 UI"、"配色/排版审美"、"前端品味" | `npx skills add leonxlnx/taste-skill --skill design-taste-frontend` | 全局 |
| `frontend-dev-guidelines`（sickn33/agentic-awesome-skills） | ⭐46.1k / 1.4k | "前端开发准则"、"代码组织约定" | `npx skills add sickn33/agentic-awesome-skills --skill frontend-dev-guidelines` | 项目级 |
| `unit-test-vue-pinia`（github/awesome-copilot） | ⭐38.8k / 1.8k | "给 Vue 组件/Pinia 写单测" | `npx skills add github/awesome-copilot --skill unit-test-vue-pinia` | 项目级 |
| `vue-expert` / `typescript-pro`（jeffallan/claude-skills） | ⭐11.4k / 3.9k / 8.3k | "Vue 专家"、"TS 专家" | `npx skills add jeffallan/claude-skills --skill vue-expert` | 项目级 |
| `vue` / `vite` / `pinia` / `vitest`（antfu/skills） | ⭐5.9k / 132k（仓库合计） | "Vue 响应式"、"Vite 配置"、"状态管理"、"写单测" | `npx skills add antfu/skills --skill vue` | 项目级 |
| `vue-best-practices` 系列（vuejs-ai/skills） | ⭐2.8k / 151k（仓库合计） | "Vue3 + TS 最佳实践"、"路由守卫"、"调试 Vue" | `npx skills add vuejs-ai/skills --skill vue-best-practices` | 项目级 |
| `element-plus`（自建，见下文） | — | "用 el- 组件"、"表单校验"、"el-table 分页" | 自建 SKILL.md 放进项目级目录 | **项目级 + 进 git** |

> **怎么选**：TS 类型审查用 `grill-me`（256k）；**日常写 Vue/Vite 首选 `affaan-m/ecc` 三件套（253k）**，星级比 antfu（5.9k）高两个数量级；`antfu/skills` 与 `vuejs-ai/skills` 的价值在于**技能更专更细**（从官方文档生成 / Vue 官方实验项目），作为补充。
> ⚠️ **Element Plus 依然没有任何 ⭐≥1K 的公共 Skill**，仍按文末模板自建。

### 二、后端（Spring Cloud + Java + MyBatis + MySQL + Redis）

#### 后端主栈（Java / Spring）

| 推荐 Skill | ⭐ / 安装量 | 触发关键词 / 调用方式 | 安装（skills.sh 方式） | 层级 |
|-----------|------------|----------------------|------------------------|------|
| `java-coding-standards`（affaan-m/ecc） | ⭐253k / 10.3k | "Java 编码规范"、"命名/异常/并发写法" | `npx skills add affaan-m/ecc --skill java-coding-standards` | **项目级 + 进 git** |
| `springboot-patterns`（affaan-m/ecc） | ⭐253k / 11.2k | "Spring Boot 写法"、"分层/依赖注入"、"配置管理" | `npx skills add affaan-m/ecc --skill springboot-patterns` | 项目级 |
| `springboot-security`（affaan-m/ecc） | ⭐253k / 10.0k | "接口鉴权"、"Spring Security"、"越权/注入" | `npx skills add affaan-m/ecc --skill springboot-security` | **项目级 + 进 git** |
| `springboot-verification`（affaan-m/ecc） | ⭐253k / 8.7k | "验证改动"、"自测与回归确认" | `npx skills add affaan-m/ecc --skill springboot-verification` | 项目级 |
| `backend-patterns`（affaan-m/ecc） | ⭐253k | "后端分层"、"服务边界"、"事务与一致性" | `npx skills add affaan-m/ecc --skill backend-patterns` | 项目级 |
| `java-springboot` / `create-spring-boot-java-project`（github/awesome-copilot） | ⭐38.8k / 19.9k | "建 Spring Boot 项目"、"Spring Boot 脚手架" | `npx skills add github/awesome-copilot --skill java-springboot` | 项目级 |
| `java-architect` / `spring-boot-engineer`（jeffallan/claude-skills） | ⭐11.4k | "微服务架构"、"Spring Cloud 设计"、"写 Controller/Service" | `npx skills add jeffallan/claude-skills --skill java-architect` | 项目级 |
| `spring-boot-engineer` / `java-architect` / `java-code-review` / `api-contract-review` / `design-patterns`（piomin/claude-ai-spring-boot） | ⭐1.3k / 各 1–53 | "REST 契约检查"、"设计模式"、"写 Controller/Service" | `npx skills add piomin/claude-ai-spring-boot --skill spring-boot-engineer` | 项目级 |

> ⚠️ 关于 piomin：它的技能在 skills.sh 上**安装量都只有个位数**（1–53），说明社区基本不从 skills.sh 装它——**直接从 GitHub 装即可**，`npx skills` 是读 GitHub 仓库而非 skills.sh 目录。

#### 数据层（MySQL / Redis）

> **上轮这里判定「无 ⭐≥1K 公共 Skill，只能自建」，本轮在 `affaan-m/ecc`（⭐253k）里找到了现成的，优先级反超自建模板。**

| 推荐 Skill | ⭐ / 安装量 | 触发关键词 / 调用方式 | 安装（skills.sh 方式） | 层级 |
|-----------|------------|----------------------|------------------------|------|
| `mysql-patterns`（affaan-m/ecc） | ⭐253k / 5.1k | "建表规范"、"索引优化"、"慢 SQL"、"事务与锁" | `npx skills add affaan-m/ecc --skill mysql-patterns` | **项目级 + 进 git** |
| `redis-patterns`（affaan-m/ecc） | ⭐253k / 5.1k | "缓存设计"、"穿透/击穿/雪崩"、"键名与过期"、"分布式锁" | `npx skills add affaan-m/ecc --skill redis-patterns` | **项目级 + 进 git** |
| `database-migrations`（affaan-m/ecc） | ⭐253k | "改表结构"、"迁移脚本"、"灰度加字段" | `npx skills add affaan-m/ecc --skill database-migrations` | 项目级 |
| `sql-optimization-patterns`（wshobson/agents） | ⭐39.5k | "SQL 调优"、"执行计划" | `npx skills add wshobson/agents --skill sql-optimization-patterns` | 项目级 |
| `sql-optimization` / `sql-code-review`（github/awesome-copilot） | ⭐38.8k | "SQL 评审"、"索引建议" | `npx skills add github/awesome-copilot --skill sql-optimization` | 项目级 |
| `database-optimizer` / `sql-pro`（jeffallan/claude-skills） | ⭐11.4k | "数据库优化"、"复杂 SQL 写法" | `npx skills add jeffallan/claude-skills --skill database-optimizer` | 项目级 |

> ⚠️ **两个看起来该推但没达标的**：`redis/agent-skills`（**Redis 官方**，含 `redis-core`/`redis-clustering`/`redis-security` 等）只有 **⭐142**；`planetscale/database-skills`（含 `mysql`）**⭐661**。内容可能不错，但按本轮「Star 尽可能高」的口径不列入——**真要 Redis 深度细节，可自行降低门槛装官方那个**。
> **MyBatis 依旧没有任何 ⭐≥1K 的公共 Skill**，按文末模板自建。

### 三、测试（新增模块）

| 推荐 Skill | ⭐ / 安装量 | 触发关键词 / 调用方式 | 安装（skills.sh 方式） | 层级 |
|-----------|------------|----------------------|------------------------|------|
| `test-driven-development`（obra/superpowers） | **⭐283k** / 220.7k | "用 TDD 写"、"先写测试再实现"、"red-green-refactor" | `npx skills add obra/superpowers --skill test-driven-development` | 全局 |
| `tdd`（mattpocock/skills） | ⭐256k / 866k | "TDD"、"先写失败的测试" | `npx skills add mattpocock/skills --skill tdd` | 全局 |
| `e2e-testing`（affaan-m/ecc） | ⭐253k / 9.5k | "端到端测试"、"E2E 用例设计" | `npx skills add affaan-m/ecc --skill e2e-testing` | 项目级 |
| `springboot-tdd`（affaan-m/ecc） | ⭐253k / 9.4k | "SpringBoot 单元测试"、"Mock/切片测试" | `npx skills add affaan-m/ecc --skill springboot-tdd` | 项目级 |
| `webapp-testing`（anthropics/skills） | ⭐175k / 152.7k | "测这个 web 页面"、"浏览器里验证" | `npx skills add anthropics/skills --skill webapp-testing` | 全局 |
| `test-driven-development`（addyosmani/agent-skills） | ⭐92.9k / 32.0k | "TDD 流程"、"测试驱动实现" | `npx skills add addyosmani/agent-skills --skill test-driven-development` | 全局 |
| `browser-testing-with-devtools`（addyosmani/agent-skills） | ⭐92.9k / 29.8k | "用 DevTools 测"、"性能/网络/控制台验证" | `npx skills add addyosmani/agent-skills --skill browser-testing-with-devtools` | 全局 |
| `e2e-testing-patterns`（wshobson/agents） | ⭐39.5k / 22.2k | "E2E 测试模式"、"测试分层" | `npx skills add wshobson/agents --skill e2e-testing-patterns` | 项目级 |
| `javascript-typescript-jest`（github/awesome-copilot） | ⭐38.8k / 12.6k | "Jest/Vitest 单测"、"mock 与快照" | `npx skills add github/awesome-copilot --skill javascript-typescript-jest` | 项目级 |
| `playwright-automation-*`（github/awesome-copilot） | ⭐38.8k / 13.7k | "Playwright 自动化"、"表单填写/录制" | `npx skills add github/awesome-copilot --skill playwright-automation-fill-in-form` | 项目级 |
| `playwright-cli`（microsoft/playwright-cli） | ⭐13.2k / 147k | "跑 Playwright"、"录制并生成测试代码" | `npx skills add microsoft/playwright-cli --skill playwright-cli` | 项目级 |
| `vitest`（antfu/skills） | ⭐5.9k / 35.1k | "Vitest 配置"、"写单测" | `npx skills add antfu/skills --skill vitest` | 项目级 |
| `vue-testing-best-practices`（vuejs-ai/skills） | ⭐2.8k / 11.5k | "组件测试"、"Vitest / Vue Test Utils / Playwright" | `npx skills add vuejs-ai/skills --skill vue-testing-best-practices` | 项目级 |

> **测试模块怎么配**：
> - **方法论**用 `obra/superpowers` 的 `test-driven-development`（⭐283k，本表最高），它是一整套开发方法论而不只是测试技巧。
> - **后端测**用 ecc 的 `springboot-tdd`（⭐253k）；**前端测**用 `vue-testing-best-practices` + `vitest`；**E2E** 用 `e2e-testing`（ecc）或 `webapp-testing`（anthropics，175k）。
> - `obra/superpowers` README 明确列出 **Cursor** 安装支持，可放心用。

### 四、评审

| 推荐 Skill | ⭐ / 安装量 | 触发关键词 / 调用方式 | 安装（skills.sh 方式） | 层级 |
|-----------|------------|----------------------|------------------------|------|
| `receiving-code-review` / `requesting-code-review`（obra/superpowers） | **⭐283k** / 188k · 223k | "怎么接评审意见"、"帮我发评审请求" | `npx skills add obra/superpowers --skill requesting-code-review` | 全局 |
| `code-review` / `review`（mattpocock/skills） | ⭐256k / 513.7k · 94.3k | "做代码评审"、"review my changes" | `npx skills add mattpocock/skills --skill code-review` | 全局 |
| `code-review-skill`（awesome-skills） | ⭐1.9k / 2.0k | "审查这个 Java/Vue/TS PR"（20+ 语言，含 Vue3.5 / TS / Java17+SpringBoot3） | `npx skills add awesome-skills/code-review-skill --skill code-review-skill` | **项目级（团队门禁）** |
| `java-code-review` / `api-contract-review`（piomin） | ⭐1.3k | "审查 Java 代码"、"REST 契约检查" | `npx skills add piomin/claude-ai-spring-boot --skill java-code-review` | 项目级 |

> 通用评审用 superpowers / mattpocock（25 万星量级）；**团队强制门禁仍建议 `code-review-skill`**——它是唯一带**分语言细则**（java.md / vue.md / typescript.md）的，能落成本司的评审清单。

### 五、架构 / 规范

| 推荐 Skill | ⭐ / 安装量 | 触发关键词 / 调用方式 | 安装（skills.sh 方式） | 层级 |
|-----------|------------|----------------------|------------------------|------|
| `improve-codebase-architecture`（mattpocock/skills） | ⭐256k / **894k** | "改进代码库架构"、"模块边界"、"依赖方向" | `npx skills add mattpocock/skills --skill improve-codebase-architecture` | 项目级 |
| `architecture-decision-records`（affaan-m/ecc） | ⭐253k | "写 ADR"、"技术选型留痕" | `npx skills add affaan-m/ecc --skill architecture-decision-records` | **项目级 + 进 git** |
| `archify`（tt-a1i/archify） | ⭐53.7k / 63.8k | "画系统架构图"、"**合 PR 前对比架构改了什么**" | `npx skills add tt-a1i/archify -g` | 全局/项目级 |
| `documentation-and-adrs`（addyosmani/agent-skills） | ⭐92.9k | "补文档与 ADR"、"决策背景与后果" | `npx skills add addyosmani/agent-skills --skill documentation-and-adrs` | 项目级 |
| `architecture-decision-records` / `architecture-patterns`（wshobson/agents） | ⭐39.5k | "ADR 模板"、"架构模式" | `npx skills add wshobson/agents --skill architecture-decision-records` | 项目级 |
| `architecture-blueprint-generator` / `create-architectural-decision-record`（github/awesome-copilot） | ⭐38.8k | "出架构蓝图"、"建 ADR" | `npx skills add github/awesome-copilot --skill architecture-blueprint-generator` | 项目级 |
| `adr-skill`（vercel/ai） | ⭐26.6k | "把决策写成可执行 ADR" | `npx skills add vercel/ai --skill adr-skill` | 项目级 |
| `drawio-skill`（**agents365-ai/drawio-skill**） | ⭐9.1k | ".drawio 架构图"、"**SQL DDL 转 ER 图**"、"C4 下钻"、"架构契约检查" | `npx skills add agents365-ai/drawio-skill --skill drawio-skill` | 项目级 |
| `uml`（markdown-viewer/skills） | ⭐3.3k | "画时序图/类图"、"UML" | `npx skills add markdown-viewer/skills --skill uml` | 全局 |

> - **`improve-codebase-architecture` 是全站安装量最高的架构类技能（889k）**，适合做代码库架构体检。
> - **`drawio-skill` 的 SQL DDL → ER 图**正好补 MyBatis/MySQL 的 ER 出图；**Diagram-as-Test** 可当 CI 架构契约门禁。原生导出需 draw.io CLI ≥30，语义类功能纯 Python 离线可用。
> - ⚠️ **提交规范无达标项**：conventional commits 类最高仅 ⭐58，建议走 **commitlint + husky** 工具链，别硬凑 skill。

### 六、工程效能（Cursor 内置，无需安装）

| 推荐 Skill | 触发关键词 / 调用方式 | 层级 |
|-----------|----------------------|------|
| `onboard` / `new-repo` / `create-skill` / `create-rule` | `/onboard`、`/new-repo`、`/create-skill`、`/create-rule` | `onboard/new-repo` 项目级；`create-skill/rule` 全局 |

> 完整 26 个内置技能清单见 [[19-cursor内置skill]]。

### 七、团队治理（贵司合规，强制项目级）

| 推荐 Skill | 安装 | 层级 |
|-----------|------|------|
| `ai-coding-policy` / `ai-code-review` / `ai-coding-audit` / `cursor-setup` / `code-agent-best-practices`（贵司） | 从贵司私有仓库 / 白名单安装 | **项目级 + 进 git（强制）** |

> 政府/工业/水务强合规，代码不出境是红线。详见 [[12-Skill安全与企业合规]]。

### 安装命令（skills.sh 统一体系）

| 目的 | 命令 |
|------|------|
| 预览仓库内有哪些技能（先看清再装） | `npx skills add owner/repo --list` |
| 装单个技能（**项目级，默认**） | `npx skills add owner/repo --skill skill-name` |
| 装到**全局**（跨项目可用） | `npx skills add owner/repo --skill skill-name -g` |
| 指定装到某个 Agent | `npx skills add owner/repo --skill skill-name -a cursor` |
| 装整个仓库全部技能 | `npx skills add owner/repo --all`（antfu 官方写法 `--skill='*'`） |
| 按关键词搜社区技能 | `npx skills find <关键词>` |
| 查看已装（全局加 `-g`） | `npx skills list` / `npx skills list -g` |
| 更新（单个 / 全部） | `npx skills update <name>` / `npx skills update` |
| 删除 | `npx skills remove <name>` |
| 把自己的流程固化成技能 | `npx skills init my-skill` |

> 项目级默认落到 `.cursor/skills/`（或 `.agents/skills/`），全局落到 `~/.cursor/skills/`（或 `~/.agents/skills/`）。Cursor 会递归扫描并自动加载。

### 全局 vs 项目级：决策框架

| 维度 | 用户级（全局 `-g`） | 项目级（默认，进 git） |
|------|--------------------|----------------------|
| 作用范围 | 你本地所有项目 | 仅本项目，队友 clone 即得 |
| 适合内容 | 个人效率工具、私人偏好 | 团队规范、技术栈、合规要求 |
| 同步到 Cloud / SSH worker | ❌ 不会同步 | ✅ 仓库里就有 |
| 版本 / 审计 | 个人维护，难统一 | 进 git，可评审、可回滚、可审计 |
| 典型例子 | `find-skills`、`grill-me`、`tdd`、`frontend-design`、`archify` | ecc 系列（`java-coding-standards`/`mysql-patterns`/`redis-patterns`）、`code-review-skill`、`element-plus`、`mybatis` |

> **一句话：个人习惯放全局，团队规矩进项目。**
> ⚠️ 关键限制（见 [[09-Cursor中的Skill全景]]）：Cursor **不会**把 `~/.cursor/skills/` 同步到 Cloud Agents、远程 SSH、self-hosted worker。团队规范必须放项目级并进 git。

### 仍需自建的栈专属技能（Element Plus / MyBatis）

这两项**没有任何 ⭐≥1K 的公共 Skill**。MySQL / Redis 本轮已由 ecc（⭐253k）覆盖，下面的模板仅用于**固化团队自己的细则**（如键名前缀、分页规范），作为公共技能的补充而非替代。

```markdown
---
name: mybatis
description: MyBatis / MyBatis-Plus 开发规范。当用户创建 Mapper、编写动态 SQL、定义 ResultMap 或做分页时自动激活。
---
# MyBatis 开发指南
## 核心规则
1. 参数用 @Param 显式命名，XML 中用 #{param} 防歧义
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

1. **治理 / 合规 + 栈专属 + 团队细则 → 一律项目级 + 进 git**
   - 贵司 `ai-coding-*` 系列；ecc 的 `java-coding-standards`、`springboot-security`、`mysql-patterns`、`redis-patterns`、`architecture-decision-records`；`code-review-skill`；自建 `element-plus`、`mybatis`
   - 理由：可审计、可评审、可同步到 worker、队友 clone 即得
2. **个人效率工具 → 全局（`-g`）**
   - `find-skills`、`grill-me`、`tdd`、`frontend-design`、`archify`、`webapp-testing`
3. **安装前先预览**：`npx skills add owner/repo --list`，确认内容再 `--skill` 安装
4. **同源优先**：ecc（⭐253k）一个仓库就覆盖了后端、数据层、前端、架构、测试，**先装它再按缺口补专项**，比零散装一堆小仓库更好维护

### 风险提示

- 从 [[12-Skill安全与企业合规]] 与 [[15-Skill市场与下载渠道]] 已知：**市场 ≠ 可信**（Snyk 审计 3984 个技能，13.4% 含严重问题；学术界扫 42447 个，26.1% 含漏洞）
- **Star 高 ≠ 安全**：⭐ 只解决"活跃度/可信度"，**不替代安全审计**
- 项目级技能**进 git 前必须做代码评审**；带 `scripts/` 的技能出事概率是纯指令型的 **2.12 倍**
- 企业：只从白名单市场下载，建立技能审批流程后再进项目级目录

## 相关

- [[09-Cursor中的Skill全景]]
- [[19-cursor内置skill]]
- [[10-Cursor安装与使用教程]]
- [[11-实战技能包六件套]]
- [[12-Skill安全与企业合规]]
- [[15-Skill市场与下载渠道]]
- [[17-文档Skill]]
- [[18-通用Skill]]
- [[02-Agent-Skills开放标准与生态全景]]

## 来源

- **https://www.skills.sh/** （本轮主数据源：技能目录与安装量；检索接口 `https://www.skills.sh/api/search?q=`）
- https://github.com/obra/superpowers （⭐283k：test-driven-development、requesting-code-review、receiving-code-review；支持 Cursor）
- https://github.com/mattpocock/skills （⭐256k：grill-me、tdd、code-review、improve-codebase-architecture）
- https://github.com/affaan-m/ecc （⭐253k：java-coding-standards、springboot-patterns/security/tdd/verification、backend-patterns、mysql-patterns、redis-patterns、database-migrations、frontend-patterns、ui-to-vue、vite-patterns、e2e-testing、architecture-decision-records）
- https://github.com/anthropics/skills （⭐175k：frontend-design、webapp-testing）
- https://github.com/addyosmani/agent-skills （⭐92.9k：frontend-ui-engineering、test-driven-development、browser-testing-with-devtools、documentation-and-adrs）
- https://github.com/leonxlnx/taste-skill （⭐85.3k：design-taste-frontend）
- https://github.com/tt-a1i/archify （⭐53.7k：架构图 + Before/Delta/After 变更对比）
- https://github.com/sickn33/agentic-awesome-skills （⭐46.1k：frontend-dev-guidelines）
- https://github.com/wshobson/agents （⭐39.5k：architecture-decision-records、e2e-testing-patterns、sql-optimization-patterns）
- https://github.com/github/awesome-copilot （⭐38.8k：java-springboot、unit-test-vue-pinia、javascript-typescript-jest、sql-optimization、architecture-blueprint-generator）
- https://github.com/vercel-labs/skills （⭐30.6k：find-skills）
- https://github.com/vercel/ai （⭐26.6k：adr-skill）
- https://github.com/microsoft/playwright-cli （⭐13.2k：playwright-cli）
- https://github.com/jeffallan/claude-skills （⭐11.4k：java-architect、spring-boot-engineer、vue-expert、database-optimizer）
- https://github.com/agents365-ai/drawio-skill （⭐9.1k：drawio-skill；skills.sh 规范名为小写 `agents365-ai`）
- https://github.com/antfu/skills （⭐5.9k：vue、vite、pinia、vitest）
- https://github.com/vuejs-ai/skills （⭐2.8k：vue-best-practices 系列）
- https://github.com/awesome-skills/code-review-skill （⭐1.9k：code-review-skill）
- https://github.com/piomin/claude-ai-spring-boot （⭐1.3k：spring-boot-engineer、java-code-review、api-contract-review 等）
- https://github.com/markdown-viewer/skills （⭐3.3k：uml）
- 贵司治理技能：`~/.workbuddy/skills/` 下 `ai-coding-*` / `cursor-setup` / `code-agent-best-practices` 系列
