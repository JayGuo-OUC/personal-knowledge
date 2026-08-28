---
title: Kubernetes 核心概念
type: tutorial
created: 2026-08-26
updated: 2026-08-26
tags: [云原生, Kubernetes, 概念]
---

# Kubernetes 核心概念

## 学习目标
- 理解 K8s 解决什么问题
- 掌握集群、节点、Pod、Deployment、Service、Namespace 等核心对象
- 理解声明式 API 的思想

## 核心概念

**Kubernetes（K8s）** 是容器编排系统，自动完成**部署、扩缩容、自愈、服务发现、负载均衡**。它把「期望状态」与「实际状态」对齐（见 [[11-控制器与编排原理]]）。

## 详细说明

### 核心对象
- **Cluster（集群）**：一组节点 + 控制平面。
- **Node（节点）**：运行容器的机器（物理机或虚拟机）。
- **Pod**：K8s 最小调度单位，包含一个或多个共享网络的容器。见 [[08-Pod与工作负载]]。
- **Deployment**：声明式管理 Pod 副本与滚动更新。
- **Service**：为一组 Pod 提供稳定访问入口与负载均衡。见 [[09-Service与网络]]。
- **Namespace**：逻辑隔离边界，用于多租户/环境划分。
- **Label / Selector**：用键值对标记资源，并通过标签选择器筛选。

### 声明式 vs 命令式
K8s 推崇**声明式**：你描述「想要什么」（YAML），控制器负责让现实趋近期望。
```bash
kubectl apply -f deploy.yaml   # 声明式
```

### 期望状态调和
用户提交期望 → API Server 存储到 etcd → 各控制器不断调谐，使实际状态逼近期望（见 [[11-控制器与编排原理]]）。

## 实践示例
最小 Deployment：
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx
spec:
  replicas: 3
  selector:
    matchLabels: { app: nginx }
  template:
    metadata:
      labels: { app: nginx }
    spec:
      containers:
        - name: nginx
          image: nginx:1.27
```

## 常见问题
**Q：Pod 和容器什么关系？**
A：Pod 包裹一个或多个紧密协作的容器，共享 IP 与存储卷；通常一个 Pod 一个主容器。

## 参考资料
- Kubernetes 官方文档 kubernetes.io/docs

## See Also
- [[07-Kubernetes架构]]
- [[08-Pod与工作负载]]
- [[09-Service与网络]]
- [[11-控制器与编排原理]]
