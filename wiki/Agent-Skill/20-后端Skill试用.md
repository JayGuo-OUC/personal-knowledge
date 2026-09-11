---
title: "20-后端Skill试用：sjz-back 全量 26 个 Skill 运行结果"
type: entry
created: 2026-09-09
updated: 2026-09-09
tags: [AI, Agent, Skill, 试用, 代码审查, 后端, Java, SpringBoot, MyBatis, MySQL, Redis, sjz-back]
sources: [E:/guojian/01project/sjz/sjz-back/.claude/skills, E:/guojian/01project/sjz/sjz-back/skill运行结果.md]
---

# 20-后端Skill试用：sjz-back 全量 26 个 Skill 运行结果

## 摘要
把后端项目 `sjz-back`（Java 8 + Spring Boot 2.3 / Spring Cloud Hoxton 多模块微服务）里已装的 26 个 skill **逐个跑了一遍**——对照每个 `SKILL.md` 的规则对仓库做合规审计，判定「是否适用 + 结论」。总体结果：**通过 0 · 部分通过 17 · 未通过 9**。最高优先级问题集中在：SQL 注入（`${id}` 拼接）、无版本化 DB 迁移、Redis `KEYS` 与大量无 TTL、字段 `@Autowired` 注入主导、测试与质量门禁缺失、配置明文密码、日志不规范。

> 本篇是 **sjz-back 全量 26 个 skill 的适用性体检（广度）**：逐项给出每个 skill 的目标、是否适配本项目、关键发现与建议。前端同类体检见 [[21-前端Skill试用]]。

---

# Skill 运行结果

- **项目**: `sjz-back`（Java 8 + Spring Boot 2.3 / Spring Cloud Hoxton 多模块微服务）
- **运行时间**: 2026-09-09
- **运行方式**: 对照各 skill 的 `SKILL.md` 对仓库做合规审计（非可执行脚本；`code-review-skill` 附带的 `pr-analyzer.py` 本次未执行）
- **Skill 来源目录**: `.claude/skills/`（与 `.agents/skills/` 内容基本一致，按去重后 26 个统计）
- **说明**: 多数 skill 面向 Java 17+ / Spring Boot 3.x，与本仓库栈存在版本差；结论按「能否在当前仓库落地」判定。

---

## 总览

| # | Skill | 是否适用 | 结论 |
|---|--------|----------|------|
| 1 | java-coding-standards | 部分适用 | 部分通过 |
| 2 | java-architect | 部分适用 | 未通过 |
| 3 | java-springboot | 适用 | 部分通过 |
| 4 | spring-boot | 部分适用 | 部分通过 |
| 5 | spring-boot-engineer | 部分适用 | 部分通过 |
| 6 | springboot-patterns | 适用 | 部分通过 |
| 7 | springboot-security | 适用 | 部分通过 |
| 8 | springboot-verification | 适用 | 未通过 |
| 9 | create-spring-boot-java-project | 不适用 | 未通过 |
| 10 | backend-patterns | 部分适用 | 部分通过 |
| 11 | mysql | 适用 | 部分通过 |
| 12 | mysql-patterns | 适用 | 部分通过 |
| 13 | mybatis | 完全适用 | 部分通过 |
| 14 | sql-pro | 适用 | 部分通过 |
| 15 | sql-optimization | 适用 | 未通过 |
| 16 | sql-optimization-patterns | 适用 | 未通过 |
| 17 | sql-code-review | 适用 | 未通过 |
| 18 | database-optimizer | 部分适用 | 未通过 |
| 19 | database-migrations | 部分适用 | 未通过 |
| 20 | redis | 适用 | 部分通过 |
| 21 | redis-patterns | 适用 | 部分通过 |
| 22 | code-review-skill | 适用 | 部分通过 |
| 23 | code-quality | 适用 | 部分通过 |
| 24 | design-patterns | 适用 | 部分通过 |
| 25 | logging-patterns | 部分适用 | 未通过 |

**统计**: 通过 0 · 部分通过 17 · 未通过 9

### 跨 Skill 最高优先级问题

1. **SQL 注入风险**: `MajorAlarmMapper.xml` 等处使用 `${id}` / `${...}`，应改为 `#{}`
2. **无版本化 DB 迁移**: 无 Flyway/Liquibase，仅有手工 SQL 导出
3. **Redis `KEYS` + 大量无 TTL**: `RedisUtil.getKeys()` / `redisTemplate.keys()` 被多处调用
4. **字段 `@Autowired` 主导**: 构造器注入极少
5. **测试/质量门禁缺失**: 正式单测几乎为 0，无 JaCoCo / SpotBugs / OWASP 扫描
6. **配置明文密码**: `bin/config/**` 等 YAML 含明文口令
7. **日志不规范**: `System.out.println`、`printStackTrace`、字符串拼接异常日志仍存在

---

## 一、Java / Spring 类

## java-coding-standards

- **技能目标**: 规范 Spring Boot Java 代码的命名、不可变性、Optional、异常处理、DI 方式与项目结构。
- **是否适用**: 部分适用 — 核心 Spring 约定可审计，但 skill 面向 Java 17+（records 等），与项目 Java 8 不匹配。
- **运行方式**: 对照仓库做合规审计
- **结论**: 部分通过
- **关键发现**:
  - `hi-dependencies/pom.xml` 锁定 Java 8，无法采用 records 等 Java 17+ 特性
  - 字段注入广泛：`@Autowired` 出现在约 170+ 个 Java 文件
  - 全局异常处理已存在：`hi-libs-utils/.../GlobalExceptionHandler.java`，但 `debug=true` 硬编码
  - 约 29 个文件仍含 `System.out.print*`
  - `catch (Exception` 出现在 150+ 个文件
- **建议**:
  1. 新代码强制构造器注入
  2. `GlobalExceptionHandler` 的 debug 改为配置项
  3. 清理 `System.out`，统一 SLF4J

---

## java-architect

- **技能目标**: 面向 Spring Boot 3.x / Java 21 的企业级微服务架构设计与实现。
- **是否适用**: 部分适用 — 架构思路可参考，但要求 Java 21、Flyway、JPA，与项目差异大。
- **运行方式**: 对照仓库做合规审计
- **结论**: 未通过
- **关键发现**:
  - 版本：Boot 2.3.12 + Hoxton + Java 8，非 Boot 3 / Java 21
  - 数据层约 100 个 `BaseMapper`（MyBatis-Plus），`JpaRepository` 为 0
  - 无 Flyway/Liquibase
  - API 文档为 Swagger 2 / knife4j，非 springdoc OpenAPI 3
  - 正式测试仅约 1 个空壳 `@SpringBootTest`，远低于 85% 覆盖率要求
- **建议**:
  1. 单独制定 Boot 2.3 → 3.x 升级路线，勿直接套模板
  2. 引入 Flyway/Liquibase
  3. 按模块补充集成测试

---

## java-springboot

- **技能目标**: Spring Boot 最佳实践——构造器注入、外部化配置、DTO 校验、分层与测试。
- **是否适用**: 适用
- **运行方式**: 对照仓库做合规审计
- **结论**: 部分通过
- **关键发现**:
  - Maven 多模块 + `hi-dependencies` 统一版本管理符合要求
  - 包结构偏领域分包（如 `ems.energy.controller`）
  - 约 83 个 `@RestController` 多数字段注入；`@Valid` 仅约 24 个文件
  - Nacos + `bootstrap.yml` 外部化配置已具备
  - 测试薄弱：无 `@WebMvcTest` / `@DataJpaTest`
- **建议**:
  1. 写接口补 `@Valid`
  2. Controller 改为构造器注入
  3. 为核心 Service 补 JUnit5 + Mockito

---

## spring-boot

- **技能目标**: Spring Boot 3.x 企业级开发分层、Security、全局异常与测试切片。
- **是否适用**: 部分适用 — 通用模式可对照，skill 面向 Boot 3.x。
- **运行方式**: 对照仓库做合规审计
- **结论**: 部分通过
- **关键发现**:
  - Controller → Service → Mapper 分层基本清晰
  - `GlobalExceptionHandler` 已集中处理业务/校验异常
  - `@Transactional` 仅约 17 个文件，覆盖有限
  - 仍使用 `WebSecurityConfigurerAdapter`（Boot 2 风格）
  - 无 `@Cacheable` / `@EnableCaching`
- **建议**:
  1. Security 向 `SecurityFilterChain` 迁移预备
  2. 读多写少接口引入 Spring Cache + Redis
  3. 写操作补 `@Transactional`

---

## spring-boot-engineer

- **技能目标**: 生成/指导 Spring Boot 3.x REST、Security、JPA、WebFlux 等工程实践。
- **是否适用**: 部分适用 — REST/Security/OAuth2 思路可参考，模板基于 Boot 3 + JPA。
- **运行方式**: 对照仓库做合规审计
- **结论**: 部分通过
- **关键发现**:
  - REST 层规模大（约 83 个 `@RestController`）
  - `hi-sso-oauth2-service` 含 Authorization Server / JWT / BCrypt
  - Nacos + Feign + Kafka 基础设施到位
  - Actuator 仅少数模块引入
  - 无测试切片，无法满足「测试全过」工作流
- **建议**:
  1. 各业务服务统一引入 Actuator health
  2. SSO/Security 补 MockMvc 测试
  3. 新功能继续沿用 MyBatis-Plus，勿复制 JPA 模板

---

## springboot-patterns

- **技能目标**: REST 分层、事务、缓存、异步、日志、分页与异常处理模式。
- **是否适用**: 适用
- **运行方式**: 对照仓库做合规审计
- **结论**: 部分通过
- **关键发现**:
  - 分层与全局异常已具备
  - `@EnableAsync` / `@Async`、`@EnableScheduling`、Kafka binder 有落地
  - `@Cacheable`/`@EnableCaching` 为 0；缓存多为 `RedisUtil` 直调
  - 可观测性（Micrometer/Prometheus）痕迹不足
- **建议**:
  1. 高频读接口封装 `@Cacheable`
  2. 引入 Micrometer 基础指标
  3. 统一分页返回格式

---

## springboot-security

- **技能目标**: 认证授权、输入校验、CSRF、密钥管理、安全头与依赖 CVE 扫描。
- **是否适用**: 适用
- **运行方式**: 对照仓库做合规审计
- **结论**: 部分通过
- **关键发现**:
  - JWT：`CustomJwtFilter`；OAuth2 SSO 模块存在
  - API 场景 `csrf().disable()` 可接受
  - 配置中存在明文密码（如 `bin/config/som-dev/*.yaml`）
  - `ignoreSecurity=true` 默认/旁路风险
  - 业务模块几乎未用 `@PreAuthorize`；未见 OWASP Dependency Check
  - `fastjson 1.2.80` 存在历史 CVE 风险
- **建议**:
  1. 生产强制关闭 ignoreSecurity
  2. 凭证改环境变量/Nacos 加密
  3. CI 引入依赖漏洞扫描，评估替换 fastjson

---

## springboot-verification

- **技能目标**: PR/发布前构建、静态分析、覆盖率、安全扫描与审查闭环。
- **是否适用**: 适用
- **运行方式**: 对照仓库做合规审计
- **结论**: 未通过
- **关键发现**:
  - `src/test/java` 正式测试极少（约 1 个空壳）
  - pom 中无 SpotBugs / PMD / Checkstyle / JaCoCo
  - 无 dependency-check 插件
  - 仍有 `System.out`、异常信息可能回传客户端
- **建议**:
  1. 根 pom 加 JaCoCo（可从较低阈值起步）
  2. CI 引入静态分析必过项
  3. 为核心模块补单测/集成测

---

## create-spring-boot-java-project

- **技能目标**: 通过 start.spring.io 创建 Java 21 + Boot 3.x 新项目骨架。
- **是否适用**: 不适用 — 本仓库为存量 Java 8 + Boot 2.3 多模块项目。
- **运行方式**: 对照仓库做合规审计
- **结论**: 未通过
- **关键发现**:
  - 版本与数据栈（JPA/PostgreSQL 模板 vs MyBatis-Plus）完全不匹配
  - 无 skill 要求的 docker-compose / springdoc / ArchUnit 骨架
  - 已有 50+ pom、多微服务，非 greenfield
- **建议**:
  1. 勿对本仓库执行脚手架初始化
  2. 新建子服务参考现有 `hi-modules` 模板
  3. 升级路径单独规划

---

## backend-patterns

- **技能目标**: 后端通用架构模式（REST、分层、缓存、事务、JWT、限流、队列）；示例偏 Node/TS。
- **是否适用**: 部分适用 — 概念可迁移，示例栈不匹配。
- **运行方式**: 对照仓库做合规审计
- **结论**: 部分通过
- **关键发现**:
  - 按业务域划分 REST；Mapper + Service 分层存在
  - Redis cache-aside、Kafka、`GlobalExceptionHandler` + `R<T>` 已落地
  - 无限流（Bucket4j/网关级）
  - JWT 有校验，方法级权限细粒度不足
- **建议**:
  1. 网关或 Filter 层加 Redis 限流
  2. 封装统一 CacheService（key/TTL 规范）
  3. Feign 调用补 Resilience4j 超时/重试

---

## 二、数据库 / MyBatis / SQL / Redis 类

## mysql

- **技能目标**: MySQL/MariaDB 生产环境 schema、索引、事务、连接池与复制策略。
- **是否适用**: 适用
- **运行方式**: 对照仓库做合规审计
- **结论**: 部分通过
- **关键发现**:
  - Druid 动态数据源已用；`max-active` 等基础配置存在
  - 部分 schema 仍为 `utf8mb3`
  - OFFSET 分页、WHERE 中 `DATE_FORMAT(列)` 可能伤索引
  - 配置文件明文数据库密码
- **建议**:
  1. 新表统一 utf8mb4
  2. 修正可疑分页 offset 计算
  3. 凭证移出仓库并校验连接池回收参数

---

## mysql-patterns

- **技能目标**: MySQL 生产级 schema/索引/事务/连接池与反模式清单。
- **是否适用**: 适用
- **运行方式**: 对照仓库做合规审计
- **结论**: 部分通过
- **关键发现**:
  - `SELECT *` 至少约 19 个 Mapper XML
  - 深 OFFSET 分页存在于 EMS/字典等模块
  - `@Transactional(rollbackFor=Exception.class)` 覆盖面有限
  - 双数据源配置偏同实例不同 URL，读写分离策略不清晰
- **建议**:
  1. Mapper 审查禁止新增 SELECT *
  2. 大表分页改 keyset
  3. 多表写补齐事务注解

---

## mybatis

- **技能目标**: 规范本项目 MyBatis-Plus：XML 共生、防注入、分页、批量、N+1 等。
- **是否适用**: 完全适用
- **运行方式**: 对照仓库做合规审计
- **结论**: 部分通过
- **关键发现**:
  - 部分 XML 放在 `resources/mapper/`，非 dao 同目录共生
  - SELECT * 在 XML 与 `@Select` 注解中均存在
  - 多数模块有 `PaginationInnerInterceptor`；仍有手写 OFFSET
  - **高危**: `MajorAlarmMapper.xml` 等 `${id}` 用法
  - N+1：`HisomPatrolTaskMapper.xml` 使用 `<collection select=...>`
  - 部分 `saveBatch` 已合规使用
- **建议**:
  1. 立即将删除/条件中的 `${id}` 改为 `#{id}`
  2. XML 迁至 dao 同目录并统一 resources 配置
  3. 嵌套 collection 改为 JOIN + 内存组装

---

## sql-pro

- **技能目标**: 优化 SQL、设计 schema、解读 EXPLAIN，跨方言查询与索引方案。
- **是否适用**: 适用（InfluxDB 不在本 skill 范围）
- **运行方式**: 对照仓库做合规审计
- **结论**: 部分通过
- **关键发现**:
  - 生产禁用 SELECT * 未遵守
  - 有 set-based 批量写入实践
  - 未见 EXPLAIN/ANALYZE 基线文档
  - `LIKE '%..%'` 参数化正确但难用索引
- **建议**:
  1. TOP 慢查询做 EXPLAIN 基线
  2. 列表查询列显式化
  3. 复杂报表评估 CTE/窗口函数

---

## sql-optimization

- **技能目标**: 跨库通用 SQL 性能优化：索引、JOIN、分页、批量、反模式。
- **是否适用**: 适用
- **运行方式**: 对照仓库做合规审计
- **结论**: 未通过
- **关键发现**:
  - SELECT *、OFFSET 深分页、列函数过滤并存
  - 批量 insert 有分批实践
  - 无 slow log / performance_schema 分析纳入仓库
- **建议**:
  1. CI/checklist 禁止 SELECT * 与列函数过滤
  2. 分页统一 MP Page 或 keyset
  3. 测试环境开启 slow log

---

## sql-optimization-patterns

- **技能目标**: 通过 EXPLAIN、索引策略与查询改写系统性消除慢查询。
- **是否适用**: 适用（PG 专属内容不适用）
- **运行方式**: 对照仓库做合规审计
- **结论**: 未通过
- **关键发现**:
  - 零 EXPLAIN 证据文档
  - N+1 collection select 存在
  - Redis 缓存与 DB 失效策略文档不足
- **建议**:
  1. 对 scene/patrol/ems 核心 SQL 跑 EXPLAIN 并补索引
  2. 消除 N+1
  3. 建立慢查询周报

---

## sql-code-review

- **技能目标**: SQL 安全、可维护性、性能与反模式审查清单。
- **是否适用**: 适用
- **运行方式**: 对照仓库做合规审计
- **结论**: 未通过
- **关键发现**:
  - `${id}` / `${map.selectedCondition...}` 注入风险
  - 多数动态 SQL 用 `#{}`（好的一面）
  - 分页 offset 计算可疑（如 `currentPage*pageSize`）
  - 表命名风格不统一
- **建议**:
  1. 立即审计全部 `${}` 用法
  2. PR 增加 SQL review 模板
  3. 修正分页并加回归测试

---

## database-optimizer

- **技能目标**: 基于 EXPLAIN 基线做索引设计、查询改写与配置调优。
- **是否适用**: 部分适用（MySQL 侧适用）
- **运行方式**: 对照仓库做合规审计
- **结论**: 未通过
- **关键发现**:
  - 技能要求优化前必须有 EXPLAIN 基线 — 仓库无证据
  - Druid 慢 SQL/wall 监控配置不明显
  - 批量写入分批已有；无索引变更 migration 流程
- **建议**:
  1. staging 采集核心查询 EXPLAIN
  2. 开启 Druid 慢 SQL 监控
  3. 索引变更记录 before/after

---

## database-migrations

- **技能目标**: 安全、可回滚、零停机的 schema/data migration（Flyway/Liquibase）。
- **是否适用**: 部分适用
- **运行方式**: 对照仓库做合规审计
- **结论**: 未通过
- **关键发现**:
  - 全仓无 Flyway/Liquibase、无 `db/migration/`
  - 仅有 `hi-libs/sql/` 下少数手工导出脚本（含 DROP TABLE 风险）
  - schema drift 依赖人工同步
- **建议**:
  1. 引入 Flyway 并建立 baseline
  2. 禁止生产执行含 DROP 的导出脚本
  3. DDL 变更必须走独立 PR + migration 文件

---

## redis

- **技能目标**: Redis / `hi-libs-redis` 使用与生产配置规范。
- **是否适用**: 适用
- **运行方式**: 对照仓库做合规审计
- **结论**: 部分通过
- **关键发现**:
  - `RedisUtil` 被广泛注入使用，连接池有基础配置
  - `enableDefaultTyping` 存在反序列化安全风险
  - `getKeys()` → `redisTemplate.keys()` 被 scene/alarm 等调用（生产禁用 KEYS）
  - 大量 `set`/`hmset` 无 TTL
- **建议**:
  1. KEYS 全部改为 SCAN
  2. 缓存/状态 key 补 TTL
  3. 移除危险 DefaultTyping

---

## redis-patterns

- **技能目标**: Redis 数据结构、缓存策略、分布式锁、限流、Pub/Sub 与反模式。
- **是否适用**: 适用
- **运行方式**: 对照仓库做合规审计
- **结论**: 部分通过
- **关键发现**:
  - 有部分 key 前缀规范与 cache-aside（如 `BaseModelBuffer`）
  - KEYS 反模式、无 TTL、锁释放非标准 Lua 模式
  - Pub/Sub 有封装但使用面窄；无限流模式
- **建议**:
  1. 实现 `scanKeys` 替换 `getKeys`
  2. 基础数据缓存加 TTL + 写路径失效
  3. 强一致协调改标准分布式锁

---

## 三、质量 / 架构 / 日志类

## code-review-skill

- **技能目标**: 系统化 PR/代码审查流程，含 Java 8 清单与 PR 分析脚本。
- **是否适用**: 适用
- **运行方式**: 对照仓库做合规审计；**未执行** `scripts/pr-analyzer.py`（面向 PR diff，非全仓静态审计）
- **结论**: 部分通过
- **关键发现**:
  - 有 `GlobalExceptionHandler`，但 `Throwable` 过宽、`debug=true`、部分异常仍返回 HTTP 200
  - 正式单测几乎缺失
  - `printStackTrace` / 空 catch / POST 做查询 等问题存在
- **建议**:
  1. 调整全局异常状态码与 debug 开关
  2. PR 强制引用 review checklist
  3. 统一异常日志写法

---

## code-quality

- **技能目标**: DRY/KISS、API 契约、空安全、异常、事务与性能等质量审查。
- **是否适用**: 适用
- **运行方式**: 对照仓库做合规审计
- **结论**: 部分通过
- **关键发现**:
  - `@Slf4j` 普及；部分 `@Transactional` 已用
  - 多处 POST 只读查询；无 `/api/v1` 版本化
  - 宽泛 catch、`findAll`/`selectList` 无分页、字段注入仍常见
- **建议**:
  1. 新接口 GET + 分页
  2. 异常日志统一 `log.error("msg {}", id, e)`
  3. 列表接口强制分页

---

## design-patterns

- **技能目标**: 指导 Factory/Strategy/Builder/Adapter 等模式选用，避免反模式。
- **是否适用**: 适用
- **运行方式**: 对照仓库做合规审计
- **结论**: 部分通过
- **关键发现**:
  - scene 模块 Strategy + Factory（`NodeStrategyFactory`、大量 `*NodeStrategy`）运用良好
  - Adapter（`DevStrategyAdapter` 等）存在；Spring DI 替代手写单例
  - 无 `@EventListener` / `ApplicationEventPublisher` 解耦
  - Builder 使用有限；策略层级较深，学习成本高
- **建议**:
  1. 补充 NodeStrategy 注册文档
  2. 跨模块副作用评估 Spring Events
  3. 避免再叠不必要 Adapter 层

---

## logging-patterns

- **技能目标**: SLF4J、参数化日志、结构化 JSON、MDC 请求追踪。
- **是否适用**: 部分适用 — Boot 2.3 需走 logstash-logback-encoder，非 Boot 3.4 原生 structured logging。
- **运行方式**: 对照仓库做合规审计
- **结论**: 未通过
- **关键发现**:
  - `@Slf4j` 广泛，但约 30 文件 `System.out`、40+ 文件 `printStackTrace`
  - 字符串拼接异常日志（BAD）
  - 无 MDC / requestId；logback 多为纯文本 pattern
  - 部分模块 logback 双 `<root>`、console debug 噪音风险
- **建议**:
  1. 引入 logstash-logback-encoder + MDC Filter
  2. 批量替换 `System.out` / `printStackTrace` / 拼接日志
  3. 合并 logback root，生产默认 INFO

---

## 附录：运行说明

1. Skill 本身主要是**知识/工作流文档**，不是可执行程序；本次「运行」= **按 skill 规则对当前仓库审计**。
2. 唯一发现的可执行脚本：`.claude/skills/code-review-skill/scripts/pr-analyzer.py`（PR 分析），本次未跑。
3. `.agents/skills/` 与 `.claude/skills/` 为同一套 skill 的双份安装，报告按 **26 个唯一 skill** 计，避免重复。
4. 若需对某一 skill 做「修复落地」或「只跑某一模块」，可指定 skill 名 + 模块名继续。

---

## 相关
- [[16-程序员推荐安装的Skill]]（这些 skill 的选型来源与安装清单）
- [[19-cursor内置skill]]（Cursor 内置 skill 对照）

## 来源
- `E:/guojian/01project/sjz/sjz-back/.claude/skills/`（被审计的 26 个 skill 规则原文）
- `E:/guojian/01project/sjz/sjz-back/skill运行结果.md`（本次运行结果原始文档）
