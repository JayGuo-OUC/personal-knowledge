---
title: Agent Skills 开放标准与生态全景
type: entry
created: 2026-09-03
updated: 2026-09-03
tags: [AI, Agent, Skill, 标准, 生态]
sources: [agentskills.io/specification, github.com/anthropics/skills, github.com/agentskills/agentskills]
---

# Agent Skills 开放标准与生态全景

## 摘要

Agent Skills 是由 Anthropic 发起、现由 `agentskills.io` 维护的**开放标准**，用于给 AI Agent 增加专业能力和可复用工作流。它已被 Claude Code、OpenAI Codex CLI、Gemini CLI、Cursor、VS Code、GitHub Copilot 等 30+ 产品采用。标准本身极简（2 个必填字段），各家在此之上加自己的扩展字段——**这带来「一次编写多处可用」，也带来「跨端行为不完全一致」**。

## 正文

### 标准的来历

- **2025-10**：Anthropic 发布 Agent Skills，最初是 Claude 的能力扩展机制
- **后续**：开放为独立标准，站点 `agentskills.io`，规范页 `/specification`
- **参考实现**：`github.com/agentskills/agentskills`，其中 `skills-ref` 是官方校验器
- **示例库**：`github.com/anthropics/skills`（官方技能仓库）
- **现状**：30+ Agent 产品支持

### 为什么值得关心「是不是开放标准」

因为**技能是可移植资产**：

```
写一次 SKILL.md
   ├── Claude Code (~/.claude/skills/)
   ├── Cursor      (~/.cursor/skills/)
   ├── Codex CLI   (~/.codex/skills/)
   └── 其它支持方
```

更妙的是 **Cursor 会主动兼容加载 Claude / Codex 的目录**（见 [[09-Cursor中的Skill全景]]），所以同一份技能可以跨工具共享，不用复制三份。

### 标准化了什么

| 层面 | 是否标准化 | 说明 |
|------|-----------|------|
| 目录结构 | ✅ | `SKILL.md` 必需；`scripts/`、`references/`、`assets/` 推荐 |
| 文件名 | ✅ | 必须叫 `SKILL.md`（大小写敏感） |
| frontmatter 必填字段 | ✅ | `name`、`description` |
| frontmatter 可选字段 | ✅ | `license`、`compatibility`、`metadata`、`allowed-tools` |
| `name` 命名规则 | ✅ | 1-64 字符，小写字母/数字/连字符，不能以连字符开头结尾，不能有连续连字符，必须与父目录名一致 |
| 正文格式 | ❌ | 完全自由，规范只给推荐章节 |
| 触发机制 | ❌ | 各客户端自己实现 |
| 加载目录 | ❌ | 各客户端自己定（但常见约定已趋同） |

**关键**：格式标准，行为不标准。所以「同一个 Skill 在 Claude Code 和 Cursor 上触发时机可能不同」。

### 各家客户端扩展字段对照

| 字段 | Claude Code | OpenAI Codex | Cursor |
|------|-------------|--------------|--------|
| `paths` / `globs` | — | — | ✅ 文件作用域 |
| `disable-model-invocation` | ✅ | 通过 `agents/openai.yaml` 的 `allow_implicit_invocation` | ✅ 仅 `/` 显式调用 |
| `user-invocable` | ✅ | — | — |
| `argument-hint` | ✅ | — | — |
| `model` | ✅ 指定模型 | — | — |
| `context: fork` | ✅ 独立子上下文 | — | — |
| `agent` | ✅ 指定子代理类型 | — | — |
| `hooks` | ✅ 生命周期钩子 | — | — |
| `icon` / `color` | — | — | ✅ Custom Mode 徽章样式 |
| `allowed-tools` | ✅ | — | 部分支持（实验性） |

> 实践建议：**跨端共享的 Skill 只用标准字段**；客户端特有字段写在单独分支或注释里，避免污染。

### 各家的加载目录

| 客户端 | 项目级 | 用户级（全局） |
|--------|--------|---------------|
| Claude Code | `.claude/skills/` | `~/.claude/skills/` |
| OpenAI Codex | `.codex/skills/` | `~/.codex/skills/` |
| Cursor | `.cursor/skills/`、`.agents/skills/` | `~/.cursor/skills/`、`~/.agents/skills/` |
| 通用（新约定） | `.agents/skills/` | `~/.agents/skills/` |

`.agents/skills/` 是后来出现的**跨工具通用目录**，Cursor 已支持。新项目可以考虑直接用它，一份技能所有工具都能读。

### 生态现状与风险

技能市场正在爆发式增长，同时**供应链安全问题已经很严重**：

- Snyk ToxicSkills 审计 3,984 个技能，**13.4% 含严重问题**，36.82% 至少有一个安全缺陷
- 学术界 Liu et al. 扫了 42,447 个技能，**26.1% 含漏洞**；带 `scripts/` 的技能出问题概率是纯指令型的 **2.12 倍**

详见 [[12-Skill安全与企业合规]]。**结论：标准开放 ≠ 生态可信，企业必须自建白名单。**

### 工具链

```bash
# 校验一个技能是否符合规范
skills-ref validate ./my-skill

# Claude Code 调试加载
claude --debug
```

Cursor 侧可用内置的 `/create-skill` 与 `/migrate-to-skills`，见 [[10-Cursor安装与使用教程]]。

## 相关

- [[01-Skill是什么]]
- [[03-SKILL.md结构与frontmatter详解]]
- [[09-Cursor中的Skill全景]]
- [[12-Skill安全与企业合规]]

## 来源

- https://agentskills.io/specification
- https://github.com/agentskills/agentskills
- https://github.com/anthropics/skills
- https://cursor.com/docs/skills
- Snyk ToxicSkills 研究报告、arXiv 2602.12430
