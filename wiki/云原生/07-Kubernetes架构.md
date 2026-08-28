---
title: Kubernetes 架构
type: concept
created: 2026-08-26
updated: 2026-08-26
tags: [云原生, Kubernetes, 架构]
---

# Kubernetes 架构

## 学习目标
- 掌握控制平面（Control Plane）各组件职责
- 掌握节点（Node）各组件职责
- 理解请求从 kubectl 到落地的流程

## 核心概念

K8s 采用**控制平面 + 工作节点**的主从架构。控制平面负责决策，节点负责干活。

## 详细说明

### 控制平面组件
- **API Server（kube-apiserver）**：集群唯一入口，所有操作经它，也是 etcd 的唯一写入者。
- **etcd**：分布式键值数据库，存储集群全部状态（唯一事实来源）。
- **Scheduler（kube-scheduler）**：把新 Pod 调度到合适节点（资源、亲和性、拓扑）。
- **Controller Manager（kube-controller-manager）**：运行各类控制器（副本、节点、端点等），执行调谐循环（见 [[11-控制器与编排原理]]）。
- **Cloud Controller Manager**：对接云厂商（负载均衡、节点管理）。

### 节点组件
- **kubelet**：节点上的 agent，管理本机 Pod 生命周期，对接容器运行时（见 [[05-容器运行时与OCI]]）。
- **kube-proxy**：维护节点网络规则，实现 Service 的负载均衡（见 [[09-Service与网络]]）。
- **容器运行时**：真正运行容器的软件（containerd / CRI-O）。

### 插件（Addons）
- **CoreDNS**：集群内部 DNS 服务发现。
- **Metrics Server**：资源指标来源（HPA 依赖）。
- **Dashboard / Ingress Controller** 等。

### 一次 `kubectl apply` 的流程
1. kubectl 把 YAML 发给 API Server。
2. API Server 校验并写入 etcd。
3. Controller/Scheduler 感知变化，做出决策。
4. 目标节点的 kubelet 调用运行时创建容器。

## 常见问题
**Q：etcd 挂了会怎样？**
A：控制平面无法写入状态，集群不可调度新负载，但已运行的 Pod 通常继续工作（取决于配置）。

## 参考资料
- Kubernetes 官方《Architecture》文档

## See Also
- [[06-Kubernetes核心概念]]
- [[05-容器运行时与OCI]]
- [[09-Service与网络]]
- [[11-控制器与编排原理]]
