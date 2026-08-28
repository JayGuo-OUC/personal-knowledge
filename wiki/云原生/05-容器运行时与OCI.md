---
title: 容器运行时与 OCI
type: concept
created: 2026-08-26
updated: 2026-08-26
tags: [云原生, 容器, OCI, 运行时]
---

# 容器运行时与 OCI 标准

## 学习目标
- 理解 OCI 规范（运行时规范 / 镜像规范）
- 区分低层运行时（runc）与高层运行时（containerd）
- 理解 K8s 中 CRI 的作用

## 核心概念

**OCI（Open Container Initiative）** 制定了两个标准：
1. **Runtime Spec**：容器运行时的行为标准。
2. **Image Spec**：容器镜像的格式标准。
这让不同工具（Docker、Podman、K8s）能互通镜像与运行容器。

## 详细说明

### 运行时分层
- **低层运行时（Low-level）**：如 **runc**，直接调用 Linux 内核创建容器（基于 Namespace/Cgroups）。
- **高层运行时（High-level）**：如 **containerd**、**CRI-O**，负责镜像拉取、存储、管理生命周期，再调用 runc。

### containerd 与 CRI-O
- **containerd**：从 Docker 剥离出的通用运行时，CNCF 毕业项目。
- **CRI-O**：专为 Kubernetes 设计的轻量运行时，直接对接 CRI。

### CRI（Container Runtime Interface）
Kubernetes 通过 **CRI** 与运行时解耦——只要实现 CRI 的运行时（containerd / CRI-O）都能被 K8s 使用，不再强依赖 Docker（见 [[07-Kubernetes架构]]）。

### shim
`containerd-shim` 在运行时与容器之间做桥接，保证运行时进程退出后容器仍存活。

## 实践示例
查看节点使用的运行时：
```bash
kubectl get nodes -o wide   # 或从节点 crictl info 查看
```

## 常见问题
**Q：K8s 弃用 Dockershim 后还能用 Docker 吗？**
A：可以构建镜像（符合 OCI），但 K8s 节点运行时改用 containerd/CRI-O；镜像格式互通，无需改动。

## 参考资料
- OCI 规范 github.com/opencontainers

## See Also
- [[03-容器技术基础]]
- [[04-Docker实战]]
- [[07-Kubernetes架构]]
