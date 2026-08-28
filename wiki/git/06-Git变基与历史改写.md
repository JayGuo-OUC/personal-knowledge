---
title: Git 变基与历史改写
type: entry
created: 2026-08-26
updated: 2026-08-26
tags: [Git, 进阶]
sources: [https://git-scm.com/book/zh/v2/Git-工具-重写历史]
---

# Git 变基与历史改写

## 摘要
`rebase`、`cherry-pick`、`reset`、`revert`、`commit --amend` 都能改写历史。核心原则：**不要改写已经推送到共享分支的提交**，否则会打乱他人基于它的工作。

## 正文

### 变基 rebase
```bash
git rebase main      # 把当前分支的提交「重放」到 main 之后，得到线性历史
git rebase -i HEAD~3 # 交互式：合并/改写/删除最近 3 个提交
```
变基 = 改变提交的根基（父提交），使历史更线性、易读。合并保留分叉，变基抹平分叉。

### 拣选 cherry-pick
```bash
git cherry-pick <commit-id> # 把某个提交「复制」到当前分支
```

### 重置 reset（针对未推送的本地历史）
```bash
git reset --soft HEAD~1   # 撤销提交，保留改动在暂存区
git reset --mixed HEAD~1  # 撤销提交，改动回到工作区（默认）
git reset --hard HEAD~1   # 彻底丢弃（危险，不可逆）
```

### 反做 revert（针对已推送）
```bash
git revert <commit-id> # 生成一个新的「反向」提交，安全抵消历史变更
```

### 修改最近提交
```bash
git commit --amend -m "新信息" # 改写最近一次提交（含补充提交）
```

## 相关
- [[04-Git分支模型]]
- [[08-Git冲突解决]]
- [[05-Git远程协作]]

## 来源
- https://git-scm.com/book/zh/v2/Git-工具-重写历史
