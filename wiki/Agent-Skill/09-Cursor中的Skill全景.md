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

Cursor 自 2.x 起原生支持 Agent Skills（开放标准）。技能从 4 个主目录 + 4 个兼容目录加载，支持 `paths`、`disable-model-invocation`、`icon`、`color` 等扩展字段。调用有三种：`/skill-name` 显式调用、`@skill-name` 附加为上下文、模型自动匹配。任何技能都能当 **Custom Mode**（`Alt+Enter`）常驻整个会话。Cursor 还内置了 25 个官方技能（与官方文档 Built-in 表合并去重后 26 个，详见 [[19-cursor内置skill]]）。

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

本机实测 `~/.cursor/skills-cursor/` 下 **25 个**；与官方文档 Built-in 表合并去重后 **26 个**。

**完整清单、逐个作用、以及哪些技能只能 `/` 手动调用 → [[19-cursor内置skill]]。**

本文只保留与「加载目录」相关的两条结论：

- 内置技能落在 **`~/.cursor/skills-cursor/`（注意带 `-cursor` 后缀）**，与上面的 `~/.cursor/skills/` 是**两个不同目录**。前者由 Cursor 托管、随客户端同步覆盖，**不要往里放自己的技能**；你自己的放 `~/.cursor/skills/`（全局）或项目 `.cursor/skills/`。
- 内置技能同样支持 Custom Mode（`Alt+Enter`），可整个会话常驻。

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
- [[19-cursor内置skill]]（内置技能全表与作用）

## 来源

- https://cursor.com/docs/skills
- 本机实测：`~/.cursor/skills-cursor\`（`.sync-manifest.json` + 25 个 SKILL.md，2026-09-08 同步）
