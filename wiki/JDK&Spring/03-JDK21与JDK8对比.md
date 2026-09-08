---
title: JDK 21 与 JDK 8 对比
type: comparison
created: 2026-09-02
updated: 2026-09-02
tags: [JDK, Java8, Java21, 版本对比, 架构升级]
sources: [OpenJDK 发行说明, Oracle Java SE Support Roadmap, Eclipse Temurin Support]
---

# JDK 21 与 JDK 8 对比

## 摘要

JDK 8（2014-03）到 JDK 21（2023-09）**跨越 13 个特性版本**，不是一次「升版本号」，而是语言、运行时、GC、工具链、部署模型五个层面的整体换代。核心落差集中在四点：**并发模型**（虚拟线程 vs 平台线程池）、**延迟**（分代 ZGC 亚毫秒 vs Parallel GC 秒级）、**容器友好度**（内建容器感知 vs 靠参数打补丁）、**开发表达力**（Records/Sealed/模式匹配/var/文本块 vs 全是样板代码）。同时要注意，JDK 8 的免费公开更新早已终止，继续停留意味着安全补丁断供。

## 一、总览对照表

| 维度 | JDK 8（2014） | JDK 21（2023，LTS） |
|------|--------------|-------------------|
| 默认 GC | Parallel GC | G1 GC（ZGC/Shenandoah 可选，分代 ZGC 为亚毫秒级） |
| 内存模型 | PermGen（`-XX:PermSize` 调参） | Metaspace（自 JDK 8 起，自动管理） |
| 并发模型 | 平台线程 1:1 OS 线程 | **虚拟线程（JEP 444）**，百万级 |
| 字符串存储 | UTF-16 char[] | Compact Strings（JDK 9+，Latin-1，省内存） |
| 容器感知 | 无（8u191 后有限 backport） | **原生支持**（JDK 10+ `UseContainerSupport` 默认开） |
| 模块化 | 无（单一庞大 rt.jar） | JPMS 模块系统（JDK 9+），可 `jlink` 裁剪运行时 |
| HTTP 客户端 | `HttpURLConnection`（老旧阻塞） | **`java.net.http.HttpClient`**（JDK 11+，支持 HTTP/2、WebSocket） |
| 打包 | 只有 fat jar | `jlink` 定制运行时 + `jpackage` 原生安装包（JDK 14+） |
| 诊断 | 商业版 JFR | **JFR 开源**（JDK 11+），配合 JMC |
| 许可（Oracle） | OTN，商用需订阅 | NFTC 免费商用（**2026-09 CPU 后转 OTN**，见下文） |

## 二、语言特性落差（8 → 21 累计）

### 已在 JDK 8 具备（基线）

Lambda 表达式、Stream API、`java.time` 日期时间 API、`Optional`、接口默认方法、`CompletableFuture`、方法引用。

### JDK 9 – 21 新增（JDK 8 全部没有）

| 版本 | 特性 | 影响 |
|------|------|------|
| 9 | 模块系统（JPMS）、`var` 之外：集合工厂方法 `List.of()` | 强封装时代的开端 |
| 10 | **局部变量类型推断 `var`** | 减少样板 |
| 11 | **HTTP Client（标准）**、单文件源码运行、TLS 1.3 | 替换 Apache HttpClient 的动机 |
| 12–13 | Switch 表达式（预览）、**文本块（预览）** | |
| 14 | **Switch 表达式（正式）**、更有用的 NPE 提示 | NPE 现在会告诉你「哪个变量是 null」 |
| 15 | **文本块（正式）**、EdDSA 签名 | 多行 JSON/SQL/模板终于不用拼 `+` |
| 16 | **Records（正式）**、instanceof 模式匹配、强封装默认开启 | DTO/值对象代码量减半 |
| 17 | **Sealed 类（正式）** | 受限继承，配合模式匹配可穷尽校验 |
| 21 | **虚拟线程、记录模式、switch 模式匹配、有序集合、分代 ZGC**（均正式） | 见 [[01-JDK21新特性]] |

### 代码对照

```java
// ===== JDK 8 =====
public class UserDTO {
    private final Long id;
    private final String name;
    // 构造器 + getter + equals + hashCode + toString ≈ 60 行
}

String json = "{\n" +
              "  \"name\": \"" + name + "\",\n" +
              "  \"age\": " + age + "\n" +
              "}";

if (obj instanceof Order) {
    Order o = (Order) obj;   // 先判断再强转，两步
    ...
}

// ===== JDK 21 =====
public record UserDTO(Long id, String name) {}   // 1 行搞定

String json = """
    {
      "name": "%s",
      "age": %d
    }
    """.formatted(name, age);

if (obj instanceof Order o) {   // 一步拿到绑定变量
    ...
}
```

## 三、运行时与性能落差

| 指标（典型 Spring Boot Web 应用） | JDK 8 | JDK 21 | 说明 |
|------|------|------|------|
| GC 停顿 | 秒级（Parallel，大堆时尤甚） | G1：十~百毫秒 / ZGC：**亚毫秒** | 抖动敏感业务改善最显著 |
| 吞吐量 | 基线 | 通常 **提升 10%–30%** | 来自 JIT、GC、内联与字符串优化累积 |
| 内存占用 | 基线 | 同负载下**下降 10%–20%** | Compact Strings + G1/ZGC 改进 |
| 启动时间 | 基线 | 略快；配合 AppCDS/AOT 可大幅缩短 | 对弹性扩缩容意义大 |
| 容器内存识别 | 需 `-Xmx` 手工压，否则易被 OOMKilled | **自动识别 cgroup 限制**，默认用 75% 可用内存作堆上限 | K8s 部署的关键差异 |

> 💡 **容器感知是最容易被低估的一条。** JDK 8 应用在 Kubernetes 里最常见的故障，就是 JVM 读宿主机内存、`-Xmx` 超过 Pod limit，被 `OOMKilled`。JDK 10+ 原生按 cgroup 限制计算堆大小，`MaxRAMPercentage` 可直接按百分比配置，见 [[08-Pod与工作负载]]。

## 四、安全与许可落差（决策权重最高）

| 项 | JDK 8 | JDK 21 |
|----|-------|--------|
| Oracle 免费公开更新 | **已终止**（2019-04 起） | NFTC 免费商用，**至 2026-09 CPU** |
| Oracle 首要支持 | 已于 2022-03 结束 | 至 2028-09 |
| Oracle 扩展支持 | 至 2030-12（需订阅） | 至 2031-09（需订阅） |
| 免费 OpenJDK 构建（Temurin 等） | 至少至 2030-12 | 至少至 2029-12 |
| 新协议/算法 | TLS 1.3 缺失、无后量子密码准备 | TLS 1.3 默认、含 **KEM API（JEP 452）** |

**关键判断**：停留在 JDK 8 并不等于「不安全」，但等于**自愿承担「新漏洞无补丁」的风险敞口**，且需要靠商业订阅或第三方（如 Azul / 国产发行版）兜底。对需要过等保测评的政企项目，组件的官方支持状态是必查项，见 [[05-升级必要性]]。

## 五、升级时的破坏性变更清单

按实际踩坑频率排序：

1. **模块强封装**（最高频）—— JDK 16 起默认禁止反射 JDK 内部类
   ```
   java.lang.reflect.InaccessibleObjectException:
   Unable to make field private final byte[] java.lang.String.value accessible
   ```
   解法：升级 Lombok/MapStruct/反射工具版本；必要时临时加 `--add-opens java.base/java.lang=ALL-UNNAMED`（应作为过渡手段，不是终局）。
2. **`sun.misc.Unsafe` 受限** → 改用 `VarHandle` 或 JEP 442 外部内存 API
3. **JAXB / JAX-WS / CORBA 从 JDK 移除**（JDK 11） → 显式加 `jakarta.xml.bind-api` 等依赖
4. **Nashorn JS 引擎移除**（JDK 15） → 改用 GraalVM JS 或 Rhino
5. **CMS GC 移除**（JDK 14） → 迁移到 G1 / ZGC
6. **SecurityManager 废弃** → 重新设计沙箱方案
7. **第三方字节码工具链** → Lombok、CGLIB、ASM、ByteBuddy、各类 APM 探针必须升级到支持 JDK 21 的版本
8. **序列化/反序列化** → 老 JDK 8 编译的 `serialVersionUID` 与类结构兼容性需回归验证
9. **JDBC 驱动** → 老版本驱动（尤其 Oracle/MySQL 5.x 驱动、老国产库驱动）需换新

## 六、升级路径建议

```
JDK 8  ──→  JDK 11  ──→  JDK 17  ──→  JDK 21
         （可选）     （可选）     （目标）
```

- **可以直跳 21**：若项目依赖生态健康（无重度 `sun.*` 内部 API 调用、无停更的老二方包），8 → 21 直跳是可行的，且比逐级迁移更省事。
- **建议保留 11/17 作为过渡验证点**：若代码库庞大、第三方依赖陈旧，逐级迁移能把「编译错误」和「运行时行为变化」分批暴露，定位成本更低。
- **务必先单独完成 JDK 升级，再动 Spring**：先让项目在 JDK 21 上编译通过、测试全绿，再升 Spring Boot。两步混在一起会让报错相互掩盖。

## 相关

- [[01-JDK21新特性]] — JDK 21 特性详解
- [[02-Spring4新特性]] — Spring Boot 4 对 JDK 版本的要求
- [[04-Spring4与Spring2对比]] — 框架侧的落差清单
- [[05-升级必要性]] — 综合论证与投入产出
- [[03-容器技术基础]] — 容器感知与镜像体积

## 来源

- OpenJDK 各版本发行说明（openjdk.org/projects/jdk/）
- Oracle Java SE Support Roadmap
- Eclipse Temurin Support（adoptium.net/support）
- Oracle《JDK 21 approaches end-of-permissive license》公告
