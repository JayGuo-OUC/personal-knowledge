---
title: Git 冲突解决
type: entry
created: 2026-08-26
updated: 2026-08-26
tags: [Git, 冲突]
sources: [https://git-scm.com/book/zh/v2/Git-分支-变基]
---

# Git 冲突解决

## 摘要
当两个分支改了同一文件的同一区域并合并时，Git 无法自动决定取舍，会产生冲突。冲突并不可怕——读懂标记、手动取舍、再提交即可。

## 正文

### 冲突标记
合并后会看到：
```
<<<<<<< HEAD
你的改动
=======
别人的改动
>>>>>>> branch-name
```
- `<<<<<<<` 到 `=======`：当前分支内容
- `=======` 到 `>>>>>>>`：待合并分支内容

### 解决步骤
1. `git status` 看哪些文件冲突（Unmerged）。
2. 打开文件，删除冲突标记，保留正确内容（可两者都要）。
3. `git add <file>` 标记为已解决。
4. `git commit` 完成合并（或 `git merge --continue`）。
5. 中途想放弃：`git merge --abort`。

### 变基中的冲突
`git rebase` 逐个重放提交，遇到冲突会暂停，解决后 `git add` 再 `git rebase --continue`。

### 工具
配置外部合并工具（`git mergetool`）可可视化解决；VS Code 自带三栏冲突编辑器。

## 相关
- [[04-Git分支模型]]
- [[06-Git变基与历史改写]]
- [[09-Git工作流与最佳实践]]

## 来源
- https://git-scm.com/ 2/Git-分支-变基
