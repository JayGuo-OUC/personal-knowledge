---
title: "24-软件开发Skill：按 skills.sh 安装量排序的通用推荐"
type: entry
created: 2026-09-10
updated: 2026-09-10
tags: [AI, Agent, Skill, 推荐, 安装量, 软件工程师, skills.sh, 代码审查, 测试, 前端, 后端, 架构, 调试, 使用场景]
sources: [https://www.skills.sh/, 16-程序员推荐安装的Skill, 22-Skill现有技术栈, 23-skill主流技术栈]
---

# 24-软件开发Skill：按 skills.sh 安装量排序的通用推荐

## 摘要

本文给「**通用软件工程师**」一份**按 skills.sh 安装量从高到低**的 Skill 推荐清单，并为**每一个 Skill 标注详细使用场景**。与 [[16-程序员推荐安装的Skill]]（按公司技术栈）、[[22-Skill现有技术栈]]、[[23-skill主流技术栈]]（按具体栈选型）不同，本篇**不绑定具体公司技术栈**，只按你提的一个硬指标——**「安装使用人数要多」**——来排序，覆盖代码审查、测试、前端、后端/数据层、架构规范、Git、调试、方法论等通用开发场景。

**全部数据来自 [skills.sh](https://www.skills.sh/) 官方目录**（与 16/22/23 同源，且 16 篇已逐条打到 `https://www.skills.sh/api/search?q=` 接口核对，共 75 条断言）。本篇**不参考任何其它市场**（如 WorkBuddy 内置市场），排序完全由 skills.sh 真实安装数决定。

### 数据口径（必读）

- **安装量**：skills.sh 全站累计安装数（唯一可信的人气指标）。
- **⭐** = GitHub 仓库 Star（`stargazers_count`，**仓库级**指标，一个仓库常含多个 Skill，非单技能独立计数）。
- 门槛：**优先列出安装量 ≥1K** 的 Skill；个别「安装量极高但栈不匹配」的会单列说明为什么不建议你装（见第四节）。
- 同一技术方向只保留**安装量最高**的那个，避免重复安装（取舍：适配度 > 安装量 > star）。
- **「使用场景」列**是本文重点：描述「什么时机触发、你大概率会说什么、它实际帮你做成什么」，便于你直接对号入座。

> 一句话结论：**安装量最高的几类是「元技能 / 代码审查 / 前端审美 / TDD」**，闭眼装不会错；栈专属技能（Java/Spring/Vue/MySQL/Redis）基本由 `affaan-m/ecc`（⭐255k，一个仓库覆盖全栈）包揽，按缺口补即可。

---

## 一、安装量天花板（全站 Top，闭眼装）

这些是全生态安装量最高的开发类 Skill，**任何软件工程师都应该先装这几个**。详细使用场景见下方对应分类小节。

| 排名 | Skill | 仓库 / ⭐ | 安装量 | 一句话定位 | 详细场景 |
|---:|---|---|---:|---|---|
| 1 | `find-skills` | vercel-labs/skills ⭐30.6k | **3.3M** | 搜并安装其它 Skill 的元技能 | 见 §2.7 |
| 2 | `grill-me` | mattpocock/skills ⭐256k | **1.09M** | TS 类型安全审查 | 见 §2.3 |
| 3 | `improve-codebase-architecture` | mattpocock/skills ⭐256k | **894k** | 代码库架构体检 | 见 §2.5 |
| 4 | `frontend-design` | anthropics/skills ⭐175k | **868k** | 生产级前端界面 | 见 §2.3 |
| 5 | `tdd` | mattpocock/skills ⭐256k | **866k** | 测试驱动开发 | 见 §2.2 |
| 6 | `code-review` | mattpocock/skills ⭐256k | **520,310** | 提交前自动找 bug | 见 §2.1 |
| 7 | `design-taste-frontend` | leonxlnx/taste-skill ⭐85.3k | **458k** | 配色/排版审美 | 见 §2.3 |
| 8 | `test-driven-development` | obra/superpowers ⭐283k | **220.7k** | 红绿 TDD 方法论 | 见 §2.2 |
| 9 | `requesting-code-review` | obra/superpowers ⭐283k | **223k** | 怎么发评审请求 | 见 §2.1 |
| 10 | `receiving-code-review` | obra/superpowers ⭐283k | **188k** | 怎么接评审意见 | 见 §2.1 |
| 11 | `webapp-testing` | anthropics/skills ⭐175k | **152.7k** | 浏览器里验证页面 | 见 §2.2 |
| 12 | `playwright-cli` | microsoft/playwright-cli ⭐13.2k | **147k** | 录制并生成测试代码 | 见 §2.2 |

> `find-skills` 3.3M 是生态第一，但它是「装别的 Skill 的 Skill」，本质是工具链入口，单列在最前；真正**写代码/审代码**最高频的是 `grill-me`(1.09M)、`code-review`(520k)、`frontend-design`(868k)、`tdd`(866k)。

---

## 二、分类推荐 + 使用场景详解（每类按安装量降序）

### 2.1 代码审查 / 质量（刚需，安装量普遍最高）

| Skill | 仓库 / ⭐ | 安装量 | 使用场景（详细说明） |
|---|---|---:|---|
| `code-review` | mattpocock/skills ⭐256k | 520,310 | **提交/合 PR 前的最后一关**。你改完一坨代码、准备 push 前，说「帮我 review 一下这次改动」，它会按 critical / warning / nit 三级给出结论：抓空指针、资源未关闭、并发竞态、SQL 注入、N+1 查询、性能退化等真实 bug，而不是空话。适合每次 PR 前跑一遍，是全清单里性价比最高的一个。 |
| `code-review-skill` | awesome-skills ⭐1.9k | 2.0k | **团队强制门禁**。它内置按语言拆分的评审细则（java.md / vue.md / typescript.md / python.md …），能对照你司技术栈逐条检查。场景：你想把评审标准固化成「团队清单」，让每个 PR 都按同一把尺子过，而不是靠 reviewer 个人经验。 |
| `java-code-review` / `api-contract-review` | piomin/claude-ai-spring-boot ⭐1.3k | 个位数（建议从 GitHub 直装） | **Spring 项目专项评审**。当你写完一批 Controller/Service，让它按 Spring 最佳实践 + REST 契约检查：路径命名、状态码、DTO 校验、事务边界、契约与实现是否一致。安装量低但方向精准，适合 Java 后端常驻。 |
| `requesting-code-review` | obra/superpowers ⭐283k | 223k | **你准备开 PR 时**。它教你写好 PR 描述：该 highlight 哪些改动、哪些地方有风险需要 reviewer 重点看、怎么把「为什么这么改」讲清楚，从而拿到更高质量、更快的评审。 |
| `receiving-code-review` | obra/superpowers ⭐283k | 188k | **你收到评审意见时**。它帮你把一堆 comment 分类（哪些是真问题、哪些只是风格偏好），并给出「不防御、可执行」的修改策略：先改哪条、怎么回复、何时该坚持自己的方案。避免评审变成拉锯战。 |

### 2.2 测试 / TDD

| Skill | 仓库 / ⭐ | 安装量 | 使用场景（详细说明） |
|---|---|---:|---|
| `tdd` | mattpocock/skills ⭐256k | 866k | **实现一个新功能/修一个 bug 时**。它强制你先写一条会失败的测试（红），再写最小实现让它变绿，最后重构（绿）。场景：你接到「加个折扣计算逻辑」这种需求，先用它把边界用例写成测试，再动手写业务代码，避免写完才发现漏了负数/溢出的坑。 |
| `test-driven-development` | obra/superpowers ⭐283k | 220.7k | **想建立「测试驱动」的长期工作习惯**。它是一整套方法论（不只是个测试技巧）：怎么把需求拆成可测的规格、怎么保持测试套件快、怎么用子代理并行铺测试。适合个人或小团队做工程纪律升级。 |
| `webapp-testing` | anthropics/skills ⭐175k | 152.7k | **前端页面/Web 应用做完后做真机验证**。它在真实浏览器里把关键路径点一遍：登录→下单→支付，检查渲染、交互、控制台报错、网络失败。场景：你说「帮我验证一下这个页面在浏览器里能正常跑」，它驱动浏览器实际点击并回报问题，而不是只看代码猜。 |
| `playwright-cli` | microsoft/playwright-cli ⭐13.2k | 147k | **想给重复操作写 E2E 测试但懒得手敲选择器**。你让它在浏览器里录一遍人工操作（点按钮、填表单、断言），它自动生成可维护的 Playwright 测试脚本。适合把「每次发版都要手点一遍」的回归流程固化成代码。 |
| `test-driven-development` | addyosmani/agent-skills ⭐92.9k | 32.0k | **需要一个轻量 TDD 流程引导**。与 obra 版相比，它更聚焦「如何把功能拆成红绿步骤、如何写可测单元」，适合不想引入整套 superpowers 方法论、只要 TDD 步骤的人。 |
| `browser-testing-with-devtools` | addyosmani/agent-skills ⭐92.9k | 29.8k | **页面「看起来对但就是不对劲」时**。它用 DevTools 视角帮你查：性能瀑布（是不是有大图/长任务卡住）、网络请求（是不是 404/慢接口）、控制台警告、内存泄漏。场景：用户说「页面有点卡」，你用它做一轮浏览器体检。 |
| `e2e-testing-patterns` | wshobson/agents ⭐39.5k | 22.2k | **你的 E2E 测试越来越慢、越来越脆时**。它给测试分层与稳定性模式：page object、测试数据管理、flaky 重试策略、关键路径 vs 全量覆盖的取舍。适合测试资产已有规模、需要治理的团队。 |
| `javascript-typescript-jest` | github/awesome-copilot ⭐38.8k | 12.6k | **给 JS/TS 业务代码补单测**。它按 Jest/Vitest 规范写单测：mock 依赖、参数化用例、快照测试、覆盖率。场景：你改了个工具函数，让它顺手补上单测和边界 case。 |
| `vitest` | antfu/skills ⭐5.9k | 35.1k | **Vue/Vite 项目配测试环境**。它帮你写 `vitest.config`、选环境（jsdom/node）、接 Vue Test Utils、跑覆盖率。适合从零把测试链路搭起来。 |
| `vue-testing-best-practices` | vuejs-ai/skills ⭐2.8k | 11.5k | **给 Vue 组件/Pinia 写测试**。它给组件渲染测试、事件触发断言、Pinia store 测试、以及用 Playwright 做组件级 E2E 的推荐写法。场景：你新建了一个带状态的复杂组件，让它给一套测试样板。 |
| `springboot-tdd` / `e2e-testing` | affaan-m/ecc ⭐253k | 9.4k / 9.5k | **Java Spring Boot 后端测试**。`springboot-tdd` 用 MockMvc/切片测试验证 Controller 与 Service；`e2e-testing` 设计端到端用例。场景：你写完一个 REST 接口，先用切片测试验证 HTTP 层，再补业务层单测。 |
| `unit-test-vue-pinia` | github/awesome-copilot ⭐38.8k | 1.8k | **给 Vue 组件 + Pinia store 补单元测试**。轻量场景：你只想快速给某个组件挂上测试，不想引入整套测试框架讨论，它给最小可用样板。 |

### 2.3 前端（Vue / TS / 视觉还原）

| Skill | 仓库 / ⭐ | 安装量 | 使用场景（详细说明） |
|---|---|---:|---|
| `frontend-design` | anthropics/skills ⭐175k | 868k | **你要从零做一个界面、或觉得现有界面「很 AI 味」时**。它给生产级的视觉与交互指导：信息层级、留白、配色对比、组件间距、响应式断点，产出不像模板套出来的页面。场景：产品丢来一张草图说「做个后台列表页」，它帮你定下专业不廉价的视觉方案。 |
| `design-taste-frontend` | leonxlnx/taste-skill ⭐85.3k | 458k | **界面做完了但「土」或「乱」时**。它做「审美体检」：配色是否冲突、层级是否清晰、字体与间距是否统一，并给出具体改进点。场景：你自己都被自己生成的 UI 丑到了，让它挑刺并给改法。 |
| `grill-me` | mattpocock/skills ⭐256k | 1.09M | **TS 代码写完、准备合并前做类型安全体检**。它专门抓 TypeScript 的「假安全」：滥用 `any`、不安全的类型断言、漏标返回类型、错误泛型、隐式 any 蔓延。场景：你重构了一大片类型，说「grill 一下这段 TS」，它把类型漏洞逐条列出来。 |
| `vue` / `vite` / `pinia` / `vitest` | antfu/skills ⭐5.9k | 132k（仓库合计） | **用 Vue 生态日常开发**。它是 antfu（Vue 核心成员）出的官方实验性合集：响应式原理、`vite` 配置与优化、`pinia` 状态管理、`vitest` 测试。场景：你卡在某个 Vue 响应式细节或 Vite 构建优化，问它比翻文档快。 |
| `frontend-ui-engineering` | addyosmani/agent-skills ⭐92.9k | 35.1k | **前端工程化与组件架构**。它关注设计系统、组件 API 设计、可访问性（a11y）、响应式策略、性能预算。场景：你要搭一个可复用的组件库，让它定下组件 props/插槽/受控模式的规范。 |
| `vue-best-practices` | vuejs-ai/skills ⭐2.8k | 38.4k | **写/改 Vue3 组件时的即时规范**。覆盖 Composition API、`<script setup>`、响应式误区、Props/Emits 契约、组合式函数抽离。场景：新手接手 Vue 项目，边写边让它把「怎么写才地道」讲清楚。 |
| `typescript-expert` | sickn33/agentic-awesome-skills ⭐46.2k | 12.0k | **遇到 TS 高级写法或类型设计难题时**。它帮你设计类型、泛型约束、类型守卫、工程级 `tsconfig`。场景：你要抽象一个通用的 API 响应包装类型，让它给严谨且不啰嗦的类型定义。 |
| `frontend-dev-guidelines` | sickn33/agentic-awesome-skills ⭐46.1k | 1.4k | **团队想统一前端代码组织约定**。它给目录结构、命名、模块边界、提交前自检清单。场景：新项目立项，先让它产出一份前端开发准则文档，全员对齐。 |
| `ui-to-vue` | affaan-m/ecc ⭐253k | 5.1k | **你拿到 UI 设计稿/截图，要落地成 Vue 组件**。它把视觉稿转成可运行的 Vue3 + TS 代码，并支持 `--ui element-plus` 直接套 Element Plus 组件。场景：设计给了 Figma 导出图，说「把这个登录页转成 Vue 组件」，它产出结构+样式。⚠️ 依赖 DashScope API Key 与网络。 |
| `vite-patterns` | affaan-m/ecc ⭐253k | 5.2k | **Vite 构建慢、分包乱、插件不会写时**。它给 Vite 配置优化、code-splitting、按需加载、自定义插件写法。场景：你的大包首屏 5s，让它做构建层体检与分包改造。 |
| `element-plus-vue3` | partme-ai/full-stack-skills ⭐658 | 1.9k | **用 Element Plus 组件时查正确用法**。覆盖 `el-form` 校验、`el-table` 分页、`el-dialog` 等。场景：你忘了 `el-table` 怎么配分页+插槽，问它给现成写法。⚠️ 仓库 star 偏低，装后先读原文确认质量。 |
| `vuejs-ai` 系列（vue-router / vue-pinia 等细分） | vuejs-ai/skills ⭐2.8k | 151k（仓库合计） | **Vue 路由/状态管理专项**。细分最佳实践：路由守卫、懒加载、Pinia store 组织、持久化。场景：你要做带权限的路由守卫，让它给标准实现。 |

### 2.4 后端 / 数据层（Java / Spring / MySQL / Redis / Kafka）

> 这一整块基本被 **`affaan-m/ecc`（⭐253k，一个仓库覆盖全栈）** 包揽，按缺口补即可，不必零散装一堆小仓库。

| Skill | 仓库 / ⭐ | 安装量 | 使用场景（详细说明） |
|---|---|---:|---|
| `backend-patterns` | affaan-m/ecc ⭐253k | 13.2k | **设计后端方案/做架构评审时**。它给跨语言通用的后端模式：REST 分层、事务边界、缓存策略（cache-aside）、JWT 鉴权、限流、消息队列接入。场景：你要新增一个订单服务，让它先列清分层与一致性方案，避免拍脑袋。 |
| `springboot-patterns` | affaan-m/ecc ⭐253k | 11.2k | **写 Spring Boot 代码时保住「地道写法」**。覆盖分层（Controller/Service/Mapper）、构造器注入、配置管理、异常处理。场景：你写了个 @Autowired 字段注入，它提示改构造器注入并解释为什么。 |
| `java-coding-standards` | affaan-m/ecc ⭐253k | 10.3k | **代码规范落地与评审**。命名、不可变性、Optional 使用、异常处理、DI 方式、项目结构。场景：做 Java 团队规范门禁，让它对照清单挑出不合规范的写法（比通用 clean-code 更贴 Java）。 |
| `springboot-security` | affaan-m/ecc ⭐253k | 10.0k | **写接口鉴权/防攻击时**。覆盖 Spring Security 配置、越权（IDOR）、SQL/命令注入、SSRF。场景：你新开一个管理接口，让它检查有没有越权风险、参数有没有被注入。 |
| `java-springboot` | github/awesome-copilot ⭐38.8k | 19.9k | **快速写接口与分层**。构造器注入、外部化配置、DTO 校验（Bean Validation）、全局异常处理、Controller→Service→Mapper 分层。场景：接到「写个用户查询接口」，它给从 Controller 到返回体的完整范本。 |
| `java-junit` | github/awesome-copilot ⭐38.8k | 11.3k | **给 Java 补 JUnit 5 单测**。参数化/数据驱动测试、Maven/Gradle 标准测试结构（`src/test/java`）。场景：你写完一个工具类，让它生成参数化单测覆盖边界值。 |
| `microservices-patterns` | wshobson/agents ⭐39.5k | 11.8k | **做微服务拆分与治理设计时**。服务拆分边界、服务发现、熔断降级、API 网关、分布式事务/Saga、配置中心。场景：单体要拆微服务，让它给拆法与服务间通信方案。 |
| `mysql-patterns` | affaan-m/ecc ⭐253k | 5.2k | **写 SQL / 设计表结构时**。schema 设计、索引选择、事务与锁、连接池，外加反模式清单（`SELECT *`、深分页、列上函数致索引失效、隐式类型转换）。场景：一条慢 SQL 卡住接口，让它定位索引/写法问题。 |
| `redis-patterns` | affaan-m/ecc ⭐253k | 5.1k | **写缓存逻辑时**。键命名 `resource:id:field`、必须设 TTL、穿透/击穿/雪崩应对、分布式锁、限流、热 key 处理。场景：你准备加缓存，让它定下键名规范与过期策略，顺带排查缓存一致性。 |
| `kafka-development` | mindrally/skills ⭐260 | 1.0k | **用 Kafka 做消息/事件流时**。producer/consumer 模式、分区策略、消费者组、Kafka Streams、Schema Registry、CDC 管道。场景：你要接一个「订单创建后发事件」的链路，让它给生产/消费骨架与分区方案。⚠️ 刚过 1K、仓库 star 偏低，装前先读原文。 |
| `jpa-patterns` | affaan-m/ecc ⭐253k | 9.2k | **项目用 JPA/Hibernate 时**。仓储/实体/关系映射、懒加载陷阱、N+1 规避。场景：你用 MyBatis 则不适用；若某服务改 JPA，再装它。 |
| `spring-boot-engineer` / `java-architect` | jeffallan/claude-skills ⭐11.4k | 7.8k / 5.2k | **面向 Boot 3 + JPA + Security + WebFlux 的企业级工程**。给微服务架构模板（Flyway、JPA 分层、服务网格）。场景：你明确要 Boot 3 新特性实现，可换掉通用的 `java-springboot`。 |
| `sql-optimization-patterns` | wshobson/agents ⭐39.5k | — | **SQL 调优**。执行计划解读、索引命中、改写反模式。场景：一条查询从 200ms 降到 5ms，让它给执行计划层面的优化建议。 |

### 2.5 架构 / 规范 / 文档 / 接口导出

| Skill | 仓库 / ⭐ | 安装量 | 使用场景（详细说明） |
|---|---|---:|---|
| `improve-codebase-architecture` | mattpocock/skills ⭐256k | 894k | **接手一个混乱代码库、或准备大重构前**。它做架构体检：模块边界是否被破坏、有没有循环依赖、分层是否清晰、依赖方向是否失控，并给出优先级排好的修复清单。场景：新项目 onboarding，先跑一遍拿到「这张图哪里烂」的地图。 |
| `archify` | tt-a1i/archify ⭐53.7k | 63.8k | **合 PR 前想看清「这次改动动了哪些架构」**。它画系统架构图，并支持 Before / Delta / After 对比——你改完代码，它能标出相比改之前架构变了哪几处，防止偷偷引入坏依赖。场景：大重构后，用它生成变更对比图贴进 PR 描述。 |
| `api-and-interface-design` | addyosmani/agent-skills ⭐93.2k | 31.7k | **写代码前先定接口契约**。REST 资源设计、请求/响应结构、错误码规范、版本化策略。场景：前后端联调前，先让它出一份接口契约，双方按契约并行开发，减少返工。 |
| `api-documentation-generator` | sickn33/agentic-awesome-skills ⭐46.2k | 2.1k | **需要从代码/需求生成接口文档且不绑定框架时**。通用文档生成器。场景：你有一堆零散接口，想统一产出可读文档，用它兜底（质量高、仓库 ⭐46k）。 |
| `spring-boot-openapi-documentation` | giuseppe-trisciuoglio/developer-kit ⭐343 | 3.1k | **把后端接口「全部导出」成规范文档**。扫描 `@RestController` / `@RequestMapping`，生成 OpenAPI 3 规范 + 可交互文档，供测试与前端联调。场景：你提过「把后端接口全部导出方便测试」，它就是直接命中项。⚠️ 仓库 ⭐343 偏低、installs 含预装灌水，装后先读 SKILL.md 确认基于 springdoc 还是手动解析。 |
| `architecture-decision-records` | affaan-m/ecc ⭐253k | — | **做关键技术选型、需要留痕时**。把「为什么选 A 不选 B」写成 ADR，含背景/决策/后果。场景：团队决定引入 Kafka，让它生成一份 ADR 进 git，未来的人能看懂当初的取舍。 |
| `documentation-and-adrs` | addyosmani/agent-skills ⭐92.9k | — | **补项目文档 + ADR**。除决策记录外，还帮你写决策背景与后果说明。场景：存量项目缺文档，让它系统性补上设计与决策说明。 |
| `drawio-skill` | agents365-ai/drawio-skill ⭐9.1k | — | **把 SQL DDL 直接转成 ER 图、或画 C4 架构图**。支持架构契约检查（Diagram-as-Test，可当 CI 门禁）。场景：你设计了一堆表，让它一键出 ER 图；或用 C4 下钻展示系统分层。原生导出需 draw.io CLI ≥30，语义类功能纯 Python 离线可用。 |
| `unit-test-wiremock-rest-api` | giuseppe-trisciuoglio/developer-kit ⭐343 | 2.9k | **不依赖真实后端地给 REST 接口写测试**。用 WireMock 给接口打桩/模拟响应。场景：你导出接口清单后，用它驱动 Mock 测试——「拿到接口定义 → 用 Mock 把用例跑起来」，与 `java-junit` 配套。⚠️ 同仓库 ⭐343 偏低，装前读原文。 |
| `api-security-testing` | usestrix/strix ⭐61.6k | 4.3k | **接口导出后做一轮安全体检**。按 OWASP Top 10 扫描：越权、注入、敏感数据暴露等。场景：发版前对核心接口跑一轮安全测试，仓库 ⭐61.6k 质量高。⚠️ 偏渗透测试工具型，按需启用。 |

### 2.6 Git / 版本 / 发布

| Skill | 仓库 / ⭐ | 安装量 | 使用场景（详细说明） |
|---|---|---:|---|
| `git-commit` | github/awesome-copilot ⭐38.8k | 44.6k | **你准备提交代码时**。按 Conventional Commits 规范生成提交信息（feat/fix/docs/refactor…）和 PR 描述，让 git 历史可读、能自动生成 changelog。场景：你改了一堆文件，说「帮我写个提交信息」，它按改动内容归并成规范 commit。 |
| `changelog-generator` | （同系列） | — | **发版时**。从 git 提交历史自动汇总成 CHANGELOG，按类型分组（新增/修复/变更）。场景：你要切个版本 tag，让它产出这版的变更清单贴进 release notes。 |
| 提交规范类（≤1K 星级） | — | — | 主流仅 ⭐58，**建议走 commitlint+husky 工具链**而非硬凑 skill——这类 skill 质量与维护度都不如成熟 CLI 工具。 |

### 2.7 方法论 / 元技能（提升整体产出）

| Skill | 仓库 / ⭐ | 安装量 | 使用场景（详细说明） |
|---|---|---:|---|
| `superpowers`（TDD + 评审 + 调试 + 子代理开发） | obra/superpowers ⭐283k | 220k+ | **想系统性升级「怎么用 AI 写代码」的纪律**。它是一整套方法论：先想清楚再写、红绿测试驱动、子代理并行铺实现、怎么请求/接收评审、怎么有条理地调试。场景：你不是缺某个点工具，而是想让整个开发流程更稳更快，装它就对了。 |
| `find-skills`（元技能入口） | vercel-labs/skills ⭐30.6k | 3.3M | **你不知道该装哪个 skill、或想偷懒时**。用自然语言说「我需要个能帮我做数据库迁移的 skill」，它去 skills.sh 搜并直接装最好的那个。场景：以后「想装什么直接说」，不必每次手动查市场。 |

---

## 三、安装命令速查（skills.sh 体系，跨平台可用）

适用场景：你在 **Cursor / Claude Code / Copilot** 等支持 `npx skills` 的环境里按安装量装。

```bash
# 0) 元技能：先装它，之后「想装什么直接说」
npx -y skills add vercel-labs/skills --skill find-skills -g

# 1) 安装量 Top 通用四件套（审查/架构/前端/测试）
npx -y skills add mattpocock/skills --skill code-review --skill improve-codebase-architecture --skill grill-me --skill tdd -g
npx -y skills add anthropics/skills --skill frontend-design -g
npx -y skills add obra/superpowers --skill test-driven-development --skill requesting-code-review --skill receiving-code-review -g

# 2) 后端全栈（一个仓库覆盖 Java/Spring/MySQL/Redis/前端/测试）
npx -y skills add affaan-m/ecc --skill backend-patterns --skill springboot-patterns --skill java-coding-standards --skill mysql-patterns --skill redis-patterns --skill ui-to-vue -y --agent cursor

# 3) 前端补充
npx -y skills add vuejs-ai/skills --skill vue-best-practices --skill vue-testing-best-practices -y --agent cursor
npx -y skills add antfu/skills --skill vue --skill vite --skill vitest -y --agent cursor

# 4) 通用工程（评审/API 设计/Git 提交/微服务）
npx -y skills add github/awesome-copilot --skill java-springboot --skill java-junit --skill git-commit -y --agent cursor
npx -y skills add addyosmani/agent-skills --skill api-and-interface-design --skill frontend-ui-engineering -y --agent cursor
npx -y skills add wshobson/agents --skill microservices-patterns -y --agent cursor
```

> `-g` = 全局（跨项目可用，个人效率工具）；`--agent cursor` = 项目级（进 git，团队共享）。安装后核对目录里应有 `SKILL.md`。

---

## 四、安装量高但仍不建议你装（诚实标注，别被热度带偏）

这些在 skills.sh 上安装量确实高，但**与「通用软件工程师日常开发」不匹配**，列在这里提醒你别无脑装：

| Skill | 安装量 | 为什么不建议 |
|---|---:|---|
| `typescript-advanced-types` | 72,710 | 只讲**类型体操**（条件类型/类型编程），写业务代码用不上 |
| `upstash/skills/upstash-redis-js` | 9,945 | **Node/JS 客户端**，Java 后端用不了 |
| `create-spring-boot-kotlin-project` / `kotlin-springboot` | 8,760 / 9,757 | **Kotlin** 项目专用 |
| `create-spring-boot-java-project` | 9,510 | 只在**新建** Spring Boot 项目时用（Java 21 + Boot 3 骨架）；**别对存量项目执行**，会按新栈覆盖结构 |
| `frontend-patterns` / `frontend-dev-guidelines` / `frontend-ui-engineering` 中的 React 系 | ≥1K | 含 React/Next/MUI/TanStack 教条，会把 agent 导向错误的 Vue API |

---

## 五、安全提醒（装之前必读）

- 市场 ≠ 可信：Snyk 审计 3984 个技能，13.4% 含严重问题；学术界扫 42447 个，26.1% 含漏洞（详见 [[12-Skill安全与企业合规]]）。
- **安装量高 ≠ 安全**：安装数只代表流行度，不替代安全审计。
- 带 `scripts/` 的技能出事概率是纯指令型的 **2.12 倍**；项目级技能进 git 前必须做代码评审。
- 强合规场景（代码不出境是红线）：治理/合规类 Skill 必须走白名单、进项目级并随仓库分发，详见 [[16-程序员推荐安装的Skill]] 与 [[12-Skill安全与企业合规]]。

---

## 相关

- [[16-程序员推荐安装的Skill]]（按公司技术栈定制的推荐 + 全局/项目级决策）
- [[22-Skill现有技术栈]]（受存量版本约束的选型，含版本护栏）
- [[23-skill主流技术栈]]（不受版本约束的主流栈版本）
- [[18-通用Skill]]（7 个不绑定语言栈的通用 Skill）
- [[17-文档Skill]]（四类交付文档 Skill）
- [[12-Skill安全与企业合规]]（装之前必读）
- [[15-Skill市场与下载渠道]]（去哪下载经典 Skill）

## 来源

- **skills.sh 官方目录**（本篇唯一数据源）：https://www.skills.sh/ ，检索接口 `https://www.skills.sh/api/search?q=`（检索于 2026-09-09 / 2026-09-10；16 篇已逐条核对 75 条断言）
- GitHub API `stargazers_count`（star 数据，仓库级指标）
- 交叉复用：[[16-程序员推荐安装的Skill]]、[[22-Skill现有技术栈]]、[[23-skill主流技术栈]] 的 ⭐/安装量数据
