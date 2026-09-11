---
title: "23-skill主流技术栈：不受版本约束的选型清单"
type: entry
created: 2026-09-10
updated: 2026-09-10
tags: [AI, Agent, Skill, 选型, 后端, Java, SpringCloud, SpringBoot, MyBatis, MySQL, Redis, Kafka, 前端, Vue3, TypeScript, ElementPlus, UI还原, skills.sh]
sources: [https://www.skills.sh/, GitHub API stargazers_count, 22-Skill现有技术栈, 21-前端Skill试用, 20-后端Skill试用]

---

# 23-skill主流技术栈：不受版本约束的选型清单

## 摘要
按「公司技术栈」梳理的 skill 清单：**后端 Java / Spring Cloud / MyBatis / MySQL / Redis / Kafka**，**前端 Vue3 + TypeScript + Element Plus**，并覆盖「**从 UI 设计稿实现前端页面**」这条链路。**本次不考虑存量项目与版本约束**（不再受 JDK 8 / Boot 2.3 限制，按当前主流版本选型）。全部取自 **skills.sh**，门槛 **安装量 ≥1K**，**一个技术方向只保留一个**。共 **16 个可安装 skill + 1 个需自建方向（MyBatis）**；另按「接口导出 → 测试」工作流在第十节扩展 3 个 skill（接口文档导出 / 接口 Mock 测试 / 接口安全测试）。

> 与 [[22-Skill现有技术栈]] 的关系：22 篇是**受存量版本约束**（JDK 8 + Boot 2.3）的版本，需要配版本护栏；**本篇不受版本约束**，按主流技术栈直接选最优解。两篇栈相同、结论高度重叠，差异主要在「是否需要考虑向下兼容」与「Element Plus 是否给出可装方案」。

---

## 一、选型原则（本轮四条）

1. **来源唯一**：全部来自 skills.sh 公开检索，取 `installs ≥ 1000`；star 取自 GitHub API `stargazers_count`（仓库级，非单技能计数）。
2. **一个方向一个**：同一技术方向只留一个，取舍顺序 **适配度 > 安装量 > star**。例如 Vue3 有 `vue-best-practices`(38.4k) 与 `antfu/vue`(33.4k)，只留前者，不再叠装 `vue-pinia-best-practices` / `vue-router-best-practices`。
3. **不设版本门槛**：不再排除面向 Java 17+ / Spring Boot 3.x 的 skill（这是与 [[22-Skill现有技术栈]] 最大的不同）。
4. **适配优先于热度**：热度高但栈不匹配的排除。例如 `upstash-redis-js`(9,945) 是 **Node/JS 客户端**；`typescript-advanced-types`(72,710) installs 极高但只讲**类型体操**，日常业务用不上。

---

## 二、后端（Java / Spring Cloud / MyBatis / MySQL / Redis / Kafka）

| # | 方向 | 推荐 skill | 来源仓库 | 安装量 | Star | 用法（触发场景 / 帮你做什么） |
|---:|---|---|---|---:|---:|---|
| 1 | **Spring Boot 核心** | `java-springboot` | `github/awesome-copilot` | **19,987** | ⭐38,819 | 写接口与分层时给最佳实践：构造器注入、外部化配置、DTO 校验、全局异常处理、Controller→Service→Mapper 分层。触发：「写个 XX 接口」「这个 Service 怎么分层」。 |
| 2 | **Spring Cloud / 微服务** | `microservices-patterns` | `wshobson/agents` | **11,775** | ⭐39,535 | 服务拆分边界、服务发现、熔断降级、网关、分布式事务/Saga、配置中心。用于**微服务架构设计与评审**。 |
| 3 | **后端架构模式** | `backend-patterns` | `affaan-m/ecc` | **13,165** | ⭐255,173 | REST 分层、事务边界、缓存策略（cache-aside）、JWT 鉴权、限流、消息队列接入模式。做**后端方案设计**时的第一参考。 |
| 4 | **Java 编码规范** | `java-coding-standards` | `affaan-m/ecc` | **10,363** | ⭐255,173 | 命名、不可变性、Optional、异常处理、DI 方式、项目结构。用于**规范落地与评审**（比通用 clean-code 更贴 Java）。 |
| 5 | **MySQL** | `mysql-patterns` | `affaan-m/ecc` | **5,230** | ⭐255,173 | schema 设计、索引、事务、连接池 + 反模式清单（`SELECT *`、深分页、列上函数致索引失效）。写 SQL / Mapper 时触发。 |
| 6 | **Redis** | `redis-patterns` | `affaan-m/ecc` | **5,204** | ⭐255,173 | 键命名 `resource:id:field`、必须设 TTL、穿透/击穿/雪崩、分布式锁、限流、热 key。写缓存逻辑时触发。 |
| 7 | **Kafka** | `kafka-development` | `mindrally/skills` | **1,049** | ⭐260 | producer/consumer 模式、分区策略、消费者组、Kafka Streams、Schema Registry、CDC 管道。写消息生产/消费时触发。 |
| 8 | **Java 单元测试** | `java-junit` | `github/awesome-copilot` | **11,329** | ⭐38,819 | **JUnit 5** 单测与参数化/数据驱动测试，Maven/Gradle 标准结构（`src/test/java`）。补测试时触发。 |
| 9 | **MyBatis** | ⚠️ **无**（≥1K 检索 0 条） | — | — | — | **建议自建**：`${}` 与 `#{}` 注入红线、XML 与 dao 同目录共生、`saveBatch` 批量、嵌套 collection 改 JOIN 防 N+1、分页插件统一。 |

**两条补充说明**

- **MyBatis 真的没有**：用 `mybatis` / `mybatis plus` / `persistence layer` 多轮检索，**≥1K 结果为 0**（`mybatis plus` 返回的是 `element-plus-vue3`、`web-search-plus` 这类名字误匹配）。ORM 方向唯一过线的是 `affaan-m/ecc/jpa-patterns`(9,190 / ⭐255,173)，但那是 **JPA/Hibernate**，与你用的 MyBatis 不是一回事，**不推荐**。
- **Kafka 偏冷门**：`kafka-development`(1,049) 是唯一过线的 Kafka 专项 skill，刚过门槛、仓库 ⭐260 偏低，但描述已确认覆盖生产/消费、分区、Streams、Schema Registry、CDC，方向正确。若你做的是**事件溯源**，可另看 `wshobson/agents/event-store-design`(9,594 / ⭐39,535)，但它不是 Kafka 使用指南。

---

## 三、前端（Vue3 / TypeScript / Element Plus / UI 还原）

| # | 方向 | 推荐 skill | 来源仓库 | 安装量 | Star | 用法 |
|---:|---|---|---|---:|---:|---|
| 10 | **Vue 3 框架** | `vue-best-practices` | `vuejs-ai/skills` | **38,433** | ⭐2,836 | Vue3 + Composition API + `<script setup>` 组件设计、响应式、Props/Emits、组合式函数。写/改 Vue 组件时触发。 |
| 11 | **TypeScript** | `typescript-expert` | `sickn33/agentic-awesome-skills` | **11,966** | ⭐46,209 | 类型设计、泛型、类型守卫、工程配置。写 TS 业务代码与类型定义时触发。 |
| 12 | **Element Plus** | `element-plus-vue3` | `partme-ai/full-stack-skills` | **1,941** | ⭐658 | 唯一过线的 **Element Plus 专项** skill。用于 `el-form` / `el-table` / `el-dialog` 等组件的正确用法。⚠️ 仓库 star 偏低、本轮未取到 SKILL.md 原文，**装后先读一遍**；不合用就自建（sjz-front 已有模板）。 |
| 13 | **UI 设计稿还原** | `ui-to-vue` | `affaan-m/ecc` | **5,126** | ⭐255,173 | **把 UI 给的设计稿/截图转成 Vue 组件**，支持 Element Plus（`--ui element-plus`）。这是「从 UI 实现页面」链路的主力。⚠️ 依赖 DashScope API Key 与网络。 |
| 14 | **前端测试** | `vue-testing-best-practices` | `vuejs-ai/skills` | **11,496** | ⭐2,836 | 组件测试、Pinia store 测试、E2E 策略。项目引入 Vitest 后启用。 |

> **UI 还原备选**：如果 UI 用 **Figma**，可改选 `figma/mcp-server-guide/implement-design`（6,003 / ⭐1,969，Figma 官方出品，installs 更高）；本轮未读到其原文，故主推已验证可用的 `ui-to-vue`。

---

## 四、工程通用（前后端都受益）

| # | 方向 | 推荐 skill | 来源仓库 | 安装量 | Star | 用法 |
|---:|---|---|---|---:|---:|---|
| 15 | **代码评审** | `code-review` | `mattpocock/skills` | **520,310** | ⭐257,863 | 全库安装量第一。提交前自动找 bug、安全与性能问题，输出分级结论。PR 前跑一遍——**本清单性价比最高的一个**。 |
| 16 | **API 设计** | `api-and-interface-design` | `addyosmani/agent-skills` | **31,705** | ⭐93,221 | REST 接口契约设计、请求/响应结构、错误码、版本化。设计新接口时触发（联调前先定契约）。 |
| 17 | **Git 提交规范** | `git-commit` | `github/awesome-copilot` | **44,591** | ⭐38,819 | Conventional Commits 规范提交信息与 PR 描述（同类 `conventional-commit` 16,183 属同方向，不重复装）。 |

---

## 五、安装命令（按仓库合并，减少克隆次数）

在项目根目录执行。`--agent cursor` 为**快模式**（只给 Cursor 建软链，秒级完成）；若要全平台版换成 `--agent '*'`（**注意：全平台版单 skill 约 7 分钟**，16 个会很久）。

```bash
# 后端：Spring Boot / JUnit / Git 提交
npx -y skills add github/awesome-copilot --skill java-springboot --skill java-junit --skill git-commit -y --agent cursor

# 后端：架构模式 / Java 规范 / MySQL / Redis / UI 还原
npx -y skills add affaan-m/ecc --skill backend-patterns --skill java-coding-standards --skill mysql-patterns --skill redis-patterns --skill ui-to-vue -y --agent cursor

# 前端：Vue3 / 前端测试 / Element Plus
npx -y skills add vuejs-ai/skills --skill vue-best-practices --skill vue-testing-best-practices -y --agent cursor
npx -y skills add partme-ai/full-stack-skills --skill element-plus-vue3 -y --agent cursor

# 微服务 / TypeScript / Kafka / 代码评审 / API 设计
npx -y skills add wshobson/agents --skill microservices-patterns -y --agent cursor
npx -y skills add sickn33/agentic-awesome-skills --skill typescript-expert -y --agent cursor
npx -y skills add mindrally/skills --skill kafka-development -y --agent cursor
npx -y skills add mattpocock/skills --skill code-review -y --agent cursor
npx -y skills add addyosmani/agent-skills --skill api-and-interface-design -y --agent cursor

# 第十节：接口导出与测试工程化（按工作流扩展）
# Spring Boot 接口文档导出 + WireMock 接口 Mock 测试（同仓库，一次克隆）
npx -y skills add giuseppe-trisciuoglio/developer-kit --skill spring-boot-openapi-documentation --skill unit-test-wiremock-rest-api -y --agent cursor
# 接口安全测试（OWASP）
npx -y skills add usestrix/strix --skill api-security-testing -y --agent cursor
# 通用接口文档导出（sickn33 仓库，与 #11 typescript-expert 同仓，可合并克隆）
npx -y skills add sickn33/agentic-awesome-skills --skill api-documentation-generator -y --agent cursor
```

> 安装后核对：`.agents/skills/` 下每个目录应有 `SKILL.md`。如遇 GitHub SSL 握手失败，用镜像 `git config --global url."https://ghproxy.net/https://github.com/".insteadOf "https://github.com/"`，**装完记得 `--unset`**。

---

## 六、与 22 篇的差异（为什么两篇都要留）

| 维度 | [[22-Skill现有技术栈]] | 本篇（23） |
|---|---|---|
| 版本约束 | **受约束**（存量 JDK 8 + Boot 2.3） | **不受约束**，按主流版本选 |
| 版本护栏 | 必需（否则 agent 会生成 records / Jakarta / JPA 等不兼容代码） | 不需要 |
| Element Plus | 建议自建（当时判定无可用方案） | 给出 `element-plus-vue3`(1,941) 可装方案 + 自建备选 |
| 其余选型 | 与本篇一致 | 与 22 篇一致 |

---

## 七、自建建议（唯一缺口：MyBatis）

| 方向 | 自建要点 |
|---|---|
| **MyBatis** | 值位置一律 `#{}`（`${}` 仅用于动态表名/排序等**标识符**）、XML 与 dao 同目录共生、`saveBatch` 批量写入、嵌套 `<collection select>` 改 JOIN 防 N+1、统一分页插件 |

参考：sjz-front 的 `.agents/skills/element-plus/` 是自建模板的现成范例，照此格式写一份 MyBatis 版即可。

---

## 八、验证状态说明（诚实标注）

| 状态 | 涉及 skill |
|---|---|
| ✅ **已读 SKILL.md 原文确认** | `java-junit`（JUnit 5 最佳实践）、`kafka-development`（Kafka 事件流/Streams/CDC）、`ui-to-vue`、`vue-best-practices`、`vue-testing-best-practices`、`mysql-patterns`、`redis-patterns`、`backend-patterns`、`java-coding-standards`、`java-springboot`（以上后 7 项经 [[20-后端Skill试用]] / [[21-前端Skill试用]] 实测验证） |
| ⚠️ **未取到原文，仅依据 installs / star / 名称与方向判断** | `microservices-patterns`（wshobson 仓库 `plugins/` 下未定位到路径）、`typescript-expert`、`element-plus-vue3`、`code-review`、`api-and-interface-design`、`git-commit`；**第十节**：`spring-boot-openapi-documentation`、`unit-test-wiremock-rest-api`（developer-kit ⭐343，未读原文）、`api-security-testing`（strix，未读原文）、`api-documentation-generator` |

未验证的 6 个均为高安装量主流 skill，风险低，但**建议安装后先扫一眼 SKILL.md** 再决定是否常驻。

---

## 九、曾被版本约束排除、现已解禁的 skill

> 本篇**不受版本约束**，所以在 [[22-Skill现有技术栈]]（受 JDK 8 / Boot 2.3 约束的姐妹篇）里因「面向 Java 17+ / Spring Boot 3.x、与存量栈不匹配」而被排除的下述 skill，**在这里是可以装的**。按与主表的关系分两类：**替换选项**（同方向，二选一）与**场景限定**（特定场景才用）。

### 9.1 替换选项（与主表二选一，切勿重复装）

| 方向 | 被解禁的 skill | 来源仓库 | 安装量 | Star | 与主表的关系 / 用法 |
|---|---|---|---:|---:|---|
| Spring Boot | `java-spring-boot` | `pluginagentmarketplace/custom-plugin-java` | **11,705** | ⭐**40** | 与主表 `java-springboot`(19,987) **同方向**。`spring_version` 默认 **3.2**，内容更贴 Boot 3 新特性；但仓库仅 ⭐40、社区验证极少，**仅当你明确要 Boot 3 细节时才替换**。 |
| Spring Boot | `spring-boot-engineer` | `jeffallan/claude-skills` | **7,781** | ⭐11,389 | 侧重 **Boot 3 + JPA + Security + WebFlux** 工程实践。若项目确实用 JPA（而非 MyBatis），它比 `java-springboot` 更贴；否则仍用主表的 `java-springboot`。 |
| 架构设计 | `java-architect` | `jeffallan/claude-skills` | **5,219** | ⭐11,389 | 与主表 `microservices-patterns`(11,775) **同属架构方向**。它给的是 **Java 21 / Boot 3 企业级微服务架构模板**（含 Flyway、JPA 分层）。要 Boot 3 架构模板就换它；要框架无关的治理模式就留 `microservices-patterns`。 |
| 架构设计 | `microservices-architect` | `jeffallan/claude-skills` | **4,259** | ⭐11,389 | 与 23 主表 `microservices-patterns`(11,775) **同方向**。给 **Java 21 / Boot 3 企业级微服务架构模板**（服务拆分、服务网格、可观测性）。要 Boot 3 架构细节就换它；要框架无关治理模式就留主表。 |
| Java 编码 | `mindrally/java` | `mindrally` 仓库 | 安装量未单独核实（见 [[22-Skill现有技术栈]] 实测） | — | 与 23 主表 `java-coding-standards`(10,363) **同方向**。**写 Java 17+**（records / sealed / 模式匹配 / text blocks）。本篇不受版本约束，可作「现代 Java 编码」替换项；但 skills.sh 当前同名量低、未取到原文，**装前先读 SKILL.md**。 |

> **补充来源说明**（本次补全检索 skills.sh，数据截至 2026-09-10）：
> - `microservices-architect`、`spring-boot-engineer`、`java-architect` 同属 `jeffallan/claude-skills`（⭐11,389），均面向 **Java 21 / Boot 3**，是 22 篇「版本约束」下被排除的企业级模板系列；本篇解禁后作为对应方向的替换项。
> - `java-architect` 另有同名 `piomin/claude-ai-spring-boot/java-architect`（仅 1 安装），**以 jeffallan 版（5,219）为准**。
> - `mindrally/java`（写 Java 17+）来源为 [[22-Skill现有技术栈]] 实测记录；skills.sh 当前未收录其独立安装量（同名仅 `mindrally/skills/spring-boot` 769），故标注「未核实」，装前先读原文。
> - 同系列 `java-microservices`(`pluginagentmarketplace/custom-plugin-java`) 仅 484 安装，**未过 1K 门槛，不列入主清单**；如需 Boot 3 微服务脚手架可临时取用。

### 9.2 场景限定（不是日常开发 skill，按需临时用）

| skill | 来源仓库 | 安装量 | Star | 什么时候用 |
|---|---|---:|---:|---|
| `create-spring-boot-java-project` | `github/awesome-copilot` | **9,510** | ⭐38,819 | **只在新建 Spring Boot 项目时**用：按 Java 21 + Boot 3 生成骨架（含 docker-compose / springdoc / ArchUnit）。⚠️ **别对存量项目执行**，会按新栈覆盖项目结构与约定——这正是它在 22 篇被排除的唯一原因。 |
| `jpa-patterns` | `affaan-m/ecc` | **9,190** | ⭐255,173 | 仅当项目**引入 JPA / Hibernate** 时才需要（仓储/实体/关系映射/懒加载陷阱）。当前用 MyBatis 则**不适用**；将来某服务改用 JPA 再装。 |

### 9.3 仍然排除的（与版本无关，别一并装上）

这几项**在任何一篇里都不建议装**，原因不是版本，别因为"解禁"就一起装：

| skill | 安装量 | 排除原因（与版本无关） |
|---|---:|---|
| `upstash/skills/upstash-redis-js` | 9,945 | **Node/JS 客户端**，Java 后端用不了 |
| `typescript-advanced-types` | 72,710 | 只讲**类型体操**（条件类型/类型编程），写业务代码用不上 |
| `create-spring-boot-kotlin-project` / `kotlin-springboot` | 8,760 / 9,757 | **Kotlin** 项目专用 |
| `frontend-patterns` / `frontend-dev-guidelines` / `frontend-ui-engineering` | ≥1K | **React / Next / MUI / TanStack** 教条，会把 agent 导向错误的 Vue API |

> 一句话：**解禁的是"版本门槛"，不是"方向匹配"**——同方向仍只装一个，栈不匹配的照旧排除。

---

## 十、接口导出与测试工程化（按你的工作流扩展）

> 你提出「把项目后端的接口全部导出方便测试 / 接口文档导出」，并让我顺着工作流扩展。这条链路在主表是**缺口**：主表只有 `api-and-interface-design`（写代码前的契约设计）和 `java-junit`（单测），缺「**从已有 Controller 导出 OpenAPI**」和「**用 Mock 把接口跑起来测**」。本节补齐，均取自 skills.sh、门槛 installs≥1K，**一个方向只留一个**。

### 10.1 接口文档导出（从代码生成 OpenAPI / Swagger）

这是对你需求最直接的命中——把后端 `@RestController` 的接口"全部导出"成规范文档。

| 方向 | 推荐 skill | 来源仓库 | 安装量 | Star | 用法（对你工作流的价值） |
|---|---|---|---:|---:|---|
| 接口文档导出（Spring Boot 原生） | `spring-boot-openapi-documentation` | `giuseppe-trisciuoglio/developer-kit` | **3,052** | ⭐**343** | 扫描 `@RestController` / `@RequestMapping`，生成 **OpenAPI 3 规范 + 可交互文档**，把后端接口"全部导出"成 `openapi.json`，供测试与前端联调。⚠️ 仓库 ⭐343 偏低、installs 含 skills.sh 预装灌水，**装后先读 SKILL.md** 确认它基于 springdoc-openapi 还是手动解析。 |
| 接口文档导出（框架无关通用） | `api-documentation-generator` | `sickn33/agentic-awesome-skills` | **2,146** | ⭐46,209 | 通用文档生成器，不绑定 Spring。若上者不合用，用它兜底（仓库 ⭐46,209、质量高）。 |

> 与主表 `api-and-interface-design`(31,705) 的区别：**那里是"写代码前先定契约"**，**这里是"代码写完了把接口导出来"**——互补，非重复。

### 10.2 接口测试 / Mock（把导出的接口跑起来测）

| 方向 | 推荐 skill | 来源仓库 | 安装量 | Star | 用法 |
|---|---|---|---:|---:|---|
| 接口测试 + Mock（WireMock） | `unit-test-wiremock-rest-api` | `giuseppe-trisciuoglio/developer-kit` | **2,869** | ⭐**343** | 用 **WireMock** 给 REST 接口打桩/模拟响应，写**不依赖真实后端的接口测试**。正好接在"导出接口"之后：拿到接口清单 → 用 Mock 驱动测试。与主表 `java-junit`(11,329) 配套（它给 JUnit 框架，本 skill 给 Mock 能力）。⚠️ 同仓库 ⭐343 偏低，装前读原文。 |

### 10.3 接口安全测试（可选扩展）

| 方向 | 推荐 skill | 来源仓库 | 安装量 | Star | 用法 |
|---|---|---|---:|---:|---|
| 接口安全测试（OWASP） | `api-security-testing` | `usestrix/strix` | **4,337** | ⭐61,562 | 把导出的接口做**安全扫描**（OWASP Top 10：越权、注入、敏感数据暴露等）。仓库 ⭐61,562、质量高。适合在"导出门"后做一轮安全体检。⚠️ 它是**渗透测试工具型** skill，偏向安全而非功能测试，按需启用。 |

### 10.4 没过 1K 门槛、但你可能会想要的（诚实标注，不列入主清单）

| 方向 | skill | 安装量 | 说明 |
|---|---|---:|---|
| 接口功能自动化测试 | `api-testing`（`petrkindlmann/qa-skills`） | 745 | 功能级接口测试，差一点过线；仓库 ⭐117 低，质量一般。 |
| 接口用例测试（Postman 风格） | `casely`（`johnwayneeee/casely-qa-skill`） | 893 | 用例式 API 测试，未过 1K。 |
| 契约测试（Pact） | `api-contract-testing`（`aj-geddes/useful-ai-prompts`） | 888 | 热度最高的契约测试 skill，仍未过 1K；`pactflow` 仅 98。 |
| 参数化单测 | `unit-test-parameterized`（`giuseppe-trisciuoglio/developer-kit`） | 2,845 | **已覆盖**：主表 `java-junit`(11,329) 本就含参数化/数据驱动测试，无需重复装。 |

> 一句话落地：接口导出用 `spring-boot-openapi-documentation`、接口 Mock 测试用 `unit-test-wiremock-rest-api`、安全体检用 `api-security-testing`；**功能级接口自动化测试目前 skills.sh 没有过 1K 的成熟方案**，先用 WireMock + JUnit 组合顶上。

---

## 相关
- [[22-Skill现有技术栈]]（受存量版本约束的姐妹篇，选型几乎相同，配了版本护栏）
- [[16-程序员推荐安装的Skill]]（更早的通用推荐，本篇在其基础上按栈去重）
- [[21-前端Skill试用]]（前端 20 个 skill 在 sjz-front 的实测：PASS 6 / WARN 9 / FAIL 5）
- [[20-后端Skill试用]]（后端 26 个 skill 在 sjz-back 的实测结果）

## 来源
- skills.sh 公开检索接口：`https://www.skills.sh/api/search?q=...`（installs 数据，检索于 2026-09-10）
- GitHub API `stargazers_count`（star 数据，检索于 2026-09-10）
- 实测交叉验证：[[20-后端Skill试用]]、[[21-前端Skill试用]]、`E:/guojian/01project/sjz/sjz-front/.agents/skills/`
