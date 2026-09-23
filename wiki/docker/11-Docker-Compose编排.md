---
title: Docker Compose 编排
type: entry
created: 2026-09-17
updated: 2026-09-17
tags: [Docker, Compose, 编排]
sources: [内部整理, docs.docker.com/compose]
---

# 11 Docker Compose 编排

## 摘要

当应用由多个容器（web + 数据库 + 缓存）组成，一条条 `docker run` 既繁琐又难复现。Docker Compose 用**一个 `compose.yaml` 文件**声明所有服务、网络、卷，再用几条命令一键启停。本文讲清文件格式、常用命令与关键字段。

## 正文

### 1. 它解决什么问题

没有 Compose 时，起一个「web + mysql + redis」要敲三条 `docker run`，还得手动建网络、挂卷、配环境变量，且无法版本化。Compose 把这些写成声明式 YAML，**可入库、可复现、一条命令拉起**。

### 2. 最小示例

`compose.yaml`：

```yaml
services:
  web:
    image: nginx:1.27
    ports:
      - "8080:80"
    networks: [appnet]

networks:
  appnet:
```

运行：

```bash
docker compose up -d        # 后台启动
docker compose ps           # 看状态
docker compose down         # 停止并移除容器/网络（默认保留卷）
docker compose down -v      # 连卷一起删（数据清空，谨慎）
```

> 注意是 `docker compose`（空格，v2 内置插件），不是旧的 `docker-compose`（横杠，已废弃）。

### 3. 完整字段速查

```yaml
services:
  web:
    build: .                 # 用当前目录 Dockerfile 构建（也可用 build: {context: ., dockerfile: Dockerfile.prod}）
    image: myweb:1.0         # 构建/拉取的镜像名；与 build 同用时作为构建结果名
    container_name: web1
    ports:
      - "8080:80"
    environment:             # 环境变量（列表或 map）
      - TZ=Asia/Shanghai
    env_file:                # 从文件批量注入
      - .env
    volumes:
      - webdata:/usr/share/nginx/html   # 命名卷
      - ./nginx.conf:/etc/nginx/nginx.conf:ro  # 绑定挂载
    networks: [appnet]
    depends_on:              # 启动顺序依赖（仅顺序，不等「就绪」）
      db:
        condition: service_healthy   # 等 db 健康后再起 web
    restart: unless-stopped
    healthcheck:             # 健康检查
      test: ["CMD", "curl", "-f", "http://localhost/health"]
      interval: 30s
      timeout: 5s
      retries: 3
    deploy:                  # 资源限制（compose v2 用，Swarm/部分引擎生效）
      resources:
        limits:
          cpus: "1.0"
          memory: 512M

  db:
    image: postgres:16
    environment:
      POSTGRES_PASSWORD: "123456"
      POSTGRES_DB: appdb
    volumes:
      - dbdata:/var/lib/postgresql/data
    networks: [appnet]
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      retries: 5

volumes:
  webdata:
  dbdata:

networks:
  appnet:
```

### 4. 常用命令大全

```bash
docker compose up -d            # 后台启动全部
docker compose up -d --build    # 强制重新构建镜像后启动
docker compose ps               # 服务状态
docker compose logs web         # 看某服务日志（-f 跟随）
docker compose exec web bash    # 进某服务容器
docker compose stop             # 停止（保留容器）
docker compose start            # 启动
docker compose restart web      # 重启某服务
docker compose down             # 停并删容器/网络
docker compose down -v          # 连命名卷一起删
docker compose config           # 校验并展开最终配置（排错利器）
docker compose pull             # 只拉镜像不启动
```

### 5. 多环境（覆盖文件）

```bash
docker compose -f compose.yaml -f compose.prod.yaml up -d
```

用 `compose.override.yaml`（默认自动合并）区分开发/生产配置。

### 6. depends_on 与「等待就绪」

`depends_on` 只保证**启动顺序**，不保证依赖「已可用」。正确做法：

- 给依赖服务加 `healthcheck`。
- 用 `depends_on: {condition: service_healthy}` 让 Compose 等它健康。
- 或在应用里加重连/重试逻辑（更稳）。

### 7. 变量与 .env

```yaml
environment:
  - POSTGRES_PASSWORD=${DB_PASSWORD}    # 从 .env 读取
```

`.env` 文件：

```
DB_PASSWORD=123456
```

Compose 自动加载同目录 `.env`。

## 相关

- [[09-数据持久化Volume与挂载]]
- [[10-容器网络]]
- [[12-实战全栈应用编排]]
- [[14-生产环境最佳实践]]

## 来源

- docs.docker.com/compose/compose-file/
- 内部整理
