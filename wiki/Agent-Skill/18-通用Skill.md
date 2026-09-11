---
title: "18-通用Skill：架构 / 质量 / 调试 / 重构 / 提交规范"
type: entry
created: 2026-09-10
updated: 2026-09-10
tags: [AI, Agent, Skill, 通用, 架构, 代码质量, 调试, 重构, 提交规范, 安全评审, skills.sh]
sources: [https://www.skills.sh/, GitHub stargazers_count, 17-文档Skill]

---

# 18-通用Skill：架构 / 质量 / 调试 / 重构 / 提交规范

## 摘要
**不绑定具体语言栈**的通用工程能力清单：架构改进、代码评审、系统化调试、重构、架构模式、提交规范、安全评审。全部取自 **skills.sh**，门槛 **安装量 ≥1K**，**一个方向只保留一个**。共 **7 个主装 skill**。

> 分工：本篇 = **通用工程能力**（任何语言都用得上）；[[17-文档Skill]] = 文档编写；[[23-skill主流技术栈]] = 按 Java / Vue3 具体语言栈的选型。三篇互不重叠，可同时装配。

---

## 一、选型原则

1. **来源唯一**：skills.sh 检索，`installs ≥ 1000`；star 取自 GitHub `stargazers_count`。
2. **一个方向一个**：架构改进 / 代码评审 / 调试 / 重构 / 架构模式 / 提交规范 / 安全评审 各留一个。
3. **警惕 installs 灌水**：本轮再次验证——`microsoft/azure-skills/azure-compliance` installs 高达 569,861，但它是 **Azure 平台绑定**的合规 skill，非通用能力，**未选入主表**。同理 [[17-文档Skill]] 中 `warpdotdev/write-tech-spec`(24,793 installs / 仅 ⭐564) 也是厂商预装灌水。**installs 高只说明装得多，不说明适合你**。

---

## 二、完整清单（7 个主装）

| # | 方向 | skill | 来源仓库 | 安装量 | Star | 用法（触发场景 / 帮你做什么） |
|---:|---|---|---|---:|---:|---|
| 1 | **代码库架构改进** | `improve-codebase-architecture` | `mattpocock/skills` | **901,011** | ⭐257,863 | 「这个模块的架构该怎么理顺」→ 分析现有代码结构，给出分层、依赖、边界的重构方向。**全库安装量最高的 skill**。 |
| 2 | **代码评审** | `code-review` | `mattpocock/skills` | **520,310** | ⭐257,863 | 提交前跑一遍 → 自动找出 bug、安全隐患、性能问题并分级输出。**日常最高性价比的一个**，建议每次 PR 前用。 |
| 3 | **系统化调试** | `systematic-debugging` | `obra/superpowers` | **253,410** | ⭐284,019 | 遇到疑难 bug 时 → 强制走「复现→定位假设→最小化验证→根因→修复」流程，避免瞎猜乱改。**比"帮我看看哪里错了"有效得多**。 |
| 4 | **提交规范** | `git-commit` | `github/awesome-copilot` | **44,591** | ⭐38,819 | 生成 Conventional Commits 规范的提交信息与 PR 描述。同类 `conventional-commit`(16,187) 属同方向，不重复装。 |
| 5 | **架构模式参考** | `architecture-patterns` | `wshobson/agents` | **21,882** | ⭐39,535 | 选型/设计时给出成熟架构模式参考（分层、事件驱动、CQRS、六边形等），用于方案评审与对比。 |
| 6 | **重构** | `refactor` | `github/awesome-copilot` | **21,635** | ⭐38,819 | 「把这个方法/类重构一下」→ 安全地做提取方法、消除重复、简化条件等，并保持行为不变。 |
| 7 | **安全评审** | `security-review` | `affaan-m/ecc` | **16,130** | ⭐255,183 | 上线前安全自查 → 注入、越权、敏感信息泄露、依赖 CVE 等。强合规场景（政府/工业/水务）建议设为**发布门禁**。 |

---

## 三、⚠️ 合规方向：没有适配国内政企的通用 skill

检索到的合规类 skill 全部**绑定特定法规或平台**，与贵司「政府 / 工业 / 水务 + 代码数据不出境」的场景不匹配：

| skill | 安装量 | 为什么不适合 |
|---|---:|---|
| `microsoft/azure-skills/azure-compliance` | 569,861 | 绑定 Azure 云平台 |
| `wshobson/agents/pci-compliance` | 9,320 | 支付卡行业 PCI-DSS |
| `wshobson/agents/accessibility-compliance` | 12,985 | 无障碍访问（前端） |
| `affaan-m/ecc/healthcare-phi-compliance` | 7,426 | 美国医疗 HIPAA |

**建议自建**：贵司真正需要的是「**代码与数据不出境**」的检查（境外 API 调用、敏感数据外传），这在 skills.sh 上没有通用项。自建要点可参考 [[16-程序员推荐安装的Skill]] 中已沉淀的 `data-compliance-guard`（含 `scripts/scan-egress.py` 扫描脚本，支持 `.cn`/内网域名白名单不误报），已安装在 `~/.cursor/skills/`。

---

## 四、安装命令

`--agent cursor` 为快模式（只给 Cursor 建软链，秒级完成）；全平台版换成 `--agent '*'`（单 skill 约 7 分钟）。

```bash
# 架构改进 + 代码评审（同一仓库，一次装完）
npx -y skills add mattpocock/skills --skill improve-codebase-architecture --skill code-review -y --agent cursor

# 系统化调试
npx -y skills add obra/superpowers --skill systematic-debugging -y --agent cursor

# 提交规范 + 重构
npx -y skills add github/awesome-copilot --skill git-commit --skill refactor -y --agent cursor

# 架构模式 + 安全评审
npx -y skills add wshobson/agents --skill architecture-patterns -y --agent cursor
npx -y skills add affaan-m/ecc --skill security-review -y --agent cursor
```

> 如遇 GitHub SSL 握手失败：`git config --global url."https://ghproxy.net/https://github.com/".insteadOf "https://github.com/"`，**装完记得 `--unset`**。

---

## 五、与 17 / 23 篇的装配关系

| 篇目 | 管什么 | 何时用 |
|---|---|---|
| [[18-通用Skill]]（本篇） | 架构改进、评审、调试、重构、提交、安全 | **任何项目都装**，与语言无关 |
| [[17-文档Skill]] | 需求规格 / 概要设计 / 详细设计 / 用户手册 | 要出交付文档时 |
| [[23-skill主流技术栈]] | Java / Spring Cloud / MyBatis / MySQL / Redis / Kafka + Vue3 / TS / Element Plus | 按具体项目语言栈配 |

三篇可叠加，无重复（本篇的 `code-review` 与 23 篇的 `code-review` 是同一个，装一次即可）。

---

## 相关
- [[17-文档Skill]]（文档编写类 skill，与本篇互补）
- [[16-程序员推荐安装的Skill]]（更早的通用推荐，含自建六件套）
- [[23-skill主流技术栈]]（按语言栈的选型）
- [[12-Skill安全与企业合规]]（Skill 供应链安全与治理框架）

## 来源
- skills.sh 公开检索接口：`https://www.skills.sh/api/search?q=...`（installs，检索于 2026-09-10）
- GitHub `stargazers_count`（star，检索于 2026-09-10）
- 检索关键词：`architecture` / `code quality` / `commit convention` / `compliance` / `security review` / `testing strategy` / `refactoring` / `debugging` 等 8 组
