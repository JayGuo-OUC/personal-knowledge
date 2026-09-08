---
name: commit-and-pr
description: >-
  生成符合 Conventional Commits 规范的 commit message 与结构化 PR 描述，支持拆分过大的改动。
  当用户要提交代码、写提交信息、开 PR、写变更说明，或说「提交一下 / 写个 commit / 开个 PR」时使用。
license: Proprietary
metadata:
  author: platform-team
  version: "1.0"
---

# 规范化提交与 PR

## 何时使用

- 用户要提交代码、写 commit message
- 要开 PR、写 PR 描述或变更说明
- 改动太大需要拆分成多个提交
- 需要生成 changelog 条目

## 步骤

### 1. 摸清改动

```bash
git status --porcelain
git diff --stat
git diff
git log --oneline -10        # 看看团队的历史风格
```

**先看历史提交风格**——如果团队已有约定，跟随团队，不要硬套规范。

### 2. 判断是否需要拆分

| 信号 | 处理 |
|------|------|
| 改动只做一件事 | 单个提交 |
| 混了「重构 + 新功能 + 修 bug」 | **必须拆** |
| 混了格式化/自动生成的改动 | **必须拆**（单独一个 `chore`/`style` 提交） |
| 单文件超过 300 行改动 | 考虑按逻辑块拆 |

拆分用 `git add -p` 交互式暂存。

### 3. 写 commit message

**格式**：

```
<type>(<scope>): <subject>

<body>

<footer>
```

**type 取值**：

| type | 用途 |
|------|------|
| `feat` | 新功能 |
| `fix` | 修 bug |
| `refactor` | 重构（不改变外部行为） |
| `perf` | 性能优化 |
| `test` | 测试 |
| `docs` | 文档 |
| `style` | 格式（不影响逻辑） |
| `chore` | 构建/工具链/依赖 |
| `revert` | 回滚 |

**subject 规则**：
- 祈使句、现在时（「新增」而非「新增了」「已新增」）
- 不超过 50 字符（中文不超过 25 字）
- 结尾不加句号
- 说清「做了什么」，不说「怎么做的」

**body**：说清**为什么**这么改，而非重复 diff 内容。每行 ≤72 字符。

**footer**：关联 issue、破坏性变更。

**AI 辅助标记**（与 `ai-code-provenance` 配合）：

```
AI-assisted: <模型名> | 提示词: <摘要>
Reviewed-by: <评审人>
```

### 4. 示例

```
feat(user): 新增用户 Excel 批量导入

支持从 Excel 导入用户，逐行校验手机号与身份证格式，
失败行单独收集并在结果页展示，不中断整体导入。

原有手工录入在批量场景下效率过低（参见 #142）。

AI-assisted: cursor-composer | 提示词: 实现用户 Excel 导入并校验手机号格式
Reviewed-by: 张三
Closes #142
```

```
fix(auth): 修复 token 过期后未跳转登录页

拦截器只处理了 401，未处理 403，导致 token 刷新失败后
页面停留在空白状态。

fix(auth): 修复 token 过期后未跳转登录页
```

### 5. 写 PR 描述

固定模板：

```markdown
## 做了什么
<一到三句话说清变更>

## 为什么
<背景 / 需求来源 / 关联 issue>

## 怎么验证的
- [ ] 单元测试：<结果>
- [ ] 手工验证：<步骤与结果>
- [ ] 回归范围：<受影响的模块>

## 风险与影响
| 影响面 | 说明 |
|--------|------|
| 数据库 | 无 / 迁移脚本 xxx |
| 接口 | 无 / 变更说明 |
| 配置 | 无 / 新增配置项 xxx |
| 依赖 | 无 / 新增 xxx |

## AI 辅助情况
- 是否 AI 生成/修改：是 / 否
- 模型：<名称>
- 是否已完成人工评审：是 / 否（评审人：<姓名>）

## 检查清单
- [ ] 自测通过
- [ ] 已补充或更新测试
- [ ] 已跑合规检查（`data-compliance-guard`）
- [ ] 已过代码评审（`code-review-gate`）
- [ ] 无需回滚方案 / 回滚方案：<说明>
```

### 6. 执行提交

```bash
git add <具体文件>            # 不要用 git add .
git commit -F <message-file>  # 或用 -m
```

## 边界（Do NOT）

- **不要用 `git add .`**——会带进临时文件和不该提交的东西
- **不要提交密钥、`.env`、日志文件、构建产物**——提交前跑一次 `data-compliance-guard`
- **不要把多个不相关改动塞进一个提交**
- **不要编造 issue 编号**——没有就留空
- **不要写「修改了一些 bug」这种空话**
- **未跑通的改动不要写「已测试」**
- 提交前确认 `git diff` 里没有调试代码和 `console.log`

## 相关

- `code-review-gate` — 提交前的评审门禁
- `ai-code-provenance` — AI 代码留痕
- `data-compliance-guard` — 提交前的合规扫描
