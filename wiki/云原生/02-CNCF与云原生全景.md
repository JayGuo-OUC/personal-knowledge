---
title: CNCF 与云原生全景
type: concept
created: 2026-08-26
updated: 2026-08-26
tags: [云原生, CNCF, 生态]
---

# CNCF 与云原生全景

## 学习目标
- 了解 CNCF 是什么、做什么
- 理解开源项目的成熟度分级
- 看懂云原生全景图（Landscape）的分层

## 核心概念

**CNCF（Cloud Native Computing Foundation，云原生计算基金会）** 是 Linux 基金会下的非营利组织，致力于推动云原生技术的标准化与开源生态。Kubernetes 就是 CNCF 的毕业（Graduated）项目。

## 详细说明

### 项目成熟度分级
1. **Sandbox（沙箱）**：早期、实验性项目。
2. **Incubating（孵化中）**：生产可用、采用度增长。
3. **Graduated（毕业）**：成熟稳定、广泛生产使用（如 Kubernetes、Prometheus、etcd、containerd、Envoy）。

### 云原生全景图分层（Landscape）
- **应用定义与开发（App Definition & Development）**：数据库、流处理、应用定义。
- **编排与管理（Orchestration & Management）**：调度、协调、服务发现、服务网格。见 [[13-服务网格ServiceMesh]]。
- **运行时（Runtime）**：容器运行时、存储、网络。见 [[05-容器运行时与OCI]]、[[09-Service与网络]]、[[10-存储与配置]]。
- **供应层（Provisioning）**：自动化、容器注册、安全、密钥。见 [[17-云原生安全]]。
- **可观测性与分析（Observability & Analysis）**：监控、日志、追踪、混沌工程。见 [[14-可观测性]]。
- **平台（Platform）**：各类发行版与托管服务。

### 代表性毕业项目
- **Kubernetes**：容器编排事实标准（[[06-Kubernetes核心概念]]）
- **Prometheus**：监控与告警（[[14-可观测性]]）
- **Envoy / Istio**：服务网格数据面与控制面（[[13-服务网格ServiceMesh]]）
- **containerd**：容器运行时（[[05-容器运行时与OCI]]）
- **etcd**：分布式键值存储，K8s 的数据库（[[07-Kubernetes架构]]）

## 实践示例
初学时不必掌握全景图全部。建议以 **Kubernetes 为主线**，再按需求延伸到监控、网格、安全等周边。

## 常见问题
**Q：全景图项目太多，怎么选？**
A：优先选 Graduated 项目，社区成熟、风险低。

## 参考资料
- https://www.cncf.io/projects/
- https://landscape.cncf.io/

## See Also
- [[01-云原生概览]]
- [[06-Kubernetes核心概念]]
- [[14-可观测性]]
