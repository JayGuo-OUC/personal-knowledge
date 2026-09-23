---
title: Dockerfile 完全指南
type: entry
created: 2026-09-17
updated: 2026-09-17
tags: [Docker, Dockerfile, 镜像构建]
sources: [内部整理, docs.docker.com/engine/reference/builder]
---

# 07 Dockerfile 完全指南

## 摘要

Dockerfile 是**构建镜像的蓝图**——一个文本文件，里面是一条条指令，每条指令生成镜像的一层。本文逐一拆解全部常用指令、`.dockerignore`、多阶段构建，以及生产级镜像的优化与最佳实践。这是 Docker 最核心、最高频的技能。

## 正文

### 1. 基本结构

```dockerfile
# 语法指令（可选，指定 builder 版本）
# syntax=docker/dockerfile:1

FROM python:3.12-slim          # 基础镜像（必须第一条有效指令）
WORKDIR /app                   # 设置工作目录
COPY requirements.txt .        # 复制文件到镜像
RUN pip install -r requirements.txt   # 构建期执行命令（生成新层）
EXPOSE 8000                    # 声明暴露端口（仅文档作用）
ENV APP_ENV=production         # 设置环境变量
CMD ["python", "app.py"]       # 容器启动默认命令
```

构建：

```bash
docker build -t myapp:1.0 .        # 最后的点是「构建上下文」目录
docker build -t myapp:1.0 -f Dockerfile.prod .
```

> **构建上下文**：`docker build` 会把指定目录整个打包发给 Docker 守护进程。所以目录里别放大文件，并用 `.dockerignore` 排除无关内容。

### 2. 全部常用指令详解

| 指令 | 作用 | 要点 |
|------|------|------|
| `FROM <img>` | 指定基础镜像 | 必须是第一条；可用 `FROM scratch` 从零开始 |
| `ARG <k>[=v]` | 构建期变量 | 只在 build 期有效，`--build-arg K=V` 传入 |
| `ENV <k>=<v>` | 环境变量 | 构建期和运行期都生效，可被覆盖 |
| `WORKDIR <path>` | 工作目录 | 不存在则创建；后续指令的相对路径基于此 |
| `COPY [--chown=u:g] <src> <dest>` | 复制文件 | 仅复制本地文件，推荐优先用 |
| `ADD <src> <dest>` | 复制/解压 | 支持 URL 与自动解压 tar；除需解压 tar 外尽量用 COPY |
| `RUN <cmd>` | 构建期执行 | 生成新层；多条用 `&&` 合并减少层数 |
| `CMD` | 容器默认启动命令 | 只能有一个，可被 `docker run` 尾部参数覆盖 |
| `ENTRYPOINT` | 容器入口（不可覆盖） | 与 CMD 配合：ENTRYPOINT 定程序，CMD 定默认参数 |
| `EXPOSE <port>` | 声明端口 | 仅为文档；真正映射靠 `docker run -p` |
| `VOLUME <path>` | 声明挂载点 | 运行时自动挂匿名卷，见 [[09-数据持久化Volume与挂载]] |
| `USER <u>[:g]` | 切换用户 | 生产应**非 root** 运行 |
| `LABEL <k>=<v>` | 元数据 | 如 `LABEL maintainer="dev@x.com"` |
| `HEALTHCHECK` | 健康检查 | 让 Docker 知道容器内应用是否真「活着」 |
| `ONBUILD` | 触发器 | 本镜像被别人 FROM 时才执行（较少用） |
| `SHELL ["exe","param"]` | 指定 shell | Windows 镜像常用 |

### 3. COPY vs ADD

- **优先 COPY**：语义清晰，就是复制本地文件。
- **用 ADD 的场景**：需要自动解压本地 tar 包（`ADD app.tar.gz /opt`）。复制远程 URL 不推荐（无解压、无缓存控制），改用 `RUN curl && tar`。

### 4. RUN 的层优化

```dockerfile
# ❌ 每层分开，层数多、缓存易失效、残留 apt 缓存
RUN apt-get update
RUN apt-get install -y curl
RUN apt-get clean

# ✅ 合并成一条，清掉缓存，层数少体积小
RUN apt-get update \
    && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*
```

### 5. CMD vs ENTRYPOINT（易混）

```dockerfile
# 情形 A：只用 CMD，docker run 可整体覆盖
CMD ["python", "app.py"]
# docker run myimg node server.js  → 用 node 替换

# 情形 B：ENTRYPOINT 固定程序，CMD 当默认参数
ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["python", "app.py"]
# docker run myimg --verbose  → 相当于 docker-entrypoint.sh --verbose
```

> 经验：想让镜像「像个可执行程序、参数可追加」用 ENTRYPOINT+CMD；想让默认命令容易被整体替换用 CMD。

### 6. ARG vs ENV

```dockerfile
ARG VERSION=3.12          # 仅构建期可见
FROM python:${VERSION}    # ARG 在 FROM 前定义，FROM 里可用
ENV APP_HOME=/app         # 运行期也可见，进容器 echo $APP_HOME 有值
```

### 7. 多阶段构建（Multi-stage）—— 关键优化

把「编译」和「运行」分开，最终镜像只含运行所需：

```dockerfile
# ---- 阶段一：构建 ----
FROM golang:1.22 AS builder
WORKDIR /src
COPY . .
RUN CGO_ENABLED=0 go build -o /app/server

# ---- 阶段二：运行（极小）----
FROM gcr.io/distroless/static-debian12   # 无 shell 的最小基础镜像
COPY --from=builder /app/server /server
USER nonroot:nonroot
ENTRYPOINT ["/server"]
```

构建：

```bash
docker build -t mygoapp .   # 自动只用最后阶段，前面阶段被丢弃
```

> 多阶段能把 Go/Java/Rust 等「需要编译工具链」的镜像从 1GB+ 压到几十 MB。**强烈推荐**用于任何编译型语言。

### 8. .dockerignore

放在构建上下文根目录，排除不需要发给守护进程的文件：

```
.git
node_modules
*.log
Dockerfile
.dockerignore
dist
.env
```

> 不写它，`node_modules` 等会被打进上下文，既慢又可能覆盖镜像内正确依赖。

### 9. 构建缓存

Docker 按指令顺序复用缓存层。想让缓存命中率高：

- 先 `COPY` 依赖清单（如 `requirements.txt`/`package.json`）并 `RUN` 安装，**再** `COPY` 源码。
- 这样源码改了不影响依赖层缓存，重装依赖极快。

```dockerfile
COPY package.json package-lock.json ./
RUN npm ci
COPY . .          # 源码变化只使这一层及之后失效
```

### 10. 安全与最小化

- 用 `-slim` / `alpine` / `distroless` 基础镜像。
- 用 `USER` 非 root 运行。
- 加 `HEALTHCHECK`。
- 定期 `docker scan`（或 Trivy）扫漏洞，见 [[14-生产环境最佳实践]]。

### 11. 一个生产级示例（Python）

```dockerfile
FROM python:3.12-slim
WORKDIR /app
ENV PYTHONUNBUFFERED=1 PIP_NO_CACHE_DIR=1
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser
EXPOSE 8000
HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')" || exit 1
CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]
```

## 相关

- [[03-镜像容器仓库核心概念]]
- [[08-构建你的第一个镜像]]
- [[09-数据持久化Volume与挂载]]
- [[14-生产环境最佳实践]]

## 来源

- docs.docker.com/engine/reference/builder/
- 内部整理（多阶段构建、缓存、安全最小化）
