---
title: 数据持久化（Volume 与挂载）
type: entry
created: 2026-09-17
updated: 2026-09-17
tags: [Docker, 数据卷, Volume, 挂载]
sources: [内部整理, docs.docker.com/storage]
---

# 09 数据持久化（Volume 与挂载）

## 摘要

容器可写层随容器删除而消失，所以**数据库、文件上传、配置**这类要长期保留的数据，必须存到容器之外。Docker 提供三种方式：数据卷（Volume，推荐）、绑定挂载（Bind mount）、tmpfs。本文讲清三者区别与用法。

## 正文

### 1. 为什么需要持久化

回看 [[03-镜像容器仓库核心概念]]：容器的改动只写在「可写层」，容器一删就没。数据库数据、用户上传文件如果写在容器里，重启/升级就丢失。**持久化 = 把数据挂到容器外的宿主存储**。

### 2. 三种存储方式对比

| 方式 | 位置 | 管理方 | 典型用途 |
|------|------|--------|---------|
| **Volume（数据卷）** | Docker 管理的宿主目录（如 `/var/lib/docker/volumes/`） | Docker | 数据库数据、需持久的应用数据（**首选**） |
| **Bind mount（绑定挂载）** | 你指定的宿主任意路径 | 你 | 挂载源码实时调试、挂载配置文件 |
| **tmpfs** | 仅内存 | — | 敏感临时数据，重启即失 |

### 3. Volume（数据卷，推荐）

```bash
# 创建命名卷
docker volume create pgdata

# 挂载到容器
docker run -d --name pg -e POSTGRES_PASSWORD=123 -v pgdata:/var/lib/postgresql/data postgres:16

# 查看卷
docker volume ls
docker volume inspect pgdata     # 看实际宿主路径、挂载点

# 删除卷（容器用了会先报错，需 -f 或先删容器）
docker volume rm pgdata
docker volume prune              # 删所有未被使用的卷（谨慎）
```

> 用 `-v 卷名:容器路径` 时若卷不存在，Docker 会**自动创建**。数据在卷里，容器删了卷还在，升级只要再挂同一个卷即可。

### 4. Bind mount（绑定挂载）

```bash
# 把宿主当前目录挂进容器（开发热更新常用）
docker run -d -p 3000:3000 -v "$(pwd)":/app -w /app node:20-alpine npm start

# 挂载单个配置文件
docker run -d -v /opt/app/nginx.conf:/etc/nginx/nginx.conf:ro nginx:1.27
# :ro 表示容器内只读，防止被改
```

> 开发时挂源码可实现「改代码容器立刻生效」（配合 nodemon 等）。**生产配置也常用只读绑定挂载**。

### 5. tmpfs（仅内存）

```bash
docker run -d --tmpfs /tmpcache redis:7
# 数据只存内存，容器停即失，适合密钥/临时缓存
```

### 6. 只读挂载与多卷

```bash
# 应用代码只读，数据目录可写
docker run -d \
  -v appcode:/app:ro \
  -v appdata:/data \
  myapp:1.0
```

### 7. 数据卷容器模式（老用法，了解即可）

早期用「专门的数据卷容器」共享数据，现在多用 **命名卷 + Docker Compose** 或直接 `docker volume`，见 [[11-Docker-Compose编排]]。

### 8. 备份与迁移 Volume

```bash
# 把卷数据打包成 tar（用一个临时容器挂载卷）
docker run --rm -v pgdata:/data -v $(pwd):/backup alpine \
  tar czf /backup/pgdata.tar.gz -C /data .

# 恢复
docker run --rm -v pgdata:/data -v $(pwd):/backup alpine \
  tar xzf /backup/pgdata.tar.gz -C /data
```

### 9. 选择决策

- 数据库/要持久的数据 → **Volume**。
- 开发挂源码、挂配置文件 → **Bind mount**（只读挂配置更安全）。
- 临时敏感数据 → **tmpfs**。
- 永远别把「要长期保留的数据」只写在容器可写层。

## 相关

- [[03-镜像容器仓库核心概念]]
- [[05-容器生命周期管理]]
- [[10-容器网络]]
- [[11-Docker-Compose编排]]

## 来源

- docs.docker.com/storage/volumes | bind-mounts | tmpfs
- 内部整理
