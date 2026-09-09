---
title: Cursor 内置 Skill 一览
type: term
created: 2026-09-08
updated: 2026-09-08
tags: [AI, Cursor, Skill, 内置, 速查]
sources: [cursor.com/docs/skills, 本机实测 C:\Users\lenovo\.cursor\skills-cursor\]
---

# Cursor 内置 Skill 一览

## 摘要

Cursor 自带一批**由官方托管、随客户端自动同步**的内置技能，不需要安装也不能删除。本文合并**本机实测（25 个）**与**官方文档 Built-in 表（19 个）**去重后，给出 **26 个**内置技能的完整清单与作用说明，并实测标注了哪些技能设了 `disable-model-invocation: true`（**只能 `/` 手动调用，模型不会自动用**）。

## 正文

### 数据口径与三个数量

| 来源 | 数量 | 说明 |
|------|------|------|
| 本机 `~/.cursor/skills-cursor/` | **25** | 实测目录；`.sync-manifest.json` 里 25 个**全部**标记为 Cursor 托管，最后同步时间 **2026-09-08 16:10** |
| 官方文档 Built-in Cursor skills 表 | **19** | 官方原文写的是 "a small set"（一小部分），并非全集 |
| 合并去重 | **26** | 官方有而本机未同步 1 个；本机有而官方表未列 7 个 |

- **官方有、本机没有（1 个）**：`/cursor-blame`
- **本机有、官方表未列（7 个）**：`/deploy-with-vercel`、`/goal`、`/new-repo`、`/onboard`、`/origin`、`/rename-chat`、`/share`

> 也就是说：**官方文档那份表是不全的**，想知道自己机器上到底有哪些，直接看 `~/.cursor/skills-cursor/`（Windows：`C:\Users\<用户名>\.cursor\skills-cursor\`）。

### 速查总表（26 个）

「`/` 专用」= 该技能 frontmatter 设了 `disable-model-invocation: true`，**只能手动 `/skill-name` 调用**，模型不会根据对话自动启用。

| 技能 | 作用 | `/` 专用 | 备注 |
|------|------|:--------:|------|
| `/automate` | 创建 Cursor Automations：由定时、Slack 消息、GitHub 事件等触发 | | |
| `/autopilot` | 盯 PR：处理评审意见、解决冲突、修失败检查，循环推进到可合并 | | 见命名漂移说明 |
| `/canvas` | 生成随对话渲染的**交互式 React 面板**（图表、表格、时间线、审计报告等可视化交付） | | 内置里唯一带大量捆绑资源（15 个附加文件） |
| `/create-hook` | 创建 Cursor hooks 并维护 `hooks.json`，在 Agent 生命周期事件前后自动执行 | | |
| `/create-rule` | 创建 Cursor rules：编码标准、项目约定、按文件类型生效的规则（含 `.cursor/rules/`、AGENTS.md） | | |
| `/create-skill` | **创建新 Skill**（引导式）。内置里最详尽的一个，正文 498 行 | | 写技能前先让它引导 |
| `/create-subagent` | 创建自定义子代理：专门角色与委派指令（评审员、调试员、领域助手） | ✅ | |
| `/cursor-blame` | 追查 **AI 产出的改动**以及产生这些改动的提示词 | | **本机未同步**（官方表有） |
| `/deploy-with-vercel` | 把当前仓库关联到 Vercel 项目，并用 Vercel MCP 工具部署 | ✅ | 本机新增，旧版无 |
| `/goal` | 设定一个目标，让 Cursor 自主推进直到完成 | ✅ | |
| `/loop` | 按间隔重复执行提示词或技能，如 `/loop 5m /foo` | | |
| `/migrate-to-skills` | 把「Applied intelligently」规则（`.cursor/rules/*.mdc`）和斜杠命令（`.cursor/commands/*.md`）迁移成 Skill | ✅ | 升级改造用 |
| `/new-repo` | 为当前项目创建 **Cursor 托管的仓库**并推送（项目还没有 git remote 时用） | | |
| `/onboard` | 新用户引导：了解基本偏好 → 选第一个目标 → 指路下一步 | ✅ | |
| `/origin` | 安装 / 登录 / 更新 / 修复 **origin CLI**（Cursor 托管仓库的 git 远端 `origin.cursor.com`） | | |
| `/rename-chat` | 按当前会话焦点重命名会话 | ✅ | 正文最短，仅 7 行 |
| `/review` | 选择并运行**合适的**代码评审子代理（在 Bugbot 与 Security 之间选） | ✅ | |
| `/review-bugbot` | 用 Bugbot 子代理查 bug 与回归 | | |
| `/review-security` | 用 Security Review 子代理查安全漏洞 | | |
| `/sdk` | 用 Cursor SDK 写应用 / 脚本 / CI / 自动化（TS `@cursor/sdk`、Python `cursor-sdk`），支持 `Agent.create` 等 | | 正文 363 行 |
| `/share` | 保存 / 备份 / 分享当前项目到 Cursor，自动建版本化副本（**不懂 git 也能用**） | | |
| `/shell` | 把后面的文本**当 shell 命令原样执行** | ✅ | |
| `/split-to-prs` | 把大改动拆成多个可评审的小 PR | | |
| `/statusline` | 配置 CLI 状态栏（prompt 上方显示会话上下文） | | |
| `/update-cli-config` | 修改 `~/.cursor/cli-config.json`：权限、审批模式、vim 模式、沙箱、显示选项 | | |
| `/update-cursor-settings` | 修改 Cursor / VS Code 的 `settings.json`：主题、字号、tab、保存格式化、快捷键等 | | |

### 按用途分组

| 分类 | 技能 |
|------|------|
| **元技能 / 创建类**（把重复劳动固化下来） | `create-skill`、`create-rule`、`create-hook`、`create-subagent`、`migrate-to-skills`、`onboard` |
| **代码评审** | `review`、`review-bugbot`、`review-security`、`cursor-blame` |
| **PR / 仓库 / 协作** | `autopilot`、`split-to-prs`、`new-repo`、`origin`、`share` |
| **自动化 / 循环** | `automate`、`loop`、`goal` |
| **输出 / 集成** | `canvas`、`sdk`、`shell`、`deploy-with-vercel` |
| **环境与会话配置** | `update-cursor-settings`、`update-cli-config`、`statusline`、`rename-chat` |

### 值得注意的 5 点

1. **8 个技能只能手动 `/` 调用**（实测 `disable-model-invocation: true`）：
   `create-subagent`、`deploy-with-vercel`、`goal`、`migrate-to-skills`、`onboard`、`rename-chat`、`review`、`shell`。
   这些等价于传统斜杠命令——你不喊它，它不会出现。剩下 17 个模型会根据对话自动判断是否启用。
2. **写自己的技能，先让 `/create-skill` 引导**。它的正文 498 行，是内置里最完整的规范说明，比自己照着文档猜字段省事。
3. **`/canvas` 是唯一带大量捆绑资源的内置技能**（15 个附加文件）。它定义了「什么情况下必须出可视化面板」——包括从 MCP 工具（Datadog、Sentry、Linear 等）取到数据时，要求渲染成画布而不是把数据倒进聊天框。这条对做汇报很有用。
4. **内置技能目录是 `~/.cursor/skills-cursor/`（带 `-cursor` 后缀），不是 `~/.cursor/skills/`。**
   ⚠️ **不要往 `skills-cursor/` 里放自己的东西**——它由 Cursor 托管，会随版本同步覆盖。你自己的技能放 `~/.cursor/skills/`（全局）或项目 `.cursor/skills/`（项目级）。
5. **命名漂移**：`/autopilot`（盯 PR）在部分版本的官方文档与镜像里写作 `/babysit`，功能描述完全一致。当前官方文档与本机实测均为 `/autopilot`；如果你客户端里看到的是 `/babysit`，那是同一个技能改了名，不是两个。

### 怎么调用

| 方式 | 操作 | 效果 |
|------|------|------|
| 显式执行 | 聊天框输入 `/` + 技能名 | Agent 读取并**执行**工作流，技能附加到**这一条消息** |
| 附加上下文 | 输入 `@` + 技能名 | 加载为上下文，**不自动执行** |
| 自动匹配 | 直接描述任务 | Agent 按 description 自行判断（**仅限未设 `disable-model-invocation` 的**） |
| 常驻会话 | `Alt+Enter`（Mac `Option+Enter`） | 变 **Custom Mode**，整个会话生效，输入框显示徽章 |

> 三种调用方式与 Custom Mode 的细节见 [[09-Cursor中的Skill全景]]。

## 相关

- [[09-Cursor中的Skill全景]]（加载目录、扩展字段、团队分发）
- [[10-Cursor安装与使用教程]]（装第三方技能 + 排错）
- [[16-程序员推荐安装的Skill]]（本司技术栈该装哪些外置技能）
- [[03-SKILL.md结构与frontmatter详解]]（自己写技能时的字段规范）
- [[02-Agent-Skills开放标准与生态全景]]

## 来源

- 本机实测：`C:\Users\lenovo\.cursor\skills-cursor\`（25 个 SKILL.md，逐个解析 frontmatter 的 `name` / `description` / `disable-model-invocation`；`.sync-manifest.json` 记录 25 个全部为 Cursor 托管，最后同步 2026-09-08 16:10）
- Cursor 官方文档 · Agent Skills：https://cursor.com/docs/skills （Built-in Cursor skills 表，19 项）
