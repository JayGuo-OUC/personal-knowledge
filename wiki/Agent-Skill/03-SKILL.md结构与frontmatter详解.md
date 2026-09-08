---
title: SKILL.md 结构与 frontmatter 详解
type: entry
created: 2026-09-03
updated: 2026-09-03
tags: [AI, Agent, Skill, 规范, frontmatter]
sources: [agentskills.io/specification, cursor.com/docs/skills]
---

# SKILL.md 结构与 frontmatter 详解

## 摘要

`SKILL.md` = **YAML frontmatter + Markdown 正文**。开放标准只强制 2 个字段：`name`（≤64 字符，小写+连字符，必须与父目录同名）和 `description`（≤1024 字符，写清「做什么 + 何时用」）。`description` 是**最重要的字段**——它是 Agent 决定要不要加载这个技能的唯一依据。Cursor 额外支持 `paths`、`disable-model-invocation`、`icon`、`color`。

## 正文

### 文件骨架

```
skill-name/                 # 目录名必须与 name 一致
├── SKILL.md                # 必需
├── scripts/                # 可选：可执行代码
├── references/             # 可选：按需读取的文档
└── assets/                 # 可选：模板、图片、数据文件
```

### frontmatter 全表（开放标准）

| 字段 | 必填 | 约束 | 用途 |
|------|------|------|------|
| `name` | ✅ | 1-64 字符；仅 `a-z`、`0-9`、`-`；不以 `-` 开头/结尾；不含连续 `--`；**必须与父目录名一致** | 技能唯一标识 |
| `description` | ✅ | 1-1024 字符；非空；写清做什么 + 何时用；不含 XML 标签 | **触发依据** |
| `license` | ❌ | 短字符串或指向 bundled 许可证文件 | 许可声明 |
| `compatibility` | ❌ | 1-500 字符 | 环境要求（OS、依赖、网络） |
| `metadata` | ❌ | 字符串键值映射 | 自定义元数据（作者、版本…） |
| `allowed-tools` | ❌ | 空格分隔字符串（**实验性**，各端支持不一） | 预授权工具，如 `Bash(git:*) Read` |

### Cursor 扩展字段

| 字段 | 类型 | 作用 |
|------|------|------|
| `paths` | glob 列表或逗号分隔字符串 | 把技能限定到匹配的文件。命中时才出现 |
| `disable-model-invocation` | boolean | `true` = 只能 `/skill-name` 显式调用，模型不会自动应用 |
| `icon` | string | Custom Mode 徽章图标（`code`/`terminal`/`bug`/`git-branch`/`book-open`/`beaker`/`shield`/`rocket`…） |
| `color` | enum | 徽章颜色：`default`/`green`/`cyan`/`blue`/`purple`/`magenta`/`orange`/`yellow`/`red`/`brand` |
| `metadata` | map | 同标准 |

> `globs` 是遗留字段，Cursor 仍兼容，**新技能一律用 `paths`**。

### `name` 命名规则（最容易踩坑）

✅ 合法：`pdf-processing`、`data-analysis`、`code-review`、`my-skill-v2`

❌ 非法：

| 错误示例 | 原因 |
|---------|------|
| `PDF-Processing` | 大写 |
| `-pdf-tool` | 以连字符开头 |
| `pdf-` | 以连字符结尾 |
| `pdf--processing` | 连续连字符 |
| `my skill` | 空格 |
| `my_skill` | 下划线 |

另外 Claude Code 额外保留 `anthropic`、`claude` 两个词不能用作名字。

### `description` 写法（最重要）

这是**唯一在启动阶段就暴露给 Agent 的信息**。写坏了，技能永远不会被触发。

**公式**：`做什么（动词 + 对象）+ 何时用（触发场景关键词）`

✅ 好例子：

```yaml
description: >-
  从 PDF 中提取文本和表格、填写表单、合并多个 PDF。
  当用户提到 PDF、表单、文档抽取，或需要处理 .pdf 文件时使用。
```

❌ 坏例子：`description: 处理 PDF。`

判断标准：
- 能不能从中读出**具体动作**？（"提取/填写/合并" ✅ vs "处理" ❌）
- 有没有**触发关键词**？（PDF、表单、合并 ✅）
- 有没有说清**使用场景**？（用户提到…时使用 ✅）

**测试方法**（Anthropic 官方推荐）：准备一组评测问题，**一半应该触发、一半不应该触发**，看命中率。

### 正文推荐结构

规范对正文**没有格式限制**，但官方推荐这套（实践证明最好用）：

```markdown
## 何时使用（When to Use）
- 触发条件 1
- 触发条件 2

## 步骤（Instructions）
1. ...
2. ...

## 示例（Examples）
输入 → 输出 的完整例子

## 边界（Do NOT / Constraints）
- 明确禁止的事
- 出错时的兜底做法
```

硬性约束：
- **正文控制在 500 行以内**，超了拆到 `references/`
- 引用文件用**相对路径**，且**只深一层**
- 至少给**一个完整的输入/输出示例**

### 完整示例（含可选字段）

```markdown
---
name: pdf-processing
description: >-
  Extract PDF text, fill forms, merge files.
  Use when handling PDFs, forms, or document extraction.
license: Apache-2.0
compatibility: Requires Python 3.11+, pdfplumber, and pikepdf
metadata:
  author: example-org
  version: "1.0"
allowed-tools: Bash(python:*) Read
---

# PDF Processing

## When to Use
- 用户要求提取 PDF 内容
- 需要合并/拆分 PDF

## Quick Start
提取文本：`python scripts/extract.py input.pdf --format text`

合并文件：`python scripts/merge.py a.pdf b.pdf -o out.pdf`

## Detailed Rules
复杂场景见 [references/FORMS.md](references/FORMS.md)

## Do NOT
- 不要用 shell 的 `cat` 去读 PDF（二进制会污染上下文）
- 不要在没有备份的情况下覆盖原文件
```

### 校验

```bash
skills-ref validate ./pdf-processing
```

会检查 frontmatter 合法性与命名规范。CI 里可以跑这个做门禁。

## 相关

- [[04-渐进式披露机制]]
- [[08-如何写出好Skill]]
- [[06-目录结构与捆绑资源]]
- [[13-速查表与FAQ]]

## 来源

- https://agentskills.io/specification
- https://cursor.com/docs/skills#frontmatter-fields
- Anthropic《The Complete Guide to Building Skill for Claude》
