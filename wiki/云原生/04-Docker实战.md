---
title: Docker 实战
type: tutorial
created: 2026-08-26
updated: 2026-08-26
tags: [云原生, Docker, 实战]
---

# Docker 实战

## 学习目标
- 掌握镜像构建（Dockerfile）
- 熟悉容器生命周期命令
- 会用 Volume 与网络
- 了解 Docker Compose 多容器编排

## 核心概念

**Docker** 是最流行的容器工具集：包含镜像构建、容器运行、仓库分发。核心对象：镜像（Image）、容器（Container）、仓库（Registry）。

## 详细说明

### 关键命令
```bash
docker build -t myapp:1.0 .      # 构建镜像
docker run -d -p 8080:80 myapp:1.0  # 后台运行并映射端口
docker ps                         # 查看运行中的容器
docker logs <id>                 # 查看日志
docker exec -it <id> bash        # 进入容器
docker rm -f <id>                # 删除容器
```

### Dockerfile 示例
```dockerfile
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --omit=dev
COPY . .
EXPOSE 3000
CMD ["node", "server.js"]
```
要点：使用**多阶段构建**减小体积；合理排序指令以利用**构建缓存**。

### 数据卷（Volume）
容器本身是易失的。用 Volume 持久化数据：
```bash
docker run -v mydata:/var/lib/mysql mysql:8
```

### 网络
Docker 提供 bridge / host / none 等网络驱动，容器间可通过自定义 bridge 互通。

### Docker Compose
用 `docker-compose.yml` 编排多个服务：
```yaml
version: "3.8"
services:
  web:
    build: .
    ports: ["8080:3000"]
  redis:
    image: redis:7
```

## 常见问题
**Q：镜像太大怎么办？**
A：用 alpine 基础镜像、多阶段构建、合并 RUN 层、清理缓存。

## 参考资料
- Docker 官方文档 docs.docker.com

## See Also
- [[03-容器技术基础]]
- [[05-容器运行时与OCI]]
- [[08-Pod与工作负载]]
