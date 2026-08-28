---
title: CI/CD 与 DevOps
type: concept
created: 2026-08-26
updated: 2026-08-26
tags: [云原生, DevOps, CI/CD, GitOps]
---

# CI/CD 与 DevOps

## 学习目标
- 理解 DevOps 文化与 CI/CD 的关系
- 掌握流水线关键阶段
- 了解 GitOps 与渐进式交付

## 核心概念

**DevOps** 是开发（Dev）与运维（Ops）协作的文化与实践，目标是更快、更可靠地交付。**CI/CD**（持续集成 / 持续交付）是其工程落地手段。它是云原生四大特征之一（见 [[01-云原生概览]]）。

## 详细说明

### CI（持续集成）
开发者频繁合并代码到主干，每次合并自动**构建 + 测试**，尽早暴露问题。

### CD（持续交付 / 部署）
- **持续交付**：保证代码随时可安全发布到生产（手动点发布）。
- **持续部署**：通过流水线自动部署到生产。

### 典型流水线阶段
1. 代码提交触发 → 2. 构建镜像（见 [[04-Docker实战]]）→ 3. 单元测试/扫描（见 [[17-云原生安全]]）→ 4. 部署到 K8s（见 [[06-Kubernetes核心概念]]）→ 5. 验证与健康检查。

### 工具
- **GitHub Actions / GitLab CI / Jenkins / Tekton**：流水线引擎。
- **Argo CD / Flux**：**GitOps** 工具——以 Git 仓库为唯一事实来源，自动把集群状态同步到 Git 声明（见 [[11-控制器与编排原理]] 的调谐思想）。

### 渐进式交付
结合服务网格（见 [[13-服务网格ServiceMesh]]）做金丝雀、蓝绿、滚动发布，降低风险。

## 实践示例
Argo CD 把 Git 中的 manifests 同步到集群：
```bash
argocd app create myapp --repo <git> --path k8s --dest-server https://kubernetes.default.svc
```

## 常见问题
**Q：GitOps 和传统 CI/CD 区别？**
A：GitOps 强调「集群状态由 Git 声明驱动、工具自动调和」，更接近 K8s 声明式哲学。

## 参考资料
- 《Accelerate》DevOps 度量研究
- argoproj.github.io

## See Also
- [[01-云原生概览]]
- [[04-Docker实战]]
- [[06-Kubernetes核心概念]]
- [[13-服务网格ServiceMesh]]
- [[17-云原生安全]]
