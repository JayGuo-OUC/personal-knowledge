---
title: Serverless 与 FaaS
type: concept
created: 2026-08-26
updated: 2026-08-26
tags: [云原生, Serverless, FaaS, Knative]
---

# Serverless 与 FaaS

## 学习目标
- 理解 Serverless 的「无服务器」含义
- 掌握 FaaS（函数即服务）模型与冷启动
- 了解 Knative 等云原生 Serverless 方案

## 核心概念

**Serverless（无服务器）** 并非没有服务器，而是**无需关心服务器**：算力按用量计费、自动扩缩（含缩到零）、运维交给平台。

**FaaS（Function as a Service）** 是 Serverless 的典型形态：把代码写成「函数」，由事件触发执行。

## 详细说明

### 与容器的区别
- 容器：你管理长期运行的进程与副本（见 [[03-容器技术基础]]）。
- Serverless：平台在事件到来时才启动实例，空闲缩到零，按执行时长/次数计费。

### 冷启动（Cold Start）
函数首次或长时间未调用时需初始化运行时，引入延迟。缓解：预热、精简依赖、使用常驻方案。

### 事件驱动
函数由事件触发：HTTP 请求、消息队列、对象存储上传、定时器等——天然契合微服务中的异步场景（见 [[12-微服务架构]]）。

### 云原生方案：Knative
Knative 构建在 Kubernetes 之上，提供：
- **Serving**：自动扩缩（含缩到零）、流量切分（蓝绿/金丝雀）。
- **Eventing**：事件路由与投递。
让 Serverless 能力直接跑在自己的 K8s 集群（见 [[06-Kubernetes核心概念]]）。

### 其他
- **OpenFaaS**：把任意容器变成函数。
- 各大云厂商托管 FaaS：AWS Lambda、阿里云函数计算等。

## 实践示例
Knative Service 定义：
```yaml
apiVersion: serving.knative.dev/v1
kind: Service
metadata: { name: hello }
spec:
  template:
    spec:
      containers:
        - image: gcr.io/knative-samples/hello
```

## 常见问题
**Q：长耗时、有状态任务适合 Serverless 吗？**
A：不太适合。Serverless 适合短、无状态、事件触发型负载。

## 参考资料
- CNCF Serverless Whitepaper
- knative.dev

## See Also
- [[03-容器技术基础]]
- [[06-Kubernetes核心概念]]
- [[12-微服务架构]]
