---
title: Spring Boot 4 与 Spring Boot 2 对比
type: comparison
created: 2026-09-02
updated: 2026-09-02
tags: [Spring, SpringBoot2, SpringBoot4, 版本对比, 迁移, 架构升级]
sources: [Spring Boot 4.0 Release Notes & Migration Guide, OpenRewrite 迁移配方, endoflife.date/spring-boot]
---

# Spring Boot 4 与 Spring Boot 2 对比

## 摘要

Spring Boot 2.3（2020-05）到 Spring Boot 4.1（2026-06）跨越**两个大版本、6 年时间**，中间隔着 Boot 3 那次「Jakarta 命名空间 + Java 17 基座」的断代式改造。落点不在「新增了多少功能」，而在三件必须先解决的事：**`javax.*` → `jakarta.*` 全量替换**、**Spring Security 配置模型重写**、**第三方依赖连锁升级**。这三件占去迁移工作量的八成，剩下的新特性反而是收益项。**推荐路径：2.3 → 2.7 → 3.5 → 4.1，逐级迁移，不要直跳。**

## 一、基线对照表

| 维度 | Spring Boot 2.3（2020-05） | Spring Boot 4.1（2026-06） |
|------|--------------------------|--------------------------|
| Spring Framework | 5.2.x | **7.0.x** |
| 最低 Java | **8** | **17**（推荐 21 / 25） |
| 支持 Java | 8 – 15 | 17 – 26 |
| 命名空间 | `javax.*` | **`jakarta.*`** |
| Jakarta EE | Java EE 8 | **Jakarta EE 11** |
| Servlet | 4.0 | 6.1 |
| Web 容器 | Tomcat 9 | **Tomcat 11**（Undertow 暂不支持） |
| JPA / Hibernate | 2.2 / 5.4 | 3.2 / **7.x** |
| Bean Validation | 2.0 | 3.1 |
| Spring Security | 5.3 | **7.x** |
| JSON | Jackson 2.x | **Jackson 3**（`tools.jackson.*`，兼容 2.x） |
| 自动配置 | 单体 `spring-boot-autoconfigure` | **按技术栈拆分模块** |
| 配置绑定 | `@ConfigurationProperties` | 同，但**构造函数绑定成为主流** |
| 可观测性 | Spring Boot Actuator + Micrometer 1.x | **Micrometer 2 + OpenTelemetry starter** |
| 原生镜像 | 无 | **GraalVM 24 AOT，Spring Data 构建期查询编译** |
| 虚拟线程 | 无 | **默认开启**（Tomcat + `@Async`） |
| 弹性能力 | 依赖 Spring Retry / Resilience4j | **内建 `@Retryable` / `@ConcurrencyLimit`** |
| API 版本化 | 自行实现 | **框架原生支持**，符合 RFC 9745 |
| 空安全 | 各项目自定义注解 | **JSpecify 标准** |
| OSS 支持状态 | **2021-05 已 EOL**（商业支持 2022-08 终止） | 至 2027-07（估） |

## 二、五大破坏性变更（按工作量排序）

### 1️⃣ `javax.*` → `jakarta.*`（工作量最大，但最机械）

```java
// Before（Boot 2.3）
import javax.persistence.Entity;
import javax.servlet.http.HttpServletRequest;
import javax.validation.constraints.NotNull;
import javax.annotation.PostConstruct;

// After（Boot 4.x）
import jakarta.persistence.Entity;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.validation.constraints.NotNull;
import jakarta.annotation.PostConstruct;
```

**不需要替换的（属于 Java SE，不是 Jakarta EE）**——这是最常见的误伤来源：

| 保持 `javax.*` 不动 | 原因 |
|--------------------|------|
| `javax.sql.*`（`DataSource` 等） | JDK 标准库 |
| `javax.crypto.*` | JCE |
| `javax.net.ssl.*` | JSSE |
| `javax.naming.*` | JNDI |
| `javax.swing.*` / `javax.imageio.*` | JDK 标准库 |
| `javax.annotation.Nonnull`（来自 **JSR-305**） | 与 `jakarta.annotation.Nonnull` 不是一回事 |

**别用 sed 全局替换。** 三处 IDE 扫不到的隐蔽点，是「编译过了但启动炸」的根因：
- `META-INF/spring.factories`、XML 配置里的**字符串类名**
- 通过**反射**按类名加载的 Filter / Listener
- **测试代码**里的 `MockMvc`、Mockito 相关 import（只改 main 不改 test 是高频遗漏）

### 2️⃣ Spring Security 配置模型重写（改动最伤）

```java
// ===== Boot 2.3：继承适配器（Boot 3 起已彻底移除）=====
@Configuration
@EnableWebSecurity
public class SecurityConfig extends WebSecurityConfigurerAdapter {
    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http.authorizeRequests()
            .antMatchers("/api/public/**").permitAll()
            .anyRequest().authenticated()
            .and().csrf().disable();
    }
}

// ===== Boot 4.x：SecurityFilterChain Bean + Lambda DSL =====
@Configuration
@EnableWebSecurity
public class SecurityConfig {
    @Bean
    SecurityFilterChain filterChain(HttpSecurity http, JwtAuthenticationFilter jwtFilter) throws Exception {
        return http
            .authorizeHttpRequests(auth -> auth
                .requestMatchers("/api/public/**").permitAll()
                .anyRequest().authenticated())
            .addFilterBefore(jwtFilter, UsernamePasswordAuthenticationFilter.class)
            .csrf(csrf -> csrf.disable())
            .sessionManagement(s -> s.sessionCreationPolicy(SessionCreationPolicy.STATELESS))
            .build();
    }
}
```

API 对照：

| Boot 2.x（Security 5） | Boot 4.x（Security 7） |
|------------------------|------------------------|
| `WebSecurityConfigurerAdapter` | **已删除** → `SecurityFilterChain` Bean |
| `authorizeRequests()` | `authorizeHttpRequests()` |
| `antMatchers()` / `mvcMatchers()` | `requestMatchers()` |
| `.and()` 链式拼接 | **Lambda DSL**，不再需要 `.and()` |
| `csrf().disable()` | `csrf(c -> c.disable())` |
| `User.withDefaultPasswordEncoder()` | 已废弃，仅限测试 |

> 项目若自研了 JWT / SSO 过滤器、自定义 `AuthenticationProvider`、OAuth2 登录，这部分要单独排期，通常是整个迁移里唯一需要真正「重写」而非「替换」的模块。

### 3️⃣ 第三方依赖连锁升级（最容易失控）

Boot 2.3 生态里的很多库已经停更或必须有 jakarta 版本。**注意：下表为常见库的方向性参考，落版本前请在测试环境验证。**

| 组件 | Boot 2.3 时代 | 需升级到 |
|------|-------------|---------|
| MyBatis-Plus | 3.5.x | jakarta 适配版（`mybatis-plus-spring-boot3-starter` 及后续版本） |
| Swagger | springfox 3.0（**已停更**） | **springdoc-openapi 3.x** |
| PageHelper | 1.4.x | jakarta 适配版 |
| Druid | 1.2.x 早期 | 支持 jakarta 的 1.2.20+ |
| JJWT | 0.11.x | 0.12.x（API 有变化） |
| Fastjson | 1.2.x | **建议直接换 Jackson**（Fastjson 1.x 高危漏洞频出，政企项目多已被安全扫描点名） |
| Logback | 1.2.x | 1.4+/1.5+（由 Boot BOM 管理） |
| Lombok / MapStruct | 老版本 | 支持 JDK 21 的版本 |

**铁律：每次改完 pom 都跑一次 `mvn dependency:tree`，确认实际生效版本。** 依赖仲裁悄悄拉低版本是这次迁移最耗时的一类问题——典型表现为 `NoSuchMethodError` / `ClassNotFoundException`，且报错信息往往指向完全不相干的类。

### 4️⃣ Jackson 3 默认行为变化（最易被忽略的线上事故源）

| 项 | Jackson 2 | Jackson 3 |
|----|-----------|-----------|
| 包名 | `com.fasterxml.jackson.*` | `tools.jackson.*` |
| Mapper | `ObjectMapper` | `JsonMapper` |
| 属性顺序 | 声明顺序 | **字母序** |
| 日期 | 时间戳 | **ISO-8601 字符串** |

⚠️ 涉及**字段顺序敏感的签名 / 摘要 / 报文比对**，以及**依赖日期数值格式的老客户端**的接口，必须逐条回归。Boot 4 提供 `spring-boot-jackson2` 垫片，可先并存再渐进迁移。

### 5️⃣ 配置属性与 starter 改名

- 部分 `spring.*` 属性重命名或删除（如 `spring.datasource.*` → `spring.sql.init.*`、`spring.data.mongodb.*` → `spring.mongodb.*`）
- starter 改名：`spring-boot-starter-web` → **`spring-boot-starter-webmvc`**、`-aop` → **`-aspectj`**、oauth2 系列加 `security-` 前缀
- Actuator：`/actuator/prometheus` 等端点需**显式暴露**；健康检查响应结构有变化
- 测试注解：`@MockBean` / `@SpyBean` → **`@MockitoBean` / `@MockitoSpyBean`**

## 三、推荐迁移路径

```
Spring Boot 2.3
      │  ① 先升 JDK 8 → 21（单独一步，不碰 Spring）
      ▼
Spring Boot 2.7   ← ② 过渡版本，它的编译期废弃警告 = 你的待办清单
      │
      ▼
Spring Boot 3.5   ← ③ 完成 javax → jakarta、Security 6 改造
      │
      ▼
Spring Boot 4.1   ← ④ 目标版本（目标：Jackson 3、模块化、虚拟线程默认）
```

**为什么不建议 2.3 直跳 4.1**：Boot 3 和 Boot 4 各自叠加了一层破坏性变更，直跳会让两类错误交织，定位成本成倍上升。逐级迁移时，每一级的**编译期废弃警告**就是下一级的待办清单，这是最省力的导航。

> 注意：2.7 与 3.5 都是**已 EOL 的中间站**，只作跳板、不要停留为最终目标。

## 四、自动化工具（能省下大量机械劳动）

### OpenRewrite（首选）

```bash
mvn -U org.openrewrite.maven:rewrite-maven-plugin:run \
  -Drewrite.recipeArtifactCoordinates=org.openrewrite.recipe:rewrite-spring:RELEASE \
  -Drewrite.activeRecipes=org.openrewrite.java.spring.boot4.UpgradeSpringBoot_4_0 \
  -Drewrite.exportDatatables=true
```

Boot 4 的 `UpgradeSpringBoot_4_0` 配方会**链式调用 Boot 3.5 迁移配方**，因此可直接作用于仍停留在 3.x 的项目。它自动完成：

- 升级 parent / 依赖 / 插件版本到 4.0.x
- 重命名改名的 starter、处理模块化拆分后的包路径
- `@MockBean` → `@MockitoBean`
- 配置属性重命名，被移除的属性**注释掉**等待人工处理
- 联动迁移：Spring Framework 7、Spring Security 7、Hibernate 7.1、Testcontainers 2、Spring Cloud 2025.1、SpringDoc 3.0、JUnit 6

**它做不到的**（必须人工）：
- Jackson 2 → Jackson 3 的完整迁移（配方默认保守，只加兼容垫片，保留 Jackson 2 import）
- Spring Security 自定义过滤器 / 自定义 Provider 的语义级改写
- 反射加载的字符串类名、`spring.factories` 残留

### spring-boot-properties-migrator

升级后临时加入依赖，启动时打印废弃属性警告：

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-properties-migrator</artifactId>
    <scope>runtime</scope>
</dependency>
```

处理完即可移除。

## 五、工作量与排期参考

按一个**中型单体/少量模块**的项目估算（含自研 JWT 鉴权 + MyBatis/MyBatis-Plus + 若干第三方 SDK）：

| 阶段 | 预估工时 | 主要风险 |
|------|---------|---------|
| JDK 8 → 21 编译通过 | 1–2 人日 | 强封装反射报错、老字节码工具 |
| 2.3 → 2.7 | 1–2 人日 | 配置项变更 |
| 2.7 → 3.5（jakarta + Security 6） | 3–5 人日 | 第三方依赖断链、反射加载残留 |
| 3.5 → 4.1（模块化 + Jackson 3） | 2–3 人日 | JSON 输出行为变化 |
| 全量回归 + 压测 | 3–5 人日 | 性能与行为差异 |
| **合计** | **约 10–17 人日 / 项目** | |

**降本关键**：先把一个**非核心、依赖最少**的服务走完全流程，把踩坑清单和版本对照表固化下来，后续服务按表执行，边际成本会大幅下降。

## 相关

- [[02-Spring4新特性]] — Boot 4 特性详解
- [[03-JDK21与JDK8对比]] — JDK 侧的落差清单
- [[05-升级必要性]] — 为什么这件事现在必须做
- [[12-微服务架构]] — 升级后的架构收益
- [[17-云原生安全]] — 供应链与组件安全要求

## 来源

- Spring Boot 4.0 Release Notes 与 Migration Guide（spring.io）
- OpenRewrite：`org.openrewrite.java.spring.boot4.UpgradeSpringBoot_4_0` 配方文档
- endoflife.date/spring-boot（版本支持状态）
- 社区迁移实践记录（javax→jakarta 替换遗漏、依赖仲裁冲突等典型问题复盘）
