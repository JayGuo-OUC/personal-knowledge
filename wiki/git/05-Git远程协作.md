---
title: Git 远程协作
type: entry
created: 2026-08-26
updated: 2026-08-26
tags: [Git, 远程, 协作]
sources: [https://git-scm.com/book/zh/v2/服务器上的-Git-远程分支]
---

# Git 远程仓库与协作

## 摘要
远程仓库（Remote）是多人共享的同步点。通过 `remote` 配置、`fetch`/`pull`/`push` 在本地与远端之间同步，理解「跟踪分支」是避免 push/pull 冲突的关键。

## 正文

### 配置远端
```bash
git remote add origin <url>   # 关联远端
git remote -v                 # 查看远端地址
git remote set-url origin <new-url> # 改地址
```

### 同步命令
```bash
git fetch origin   # 拉取远端更新到本地（不自动合并）
git pull           # fetch + merge（等价于 git fetch && git merge）
git push -u origin main  # 推送并建立跟踪关系
```

### 跟踪分支
本地 `main` 通常「跟踪」`origin/main`。`git pull` 默认把远端跟踪分支合并进当前分支。`-u`（--set-upstream）首次推送时建立跟踪。

### 两种协作模型
- **共享仓库**：所有人往同一仓库的不同分支推，靠分支权限与 PR/MR 评审。
- **Fork 模型**：fork 出自己的仓库，改完向源仓库提 Pull Request，维护者合并。

### 注意
- 推送前先 `git fetch` 看看远端有没有别人提交，避免「非快进」被拒；用 `git pull --rebase` 可让本地提交变基到远端之后，保持线性历史。

## 相关
- [[04-Git分支模型]]
- [[09-Git工作流与最佳实践]]
- [[06-Git变基与历史改写]]

## 来源
- https://git-scm.com/book/zh/v2/服务器上的-Git-远程分支
