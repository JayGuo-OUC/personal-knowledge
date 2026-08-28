---
title: Git 工作流与最佳实践
type: entry
created: 2026-08-26
updated: 2026-08-26
tags: [Git, 最佳实践]
sources: [https://git-scm.com/book/zh/v2/分布式-Git-分布式工作流程]
---

# Git 工作流与最佳实践

## 摘要
不同团队规模适合不同工作流：GitFlow 适合有发布节奏的软件；GitHub Flow 适合持续部署；Trunk-Based 适合高频集成。配合规范的提交信息和钩子，可大幅提升协作质量。

## 正文

### 常见工作流
- **GitFlow**：main（生产）+ develop（集成分支）+ feature/release/hotfix。结构清晰但偏重，适合有明确版本发布的项目。
- **GitHub Flow**：只有一个 main，一切通过分支 + PR 合并，简单适合 Saas/持续部署。
- **Trunk-Based**：所有人尽量短命分支、频繁合回主干，配套 CI/CD 与特性开关。

### 提交信息规范（Conventional Commits）
```
<type>(<scope>): <subject>
feat: 新增用户登录
fix(auth): 修复 token 过期
```
常见 type：feat / fix / docs / refactor / test / chore。规范提交可自动生成 Changelog。

### 钩子 hooks
`.git/hooks/` 或 Git 客户端钩子可在 commit/push 前自动跑 lint、测试，挡住低级错误。

### 经验要点
- 提交要「小而完整」，一个提交解决一件事。
- 推送到共享分支前，优先用 `git pull --rebase` 保持线性。
- 永远用 `git push --force-with-lease` 替代 `--force`，更安全。

## 相关
- [[04-Git分支模型]]
- [[05-Git远程协作]]
- [[06-Git变基与历史改写]]

## 来源
- https://git-scm.com/book/zh/v2/分布式-Git-分布式工作流程
