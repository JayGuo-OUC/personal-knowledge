---
title: "25-开发Skill最佳实践：按工作流组织的安装与使用方案"
type: entry
created: 2026-09-10
updated: 2026-09-10
tags: [AI, Agent, Skill, 最佳实践, 工作流, 软件工程师, Cursor, 需求规格, 概要设计, 详细设计, 编码, Git, 接口文档, 接口测试, 功能测试, skills.sh]
sources: [17-文档Skill, 18-通用Skill, 22-Skill现有技术栈, 23-skill主流技术栈, 24-软件开发Skill, 16-程序员推荐安装的Skill]
---

# 25-开发Skill最佳实践：按工作流组织的安装与使用方案

## 摘要

本文不按「热门度」或「语言栈」给你一份平铺清单，而是**按你真实的开发工作流**把 Skill 串成一套可落地的「最佳实践方案」：

> **拿到项目 → 需求规格说明书 → 概要设计 → 详细设计 → 编码 → Git 版本管理 → 导出接口文档 → 测试（接口测试 + 功能测试）**

针对每个阶段，给出**该装哪些 Skill、什么时候触发、怎么用、全局还是项目级安装**。所有 Skill 均来自 **skills.sh**（与 [[17-文档Skill]] [[18-通用Skill]] [[22-Skill现有技术栈]] [[23-skill主流技术栈]] [[24-软件开发Skill]] 同源），适配你的技术栈 **Java / Spring Cloud / MyBatis / MySQL / Redis / Kafka + Vue3 / TypeScript / Element Plus**，AI 辅助工具为 **Cursor**。

> 你的存量项目（如 `HiSCADA7.5-ADP`）是 **JDK 8 + Spring Boot 2.3** 约束版；新项目可按主流版本。凡涉及版本差异处见第六节「版本护栏」。

---

## 一、方案总览：你的工作流 → Skill 地图

| 阶段 | 你要做的事 | 命中 Skill 类别 | 代表 Skill |
|---|---|---|---|
| ① 需求 | 写《需求规格说明书》SRS | 文档 Skill | `create-specification` |
| ② 概要设计 | 写《概要设计说明书》 | 文档 + 架构 Skill | `architecture-blueprint-generator` / `improve-codebase-architecture` / `architecture-patterns` |
| ③ 详细设计 | 写《详细设计说明书》 | 文档 Skill | `create-oo-component-documentation` |
| ④ 编码 | 后端 Java/Spring、前端 Vue3/TS | 栈专属 Skill + 通用质量 Skill | `java-springboot` / `vue-best-practices` / `code-review` / `grill-me` |
| ⑤ Git | 提交、PR、变更记录 | 通用工程 Skill | `git-commit` / `changelog-generator` |
| ⑥ 接口文档 | 把后端接口「全部导出」 | 接口导出 Skill | `spring-boot-openapi-documentation` / `api-and-interface-design` |
| ⑦ 测试 | 接口测试 + 功能测试 | 测试 Skill | `java-junit` + `unit-test-wiremock-rest-api` / `webapp-testing` + `playwright-cli` |

**两条贯穿全程的能力（任何阶段都能用）：**
- **代码评审**：`code-review`（每次 PR 前必跑，性价比最高）
- **调试**：`systematic-debugging`（遇疑难 bug 时强制走复现→定位→根因流程）
- **元技能入口**：`find-skills`（以后想装什么直接说，不必再查市场）

---

## 二、按阶段的最佳实践

### 阶段① 需求规格说明书（SRS）

| Skill | 安装量 | 最佳实践用法 |
|---|---:|---|
| `create-specification` | 13,397 | 拿到项目/需求后第一件事：让 AI 产出目标、范围、功能/非功能需求、验收标准、约束。**先有规格再开发**，避免边写边改需求。 |
| `update-specification` | 9,236 | 需求变更时**增量更新**规格，而不是重写——文档能跟着需求走。 |
| `create-github-issues-for-unmet-specification-requirements` | 8,975 | 把规格里「未满足的需求」自动转成 issue，形成「需求→任务」闭环。 |
| `mermaid-diagrams` | 4,863 | 需求里的流程图、状态图、用例图，直接出 Mermaid 粘进文档。 |

> 触发话术：「帮我写一份 XX 系统的需求规格说明书，按功能/非功能需求、验收标准分章节。」

### 阶段② 概要设计说明书

| Skill | 安装量 | 最佳实践用法 |
|---|---:|---|
| `architecture-blueprint-generator` | 11,964 | 产出系统架构蓝图：分层、模块划分、技术选型、关键组件关系——对应概要设计的「架构总览」章节。 |
| `improve-codebase-architecture` | ~894k | **接手存量项目 / 准备大重构前**先跑一遍：模块边界、循环依赖、分层是否清晰，给出优先级排好的修复清单。 |
| `architecture-patterns` | 21,882 | 选型/设计时给成熟模式参考（分层、事件驱动、CQRS、六边形），用于方案评审与对比。 |
| `architecture-decision-records` | 16,372 | 把「为什么选 Kafka 而不是 RabbitMQ」写成 ADR（背景/决策/后果）。**选型理由单独成文**，后续变更好追溯，直接可引用进设计说明书。 |
| `mermaid-diagrams` | 4,863 | 架构图、时序图、部署图，出 Mermaid 代码贴文档。 |

> 触发话术：「基于这份需求规格，出一份概要设计（架构蓝图 + 模块划分 + 关键选型 ADR）。」

### 阶段③ 详细设计说明书

| Skill | 安装量 | 最佳实践用法 |
|---|---:|---|
| `create-oo-component-documentation` | 7,022 | 给某个模块写详细设计：类的职责、公开接口、依赖关系、协作时序——OO 粒度的模块/类设计章节。 |
| `update-oo-component-documentation` | 6,991 | 代码改了之后**同步更新**详细设计，避免文档三个月就失效。 |

> 触发话术：「给『用户认证模块』写详细设计，包含类图、接口契约、协作时序。」

### 阶段④ 编码

**后端（Java / Spring Cloud / MyBatis / MySQL / Redis / Kafka）**

| Skill | 安装量 | 最佳实践用法 |
|---|---:|---|
| `java-springboot` | 19,987 | 写接口/分层时给最佳实践：构造器注入、外部化配置、DTO 校验、全局异常处理、Controller→Service→Mapper 分层。 |
| `backend-patterns` | 13,165 | 设计方案时给 REST 分层、事务边界、缓存策略（cache-aside）、JWT 鉴权、限流、MQ 接入。 |
| `java-coding-standards` | 10,363 | 编码规范落地与评审：命名、不可变性、Optional、异常处理、DI 方式。 |
| `mysql-patterns` | 5,230 | 写 SQL / Mapper 时：schema、索引、事务、反模式清单（SELECT *、深分页、列上函数致索引失效）。 |
| `redis-patterns` | 5,204 | 写缓存逻辑时：键命名、必须设 TTL、穿透/击穿/雪崩、分布式锁。 |
| `kafka-development` | 1,049 | 写消息生产/消费时：producer/consumer、分区、消费者组、CDC 管道。 |
| `microservices-patterns` | 11,775 | 微服务拆分与治理：服务边界、熔断降级、网关、分布式事务/Saga。 |
| ⚠️ MyBatis | 无公共 skill | **自建**（见第六节 22/23 篇结论）：`${}`/`#{}` 红线、XML 与 dao 同目录、`saveBatch`、N+1 防呆。 |

**前端（Vue3 / TypeScript / Element Plus）**

| Skill | 安装量 | 最佳实践用法 |
|---|---:|---|
| `vue-best-practices` | 38,433 | 写/改 Vue3 组件时：Composition API、`<script setup>`、响应式误区、Props/Emits 契约。 |
| `typescript-expert` | 11,966 | 类型设计、泛型约束、类型守卫、`tsconfig` 工程配置。 |
| `element-plus-vue3` | 1,941 | `el-form` 校验、`el-table` 分页，`el-dialog` 用法（⚠️ 仓库 star 偏低，装后先读原文；不合用则沿用 sjz-front 自建模板）。 |
| `ui-to-vue` | ~5.1k | 拿到 UI 设计稿/截图转成 Vue 组件，支持 `--ui element-plus`。（⚠️ 依赖 DashScope API Key 与网络。） |
| `vue-testing-best-practices` | 11,496 | 项目引入 Vitest 后，给组件 + Pinia store 测试样板。 |

**通用代码质量（前后端都该常驻）**

| Skill | 安装量 | 最佳实践用法 |
|---|---:|---|
| `code-review` | 520,310 | **每次 PR 前必跑**：自动找 bug、安全/性能问题，分级输出。全清单性价比 No.1。 |
| `grill-me` | 1.09M | TS 代码合并前做类型安全体检：抓 `any`、不安全断言、隐式 any。 |
| `frontend-design` | 868k | 从零做界面或现有界面「很 AI 味」时给生产级视觉指导。 |
| `design-taste-frontend` | 458k | 界面「土/乱」时做审美体检并给改法。 |
| `refactor` | 21,635 | 安全地提取方法、消除重复、简化条件，保持行为不变。 |

### 阶段⑤ Git 版本管理

| Skill | 安装量 | 最佳实践用法 |
|---|---:|---|
| `git-commit` | 44,591 | 提交前按 Conventional Commits 生成规范提交信息与 PR 描述，让历史可读、可自动生成 changelog。 |
| `changelog-generator` | — | 发版时从 git 历史汇总成 CHANGELOG。 |
| `systematic-debugging` | 253,410 | 开发中遇疑难 bug，强制走「复现→定位假设→最小化验证→根因→修复」，避免瞎猜。 |

> 提交规范类小 skill（≤1K 星级）建议走 **commitlint + husky** 工具链，比硬凑 skill 更稳（见 [[18-通用Skill]]）。

### 阶段⑥ 导出接口文档

| Skill | 安装量 | 最佳实践用法 |
|---|---:|---|
| `spring-boot-openapi-documentation` | 3,052 | 扫描 `@RestController` / `@RequestMapping`，生成 **OpenAPI 3 + 可交互文档**，把后端接口「全部导出」成 `openapi.json` 供测试与前端联调。（⚠️ 仓库 star 偏低、installs 含预装灌水，装后先读 SKILL.md 确认基于 springdoc 还是手动解析。） |
| `api-and-interface-design` | 31,705 | **写代码前先定接口契约**（REST 资源、请求/响应、错误码、版本化），前后端按契约并行开发、减少返工。与「导出」互补：一个是「先定」，一个是「后导」。 |
| `api-documentation-generator` | 2,146 | 框架无关的通用文档兜底（⭐46,209 质量高），上者不合用时用它。 |

### 阶段⑦ 测试：接口测试 + 功能测试

**接口测试（API / 接口层）**

| Skill | 安装量 | 最佳实践用法 |
|---|---:|---|
| `java-junit` | 11,329 | JUnit 5 单测与参数化测试；Spring 项目用 MockMvc/切片测试验证 Controller 的 HTTP 层。 |
| `unit-test-wiremock-rest-api` | 2,869 | 用 WireMock 给 REST 接口打桩，**不依赖真实后端**地写接口测试。正好接在「导出接口」之后：拿到接口清单 → 用 Mock 把用例跑起来。 |
| `api-security-testing` | 4,337 | 接口导出后做一轮 OWASP 安全扫描（越权、注入、敏感数据暴露）。⚠️ 偏渗透测试工具型，按需启用。 |

**功能测试（页面 / 端到端）**

| Skill | 安装量 | 最佳实践用法 |
|---|---:|---|
| `webapp-testing` | 152,697 | 页面/Web 应用做完后在**真实浏览器**里把关键路径点一遍（登录→下单→支付），检查渲染、交互、控制台报错。 |
| `playwright-cli` | 147k | 录一遍人工操作自动生成 Playwright E2E 脚本，把「每次发版手点回归」固化成代码。 |
| `e2e-testing-patterns` | 22,209 | E2E 测试变慢变脆时给分层与稳定性模式（page object、flaky 重试、关键路径取舍）。 |
| `vitest` / `vue-testing-best-practices` | 35,127 / 11,496 | Vue/Vite 项目的组件与 Pinia store 单元测试。 |
| `tdd` | 866k | 实现新功能/修 bug 时**先写失败测试再写实现**，边界用例提前覆盖。 |

> 一句话落地：**接口测试 = `spring-boot-openapi-documentation`（导出）+ `java-junit`/`unit-test-wiremock-rest-api`（测）+ `api-security-testing`（安全）**；**功能测试 = `webapp-testing` + `playwright-cli` + `vue-testing-best-practices`**。

---

## 三、安装作用域最佳实践（全局 vs 项目级）

按你已确认的约定（见 MEMORY.md）：**与语言/框架无关的能力装全局，绑定语言栈的能力装项目级并进 git**。

| 作用域 | 安装参数 | 包含 Skill | 理由 |
|---|---|---|---|
| **全局** `-g` | 落 `~/.cursor/skills/` | 17 篇文档全套、`find-skills`、`code-review`、`improve-codebase-architecture`、`git-commit`、`refactor`、`systematic-debugging`、`architecture-patterns`、`security-review`、`grill-me`、`frontend-design`、`design-taste-frontend`、`tdd`、`webapp-testing`、`playwright-cli` | 任何项目都受益，装一次即可，不随项目重复。 |
| **项目级** `--agent cursor` | 落 `<项目>/.agents/skills/` 并进 git | 22/23 篇栈专属（`java-springboot`、`mysql-patterns`、`redis-patterns`、`kafka-development`、`vue-best-practices`、`typescript-expert`、`element-plus-vue3`、`ui-to-vue` 等）、接口导出（`spring-boot-openapi-documentation`、`unit-test-wiremock-rest-api`、`api-security-testing`） | 绑定具体栈，避免给不匹配项目加载无关 skill 污染上下文；随仓库分发让团队一致。 |
| **治理/合规强制项目级** | 进 git + 白名单 | 自建 `data-compliance-guard`（代码不出境扫描） | 合规红线（政府/工业/水务），必须随仓库分发，不能只靠全局。 |

> 注意：全局目录是 `~/.cursor/skills/`，**不是** `~/.cursor/skills-cursor/`（那是 Cursor 内置技能，会被同步覆盖）。

---

## 四、一键安装命令（按阶段分组）

在 **项目根目录** 执行。`--agent cursor` 为快模式（只给 Cursor 建软链，秒级完成）；要全平台版换成 `--agent '*'`（单 skill 约 7 分钟）。

```bash
# ── ① 需求/② 概要/③ 详细 文档 Skill（全局）────────────
npx -y skills add github/awesome-copilot \
  --skill create-specification --skill update-specification \
  --skill architecture-blueprint-generator \
  --skill create-oo-component-documentation --skill update-oo-component-documentation \
  --skill documentation-writer --skill create-readme -g
npx -y skills add wshobson/agents --skill architecture-decision-records -g
npx -y skills add softaworks/agent-toolkit --skill mermaid-diagrams -g

# ── ④ 通用代码质量/调试/提交（全局）────────────────────
npx -y skills add mattpocock/skills \
  --skill code-review --skill improve-codebase-architecture --skill grill-me --skill tdd -g
npx -y skills add obra/superpowers --skill systematic-debugging -g
npx -y skills add github/awesome-copilot --skill git-commit --skill refactor -g
npx -y skills add wshobson/agents --skill architecture-patterns -g
npx -y skills add affaan-m/ecc --skill security-review -g
npx -y skills add anthropics/skills --skill frontend-design -g
npx -y skills add leonxlnx/taste-skill --skill design-taste-frontend -g

# ── ④ 后端栈专属（项目级）────────────────────────────
npx -y skills add github/awesome-copilot --skill java-springboot --skill java-junit -y --agent cursor
npx -y skills add affaan-m/ecc \
  --skill backend-patterns --skill java-coding-standards \
  --skill mysql-patterns --skill redis-patterns -y --agent cursor
npx -y skills add wshobson/agents --skill microservices-patterns -y --agent cursor
npx -y skills add mindrally/skills --skill kafka-development -y --agent cursor

# ── ④ 前端栈专属（项目级）────────────────────────────
npx -y skills add vuejs-ai/skills --skill vue-best-practices --skill vue-testing-best-practices -y --agent cursor
npx -y skills add sickn33/agentic-awesome-skills --skill typescript-expert -y --agent cursor
npx -y skills add partme-ai/full-stack-skills --skill element-plus-vue3 -y --agent cursor
npx -y skills add affaan-m/ecc --skill ui-to-vue -y --agent cursor

# ── ⑥ 接口文档导出 + ⑦ 接口/功能测试（项目级）─────────
npx -y skills add giuseppe-trisciuoglio/developer-kit \
  --skill spring-boot-openapi-documentation --skill unit-test-wiremock-rest-api -y --agent cursor
npx -y skills add addyosmani/agent-skills --skill api-and-interface-design -y --agent cursor
npx -y skills add usestrix/strix --skill api-security-testing -y --agent cursor
npx -y skills add microsoft/playwright-cli --skill playwright-cli -y --agent cursor
npx -y skills add anthropics/skills --skill webapp-testing -y --agent cursor

# ── 元技能入口（全局，最后装）────────────────────────
npx -y skills add vercel-labs/skills --skill find-skills -g
```

> 安装后核对：全局在 `~/.cursor/skills/<name>/SKILL.md`；项目级在 `<项目>/.agents/skills/<name>/SKILL.md`。遇 GitHub SSL 握手失败用镜像 `git config --global url."https://ghproxy.net/https://github.com/".insteadOf "https://github.com/"`，**装完记得 `--unset`**。

---

## 五、推荐日常节奏（怎么真正用起来）

1. **立项**：`create-specification` → `architecture-blueprint-generator`（+ ADR）→ `create-oo-component-documentation`，三份文档串成一条线，前一步输出即后一步输入。
2. **编码中**：写接口挂 `java-springboot`，写 Vue 挂 `vue-best-practices`；TS 改完 `grill-me` 体检；界面做丑了 `design-taste-frontend` 挑刺。
3. **提交前**：`code-review` 跑一遍 → `git-commit` 生成规范提交。
4. **联调前**：`spring-boot-openapi-documentation` 导出接口 → 前端按文档对接，测试按文档写 Mock。
5. **提测/发版前**：`java-junit` + `unit-test-wiremock-rest-api` 跑接口测试；`webapp-testing` / `playwright-cli` 跑功能测试；强合规项目加 `api-security-testing` + 自建 `data-compliance-guard` 门禁。
6. **需求/代码变更**：用 `update-specification` / `update-oo-component-documentation` 让文档跟着走，别让文档三个月就失效。

---

## 六、版本护栏（存量 JDK 8 + Spring Boot 2.3 必读）

你的存量项目（如 `HiSCADA7.5-ADP`）是 **JDK 8 + Spring Boot 2.3 + Spring Cloud Hoxton + MyBatis-Plus**，而生态主流 Skill 多面向 **Java 17+ / Boot 3.x**。务必在项目 `.cursorrules` 或 `.agents` 加护栏，否则 agent 会生成 `records` / `sealed` / `jakarta.*` / JPA 切片等不兼容代码：

```
本仓库技术栈：JDK 8 + Spring Boot 2.3 + Spring Cloud Hoxton + MyBatis-Plus。
忽略任何 skill 中关于 Java 17+ / records / sealed / Spring Boot 3 / Jakarta /
JPA / 测试切片(@WebMvcTest) 的建议，生成代码必须兼容 JDK 8 与 javax.* 命名空间。
```

加了护栏后，22/23 篇里后端方向 skill 都能安全使用。**新项目**则可按主流版本直接装，无需护栏。

---

## 七、安全与合规提醒（装之前必读）

- 市场 ≠ 可信：Snyk 审计 3984 个技能，13.4% 含严重问题；学术界扫 42447 个，26.1% 含漏洞。
- **安装量高 ≠ 安全 / ≠ 适合你**：文档类 `warpdotdev/write-tech-spec`(24,793 installs / 仅 ⭐564) 是厂商预装灌水；合规类 `azure-compliance`(569,861) 绑定 Azure 平台——均按适配度排除。
- 带 `scripts/` 的技能出事概率是纯指令型的 **2.12 倍**；项目级技能进 git 前必须做代码评审。
- 强合规红线（代码不出境）：治理/合规类自建 `data-compliance-guard` 必须走白名单、进项目级随仓库分发（详见 [[16-程序员推荐安装的Skill]] [[12-Skill安全与企业合规]]）。

---

## 相关

- [[16-程序员推荐安装的Skill]]（装哪些 + 全局/项目级决策 + 自建六件套）
- [[17-文档Skill]]（需求规格/概要设计/详细设计/用户手册四类文档 Skill，阶段①②③主力）
- [[18-通用Skill]]（架构/评审/调试/重构/提交/安全 7 个通用 Skill，全局常驻）
- [[22-Skill现有技术栈]]（受 JDK8/Boot2.3 约束的栈专属选型 + 版本护栏）
- [[23-skill主流技术栈]]（不受版本约束的栈专属选型）
- [[24-软件开发Skill]]（按 skills.sh 安装量排序的全量推荐 + 详细使用场景）
- [[12-Skill安全与企业合规]]（装之前必读）

## 来源

- 复用本知识库已核对数据：[[17-文档Skill]] [[18-通用Skill]] [[22-Skill现有技术栈]] [[23-skill主流技术栈]] [[24-软件开发Skill]]
- 原始数据源：skills.sh 公开检索接口 `https://www.skills.sh/api/search?q=`（installs，检索于 2026-09-09 / 2026-09-10；16 篇已逐条核对 75 条断言）
- GitHub `stargazers_count`（star，仓库级指标）
