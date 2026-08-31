---
title: 云原生知识库 · 操作日志
type: synthesis
created: 2026-08-26
updated: 2026-08-27
tags: [云原生, 日志]
---

# 操作日志（Log）

append-only  chronological record。可用 `grep "^## \[" log.md` 快速检索。

## [2026-08-26] init | 初始化云原生知识库
创建 Vault 结构（WIKI-SCHEMA、README、raw/、wiki/），并一次性写入 19 篇教程笔记：
概览、CNCF 全景、容器基础、Docker、运行时/OCI、K8s 核心/架构/工作负载/网络/存储/控制器、
微服务、服务网格、可观测性、CI/CD、Serverless、安全、最佳实践、学习路线。建立交叉引用与目录索引。

## [2026-08-26] restructure | 改造为自生长知识库
将仓库重构为 raw / mine(未定稿·已定稿·AI辅助生成) / wiki / output / skills , 大类（参考 Karpathy LLM-Wiki 方法论）。
- 云原生 19 篇并入根目录 `wiki/云原生`，旧 `云原生/` 文件夹清空移除。
- 新建 `wiki/index.md`（总索引）与 `wiki/云原生/云原生-index.md`（主题索引）。
- 编写根 `CLAUDE.md`：目录结构、wiki 标准格式、新开vs并入、链接/占位页规则、mine 风格边界、问答模式、skills 沉淀条件、每日/每周任务。
- 沉淀首个技能 `skills/主题知识库搭建.md` 并建 `skills/README.md` 索引。
- 跑首次体检与示例问答，产出 `output/体检报告-2026-08-26.md` 与 `output/问答-容器与虚拟机区别-2026-08-26.md`。

## [2026-08-26] add | 新增 Git 主题知识库
在 `wiki/git/` 下新建 Git 主题，按 CLAUDE.md 标准格式写入 10 篇条目 + 主题索引 `git-index.md`：
概览、核心概念、基础命令、分支模型、远程协作、变基与历史改写、暂存与忽略、冲突解决、工作流与最佳实践、学习路线与资源。
建立交叉引用（双链）与总索引联动（`wiki/index.md` 新增 Git 主题，条目数 19 → 29）。

## [2026-08-27] fix | 修复 Git 主题双链格式
用户确认 Obsidian 未启用标题/.basename 匹配，原 `[[Git概览]]` 等写法无法定位带序号文件 `01-Git概览.md`，导致 10 条 Git 链接悬空。
将 `wiki/git/` 下全部 11 篇（10 条目 + `git-index` 索引）中的双链改写为带序号（或 git-index）格式：
`[[Git概览]]→[[01-Git概览]]`、`[[Git核心概念]]→[[02-Git核心概念]]` … `[[Git学习路线与资源]]→[[10-学习路线与资源]]`、`[[Git主题索引]]→[[git-index]]`。
全库链接校验：无孤儿页；Git 断链已全部消除。
遗留：`[[CLAUDE]]` 指向 vault 根目录 `CLAUDE.md`（规则文件），若 Obsidian vault 范围含根目录则有效，否则需在插件/设置中确认索引范围。

## [2026-08-31] add | 新增 Git 日常流程与命令速查
用户需要在 `wiki/git/` 下新增一份「按流程组织的日常操作手册」。新建 `11-Git日常流程与命令速查.md`（type: term）：
七条铁律 → 晨间同步 → 开分支 → 小步提交 → 提交前自检 → Conventional Commits → 追平主干(rebase) →
整理本地历史(amend/rebase -i) → 推送提 PR → 评审后修改(fixup) → 合入后清理 → 冲突处理 → 事故救急
(错分支/撤销/已推送回滚/reflog/误删分支/stash) + 撤销矩阵 + 命令速查表 + 全局配置与别名 +
AI 辅助编程场景下的提交纪律。
联动更新：`git-index.md`（新增条目、条目数 10→11）、`wiki/index.md`（Git 10→11 篇、总条目 29→30）、
`03-Git基础命令.md` 与 `09-Git工作流与最佳实践.md` 补反向双链。

## [2026-08-31] expand | 补充 Git 速查的分支位置标注与 rebase 详解
用户反馈「不够详细、看不出 rebase 时本地在哪个分支」。重写 `11-Git日常流程与命令速查.md`：
- 新增第〇节「我现在到底在哪个分支」：`git status` 首行四种状态表（正常 / 游离 HEAD / rebase 进行中 / merge 冲突中），明确 rebase 期间 `branch --show-current` 返回空。
- 新增第一节「rebase 到底在干什么」：before/after 提交图、Git 内部五步（找 merge-base → 摘补丁 → 游离 HEAD 落新基点 → 重放 → 分支指针搬家）、三方关系表（当前分支 / upstream / 被重放提交 / 不被改动的 upstream）、`--onto` 语法、merge vs rebase 对比图。
- 全篇每个流程加「本地位置 / 执行后」标注 + 分支位置变化表；rebase、冲突、救急各节按触发命令区分收尾方式（rebase 用 `--continue`，merge 用 `commit`）。
- 新增附录「一次完整任务的分支迁移轨迹」11 步表。
- 章节由 16 节扩为 18 节 + 附录，篇幅约翻倍。

## [2026-08-27] daily | 每日任务执行（无新资料）
按 CLAUDE.md 第八节执行每日整理流程：`Clippings/` 不存在；`raw/` 为空；`mine/` 无新增；`output/` 无新增产出。
全库无新资料需要编译进 wiki。链接校验状态与上午一致：无孤儿页、Git 断链已修复。
产出 `output/daily-log-2026-08-27.md`。知识库规模维持：29 条目（云原生 19 + Git 10），2 主题，1 skill。
