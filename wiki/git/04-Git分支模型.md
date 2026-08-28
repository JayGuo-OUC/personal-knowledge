---
title: Git 分支模型
type: entry
created: 2026-08-26
updated: 2026-08-26
tags: [Git, 分支]
sources: [https://git-scm.com/book/zh/v2/Git-分支-分支简介]
---

# Git 分支与合并

## 摘要
分支是 Git 的杀手锏：创建分支几乎零成本，每个分支就是一个独立开发线。合并分「快进（fast-forward）」与「三方合并（3-way merge）」两种；理解它们能避免大多数协作混乱。

## 正文

### 创建与切换
```bash
git branch dev        # 新建分支
git switch dev        # 切换（推荐，语义清晰）
git switch -c dev     # 新建并切换
# 旧写法：git checkout -b dev
```

### 合并
```bash
git switch main
git merge dev         # 把 dev 合并进当前分支
```
- **快进合并**：main 没有新提交，直接把指针前移，不产生新提交。
- **三方合并**：main 与 dev 各自有新提交，Git 生成一个新的「合并提交」。

### 分支策略
- 一条主分支（main）保持可发布；功能开 `feature/*` 分支；修复用 `hotfix/*`；发布用 `release/*`。
- 合并后通常删除已合并的功能分支，保持分支列表干净。

### 何时用分支
「能当一段补充就并入，是另一个开发线才新开分支」——并行任务、实验、修复都适合分支。

## 相关
- [[03-Git基础命令]]
- [[09-Git工作流与最佳实践]]
- [[08-Git冲突解决]]

## 来源
- https://git-scm.com/book/zh/v2/Git-分支-分支简介
