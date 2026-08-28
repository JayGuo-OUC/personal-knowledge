---
title: Git 核心概念
type: entry
created: 2026-08-26
updated: 2026-08-26
tags: [Git, 概念]
sources: [https://git-scm.com/book/zh/v2/起步-关于版本控制]
---

# Git 核心概念

## 摘要
理解 Git 的关键在于区分四个区域：**工作区、暂存区、本地仓库、远端仓库**，以及三个核心对象：**提交（commit）、树（tree）、Blob**。HEAD 指向当前所在提交。

## 正文

### 四个区域
| 区域 | 英文 | 说明 |
|------|------|------|
| 工作区 | Working Directory | 你实际编辑文件的目录 |
| 暂存区 | Staging / Index | 下一次提交要包含的变更快照（`git add` 后进入） |
| 本地仓库 | Local Repo (.git) | 本地保存的所有提交历史 |
| 远端仓库 | Remote | GitHub / GitLab 等共享仓库 |

### 三个对象（数据模型）
- **Blob**：文件内容（按内容寻址，相同内容只存一份）。
- **Tree**：目录结构，记录文件名与对应 Blob/tree 的指针。
- **Commit**：指向一个 tree + 父提交 + 作者/时间/消息，构成有向无环图（DAG）。

### 快照模型
Git 的「提交」是对整个项目某一时刻的**快照**（实际通过 tree 间接指向各文件 blob），而不是对上一版的差异。连续提交串成历史链，HEAD 是一个指向「当前分支最新提交」的可变指针。

### HEAD 与分支
- `HEAD` 默认指向当前分支（如 `refs/heads/main`），分支又指向某个 commit。
- 切换分支 = 移动 HEAD 到另一分支指针。

## 相关
- [[01-Git概览]]
- [[03-Git基础命令]]
- [[04-Git分支模型]]

## 来源
- https://git-scm.com/book/zh/v 2/起步-关于版本控制
- https://git-scm.com/docs/gitglossary
