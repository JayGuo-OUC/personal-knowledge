---
title: 服务网格 Service Mesh
type: concept
created: 2026-08-26
updated: 2026-08-26
tags: [云原生, 服务网格, Istio, Envoy]
---

# 服务网格 Service Mesh

## 学习目标
- 理解服务网格解决什么问题
- 掌握 Sidecar 模式与数据面/控制面
- 了解 Istio 的核心能力与典型场景

## 核心概念

**服务网格（Service Mesh）** 是专门处理**服务间通信**的基础设施层，把流量管理、安全、可观测性从应用代码中剥离出来。

## 详细说明

### 为什么需要
微服务多了之后，每个服务都要自己实现重试、超时、熔断、mTLS、监控——重复且易错。服务网格把这些**横切关注点**下沉到基础设施。

### Sidecar 模式
在每个 Pod 中注入一个**代理容器（Sidecar，如 Envoy）**，所有进出流量都经过它。应用无感知（见 [[08-Pod与工作负载]] 的 Sidecar 概念）。

### 数据面 / 控制面
- **数据面（Data Plane）**：一组 Sidecar 代理，负责实际转发流量、采集指标。
- **控制面（Control Plane）**：集中配置与下发策略（如 Istio 的 istiod）。

### Istio 核心能力
- **流量治理**：金丝雀发布、灰度、故障注入、重试超时。
- **安全**：服务间自动 mTLS、授权策略（见 [[17-云原生安全]]）。
- **可观测性**：自动生成指标、日志、分布式追踪（见 [[14-可观测性]]）。

### 服务网格 vs API 网关
- 网关管**南北向**（外部→集群）入口；
- 网格管**东西向**（服务→服务）内部通信。
两者互补（见 [[12-微服务架构]]）。

## 实践示例
Istio 金丝雀发布（按权重分流）：
```yaml
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
spec:
  http:
    - route:
        - destination: { host: web, subset: v1 }
          weight: 90
        - destination: { host: web, subset: v2 }
          weight: 10
```

## 常见问题
**Q：上服务网格会增加延迟和资源吗？**
A：会（Sidecar 多一跳），但通常换来可观的运维收益；可按需引入。

## 参考资料
- Istio 官方文档 istio.io

## See Also
- [[12-微服务架构]]
- [[14-可观测性]]
- [[17-云原生安全]]
- [[08-Pod与工作负载]]
