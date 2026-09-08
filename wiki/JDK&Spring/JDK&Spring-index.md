---
title: JDK & Spring 架构升级（主题索引）
type: index
created: 2026-09-02
updated: 2026-09-02
tags: [JDK, Spring, 主题索引, 架构升级]
sources: [OpenJDK 官方文档, Oracle Java SE Support Roadmap, Spring Boot 4.0 Release Notes, endoflife.date]
---

# JDK & Spring 架构升级 · 主题索引

> 本页是「JDK & Spring 架构升级」主题的入口。完整总索引见 [[index]]。库的规则见 [[CLAUDE]]。
>
> **主题背景**：公司后端从 **JDK 8 + Spring Boot 2.3** 升级至 **JDK 21 + Spring Boot 4.1**。本主题记录特性清单、版本落差、迁移路径与升级论证，供技术选型与排期决策使用。

## 一句话结论

**目标版本：JDK 21 + Spring Boot 4.1（不是 3.x）。** 决定性理由是 Boot 2.3（2021-05 EOL）与 JDK 8（无官方免费更新）已无任何补丁来源，在强合规行业属于不可长期接受的风险敞口；而 Boot 3.x 全系已 EOL，落 3.x 等于刚升级就要规划下一次升级。详见 [[05-升级必要性]]。

## 条目

### 特性清单

- [[01-JDK21新特性]] — 虚拟线程、记录模式、switch 模式匹配、有序集合、分代 ZGC、外部内存 API
- [[02-Spring4新特性]] — Jakarta EE 11、虚拟线程默认开启、API 版本化、内建弹性、JSpecify 空安全、模块化、Jackson 3

### 版本对比

- [[03-JDK21与JDK8对比]] — 跨越 13 个特性版本的语言/运行时/GC/容器/许可落差，附破坏性变更清单
- [[04-Spring4与Spring2对比]] — 五大破坏性变更（javax→jakarta、Security 重写、依赖连锁、Jackson 3、配置改名）+ 迁移路径与工时估算

### 决策论证

- [[05-升级必要性]] — 风险侧（EOL/合规/供应链）、收益侧（云原生/并发/延迟/成本）、信创与数据合规、风险对冲、分阶段路线图

## 关键时间节点（2026-09 当前）

| 时间 | 事件 | 应对 |
|------|------|------|
| **2026-09** | Oracle JDK 21 最后一个 NFTC 免费更新 | 改用 OpenJDK 发行版（推荐国产：Dragonwell / 毕昇） |
| 2026-12-31 | Spring Boot 4.0 OSS 支持结束 | 直接上 4.1，不要落 4.0 或 3.x |
| 已发生 | Spring Boot 3.x 全系 EOL（3.5 于 2026-06-30 结束） | 升级目标排除 3.x |
| 2027-07-31 | Spring Boot 4.1 OSS 支持截止（估） | 规划下一次例行升级 |

## 推荐阅读顺序

1. 决策者先看 **[[05-升级必要性]]** —— 判断是否要做、为什么现在做
2. 架构/技术负责人看 **[[03-JDK21与JDK8对比]]** 与 **[[04-Spring4与Spring2对比]]** —— 摸清工作量与风险
3. 执行团队看 **[[01-JDK21新特性]]** 与 **[[02-Spring4新特性]]** —— 具体怎么改、能用什么

## 跨主题关联（云原生）

- [[01-云原生概览]] — 云原生的定义与四大特征
- [[03-容器技术基础]] — 容器感知、镜像分层（JDK 8 的 OOMKilled 问题在此）
- [[08-Pod与工作负载]] — 资源限制与探针（liveness / readiness）
- [[12-微服务架构]] — API 版本化、弹性能力的落点
- [[14-可观测性]] — Micrometer 2 + OpenTelemetry
- [[15-CI-CD与DevOps]] — 迁移分阶段实施
- [[16-Serverless与FaaS]] — 原生镜像与冷启动
- [[17-云原生安全]] — 供应链安全与组件 EOL 治理
- [[18-云原生最佳实践]] — 不可变、声明式、弹性、渐进交付

## 相关

- [[index]]
- [[CLAUDE]]

## 来源

- OpenJDK JEP 索引（openjdk.org）
- Oracle Java SE Support Roadmap 与 JDK 21 许可过渡公告
- Spring Boot 4.0 / 4.1 Release Notes 与 Migration Guide
- endoflife.date/spring-boot
- OpenRewrite `UpgradeSpringBoot_4_0` 配方文档
- Eclipse Temurin Support（adoptium.net/support）
