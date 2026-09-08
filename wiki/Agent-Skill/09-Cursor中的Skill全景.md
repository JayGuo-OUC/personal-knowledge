---
title: Cursor 中的 Skill 全景
type: entry
created: 2026-09-03
updated: 2026-09-03
tags: [AI, Cursor, Skill, 配置]
sources: [cursor.com/docs/skills, 本机实测 ~/.cursor/skills-cursor/]
---

# Cursor 中的 Skill 全景

## 摘要

Cursor 自 2.x 起原生支持 Agent Skills（开放标准）。技能从 4 个主目录 + 4 个兼容目录加载，支持 `paths`、`disable-model-invocation`、`icon`、`color` 等扩展字段。调用有三种：`/skill-name` 显式调用、`@skill-name` 附加为上下文、模型自动匹配。任何技能都能当 **Custom Mode**（`Alt+Enter`）常驻整个会话。Cursor 还内置了 24 个官方技能。

## 正文

### 加载目录（8 个）

| 目录 | 作用域 | 说明 |
|------|--------|------|
| `.agents/skills/` | 项目级 | 新的跨工具通用约定 |
| `.cursor/skills/` | 项目级 | Cursor 原生 |
| `~/.agents/skills/` | 用户级（全局） | |
| `~/.cursor/skills/` | 用户级（全局） | |
| `.claude/skills/` | 项目级 | **兼容加载**（Claude Code 目录） |
| `.codex/skills/` | 项目级 | **兼容加载**（Codex 目录） |
| `~/.claude/skills/` | 用户级 | **兼容加载** |
| `~/.codex/skills/` | 用户级 | **兼容加载** |

> ⚠️ **重要限制**：Cursor **不会**把你本地的 `~/.cursor/skills/` 同步到 **Cloud Agents、远程 SSH 会话、self-hosted worker**。这些环境里只能用**仓库里的项目级技能**，或把技能打进 worker 镜像。
>
> 推论：**团队规范必须放项目级目录并进 git。**

Windows 实际路径：`C:\Users\<用户名>\.cursor\skills\`

### Cursor 扩展字段

| 字段 | 作用 |
|------|------|
| `paths` | glob 模式限定文件范围，命中才出现。支持列表或逗号分隔字符串 |
| `disable-model-invocation` | `true` = 只能 `/` 显式调用，模型不自动应用（等价于传统斜杠命令） |
| `icon` | Custom Mode 徽章图标：`code`/`terminal`/`bug`/`git-branch`/`book-open`/`beaker`/`shield`/`rocket` 等 |
| `color` | 徽章颜色：`default`/`green`/`cyan`/`blue`/`purple`/`magenta`/`orange`/`yellow`/`red`/`brand` |
| `metadata` | 任意键值 |

`globs` 是遗留字段，仍兼容但新技能请用 `paths`。

### 三种调用方式

| 方式 | 操作 | 效果 |
|------|------|------|
| **显式执行** | 聊天框输入 `/` + 技能名 | Agent 读取并**执行**工作流。技能附加到**这一条消息** |
| **附加上下文** | 输入 `@` + 技能名 | 加载为上下文，**不自动执行** |
| **自动匹配** | 直接描述任务 | Agent 根据 description 自行判断是否应用 |

**Custom Mode**（`Alt+Enter` / Mac `Option+Enter`）：
把技能变成常驻会话的模式，输入框显示徽章。适合「接下来一小时都在做这件事」的场景（如 TDD、迁移）。用 `icon` 和 `color` 定制徽章外观。

### 内置技能（Cursor 官方自带）

本机实测 `~/.cursor/skills-cursor/` 下 24 个：

| 技能 | 作用 |
|------|------|
| `/automate` | 创建 Automations（定时、Slack、GitHub 事件触发） |
| `/autopilot` | 盯 PR，处理反馈、冲突、失败检查 |
| `/canvas` | 创建随对话渲染的交互式 React artifact |
| `/create-hook` | 创建 Cursor hooks 并更新 `hooks.json` |
| `/create-rule` | 创建 Cursor rules |
| `/create-skill` | **创建新技能**（引导式，推荐用它起手） |
| `/create-subagent` | 创建自定义子代理 |
| `/goal` | 目标导向执行 |
| `/loop` | 按间隔重复执行提示词或技能 |
| `/migrate-to-skills` | 把 Rules / Commands 转成 Skills |
| `/new-repo` | 新建仓库脚手架 |
| `/onboard` | 项目上手引导 |
| `/origin` | — |
| `/rename-chat` | 重命名会话 |
| `/review` | 选择并运行合适的代码评审代理 |
| `/review-bugbot` | 用 Bugbot 查 bug 与回归 |
| `/review-security` | 安全漏洞评审 |
| `/sdk` | 用 Cursor SDK 构建应用 |
| `/share` | 分享 |
| `/shell` | 把文本当 shell 命令原样执行 |
| `/split-to-prs` | 把大改动拆成多个小 PR |
| `/statusline` | 配置 CLI 状态栏 |
| `/update-cli-config` | 更新 `~/.cursor/cli-config.json` |
| `/update-cursor-settings` | 更新 Cursor/VS Code 设置 |

> 官方文档还提到 `/cursor-blame`（追查 AI 产出的改动与对应提示词）。

### 嵌套目录与 monorepo

```
.cursor/skills/
├── shipping/                    # 分类目录，纯组织
│   ├── land-it/SKILL.md         # 技能名 = land-it
│   └── careful-merge/SKILL.md
└── debugging/
    └── using-datadog/SKILL.md

apps/web/.cursor/skills/         # 嵌套项目目录
    └── deploy-web/SKILL.md      # 自动只对 apps/web/ 内文件生效
```

- Cursor **递归遍历**技能根目录
- 技能身份 = **包含 SKILL.md 的目录名**，不是上层分类目录
- 嵌套项目目录的技能**自动作用域限定**到该目录，无需设 `paths`

### 团队分发

| 方式 | 操作 |
|------|------|
| **Git（推荐）** | 技能放 `.cursor/skills/` 提交进仓库，队友 clone 即得 |
| **GitHub 远程导入** | 侧边栏 **Customize** → **Rules** → **Add Rule** → **Remote Rule (Github)** → 填仓库 URL |
| **查看已加载技能** | 侧边栏 **Customize** → **Skills** |

从插件或项目安装的技能会与 Rules 一起出现在 **Agent Decides** 区块。

## 相关

- [[10-Cursor安装与使用教程]]
- [[02-Agent-Skills开放标准与生态全景]]
- [[03-SKILL.md结构与frontmatter详解]]
- [[11-实战技能包六件套]]

## 来源

- https://cursor.com/docs/skills
- 本机实测：`C:\Users\郭健\.cursor\skills-cursor\`（`.sync-manifest.json` + 24 个 SKILL.md）
