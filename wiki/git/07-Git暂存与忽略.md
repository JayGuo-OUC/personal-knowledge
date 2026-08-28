---
title: Git 暂存、忽略与清理
type: entry
created: 2026-08-26
updated: 2026-08-26
tags: [Git, 工作流]
sources: [https://git-scm.com/docs/git-stash, https://git-scm.com/docs/gitignore]
---

# Git 暂存与忽略

## 摘要
`stash` 临时保存未完成的改动以便切换上下文；`.gitignore` 声明永不跟踪的文件（依赖、构建产物、密钥）；二者共同保持仓库整洁。

## 正文

### 暂存 stash
```bash
git stash           # 把未提交改动藏起来
git stash pop       # 恢复并删除最近的 stash
git stash list      # 查看所有 stash
git stash -u        # 连同未跟踪文件一起藏
```
适合「临时切去修 bug，回来再继续」的场景。

### 忽略 .gitignore
```
# 忽略规则示例
node_modules/
*.log
.env
/dist
```
- 已被跟踪的文件不会因写入 .gitignore 而停止跟踪，需用 `git rm --cached <file>` 移除跟踪。
- 全局忽略：`git config --global core.excludesfile ~/.gitignore_global`。

### 清理
```bash
git clean -n   # 预览将删除的未跟踪文件（dry-run，安全）
git clean -f   # 删除未跟踪文件（谨慎）
```

## 相关
- [[03-Git基础命令]]
- [[09-Git工作流与最佳实践]]

## 来源
- https://git-scm.com/docs/git-stash
- https://git-scm.com/docs/gitignore
