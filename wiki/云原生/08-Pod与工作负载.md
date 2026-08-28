---
title: Pod 与工作负载
type: tutorial
created: 2026-08-26
updated: 2026-08-26
tags: [云原生, Kubernetes, 工作负载]
---

# Pod 与工作负载

## 学习目标
- 理解 Pod 的本质与用法
- 掌握各类工作负载控制器（Deployment / StatefulSet / DaemonSet / Job）
- 会写典型工作负载 YAML

## 核心概念

**Pod** 是 K8s 最小调度单位。工作负载（Workload）控制器负责以不同策略管理 Pod 集合。

## 详细说明

### Pod
- 一个或多个容器共享**网络命名空间**（同一 IP）与**存储卷**。
- 支持 **Init Container**（主容器前运行）、**Sidecar**（辅助容器，服务网格常用，见 [[13-服务网格ServiceMesh]]）。
-  ephemeral（易失）：节点故障会重建，状态不保证。

### 工作负载控制器
| 控制器 | 适用场景 | 特点 |
|--------|----------|------|
| **Deployment** | 无状态服务 | 滚动更新、回滚、副本 |
| **StatefulSet** | 有状态（DB/中间件） | 稳定网络标识、有序启停、持久存储 |
| **DaemonSet** | 每节点一个（日志/监控 agent） | 节点级守护 |
| **Job / CronJob** | 批处理 / 定时任务 | 运行完即终止 / 周期执行 |

### 典型 Deployment
```yaml
apiVersion: apps/v1
kind: Deployment
metadata: { name: web }
spec:
  replicas: 3
  selector: { matchLabels: { app: web } }
  template:
    metadata: { labels: { app: web } }
    spec:
      containers:
        - name: web
          image: web:1.0
          ports: [{ containerPort: 8080 }]
          resources:
            requests: { cpu: 100m, memory: 128Mi }
            limits:   { cpu: 500m, memory: 256Mi }
```

### 滚动更新与回滚
```bash
kubectl set image deployment/web web=web:2.0
kubectl rollout status deployment/web
kubectl rollout undo deployment/web
```

## 常见问题
**Q：有状态服务为什么用 StatefulSet？**
A：它提供稳定的 Pod 名称、网络标识和持久卷绑定，适合数据库等。

## 参考资料
- K8s Workloads 官方文档

## See Also
- [[06-Kubernetes核心概念]]
- [[10-存储与配置]]
- [[09-Service与网络]]
- [[13-服务网格ServiceMesh]]
