---
title: Docker Hub 与私有仓库
type: entry
created: 2026-09-17
updated: 2026-09-17
tags: [Docker, 仓库, DockerHub, registry]
sources: [内部整理, docs.docker.com/registry]
---

# 13 Docker Hub 与私有仓库

## 摘要

镜像是用来「分发」的。Docker Hub 是默认公共仓库；企业出于合规与速度，常自建私有 Registry。本文覆盖登录/推送/拉取、镜像命名空间、自建 registry，以及镜像安全扫描。

## 正文

### 1. Docker Hub 基础

- 地址：hub.docker.com，默认仓库，无需配置即可 `pull`。
- 镜像全名：`docker.io/用户名/镜像名:标签`；官方镜像省略用户名（如 `nginx` = `library/nginx`）。
- 免费账户可建**公开**仓库；私有仓库数量有限制（免费层通常 1 个，付费扩容）。

### 2. 登录 / 推送 / 拉取

```bash
docker login                      # 交互输入用户名密码（或 docker login -u xxx）
docker login registry.internal:5000   # 登录私有仓库

# 推送前先打标签（标签必须含你的命名空间）
docker tag myapi:1.0 yourname/myapi:1.0
docker push yourname/myapi:1.0

# 拉取
docker pull yourname/myapi:1.0
```

> 推送失败常见原因：没 `docker login`、标签里用户名拼错、仓库设为私有而没权限。

### 3. 镜像标签策略（重要）

- 禁止生产用 `latest`（无法回滚、无法确认版本）。
- 推荐同时打**语义版本**与**git commit 短哈希**：

```bash
docker build -t myapi:1.2.3 -t myapi:$(git rev-parse --short HEAD) .
```

### 4. 自建私有 Registry（极简）

用官方 `registry` 镜像几秒起一个：

```bash
docker run -d -p 5000:5000 --name registry registry:2
# 打标签并推送
docker tag myapi:1.0 localhost:5000/myapi:1.0
docker push localhost:5000/myapi:1.0
# 从另一台机器拉（需配置 insecure-registries 或 HTTPS）
```

> 生产自建仓库需配 **HTTPS + 认证**（如用 Nginx 反代 + 基础认证，或接 Harbor）。`localhost` 的 HTTP 仅适合本机测试。

### 5. Harbor —— 企业级仓库（推荐）

 Harbor 是 CNCF 毕业项目，提供：

- 基于角色的访问控制（RBAC）
- 镜像漏洞扫描（集成 Trivy）
- 镜像签名与策略（不可变标签、过期清理）
- 复制同步、LDAP/SSO 接入

> 公司级容器平台几乎都用 Harbor 而非裸 registry。与上期「代码不出境、数据合规」要求契合——镜像可完全留在内网。

### 6. 镜像安全扫描

```bash
docker scout cves myapi:1.0          # Docker 官方扫描（需登录 Docker 账号）
# 或开源 Trivy
trivy image myapi:1.0
```

> 上线前必须扫漏洞，优先修 `CRITICAL/HIGH`。基础镜像选 `distroless`/`alpine` 可大幅减少受攻击面（见 [[07-Dockerfile完全指南]]、[[14-生产环境最佳实践]]）。

### 7. 镜像瘦身与清理策略

- 定期 `docker image prune -a` 清未用镜像（CI 机器尤其要）。
- 配置仓库的**过期/保留策略**，避免无限堆积。
- 用多阶段构建减小单镜像体积（回看 [[07-Dockerfile完全指南]]）。

## 相关

- [[03-镜像容器仓库核心概念]]
- [[07-Dockerfile完全指南]]
- [[14-生产环境最佳实践]]

## 来源

- docs.docker.com/docker-hub | docs.docker.com/registry
- 内部整理（Harbor、Trivy、镜像策略）
