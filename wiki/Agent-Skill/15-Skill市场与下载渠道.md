---
title: Agent Skills 经典市场与下载渠道
type: entry
created: 2026-09-08
updated: 2026-09-08
tags: [AI, Agent, Skill, 市场, 下载, Cursor, 工程效能]
sources: [skills.sh, agentskills.io, cursor.directory, skillsmp.com, clawhub.ai, smithery.ai, skillkit.io, agentshelf.dev, github.com/VoltAgent/awesome-agent-skills, topaiskills.com]
---

# Agent Skills 经典市场与下载渠道

## 摘要

「Skill 写一次到处跑」已成现实（见 [[02-Agent-Skills开放标准与生态全景]]），但**去哪下载靠谱的经典 Skill** 是另一回事。本文按 2026 年现状列出主流市场，并给出明确结论：**软件开发工程师首选 `skills.sh`（跨端通用、有安装量榜单）；若团队是 Cursor 重度用户（贵司已选定 Cursor），则 `cursor.directory` 最贴合**。

## 正文

### 先分清两类来源

| 类别 | 是什么 | 代表 |
|------|--------|------|
| **规范/标准源** | 定义 `SKILL.md` 格式，保证跨端兼容 | `agentskills.io`（Anthropic 发起的开放标准） |
| **下载/分发市场** | 真正能「下载经典 Skill」的地方 | `skills.sh`、`cursor.directory`、`skillsmp.com` 等 |

> 市场解决「在哪找、怎么装」；标准解决「装完能不能跨端用」。两者配合，见 [[02-Agent-Skills开放标准与生态全景]]。

### 一、跨端通用 Registry（事实标准，优先推荐）

**1. skills.sh（Vercel 官方 Agent Skills Directory）**
- 网址：https://skills.sh
- 定位：生态里最接近「默认 registry」的存在 —— "Discover and install skills for AI agents"
- 特点：**首页按安装量（installs）排排行榜**，能看出哪些技能真在生产环境被用，而非仅 GitHub star；每条技能映射到 GitHub 仓库；安装命令统一
  - `npx skills add <repo>` 装单个仓库
  - `npx skills add <repo> -all -y` 装仓库内全部
- 兼容：Claude Code、Codex、Cursor 等主流 Agent，**一行命令装到对应目录**
- 典型开发类技能：
  - `vercel-react-best-practices`（371K+ 安装）
  - `frontend-design`（368K+）
  - `web-design-guidelines`（296K+）
- 适合：**不想折腾、要「生产验证过」技能的工程师 —— 软件开发者首选**

**2. agentskills.io + `gh skill install`**
- 网址：https://agentskills.io
- 定位：开放标准规范站；同时也是 GitHub CLI `gh skill install`（v2.90+）背后的 registry
- 特点：终端优先，用开发者已有的 `gh` 命令跨 Agent 安装：
  - `gh skill install heygen-com/skills`
- 兼容：Claude Code / Cursor / Codex / Gemini CLI / Copilot / Cline / OpenCode / Warp 等 35+ 工具
- 适合：**终端党、希望「一条命令覆盖所有工具」的工程师**

**3. Anthropic 官方示例库 `github.com/anthropics/skills`**
- 165K+ star，30+ 官方参考技能（PDF 提取、浏览器自动化等）
- 学习格式、研究高质量参考技能的最佳来源；被所有市场镜像

### 二、社区聚合 / 海量市场

| 市场 | 网址 | 特点 | 适合 |
|------|------|------|------|
| **skillsmp.com** | https://www.skillsmp.com | 最大社区市场，**6 万+ 技能、7 种语言**，广度第一 | 想贪全、找冷门 |
| **ClawHub** | https://clawhub.ai | OpenClaw 生态 registry，**5700–10000+ 技能**，向量/语义搜索，`clawhub install` | OpenClaw 用户 |
| **Smithery** | https://smithery.ai | 由 MCP registry 扩展为 skills hub，**100K+ tools/skills** | MCP 工作流用户 |
| **skillkit.io** | https://skillkit.io | "Agent Skills for Cursor"，索引 **2 万+ 技能**，按 popular/recent 排序 | Cursor 用户广撒网 |
| **Agent Shelf** | https://agentshelf.dev | Cursor 可用的 agent/skill 发现 + 安装（含 MCP 服务） | Cursor 用户 |
| **skillstore.io** | https://skillstore.io | 带**安全审计**、中文支持 | 重视安全/中文用户 |
| **skills.rest** | https://skills.rest | 技能分析 + 安全审查 | 下载前先体检 |
| **context7.com** | https://context7.com（Skills 标签页） | 基于 Context7 的技能商店 | 已用 Context7 的团队 |

### 三、Cursor 专项（贴合贵司已选定 Cursor）

> 贵司已确认 Cursor 为公司 AI 辅助编程方案（见 [[09-Cursor中的Skill全景]]），以下两个最贴合日常。

**12. cursor.directory —— Cursor 社区最大的 rules / skills / MCP 聚合站**
- 网址：https://cursor.directory
- 特点：**编码类技能浓度最高**；分 MCP / Rules / Skills 几类，提供预配置模板，**复制即用**
- MCP 专区：https://cursor.directory/mcp（2000+ 为 Cursor 定制的 MCP server）
- 适合：**Cursor 重度用户的日常首选市场**

**13. GitHub Topic 索引（免费、可溯源）**
- `github.com/topics/cursor-skills` —— 各类 Cursor 专用 Skills 仓库
- `github.com/VoltAgent/awesome-agent-skills` —— 500+ 技能，兼容 Cursor，覆盖编码/自动化
- `github.com/alirezarezvani/claude-skills` —— 232+，最大的具体 Claude 技能目录（可兼容加载）

### 安装方式速查（落到实操）

| 方式 | 命令 / 操作 | 适用 |
|------|------------|------|
| 通用一键 | `npx skills add <repo>` | skills.sh 等通用 registry |
| GitHub CLI | `gh skill install <repo>` | agentskills.io 背后 |
| 手动复制 | `git clone` 后拷到 `.cursor/skills/` 或 `.agents/skills/` | Cursor / 跨端 |
| Cursor 专属 | 见 [[10-Cursor安装与使用教程]] | Cursor 项目级分发 |

### 哪个市场适合软件开发工程师（明确结论）

> **首选：`skills.sh`（Vercel Agent Skills Directory）。**
> 三条理由：① 它是跨端事实标准，一份技能 Cursor / Claude Code / Codex 通用；② **安装量排行榜能区分「真在生产用」和「仅 star」**，帮工程师避开玩具技能；③ 一行 `npx skills add` 装好，零配置。开发类技能（React/Next、前端设计、Web 规范）浓度高且实战验证过。
>
> **若团队是 Cursor 重度用户（贵司已选定 Cursor）：`cursor.directory` 是最贴合的社区市场** —— 专为 Cursor 聚合 rules / skills / MCP，编码场景覆盖最密，模板复制即用。
>
> **想贪全 / 找冷门**：`skillsmp.com`（6 万+）或 `ClawHub`（语义搜索）。
>
> 无论选哪个，**下载后先做安全自查**（见 [[12-Skill安全与企业合规]]），企业务必自建白名单。

### 风险提示（呼应 [[02-Agent-Skills开放标准与生态全景]] 与 [[12-Skill安全与企业合规]]）

- **市场 ≠ 可信**：Snyk 审计 3984 个技能，**13.4% 含严重问题**；学术界扫 42447 个，**26.1% 含漏洞**
- 带 `scripts/` 的技能出事概率是纯指令型的 **2.12 倍**
- 企业落地：只从白名单市场下载，进 git 做代码评审（见 [[12-Skill安全与企业合规]]）

## 相关

- [[02-Agent-Skills开放标准与生态全景]]
- [[09-Cursor中的Skill全景]]
- [[10-Cursor安装与使用教程]]
- [[12-Skill安全与企业合规]]
- [[14-学习路线与资源]]

## 来源

- https://skills.sh （Vercel Agent Skills Directory）
- https://agentskills.io （开放标准 + `gh skill install` registry）
- https://github.com/anthropics/skills （Anthropic 官方示例库）
- https://cursor.directory （Cursor 社区规则/Skills/MCP 聚合）
- https://www.skillsmp.com （最大社区市场，6 万+ 技能）
- https://clawhub.ai （OpenClaw 生态 registry）
- https://smithery.ai （MCP → Skills hub）
- https://skillkit.io （Agent Skills for Cursor）
- https://agentshelf.dev （Cursor agent/skill 发现）
- https://github.com/VoltAgent/awesome-agent-skills （awesome 列表）
- https://github.com/topics/cursor-skills （GitHub Topic）
- Top AI Skills Directories in 2026（topaiskills.com 综述）
- Snyk ToxicSkills 报告、arXiv 2602.12430（安全数据，见 [[12-Skill安全与企业合规]]）
