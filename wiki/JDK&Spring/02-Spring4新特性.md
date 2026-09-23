---
title: Spring Boot 4 / Spring Framework 7 新特性
type: entry
created: 2026-09-02
updated: 2026-09-18
tags: [Spring, SpringBoot4, SpringFramework7, 新特性, 架构升级]
sources: [Spring Boot 4.0 Release Notes, InfoQ 报道(2025-11), Baeldung, OpenRewrite 迁移配方文档]
---

# Spring Boot 4 / Spring Framework 7 新特性

## 摘要

Spring Boot 4.0 于 **2025-11-20** 正式发布，构建在 **Spring Framework 7** 之上；当前稳定线为 **Spring Boot 4.1.0（2026-06-10，基于 Spring Framework 7.0.8）**。这是继 Boot 3 的 Jakarta 迁移之后最大的一次代际更新：基座升至 Jakarta EE 11、内建 API 版本化与弹性能力、引入 JSpecify 空安全标准、模块化拆分自动配置、并把虚拟线程设为默认。最低 Java 17，官方推荐 Java 21/25。

> 📌 **先澄清命名**：日常说的「Spring 版本」通常指 **Spring Boot**；真正的框架是 **Spring Framework**。二者版本号不同步：
> Spring Boot 4.x ↔ Spring Framework 7.x；Spring Boot 3.x ↔ Spring Framework 6.x；Spring Boot 2.x ↔ Spring Framework 5.x。
> 本条目中的「Spring 4」= **Spring Boot 4.x**。

## 当前版本与支持状态（2026-09）

| 版本 | 发布日期 | 最低 Java | 支持 Java | OSS 支持截止 |
|------|---------|----------|----------|-------------|
| **Spring Boot 4.1**（推荐） | 2026-08-20（4.1.1） | 17 | 17 – 26 | 2027-06-30（官方估计） |
| Spring Boot 4.0 | 2025-11-20 | 17 | 17 – 25 | 2026-12-31 |
| Spring Boot 3.5 | 2025-05-31 | 17 | 17 – 25 | **已于 2026-06-30 EOL** |
| Spring Boot 3.4 及更早 | — | — | — | **全部 EOL** |

**结论：新项目/升级项目直接上 Spring Boot 4.1，不要再落 3.x。** Boot 3.x 全系已进入或即将进入 EOL，只有付费商业支持（Broadcom Tanzu / HeroDevs NES）才能继续拿补丁。

> ✅ **数据核实时点：2026-09-18（已联网复核）** — Spring Boot 4.1.0 发布日 2026-06-10、3.5 OSS EOL 2026-06-30 均与 Spring 官方博客及 endoflife/版本跟踪器一致；最新补丁已到 **4.1.1（2026-08-20）**，**4.2.0-M1** 已发布（GA 预计 2026-11）；4.1 OSS 支持截止按版本跟踪器为 **2027-06-30**，结论（新项目直接上 4.1.x）保持不变。

## 一、基座升级

| 依赖 | Spring Boot 3.x | Spring Boot 4.x |
|------|----------------|-----------------|
| Java | 17（最低） | **17 最低，21/25 推荐** |
| Spring Framework | 6.x | 7.x |
| Jakarta EE | 10 | **11** |
| Servlet | 6.0 | 6.1 |
| JPA / Hibernate | 3.1 / 6.x | 3.2 / **7.x** |
| Bean Validation | 3.0 | 3.1 |
| Tomcat | 10.x | 11.x |
| Jackson | 2.x | **3.x**（可兼容 2.x） |
| Kotlin | 1.9+ | 2.2+ |
| Gradle | 7.x / 8.x | 8.14+ / 9.x |
| JUnit | 5.x | 6.x |

⚠️ **Boot 4 暂不支持 Undertow**（未适配 Servlet 6.1）。若现网用 Undertow，需切到 Tomcat 11 或 Jetty。

## 二、虚拟线程默认开启

```yaml
# Spring Boot 3.2+
spring:
  threads:
    virtual:
      enabled: true    # 需要显式开启

# Spring Boot 4.x —— 默认已开启，无需配置
```

Tomcat 请求处理与 `@Async` 方法默认跑在虚拟线程上。需要回退（例如老代码重度 `synchronized` 导致线程固定）：

```yaml
spring:
  threads:
    virtual:
      enabled: false
```

这是「JDK 21 + Spring Boot 4」组合最大的协同红利：不改一行业务代码，IO 密集型接口的并发上限提升一个数量级。

## 三、一等公民的 API 版本化

Spring Framework 7 原生支持 REST API 版本控制（此前只能靠 URL 硬编码或第三方库）。

```java
@RestController
@RequestMapping("/api/products")
public class ProductController {

    @RequestMapping(value = "/search", version = "1")
    public List<ProductV1> searchV1(@RequestParam String query) { ... }

    @RequestMapping(value = "/search", version = "2")
    public ProductSearchResponseV2 searchV2(@RequestParam String query,
                                            @RequestParam(defaultValue = "10") int limit) { ... }
}
```

- 支持四种策略：**路径 / 请求头 / 查询参数 / 媒体类型**，通过 `ApiVersionStrategy` 配置
- 内建**废弃处理**，符合 **RFC 9745**
- `RestClient`、`WebClient`、HTTP Interface 客户端通过 `ApiVersionInserter` 自动带上版本号

**这对政企项目价值极高**——水务/工业系统常有「同一接口要长期并存多个版本、不能中断存量客户端」的硬约束。

## 四、内建弹性能力（原 Spring Retry 并入内核）

```java
@Service
@EnableResilientMethods
public class PaymentService {

    @Retryable(maxAttempts = 3)          // 声明式重试，含指数退避 + 抖动
    public void processPayment() { ... }

    @ConcurrencyLimit(maxConcurrentCalls = 5)   // 声明式并发限流
    public void updateBalance() { ... }
}
```

- `@Retryable` 自动适配响应式方法
- `@ConcurrencyLimit` **在虚拟线程场景下尤其重要**——虚拟线程让并发变得几乎免费，也意味着下游（数据库、第三方接口）更容易被瞬时打爆，必须有并发闸门

## 五、JSpecify 空安全标准化

Spring 全系迁移到 **JSpecify** 注解（OpenJDK / Broadcom / Google / JetBrains / Sonar 联合标准）。

```java
import org.jspecify.annotations.Nullable;
import org.jspecify.annotations.NonNull;
import org.jspecify.annotations.NullMarked;

@NullMarked                       // 包级默认非空
public class OrderService {
    public Order findById(UUID id) { ... }              // 返回非空
    public @Nullable Order findOrNull(UUID id) { ... }  // 显式可空
}
```

- IntelliJ IDEA 2025.3+ 提供完整数据流分析
- Kotlin 2 自动把 JSpecify 注解翻译为 Kotlin 可空类型
- 构建期检查用 **NullAway**，要求 **JDK 21+**

> 💡 这条是「选 JDK 21 而非 17」的一个具体理由：想用 NullAway 做构建期空安全门禁，JDK 21 是最低门槛。

## 六、模块化重构（对构建与镜像影响最大）

Boot 4 把单体 `spring-boot-autoconfigure` 拆成了按技术栈划分的细粒度模块，starter 也相应改名：

| Boot 3.x | Boot 4.x |
|----------|----------|
| `spring-boot-starter-web` | **`spring-boot-starter-webmvc`** |
| `spring-boot-starter-aop` | **`spring-boot-starter-aspectj`** |
| `spring-boot-starter-oauth2-client` | **`spring-boot-starter-security-oauth2-client`** |
| `spring-boot-starter-oauth2-resource-server` | **`spring-boot-starter-security-oauth2-resource-server`** |
| `spring-boot-starter-oauth2-authorization-server` | **`spring-boot-starter-security-oauth2-authorization-server`** |
| `spring-boot-starter-web-services` | **`spring-boot-starter-webservices`** |

收益：依赖树更干净、JAR 体积更小、AOT/原生镜像处理更快、IDE 不再提示用不到的配置属性。

## 七、Jackson 3（破坏性变更，迁移第一大坑）

| 项 | Jackson 2 | Jackson 3 |
|----|-----------|-----------|
| 包名 | `com.fasterxml.jackson.*` | **`tools.jackson.*`** |
| 推荐 Mapper | `ObjectMapper` | **`JsonMapper`**（不可变、按格式特化） |
| 属性排序 | 默认不排序 | **`SORT_PROPERTIES_ALPHABETICALLY = true`** |
| 日期序列化 | 默认时间戳 | **默认 ISO-8601 字符串** |

⚠️ **两个默认行为变化会改变线上 JSON 输出**，涉及字段顺序敏感的签名/摘要、以及日期格式约定的接口，必须回归验证。

Boot 4 提供 `spring-boot-jackson2` 兼容垫片，可渐进迁移（Jackson 2 与 3 并存）。

## 八、可观测性：Micrometer 2 + OpenTelemetry

- 新增 `spring-boot-starter-opentelemetry`，一次性带齐 OTLP 指标与链路导出依赖
- 升级 Micrometer 2，指标 / 日志 / 链路三者联动（traceId 自动串通）
- SSL 健康报告改进：新增 `expiringChains` 条目，去掉易误报的 `WILL_EXPIRE_SOON` 状态

与 [[14-可观测性]] 的三支柱实践天然对齐，替换掉大量自研埋点代码。

## 九、AOT 与 GraalVM 原生镜像

- 对齐 **GraalVM 24**，AOT 处理增强，构建更快、启动内存更小
- **Spring Data AOT Repositories**：把符合条件的仓库查询方法在**构建期编译成源码**，显著缩短启动时间
- 切换到**单文件可达性元数据格式**
- 空闲时应用上下文暂停，大型测试套件内存占用下降

对启用 `spring.threads.virtual` + 原生镜像的部署，冷启动可从秒级降到几十毫秒级——这是进入 [[16-Serverless与FaaS]] 与弹性伸缩的前提。

## 十、其他值得注意的变更

| 变更 | 说明 |
|------|------|
| `BeanRegistrar` | 新增编程式 Bean 注册契约，支持运行时动态注册 |
| HTTP Interface Groups | `@ImportHttpServices` 批量配置声明式 HTTP 客户端，共享同一 `RestClient` |
| `RestTestClient` | Spring 7.0 新增的非响应式测试客户端 |
| `RestTemplate` | **7.1（2026-11 预计）标记废弃，8.0 移除** → 现在就该迁移到 `RestClient` |
| `AntPathMatcher` | HTTP 请求匹配上废弃，改用 `PathPattern` |
| SpEL Optional | 更好的 Optional 支持（`?.`、Elvis 运算符） |
| SSL / 安全 | Spring Security 7，支持多因子认证（MFA） |
| 测试 | JUnit 6、Testcontainers 2.0、`@MockBean`/`@SpyBean` → `@MockitoBean`/`@MockitoSpyBean` |
| `@ConfigurationPropertiesSource` | 跨模块配置属性元数据生成提示 |
| `javax.annotation` / `javax.inject` | **不再支持**，必须换成 `jakarta.*` |

## 相关

- [[04-Spring4与Spring2对比]] — 从 Boot 2.3 出发的完整落差清单
- [[01-JDK21新特性]] — Spring 4 所依赖的 JDK 能力底座
- [[05-升级必要性]] — 版本 EOL、安全合规与投入产出
- [[12-微服务架构]] — API 版本化与弹性能力在微服务中的落点

## 来源

- Spring Boot 4.0 Release Notes（spring.io）
- InfoQ：Spring Framework 7 and Spring Boot 4 Deliver API Versioning, Resilience, and Null-Safe Annotations（2025-11）
- Baeldung：Spring Boot 4 & Spring Framework 7 – What's New
- OpenRewrite：Migrate to Spring Boot 4.0 配方文档
- endoflife.date/spring-boot
