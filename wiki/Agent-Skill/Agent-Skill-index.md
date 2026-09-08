---
title: AI Agent Skill 索引
type: index
created: 2026-09-03
updated: 2026-09-08
tags: [AI, Agent, Skill, Cursor, 工程效能]
sources: [agentskills.io/specification, cursor.com/docs/skills, resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf]
---

# AI Agent Skill 索引（MOC）

> 本主题回答一个问题：**怎么把「我反复交代给 AI 的做法」变成可版本化、可分发、按需加载的团队资产。**
> 篇目按**学习/落地顺序**排列（不是字母序），建议从头读到 10 篇，再跳去实战。

## 篇目

| # | 篇目 | 一句话 | 什么时候读 |
|---|------|--------|-----------|
| 01 | [[01-Skill是什么]] | 一个文件夹 = 一份能力包，解决「模型有能力但缺上下文」 | 第一次接触 |
| 02 | [[02-Agent-Skills开放标准与生态全景]] | Anthropic 发起的开放标准，30+ 产品已支持 | 想确认通用性 |
| 03 | [[03-SKILL.md结构与frontmatter详解]] | frontmatter 只有 2 个必填字段，全表 + 写法公式 | 动手写第一个 |
| 04 | [[04-渐进式披露机制]] | 三层加载：元数据 ~100 token → 正文 → 资源按需 | 想搞懂为什么省钱 |
| 05 | [[05-Skill的作用原理]] | 启动扫描 → 语义路由 → 加载正文 → 读引用/跑脚本 | 想搞懂底层 |
| 06 | [[06-目录结构与捆绑资源]] | scripts / references / assets 怎么组织 | 技能变复杂时 |
| 07 | [[07-Skill与Rules-Commands-MCP-Subagent对比]] | 六种扩展手段选型对照表 | 纠结用哪个 |
| 08 | [[08-如何写出好Skill]] | description 公式、正文骨架、反模式清单 | 写完想优化 |
| 09 | [[09-Cursor中的Skill全景]] | Cursor 特有的目录、内置技能、Custom Mode | 用 Cursor 必读 |
| 10 | [[10-Cursor安装与使用教程]] | 三种安装方式 + 验证 + 排错清单 | 马上要装 |
| 11 | [[11-实战技能包六件套]] | 面向强合规团队的 6 个可直接用的技能 | 要现成的 |
| 12 | [[12-Skill安全与企业合规]] | 供应链攻击实测数据 + 治理框架 | 要在公司推 |
| 13 | [[13-速查表与FAQ]] | frontmatter 全表、命名规则、10 个高频问题 | 忘了就来翻 |
| 14 | [[14-学习路线与资源]] | 分阶段路线 + 官方与社区资源 | 想系统学 |
| 15 | [[15-Skill市场与下载渠道]] | 去哪下载经典 Skill：市场清单 + 开发者首选 | 要装现成技能 |
| 16 | [[16-程序员推荐安装的Skill]] | 装哪些 + 全局/项目级决策：治理类强制项目级进 git | 要配环境 |
| 17 | [[17-文档Skill]] | 写需求规格/概要设计/详细设计的 Skill 清单与触发词 | 要出文档 |
| 18 | [[18-通用Skill]] | 架构/质量/提交规范/合规等通用优质 Skill 总览 | 想配全套 |

## 三句话速览

1. **形态**：一个目录，核心是 `SKILL.md`（YAML frontmatter + Markdown 指令），可带 `scripts/`、`references/`、`assets/`。
2. **机制**：Agent 启动时只加载所有技能的 `name + description`（约 100 token/个）；任务匹配时才读正文；引用的脚本和文档按需再读。这叫**渐进式披露**，是 Skill 相对 Rules 的核心优势。
3. **边界**：Skill **不改变模型权重，只改变上下文**。它提供的是「流程、规范、领域知识、可执行脚本」，不提供「实时数据」——那是 [[07-Skill与Rules-Commands-MCP-Subagent对比]] 里 MCP 的活。

## 配套产物

- 可直接安装的 Cursor 技能包：`skills/cursor-agent-skills/`（6 个技能，见 [[11-实战技能包六件套]]）
- 安装步骤：[[10-Cursor安装与使用教程]]

## 相关

- [[index]]（知识库总索引）
- [[01-Skill是什么]]
- [[10-Cursor安装与使用教程]]
- [[12-Skill安全与企业合规]]
- [[15-Skill市场与下载渠道]]（去哪下载经典 Skill）
- [[16-程序员推荐安装的Skill]]（装哪些 + 全局/项目级）
- [[17-文档Skill]]（写需求/概要/详细设计文档的 Skill）
- [[18-通用Skill]]（架构/质量/提交规范/合规等通用优质 Skill 总览）

## 来源

- Agent Skills 开放标准规范：https://agentskills.io/specification
- Cursor 官方文档 · Agent Skills：https://cursor.com/docs/skills
- Anthropic《The Complete Guide to Building Skill for Claude》PDF
- Anthropic 官方示例库：https://github.com/anthropics/skills
- 参考实现与校验器：https://github.com/agentskills/agentskills
- 本机实测：`~/.cursor/skills-cursor/` 下 Cursor 内置 24 个技能（`automate`/`autopilot`/`canvas`/`create-skill`/`review`/`loop` …）
- 安全实测数据：Snyk ToxicSkills 报告、arXiv 2602.12430（见 [[12-Skill安全与企业合规]]）
