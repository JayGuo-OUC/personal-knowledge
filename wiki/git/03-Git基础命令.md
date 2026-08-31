---
title: Git 基础命令
type: entry
created: 2026-08-26
updated: 2026-08-26
tags: [Git, 命令]
sources: [https://git-scm.com/docs]
---

# Git 基础命令

## 摘要
日常最常用的 Git 命令：`init`/`clone` 初始化，`status` 查看状态，`add` 暂存，`commit` 提交，`log`/`diff` 查看历史与差异。掌握这六组即可完成 80% 的日常操作。

## 正文

### 初始化与获取
```bash
git init          # 把当前目录变成仓库
git clone <url>   # 克隆远端仓库到本地
```

### 查看状态与差异
```bash
git status        # 哪些文件改了、哪些已暂存
git diff          # 工作区 vs 暂存区
git diff --staged # 暂存区 vs 最近提交
git log --oneline # 简洁历史
```

### 暂存与提交
```bash
git add <file>        # 加入暂存区
git add -p           # 交互式：只暂存部分改动（补丁模式）
git commit -m "msg"  # 提交暂存区
git commit -a -m "msg" # 跳过 add，直接提交已跟踪文件的改动
```

### 撤销与恢复
```bash
git restore <file>      # 丢弃工作区改动（未暂存）
git restore --staged <file> # 取消暂存
git rm <file>           # 删除并暂存删除
```

### 实用技巧
- `git status -s` 看精简状态；`git log --graph --oneline` 看分支图。
- 提交前先 `git diff --staged` 确认要提交的内容，避免误提交。

## 相关
- [[02-Git核心概念]]
- [[05-Git远程协作]]
- [[07-Git暂存与忽略]]
- [[11-Git日常流程与命令速查]]

## 来源
- https://git-scm.com/docs
