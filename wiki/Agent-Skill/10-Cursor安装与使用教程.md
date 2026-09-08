---
title: Cursor 安装与使用教程
type: entry
created: 2026-09-03
updated: 2026-09-03
tags: [AI, Cursor, Skill, 教程]
sources: [cursor.com/docs/skills, 本机实测]
---

# Cursor 安装与使用教程

## 摘要

Cursor 装 Skill 有三种方式：① 聊天框敲 `/create-skill` 引导式创建（最快）；② 手动在 `.cursor/skills/<技能名>/SKILL.md` 建文件（可控、可进 git）；③ 从 GitHub 仓库导入（装别人的）。**项目级放仓库、全局级放家目录**；团队规范必须走项目级，因为全局技能不会同步到云端/远程 Agent。装完开新会话验证。

## 正文

### 前置条件

| 项 | 要求 |
|----|------|
| Cursor 版本 | **2.4+**（`/migrate-to-skills` 需要 2.4+；Skills 原生支持自 2.x 起） |
| 目录 | 技能名必须小写 + 连字符，且与 `name` 字段一致 |
| 文件名 | **必须是 `SKILL.md`**（大小写敏感） |

### 方式一：`/create-skill` 引导式创建（推荐新手）

1. `Ctrl + L` 打开 Agent 聊天
2. 输入 `/create-skill` 回车
3. 按引导回答：
   - 技能用途与范围
   - 存放位置（个人 `~/.cursor/skills/` 还是项目 `.cursor/skills/`）
   - 触发场景
   - 输出格式要求
4. Agent 生成文件，你**审阅后保存**

> 提示：如果你手上有现成的 Rule 想转 Skill，直接说「把 @my-rule 转成 skill」。

### 方式二：手动创建（推荐团队用，可控且可评审）

**Windows PowerShell**（项目级）：

```powershell
# 进入你的项目根目录
cd E:\your-project

# 建目录（一个技能一个目录）
New-Item -ItemType Directory -Force -Path .cursor\skills\code-review-gate
New-Item -ItemType File -Path .cursor\skills\code-review-gate\SKILL.md
```

**Windows PowerShell**（全局级）：

```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.cursor\skills\code-review-gate"
New-Item -ItemType File -Path "$env:USERPROFILE\.cursor\skills\code-review-gate\SKILL.md"
```

对应路径即 `C:\Users\<用户名>\.cursor\skills\code-review-gate\SKILL.md`。

**Git Bash / macOS / Linux**：

```bash
mkdir -p .cursor/skills/code-review-gate
touch .cursor/skills/code-review-gate/SKILL.md
```

然后写入内容（模板见 [[03-SKILL.md结构与frontmatter详解]]）。

### 方式三：从 GitHub 导入（装别人的技能）

1. 侧边栏打开 **Customize**
2. 切到 **Rules** 标签
3. 点 **Add Rule**
4. 选 **Remote Rule (Github)**
5. 填仓库 URL

> ⚠️ **强合规团队注意**：社区技能有真实供应链风险，**13.4% 含严重问题**。导入前必须人工读原始 `SKILL.md` 与 `scripts/`，见 [[12-Skill安全与企业合规]]。

### 项目级 vs 全局级：怎么选

| 放哪 | 路径 | 适用场景 | 是否同步到云端/远程 Agent |
|------|------|---------|------------------------|
| **项目级** | `.cursor/skills/` | 团队规范、项目特有流程、发布流程 | ✅（在仓库里） |
| **全局级** | `~/.cursor/skills/` | 个人习惯、跨项目通用工具 | ❌ **不同步** |

**决策规则**：

- 团队的 → **项目级 + 进 git**
- 个人的 → 全局级
- 要上 Cloud Agent / 远程 SSH / self-hosted worker 的 → **必须项目级**

### 批量安装（复制整套技能包）

如果你有一份已写好的技能包目录（比如本库的 `skills/cursor-agent-skills/`），直接整体复制：

```powershell
# 安装到全局（个人机器上所有项目可用）
Copy-Item -Recurse -Force "E:\999知识库\skills\cursor-agent-skills\*" "$env:USERPROFILE\.cursor\skills\"

# 或安装到某个项目（团队共享，随后 git add / commit / push）
Copy-Item -Recurse -Force "E:\999知识库\skills\cursor-agent-skills\*" "E:\your-project\.cursor\skills\"
```

### 验证三招

**① 看列表**
侧边栏 **Customize** → **Skills**，应能看到刚装的技能。

**② 显式调用**
`Ctrl + L` → 输入 `/` → 应能搜到技能名 → 选中执行。

**③ 直接问 Agent**（最可靠）

> 你现在有哪些可用的 skill？把每个的 name 和 description 原样列出来。

列得出来 = 确实加载了。

### 使用方式速查

| 我想… | 操作 |
|-------|------|
| 执行一次工作流 | `/skill-name` |
| 只加载不执行 | `@skill-name` |
| 让 AI 自己判断 | 直接描述任务 |
| 整个会话都用它 | `Alt+Enter`（Mac `Option+Enter`）变 Custom Mode |
| 限定只对某些文件生效 | frontmatter 加 `paths: "**/*.tsx"` |
| 禁止自动触发 | frontmatter 加 `disable-model-invocation: true` |

### 迁移存量 Rules / Commands

Cursor 2.4+ 内置 `/migrate-to-skills`：

1. 聊天框输入 `/migrate-to-skills`
2. Agent 自动识别可迁移项并转换
3. **人工审阅** `.cursor/skills/` 下生成的技能

| 原形态 | 是否迁移 |
|--------|---------|
| 动态 Rules（`alwaysApply: false` 且无 globs） | ✅ |
| 斜杠命令（Commands） | ✅ → 带 `disable-model-invocation: true` |
| `alwaysApply: true` 的 Rules | ❌ |
| 带 globs 的 Rules | ❌ |
| 用户级 Rules | ❌（不在文件系统） |

### 排错清单

| 症状 | 原因 | 解法 |
|------|------|------|
| 技能列表里看不到 | 技能在**会话启动时**扫描 | **开新会话**或重启 Cursor |
| 文件名不对 | 必须精确 `SKILL.md` | 检查大小写 |
| `name` 与目录名不一致 | 规范要求一致 | 改一致 |
| `name` 含大写/下划线/空格 | 命名规则 | 只留小写字母、数字、连字符 |
| 从不自动触发 | description 太空泛 | 补具体动词 + 触发场景 |
| 只在特定文件才出现 | 设了 `paths` 或放在嵌套目录 | 预期行为；不需要就删掉 |
| 加载了但不照做 | 正文太长被稀释，或指令矛盾 | 精简到 500 行内 |
| 脚本执行失败 | 依赖缺失/路径写死/权限 | 脚本加依赖说明，用相对路径 |
| 云端 Agent 里没有 | 全局技能不同步 | 改放项目级并进 git |
| 改了没生效 | 缓存 | 开新会话 |

### 团队落地建议（强合规场景）

1. **建内部 Git 仓库**专放技能（如 `dev-skills`），禁止从外部市场直接装
2. **项目级** `.cursor/skills/` 进主仓库，随代码一起评审
3. **改技能走 PR**，与改 ESLint 配置同等对待
4. **CI 加校验**：`skills-ref validate ./skill-dir`
5. **建技能清单**（SBOM）：名称、来源、负责人、最近评审日期
6. **新人入职**：`/onboard` 或直接把技能仓库 clone 下来

## 相关

- [[09-Cursor中的Skill全景]]
- [[11-实战技能包六件套]]
- [[12-Skill安全与企业合规]]
- [[13-速查表与FAQ]]

## 来源

- https://cursor.com/docs/skills
- https://cursor.com/docs/skills#installing-skills-from-github
- 本机环境实测（Windows，`C:\Users\郭健\.cursor\`）
