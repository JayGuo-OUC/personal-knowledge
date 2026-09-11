---
title: "17-文档Skill：需求规格 / 概要设计 / 详细设计 / 用户手册"
type: entry
created: 2026-09-10
updated: 2026-09-10
tags: [AI, Agent, Skill, 文档, 需求规格说明书, 概要设计, 详细设计, 用户手册, 技术写作, ADR, Mermaid, skills.sh]
sources: [https://www.skills.sh/, GitHub stargazers_count, 18-通用Skill]

---

# 17-文档Skill：需求规格 / 概要设计 / 详细设计 / 用户手册

## 摘要
围绕「**编写需求规格说明书、概要设计说明书、详细设计说明书、用户使用说明手册**」这四类文档重新梳理的 skill 清单。全部取自 **skills.sh**，门槛 **安装量 ≥1K**，**一个文档方向只保留一个**。共 **7 个主装 skill**，覆盖四大文档 + ADR + 文档配图 + 项目 README。

> 本篇只管**文档编写**；架构/质量/调试/提交规范等通用工程能力见 [[18-通用Skill]]；按语言栈（Java/Vue3）的选型见 [[23-skill主流技术栈]]。

---

## 一、选型原则（本轮三条，含一个反直觉发现）

1. **来源唯一**：skills.sh 检索，取 `installs ≥ 1000`；star 取自 GitHub `stargazers_count`（仓库级）。
2. **一个文档方向一个**：需求规格 / 概要设计 / 详细设计 / 用户手册 / ADR / 配图 / README 各留一个，不叠装。
3. **⚠️ installs 高 ≠ 可信——本轮最重要的发现**：

   | skill | installs | 仓库 star | 判断 |
   |---|---:|---:|---|
   | `warpdotdev/common-skills/write-tech-spec` | 24,793 | ⭐**564** | Warp 终端**厂商预装推送**带来的安装量，非社区验证，**未选** |
   | `riekelt/technical-writer/writing-design-docs` | 5,860 | ⭐**16** | 名字最贴「设计文档写作」，但仓库几乎无人问津，**未选** |
   | `github/awesome-copilot/*` | 7k–26k | ⭐**38,819** | GitHub 官方示例库，文档类成套且可维护，**本清单主力** |

   **结论：文档类优先选 `github/awesome-copilot` 与 `wshobson/agents` 这类高 star 仓库**，installs 容易被厂商预装灌水。

---

## 二、四大文档 × 推荐 skill 对照

| 你要写的文档 | 推荐 skill | 安装量 | Star |
|---|---|---:|---:|
| **需求规格说明书**（SRS） | `create-specification` | 13,397 | ⭐38,819 |
| **概要设计说明书**（架构/模块划分） | `architecture-blueprint-generator` | 11,964 | ⭐38,819 |
| **详细设计说明书**（类/接口/职责） | `create-oo-component-documentation` | 7,022 | ⭐38,819 |
| **用户使用说明手册** | `documentation-writer` | 26,239 | ⭐38,819 |

---

## 三、完整清单（7 个主装 + 3 个配套）

| # | 方向 | skill | 来源仓库 | 安装量 | Star | 用法（触发场景 / 产出什么） |
|---:|---|---|---|---:|---:|---|
| 1 | **需求规格说明书** | `create-specification` | `github/awesome-copilot` | **13,397** | ⭐38,819 | 「写一份 XX 系统的需求规格说明书」→ 输出目标、范围、功能/非功能需求、验收标准、约束。**可先让它生成规格再据此开发**。 |
| 2 | **概要设计说明书** | `architecture-blueprint-generator` | `github/awesome-copilot` | **11,964** | ⭐38,819 | 「出一份概要设计」→ 生成系统架构蓝图：分层、模块划分、技术选型、关键组件关系。对应「概要设计说明书」的架构总览章节。 |
| 3 | **详细设计说明书** | `create-oo-component-documentation` | `github/awesome-copilot` | **7,022** | ⭐38,819 | 「给这个模块写详细设计」→ 输出类的职责、公开接口、依赖关系、协作时序。对应「详细设计说明书」的模块/类设计章节（OO 粒度）。 |
| 4 | **用户使用说明手册** | `documentation-writer` | `github/awesome-copilot` | **26,239** | ⭐38,819 | 「写用户使用手册 / 操作指南」→ 面向最终用户的分步骤说明、截图位、常见问题。本类目 install 量最高的通用文档写作 skill。 |
| 5 | **架构决策记录（ADR）** | `architecture-decision-records` | `wshobson/agents` | **16,372** | ⭐39,535 | 「为什么选 Kafka 而不是 RabbitMQ」→ 生成结构化 ADR（背景/决策/后果）。**设计说明书的"技术选型理由"章节直接可用**。 |
| 6 | **文档配图（架构图/时序图）** | `mermaid-diagrams` | `softaworks/agent-toolkit` | **4,863** | ⭐2,452 | 「画一张架构图/流程图/时序图」→ 输出 Mermaid 代码，可直接贴进 Markdown 文档。设计说明书与手册的**配图刚需**。 |
| 7 | **README / 项目说明** | `create-readme` | `github/awesome-copilot` | **18,165** | ⭐38,819 | 「给这个项目写 README」→ 项目简介、快速开始、目录结构、贡献指南。 |

### 同仓库配套（按需加装，不算方向重复）

均来自 `github/awesome-copilot`（⭐38,819），与主表配套使用：

| skill | 安装量 | 用途 |
|---|---:|---|
| `update-specification` | 9,236 | 需求变更时**增量更新**已生成的规格，避免重写 |
| `create-github-issues-for-unmet-specification-requirements` | 8,975 | 把规格中「未满足的需求」自动转成 issue，需求→任务闭环 |
| `update-oo-component-documentation` | 6,991 | 代码变更后同步更新详细设计文档 |

> 这三件套的价值在于「**文档可维护**」：写文档只是开始，代码变了文档能跟着更新才是关键。

---

## 四、安装命令

`--agent cursor` 为快模式（只给 Cursor 建软链，秒级完成）；全平台版换成 `--agent '*'`（单 skill 约 7 分钟）。

```bash
# 四大文档主力 + README（同一仓库，一次装完）
npx -y skills add github/awesome-copilot \
  --skill create-specification \
  --skill architecture-blueprint-generator \
  --skill create-oo-component-documentation \
  --skill documentation-writer \
  --skill create-readme \
  -y --agent cursor

# ADR + Mermaid 配图
npx -y skills add wshobson/agents --skill architecture-decision-records -y --agent cursor
npx -y skills add softaworks/agent-toolkit --skill mermaid-diagrams -y --agent cursor

# 可选：文档可维护性三件套
npx -y skills add github/awesome-copilot \
  --skill update-specification \
  --skill create-github-issues-for-unmet-specification-requirements \
  --skill update-oo-component-documentation \
  -y --agent cursor
```

> 如遇 GitHub SSL 握手失败：`git config --global url."https://ghproxy.net/https://github.com/".insteadOf "https://github.com/"`，**装完记得 `--unset`**。

---

## 五、实践建议（怎么写得更快）

1. **按顺序串起来**：`create-specification`（需求）→ `architecture-blueprint-generator`（概要）→ `create-oo-component-documentation`（详细）→ `documentation-writer`（用户手册）。前一步的输出直接作为后一步的输入，四份文档天然一致。
2. **配图别手画**：用到架构/流程/时序时先让 `mermaid-diagrams` 出 Mermaid 代码，粘进文档即可渲染。
3. **选型理由用 ADR 承载**：不要把「为什么这么选」塞进设计说明书正文，用 `architecture-decision-records` 单独成文再引用，后续变更也好追溯。
4. **文档写完要能跟着代码走**：加装 `update-specification` / `update-oo-component-documentation`，否则文档三个月就失效。

---

## 相关
- [[18-通用Skill]]（架构/质量/调试/提交规范等通用工程能力，与本篇互补）
- [[16-程序员推荐安装的Skill]]（更早的通用推荐）
- [[23-skill主流技术栈]]（按 Java/Vue3 语言栈的选型）
- [[22-Skill现有技术栈]]（受存量版本约束的选型）

## 来源
- skills.sh 公开检索接口：`https://www.skills.sh/api/search?q=...`（installs，检索于 2026-09-10）
- GitHub `stargazers_count`（star，检索于 2026-09-10；部分取自仓库页面，因 API 配额用尽）
- 检索关键词：`documentation` / `technical writing` / `requirements specification` / `design document` / `user manual` / `api documentation` / `srs` / `mermaid diagram` 等 12 组
