---
title: Skill 与 Rules / Commands / MCP / Subagent 对比
type: comparison
created: 2026-09-03
updated: 2026-09-03
tags: [AI, Agent, Skill, 选型, 对比]
sources: [cursor.com/docs/skills, cursor.com/docs/context/rules]
---

# Skill 与 Rules / Commands / MCP / Subagent 对比

## 摘要

现代 Agent 有六种扩展手段，容易混：**Rules**（常驻约束）、**Skills**（按需流程包）、**Commands**（显式斜杠命令）、**Subagents**（独立上下文的专职代理）、**MCP**（外部系统连接）、**Prompt**（一次性对话）。核心分界线是：**常驻 vs 按需**、**指令 vs 数据**。

## 正文

### 一图选型

```
你的需求是什么？
│
├─ 是一条简短、必须永远生效的约束？
│     └─ Rules        「新文件一律用 TypeScript」
│
├─ 是多步流程，只在特定任务时需要？
│     └─ Skills       「发布到预发：跑测试 → 构建 → 部署 → 验健康检查」
│
├─ 必须用户显式敲命令才执行，不能自动触发？
│     └─ Commands（或 Skill + disable-model-invocation: true）
│
├─ 任务很重、会污染上下文，想隔离出去？
│     └─ Subagent     「去把这 200 个文件的用法全调研一遍」
│
├─ 需要实时外部数据 / 调外部系统 API？
│     └─ MCP          「查 Jira issue 状态」「读 Notion 文档」
│
└─ 就这一次，以后不会再用？
      └─ 直接对话
```

### 六维对照表

| 维度 | Rules | **Skills** | Commands | Subagent | MCP | Prompt |
|------|-------|-----------|----------|----------|-----|--------|
| **形态** | `.mdc` 单文件 | 目录（SKILL.md + 资源） | `.md` 单文件 | `.md` 单文件 | 独立服务进程 | 对话文本 |
| **加载时机** | 常驻（或 glob 命中） | **按需**（语义匹配） | 显式 `/` 调用 | 被委派时 | 常驻（工具列表） | 一次性 |
| **上下文成本** | 命中即全文，**每次请求** | 未命中仅 ~100 token | 调用时才加载 | **独立上下文**，不污染主会话 | 工具定义常驻 | — |
| **能带脚本？** | ❌ | ✅ | ❌ | ❌ | ✅（服务端） | ❌ |
| **作用域** | 全局/项目/glob | 全局/项目/`paths` | 全局/项目 | 全局/项目 | 全局 | — |
| **可否组合** | 多条并存 | 多个并存 | 一次一个 | 可并行多个 | 多个并存 | — |
| **团队分发** | 进 git | 进 git | 进 git | 进 git | 需部署 | ❌ 丢失 |
| **典型场景** | 编码风格、红线 | 发布流程、评审清单、排障套路 | 快捷动作 | 大规模调研、长任务 | 连 Jira/DB/Notion | 一次性问答 |

### Rules vs Skills（最容易纠结的一对）

Cursor 官方的分法：

| | Rules | Skills |
|---|-------|--------|
| 目的 | 简短的编码指南与约束 | 多步骤工作流与流程 |
| 长度 | 几行 ~ 几百行 | 通常更长，含详细分步说明 |
| 应用方式 | **每次（或匹配的）对话都作为上下文** | 通过 `/skill-name` 或 `@skill-name` **按需调用** |
| 例子 | 「所有新文件均使用 TypeScript」 | 「部署到预发：跑测试、构建、部署、验证」 |

**判断口诀**：
- 能一句话说清 → **Rule**
- 需要分步、含判断分支、要带脚本/模板 → **Skill**

**成本对比**（20 份规范）：

| 方案 | 每次请求固定成本 |
|------|-----------------|
| 20 条 Rules（alwaysApply） | ~10,000 token |
| 20 个 Skills | ~2,000 token |

详见 [[04-渐进式披露机制]]。

### Skill + MCP：厨房与菜谱

Anthropic 官方比喻：

| | MCP（连接） | Skill（知识） |
|---|------------|--------------|
| 提供 | 专业厨房：工具、食材、设备 | 菜谱：做出好菜的步骤 |
| 回答 | **Agent 能做什么** | **Agent 该怎么做** |
| 缺了会怎样 | 连上了 Notion 却不知道下一步干嘛 | 知道流程但拿不到数据 |

最佳实践：**有 MCP 的地方，配一个 Skill 教 Agent 怎么用这个 MCP**。

### Subagent：什么时候该隔离上下文

用 Subagent 的信号：

- 任务会读取大量文件/长文档（调研、代码考古）
- 任务会产出大量中间过程，但主会话只需要结论
- 需要并行跑多个独立任务

Claude Code 里 Skill 还能通过 `context: fork` 直接跑在独立子上下文里——**Skill 和 Subagent 可以叠加**。

### 迁移路径（Cursor）

Cursor 2.4+ 内置 `/migrate-to-skills`，会自动转换：

| 原形态 | 是否迁移 | 说明 |
|--------|---------|------|
| 动态 Rules（`alwaysApply: false` 且无 globs） | ✅ | 转成普通 Skill |
| 斜杠命令（Commands） | ✅ | 转成 Skill + `disable-model-invocation: true`，保留显式调用行为 |
| `alwaysApply: true` 的 Rules | ❌ | 有明确的常驻语义 |
| 带 globs 的 Rules | ❌ | 触发条件与 Skill 不同 |
| 用户级 Rules | ❌ | 不存文件系统 |

详见 [[10-Cursor安装与使用教程]]。

## 相关

- [[01-Skill是什么]]
- [[09-Cursor中的Skill全景]]
- [[05-Skill的作用原理]]
- [[13-速查表与FAQ]]

## 来源

- https://cursor.com/docs/skills（Rules vs Skills 对照表）
- https://cursor.com/docs/skills#migrating-rules-and-commands-to-skills
- Anthropic《The Complete Guide to Building Skill for Claude》（Skills + MCP 一节）
