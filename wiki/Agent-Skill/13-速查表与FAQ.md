---
title: Skill 速查表与 FAQ
type: term
created: 2026-09-03
updated: 2026-09-03
tags: [AI, Agent, Skill, 速查, FAQ]
sources: [agentskills.io/specification, cursor.com/docs/skills]
---

# Skill 速查表与 FAQ

> 忘了就翻这篇。完整的原理见 [[05-Skill的作用原理]]，安装见 [[10-Cursor安装与使用教程]]。

## 一、frontmatter 速查

```yaml
---
name: my-skill              # 必填，≤64 字符，小写+数字+连字符，必须与目录名一致
description: 做什么 + 何时用   # 必填，≤1024 字符
license: Proprietary        # 可选
compatibility: 环境要求        # 可选，≤500 字符
metadata:                   # 可选
  author: xxx
  version: "1.0"
allowed-tools: Bash(git:*) Read   # 可选，实验性，空格分隔
paths: "**/*.tsx"           # Cursor 扩展：文件作用域
disable-model-invocation: false   # Cursor 扩展：true = 只能 / 显式调用
icon: shield                # Cursor 扩展：Custom Mode 图标
color: green                # Cursor 扩展：Custom Mode 颜色
---
```

### name 命名合法/非法

| ✅ | ❌ | 原因 |
|----|----|------|
| `pdf-processing` | `PDF-Processing` | 大写 |
| `data-analysis` | `-pdf-tool` | 连字符开头 |
| `code-review` | `pdf-` | 连字符结尾 |
| `my-skill-v2` | `pdf--processing` | 连续连字符 |
| | `my skill` | 空格 |
| | `my_skill` | 下划线 |

### description 写法公式

```
做什么（具体动词 + 对象） + 何时用（触发场景关键词）
```

| ❌ 差 | ✅ 好 |
|-------|-------|
| `处理 PDF。` | `提取 PDF 文本与表格、填写表单、合并文件。当用户提到 PDF、表单、文档抽取时使用。` |
| `帮助代码。` | `按六维清单评审代码并输出留痕报告。当用户要求评审、审查代码，或提交 PR 前使用。` |

## 二、目录速查

| 用途 | 路径 | 作用域 |
|------|------|--------|
| Cursor 项目级 | `.cursor/skills/<name>/SKILL.md` | 项目（**会同步到云端 Agent**） |
| Cursor 全局 | `~/.cursor/skills/<name>/SKILL.md` | 个人机器（**不同步到云端**） |
| 跨工具通用 | `.agents/skills/` 或 `~/.agents/skills/` | — |
| Claude 兼容 | `.claude/skills/`、`~/.claude/skills/` | Cursor 也会加载 |
| Codex 兼容 | `.codex/skills/`、`~/.codex/skills/` | Cursor 也会加载 |

Windows 全局实际路径：`C:\Users\<用户名>\.cursor\skills\`

## 三、目录结构速查

```
skill-name/
├── SKILL.md        # 必需
├── scripts/        # 可执行代码 → 不进上下文，只回传结果
├── references/     # 按需读取的文档 → 拆小、只深一层
└── assets/         # 模板 / 图片 / 数据文件
```

## 四、Cursor 调用方式速查

| 我想… | 操作 |
|-------|------|
| 执行一次 | 输入 `/skill-name` |
| 只加载不执行 | 输入 `@skill-name` |
| 让 AI 判断 | 直接描述任务 |
| 整个会话常驻 | `Alt+Enter`（Mac `Option+Enter`）→ Custom Mode |
| 限定文件类型 | frontmatter 加 `paths` |
| 禁止自动触发 | frontmatter 加 `disable-model-invocation: true` |
| 看已装了哪些 | 侧边栏 Customize → Skills |

## 五、渐进式披露三层

| 层 | 内容 | 时机 | 成本 |
|----|------|------|------|
| L1 | name + description | 启动 | ~100 token/技能 |
| L2 | SKILL.md 正文 | 命中后 | 建议 <5000 token / 500 行 |
| L3 | scripts / references / assets | 按需 | 用到才算 |

## 六、FAQ

**Q1：Skill 和 Rule 到底用哪个？**
一句话能说清的常驻约束 → Rule（「新文件一律用 TypeScript」）。多步流程、要带脚本模板 → Skill（「发布到预发：跑测试→构建→部署→验证」）。详见 [[07-Skill与Rules-Commands-MCP-Subagent对比]]。

**Q2：装了为什么不生效？**
技能在**会话启动时**扫描。开新会话或重启 Cursor。其次检查：文件名是否精确 `SKILL.md`（大小写敏感）、`name` 是否与目录名一致。

**Q3：为什么它从来不自动触发？**
`description` 太空泛。补具体动词和触发场景关键词。先用 `/skill-name` 显式调用验证技能本身没问题。

**Q4：为什么它老在不该出现时出现？**
`description` 关键词太宽泛。收窄描述，或用 `paths` 限定文件范围。

**Q5：加载了但 AI 不照做？**
正文太长（>500 行）导致关键指令被稀释，或指令之间有矛盾。精简正文，检查冲突。

**Q6：能同时用多个 Skill 吗？**
能。规范要求技能设计时**不要假设「只有我一个」**，避免用「总是先执行 X」这类绝对措辞。

**Q7：技能能带脚本吗？安全吗？**
能，放 `scripts/`。脚本**源码不进上下文**，只有执行结果回传——零上下文成本，且每次结果一致。但安全上：带 `scripts/` 的第三方技能出问题概率是纯指令型的 **2.12 倍**，必须逐行审。

**Q8：公司里怎么分发？**
放**项目级** `.cursor/skills/` 并进 git，走 PR 评审。**全局技能不会同步到 Cloud Agents / 远程 SSH / self-hosted worker**，所以团队规范一定要放项目级。

**Q9：能装别人写的技能吗？**
技术上能（GitHub 远程导入）。但生态有真实供应链风险：**13.4% 含严重问题、36.82% 至少有一个缺陷**。强合规团队应建内部仓库 + 白名单，且评审时**看原始文件不看渲染页面**（可能有隐藏 Unicode）。见 [[12-Skill安全与企业合规]]。

**Q10：怎么验证技能写得好不好？**
准备一组评测问题，**一半应该触发、一半不应该**，看两边命中率。只看「该触发的触发了没」会漏掉误触发。

**Q11：SKILL.md 正文有格式要求吗？**
规范**没有**任何格式限制。推荐结构：何时使用 / 步骤 / 示例 / 边界（Do NOT）。硬约束只有三条：<500 行、引用相对路径且只深一层、至少一个完整示例。

**Q12：怎么把已有的 Rules / Commands 转成 Skills？**
Cursor 2.4+ 内置 `/migrate-to-skills`。注意：`alwaysApply: true` 或带 globs 的 Rule **不会**被迁移（触发语义与 Skill 不同）。

## 相关

- [[03-SKILL.md结构与frontmatter详解]]
- [[10-Cursor安装与使用教程]]
- [[05-Skill的作用原理]]
- [[Agent-Skill-index]]

## 来源

- https://agentskills.io/specification
- https://cursor.com/docs/skills
