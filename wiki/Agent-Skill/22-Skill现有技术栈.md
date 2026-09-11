---
title: "22-Skill现有技术栈：按公司技术栈重新梳理的选型清单"
type: entry
created: 2026-09-10
updated: 2026-09-10
tags: [AI, Agent, Skill, 选型, 后端, Java, SpringCloud, MyBatis, MySQL, Redis, Kafka, 前端, Vue3, TypeScript, ElementPlus, skills.sh]
sources: [https://www.skills.sh/, GitHub API stargazers_count, 20-后端Skill试用, 21-前端Skill试用, 16-程序员推荐安装的Skill]

---

# 22-Skill现有技术栈：按公司技术栈重新梳理的选型清单

## 摘要
按「公司实际技术栈」重新做的一轮选型：后端 **Java / Spring Cloud / MyBatis / MySQL / Redis / Kafka**，前端 **Vue3 + TypeScript + Element Plus**，并额外覆盖「从 UI 设计稿实现前端页面」这条链路。全部取自 **skills.sh**，门槛 **安装量 ≥1K**，**一个技术方向只保留一个**（杜绝同方向重复安装）。共 **17 个可安装 skill + 2 个需自建方向**（MyBatis、Element Plus）。

> 与 [[16-程序员推荐安装的Skill]] 的区别：16 篇是「⭐≥1K 的仓库维度」通用推荐；**本篇是「安装量≥1K 的单技能维度」，且严格按你的栈做了去重**——同一方向只留最优那一个。实测依据见 [[20-后端Skill试用]]（后端 26 个）与 [[21-前端Skill试用]]（前端 20 个）。

---

## 一、选型原则（本轮四条）

1. **来源唯一**：全部来自 skills.sh 公开检索接口，取 `installs ≥ 1000`；star 数取自 GitHub API `stargazers_count`（仓库级，非单技能计数）。
2. **一个方向一个**：同一技术方向只留一个，取舍顺序为 **适配度 > 安装量 > star**。例如 Vue3 方向有 `vue-best-practices`(38.4k) 与 `antfu/vue`(33.4k)，只留前者，不再叠装 `vue-pinia-best-practices` / `vue-router-best-practices`。
3. **适配优先于热度**：热度高但栈不匹配的直接排除。例如 `upstash-redis-js`(9,945) 是 **Node/JS 客户端**，Java 后端不用；`create-spring-boot-java-project`(9,509) 是 **Java 21 + Boot 3 脚手架**，会毁掉存量项目。
4. **无公共 skill 的方向不硬凑**：MyBatis、Element Plus 在 ≥1K 门槛下**确实没有优质公共 skill**，按 16 篇的先例**自建**，不外求。

---

## 二、后端（Java / Spring Cloud / MyBatis / MySQL / Redis / Kafka）

| # | 方向 | 推荐 skill | 来源仓库 | 安装量 | Star | 用法（什么时候触发、帮你做什么） |
|---:|---|---|---|---:|---:|---|
| 1 | **Spring Boot 核心** | `java-springboot` | `github/awesome-copilot` | **19,987** | ⭐38,819 | 写接口/分层时给最佳实践：构造器注入、外部化配置、DTO 校验、全局异常处理、Controller→Service→Mapper 分层。触发词「写个 XX 接口」「这个 Service 怎么分层」。 |
| 2 | **微服务 / Spring Cloud** | `microservices-patterns` | `wshobson/agents` | **11,775** | ⭐39,535 | 服务拆分边界、服务发现、熔断降级、网关、分布式事务/Saga、配置中心。用于**微服务架构设计与评审**，补 Spring Cloud 治理层的方法论。 |
| 3 | **后端通用架构模式** | `backend-patterns` | `affaan-m/ecc` | **13,165** | ⭐255,173 | REST 分层、事务边界、缓存策略（cache-aside）、JWT 鉴权、限流、消息队列接入模式。跨语言通用，做**后端方案设计**时的第一参考。 |
| 4 | **Java 编码规范** | `java-coding-standards` | `affaan-m/ecc` | **10,363** | ⭐255,173 | 命名、不可变性、Optional、异常处理、DI 方式、项目结构。用于**代码规范落地与评审**（比通用 clean-code 更贴 Java）。 |
| 5 | **MySQL** | `mysql-patterns` | `affaan-m/ecc` | **5,230** | ⭐255,173 | schema 设计、索引、事务、连接池 + 反模式清单（`SELECT *`、深分页、列上函数致索引失效）。写 SQL / Mapper 时触发。 |
| 6 | **Redis** | `redis-patterns` | `affaan-m/ecc` | **5,204** | ⭐255,173 | 键命名 `resource:id:field`、必须设 TTL、穿透/击穿/雪崩、分布式锁、限流、热 key。写缓存逻辑时触发。 |
| 7 | **Kafka** | `kafka-development` | `mindrally/skills` | **1,049** | ⭐260 | producer/consumer 模式、分区策略、消费者组、Kafka Streams、Schema Registry、CDC 管道。写消息生产/消费时触发。 |
| 8 | **Java 单元测试** | `java-junit` | `github/awesome-copilot` | **11,329** | ⭐38,819 | **JUnit 5** 单测与参数化/数据驱动测试，Maven/Gradle 标准测试结构（`src/test/java`）。补测试时触发。 |
| 9 | **MyBatis** | ⚠️ **无**（≥1K 无收录） | — | — | — | **建议自建**：`${}` 与 `#{}` 注入红线、XML 与 dao 同目录共生、批量写入、N+1 排查、分页插件。16 篇已有自建模板可复用。 |

> **Kafka 说明**：`kafka-development`(1,049) 是唯一过 1K 的 Kafka skill，刚过线、仓库 star 仅 260（偏低）。它的描述已确认覆盖生产/消费、分区、Streams、Schema Registry、CDC，方向正确；但**建议安装后先读一遍 SKILL.md 再决定是否常驻**。
> **MyBatis 说明**：本轮用 `mybatis` 关键词检索，**返回 0 条 ≥1K 结果**，与 16 篇结论一致（1K 门槛下 MyBatis 无公共 skill），只能自建。

---

## 三、前端（Vue3 / TypeScript / Element Plus / UI 还原）

| # | 方向 | 推荐 skill | 来源仓库 | 安装量 | Star | 用法 |
|---:|---|---|---|---:|---:|---|
| 10 | **Vue 3 框架** | `vue-best-practices` | `vuejs-ai/skills` | **38,433** | ⭐2,836 | Vue3 + Composition API + `<script setup>` 组件设计、响应式、Props/Emits、组合式函数。写/改 Vue 组件时触发。 |
| 11 | **TypeScript** | `typescript-expert` | `sickn33/agentic-awesome-skills` | **11,966** | ⭐46,209 | 类型设计、泛型、类型守卫、工程配置。写 TS 业务代码与类型定义时触发（`typescript-advanced-types`  installs 72,710 更高，但只讲**高级类型/类型体操**，日常业务用不上，故排除）。 |
| 12 | **UI 设计稿还原** | `ui-to-vue` | `affaan-m/ecc` | **5,121** | ⭐255,173 | **把你从 UI 拿到的设计稿/截图转成 Vue 组件**，支持 Element Plus（`--ui element-plus`）。这是「从 UI 实现前端页面」这条链路的主力。⚠️ 依赖 DashScope API Key 与网络。 |
| 13 | **前端测试** | `vue-testing-best-practices` | `vuejs-ai/skills` | **11,496** | ⭐2,836 | 组件测试、Pinia store 测试、E2E 策略。项目引入 Vitest 后启用（未装测试链时先不装）。 |
| 14 | **Element Plus** | ⚠️ **无优质公共 skill** | — | — | — | **建议自建**：`el-form` 校验、`el-table` 分页、`el-dialog` 用法、图标按需引入、SCSS 主题覆盖。**sjz-front 已有自建模板可直接复制**。 |

> **UI 还原备选**：若 UI 用的是 **Figma**，可改选 `figma/mcp-server-guide` 的 `implement-design`（6,003 / ⭐1,969，Figma 官方出品）；本轮未读到其 SKILL.md 原文，故主推已验证的 `ui-to-vue`。
> **Element Plus 备选**：`partme-ai/full-stack-skills/element-plus-vue3`（1,941 / ⭐658）名义上是专门的 Element Plus skill，但本轮未取到原文、仓库 star 偏低，**不如自建可控**。

---

## 四、工程通用（前后端都受益）

| # | 方向 | 推荐 skill | 来源仓库 | 安装量 | Star | 用法 |
|---:|---|---|---|---:|---:|---|
| 15 | **代码评审** | `code-review` | `mattpocock/skills` | **520,310** | ⭐257,863 | 全库安装量第一。提交前自动找 bug、安全与性能问题，输出分级结论。PR 前跑一遍（这是本清单里**性价比最高**的一个）。 |
| 16 | **API 设计** | `api-and-interface-design` | `addyosmani/agent-skills` | **31,705** | ⭐93,221 | REST 接口契约设计、请求/响应结构、错误码、版本化策略。设计新接口时触发（前后端联调前先定契约）。 |
| 17 | **Git 提交规范** | `git-commit` | `github/awesome-copilot` | **44,591** | ⭐38,819 | Conventional Commits 规范提交信息与 PR 描述。（同类 `conventional-commit` 16,183 属同方向，不重复装。） |

---

## 五、安装命令（按仓库合并，减少克隆次数）

已在项目根目录执行；`--agent cursor` 为**快模式**（只给 Cursor 建软链，秒级完成）。若要全平台版，把 `--agent cursor` 换成 `--agent '*'`（**注意：全平台版每个 skill 约 7 分钟**，17 个会很久）。

```bash
# 后端：Spring Boot / JUnit / Git 提交
npx -y skills add github/awesome-copilot --skill java-springboot --skill java-junit --skill git-commit -y --agent cursor

# 后端：架构模式 / Java 规范 / MySQL / Redis / UI 还原
npx -y skills add affaan-m/ecc --skill backend-patterns --skill java-coding-standards --skill mysql-patterns --skill redis-patterns --skill ui-to-vue -y --agent cursor

# 前端：Vue3 / 前端测试
npx -y skills add vuejs-ai/skills --skill vue-best-practices --skill vue-testing-best-practices -y --agent cursor

# 微服务 / TypeScript / Kafka / 代码评审 / API 设计
npx -y skills add wshobson/agents --skill microservices-patterns -y --agent cursor
npx -y skills add sickn33/agentic-awesome-skills --skill typescript-expert -y --agent cursor
npx -y skills add mindrally/skills --skill kafka-development -y --agent cursor
npx -y skills add mattpocock/skills --skill code-review -y --agent cursor
npx -y skills add addyosmani/agent-skills --skill api-and-interface-design -y --agent cursor
```

> 安装后核对：`.agents/skills/` 下每个目录应有 `SKILL.md`。若遇 GitHub SSL 握手失败，用镜像 `git config --global url."https://ghproxy.net/https://github.com/".insteadOf "https://github.com/"`，装完记得 `--unset`。

---

## 六、⚠️ 版本适配提醒（务必先看）

存量后端是 **JDK 8 + Spring Boot 2.3**（见 [[20-后端Skill试用]]），而**生态主流 skill 全部面向 Java 17+ / Boot 3.x**——本轮实测再次证实：`mindrally/java` 写 Java 17+、`pluginagentmarketplace/java-spring-boot` 的 `spring_version` 默认 **3.2**、`piomin/java-architect` 要求 Java 21。

**对策（成本最低，建议立刻做）**：在项目 `.cursorrules` 或 `.agents` 里加版本护栏——

```
本仓库技术栈：JDK 8 + Spring Boot 2.3 + Spring Cloud Hoxton + MyBatis-Plus。
忽略任何 skill 中关于 Java 17+ / records / sealed / Spring Boot 3 / Jakarta /
JPA / 测试切片(@WebMvcTest) 的建议，生成代码必须兼容 JDK 8 与 javax.* 命名空间。
```

加了护栏后，本清单里 **1/2/3/4/5/6/7/8 号都能安全使用**；`create-spring-boot-java-project` 这类脚手架已在选型阶段排除。

---

## 七、需要自建的方向（无公共 skill）

| 方向 | 自建要点 |
|---|---|
| **MyBatis** | `${}` 与 `#{}` 注入红线（值位置一律 `#{}`）、XML 与 dao 同目录共生、`saveBatch` 批量、嵌套 collection 改 JOIN 防 N+1、分页插件统一 |
| **Element Plus** | `el-form` 校验规则、`el-table` 分页、`el-dialog` 用法、图标按需引入、SCSS 变量覆盖主题 |

两份自建模板在 **sjz-front 的 `.agents/skills/element-plus/`** 已有实践版本，可直接复制改造。

---

## 相关
- [[16-程序员推荐安装的Skill]]（上一轮通用推荐，本篇在其基础上按栈去重）
- [[20-后端Skill试用]]（后端 26 个 skill 在 sjz-back 的实测结果，本篇版本结论的依据）
- [[21-前端Skill试用]]（前端 20 个 skill 在 sjz-front 的实测结果）
- [[19-cursor内置skill]]（Cursor 内置 26 个技能，与外置 skill 互补，避免重复启用）

## 来源
- skills.sh 公开检索接口：`https://www.skills.sh/api/search?q=...`（installs 数据，检索于 2026-09-10）
- GitHub API `stargazers_count`（star 数据，检索于 2026-09-10）
- 实测交叉验证：[[20-后端Skill试用]]、[[21-前端Skill试用]]、`E:/guojian/01project/sjz/sjz-front/.agents/skills/`
