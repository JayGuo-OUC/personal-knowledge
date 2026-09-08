---
title: Skill 是什么
type: entry
created: 2026-09-03
updated: 2026-09-03
tags: [AI, Agent, Skill, 概念]
sources: [agentskills.io/specification, resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf]
---

# Skill 是什么

## 摘要

Skill 是**一个文件夹形态的能力包**：核心是一份 `SKILL.md`（YAML frontmatter + Markdown 指令），可附带 `scripts/`、`references/`、`assets/`。它把「你每次对话都要重新交代一遍的流程、规范、领域知识」固化成文件，Agent 启动时只读名字和描述，判断相关时才加载正文。它解决的不是「模型不会做」，而是**「模型有能力但缺上下文」**。

## 正文

### 一句话定义

> Skill = 教 Agent 怎么做某件事的、可版本控制的说明书 + 随附工具包。

官方表述（Anthropic）：

> A skill is a set of instructions — packaged as a simple folder — that teaches Claude how to handle specific tasks or workflows.

### 最小可运行形态

```
my-skill/
└── SKILL.md
```

`SKILL.md` 内容：

```markdown
---
name: my-skill
description: 一句话说清这个技能做什么、什么时候用。
---

# My Skill

## 何时使用
- 用户要求 XXX 时
- 涉及 YYY 文件时

## 步骤
1. ...
2. ...
```

就这么简单。**两个必填字段 + 一段 Markdown**，就构成一个能用的 Skill。

### 它解决的真问题

大模型「有能力但缺上下文」——具体缺四类东西：

| 缺什么        | 例子                                             | Skill 怎么补            |
| ---------- | ---------------------------------------------- | -------------------- |
| **组织私有知识** | 我们发布要走预发环境，且必须跑完契约测试                           | 写进 SKILL.md，Agent 照做 |
| **多步流程**   | 改数据库要：写迁移 → 本地验证 → 灰度 → 观察指标                   | 拆成有序步骤固化             |
| **输出格式规范** | commit message 必须 `<type>(<scope>): <subject>` | 给模板 + 正例反例           |
| **团队红线**   | 禁止把客户数据写进日志                                    | 写进「Do NOT」段          |

这些东西**不可能靠模型预训练得到**，也不可能每次对话手打一遍。

### 三个类比

**① 给新员工的操作手册（SOP）**
Skill 不是让 Agent 变聪明，是让它**按你们公司的方式干活**。就像新人入职拿到的那份《发布流程 v3.2》，照着做就不会出错。

**② 菜谱 vs 厨房（Skill vs MCP）**
Anthropic 官方的比喻：
- **MCP 提供厨房**：灶台、食材、刀具（连接外部系统、实时数据、工具调用能力）
- **Skill 提供菜谱**：先放油还是先放盐、火候多大、什么时候起锅（怎么用这些工具做出好菜）

只有厨房没有菜谱，用户连上了 Notion 却不知道下一步干嘛；只有菜谱没有厨房，巧妇难为无米之炊。

**③ npm 包**
- 可版本化（git 管理）
- 可分发（推到 GitHub，别人装）
- 可评审（改 Skill 要走 PR，跟改 ESLint 配置一样）
- 有供应链风险（装了个恶意包就完蛋 → 见 [[12-Skill安全与企业合规]]）

### Skill 影响 Agent 的四个层面

| 层面 | 影响 | 例子 |
|------|------|------|
| **知识** | 注入模型不知道的领域/组织知识 | 「HiSCADA 的测点命名规范是…」 |
| **流程** | 规定做事的顺序与检查点 | 「先跑测试 → 再构建 → 再部署 → 最后验健康检查」 |
| **工具策略** | 规定该用哪个工具、怎么调 | 「用 `scripts/deploy.sh <env>`，不要自己拼命令」 |
| **边界** | 明确规定不能做什么 | 「禁止把错误信息里的堆栈暴露给前端」 |

注意：**Skill 不改变模型权重，只改变上下文**。它的全部效力来自「被加载进提示词后模型的指令遵循能力」。这点决定了它的能力上限，也决定了它的失效模式（见 [[05-Skill的作用原理]]）。

### 什么值得做成 Skill

满足**任意两条**就该做：

- [ ] 同一件事你已经跟 AI 交代过 ≥3 次
- [ ] 是多步流程（≥3 步），且顺序重要
- [ ] 有团队规范/格式要求，做错了要返工
- [ ] 需要领域知识，AI 不知道就一定会猜错
- [ ] 需要读写特定文件或调用特定命令
- [ ] 希望团队里每个人得到一致的结果

### 什么不该做成 Skill

- **一句话能说清的约束** → 用 Rules（常驻更省事），例：「新文件一律用 TypeScript」
- **需要实时外部数据** → 用 MCP，例：「查一下 Jira 上这个 issue 的状态」
- **一次性任务** → 直接对话，别建文件
- **纯个人信息**（个人偏好、口味）→ 个人习惯放全局目录，别塞项目仓库

判断口诀：**要「常驻」的用规则，要「按需展开」的用技能。**

## 相关

- [[02-Agent-Skills开放标准与生态全景]]
- [[03-SKILL.md结构与frontmatter详解]]
- [[07-Skill与Rules-Commands-MCP-Subagent对比]]
- [[Agent-Skill-index]]

## 来源

- https://agentskills.io/specification
- Anthropic《The Complete Guide to Building Skill for Claude》Chapter 1 Fundamentals
- https://cursor.com/docs/skills
