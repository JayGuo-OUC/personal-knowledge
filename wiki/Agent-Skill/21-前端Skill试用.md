---
title: 21-前端Skill试用：sjz-front 全量 20 个 Skill 运行结果
type: entry
created: 2026-09-09
updated: 2026-09-09
tags: [AI, Agent, Skill, 试用, 前端, Vue3, Vite, Element Plus, Pinia, Vue Router, 代码审查, 技术栈匹配, sjz-front]
sources: [E:/guojian/01project/sjz/sjz-front/.agents/skills, E:/guojian/01project/sjz/sjz-front/skill运行结果.md]

---

# 21-前端Skill试用：sjz-front 全量 20 个 Skill 运行结果

## 摘要
把前端项目 `sjz-front`（Vue 3.5 + `<script setup>`（JS，非 TS）+ Pinia 3 + Vue Router 4 + Element Plus 2.13 + Tailwind 3 + Vite 7）里已装的 **20 个前端 skill 逐个做合规审计**——对照 frontmatter 合法性、结构完整性、引用有无断链、技术栈是否匹配逐项判定。结果 **PASS 6 · WARN 9 · FAIL 5**。

- **可用主力（PASS）**：`vue`、`vue-best-practices`、`pinia`、`vue-pinia-best-practices`、`vue-router-best-practices`、`element-plus`（自建）——与 Vue3 + Element Plus 后台体系强匹配。
- **按需启用（WARN）**：`vite` / `vite-patterns`（skill 面向 Vite 8/Rolldown，仓库是 Vite 7）、`frontend-design`、`vue-expert`（限定章节）、测试类（引入 Vitest 后）、`ui-to-vue`（需外部 API Key）。
- **建议停用（FAIL）**：`frontend-patterns`、`frontend-dev-guidelines`、`frontend-ui-engineering`（React/Next/MUI/TanStack 教条，会把 agent 导向错误 API）、`typescript-pro`（仓库无 TS）、`vitest`（未装测试链）。
- **目录卫生**：以 `.agents/skills/` 为准（20 个）；`agent/skills/` 有 16 个重复副本、`.claude/skills/` 为子集副本，建议清理以降低维护成本。

> 与 [[20-后端Skill试用]] 呼应：那篇是 **sjz-back 后端 26 个 skill** 的同类体检，本篇是 **sjz-front 前端 20 个** 的体检，两者构成前后端完整对照。

---

# Skill 运行结果

> 运行时间：2026-09-09  
> 判定方式：对照仓库做合规审计（frontmatter / 结构完整性 / 技术栈匹配），不是可执行脚本冒烟。  
> 主路径：`.agents/skills/`（`agent/skills/`、`.claude/skills/` 多为副本）

## 仓库技术栈（证据）

| 项 | 现状 |
| --- | --- |
| 框架 | Vue `^3.5.26` + `<script setup>`（JS，非 TS） |
| 状态 | Pinia `^3.0.4` |
| 路由 | Vue Router `^4.6.4`（Hash History） |
| UI | Element Plus `^2.13.1` + Tailwind `^3.4.19` |
| 构建 | Vite `^7.3.0` |
| 测试 | 无 Vitest / Vue Test Utils / Playwright |
| TypeScript | 无 `typescript` / `vue-tsc` / `tsconfig`；`src` 为 `.js`/`.vue` |

## 总览

| 指标 | 数量 |
| --- | ---: |
| 去重 skill（`.agents/skills`） | **20** |
| PASS | **6** |
| WARN | **9** |
| FAIL | **5** |
| `agent/skills` 重复副本 | 16 |
| 仅 `.agents` 有 | element-plus、vue-pinia-best-practices、vue-router-best-practices、vue-testing-best-practices |

### 结果速查

| # | Skill | 结果 | 一句话 |
| ---: | --- | --- | --- |
| 1 | vue | PASS | Vue 3.5 / Composition API 对齐；注意 TS 偏好与仓库不符 |
| 2 | vue-best-practices | PASS | 引用完整，与 Vue SPA 高度匹配 |
| 3 | vue-pinia-best-practices | PASS | Pinia 实践与 `src/stores` 匹配 |
| 4 | vue-router-best-practices | PASS | 路由守卫/生命周期建议可直接用 |
| 5 | pinia | PASS | 官方 Pinia 文档型 skill，版本匹配 v3.0.4 |
| 6 | element-plus | PASS | 与项目 UI 强匹配；图标包建议偏理想化 |
| 7 | vue-expert | WARN | 核心 Vue/Pinia/Vite 有用；Nuxt/TS/测试面过大 |
| 8 | vite | WARN | Vite 相关，但默认 Vite 8/Rolldown，仓库是 Vite 7 |
| 9 | vite-patterns | WARN | proxy/env 可用；夹杂 React / Vite 8 示例 |
| 10 | frontend-design | WARN | 设计品味可用，勿覆盖 Element Plus 后台规范 |
| 11 | design-taste-frontend | WARN | 偏落地页/React；明确排除 dashboard |
| 12 | unit-test-vue-pinia | WARN | skill 完整，但仓库尚无测试工具链 |
| 13 | vue-testing-best-practices | WARN | 引用完整，当前无可测面 |
| 14 | ui-to-vue | WARN | 截图转 Vue 可选；依赖外部 CLI/API |
| 15 | grill-me | WARN | frontmatter 合法，正文几乎为空 stub |
| 16 | typescript-pro | FAIL | 仓库无 TS / tRPC，不宜自动启用 |
| 17 | vitest | FAIL | 未安装 Vitest，无法落地 |
| 18 | frontend-patterns | FAIL | React/Next 专用，与本仓库冲突 |
| 19 | frontend-dev-guidelines | FAIL | React/MUI/TanStack 教条，违背现有约定 |
| 20 | frontend-ui-engineering | FAIL | 断链 + React 示例，不适合本 Vue 项目 |

---

## 详细结果

### 1. vue — PASS

- **Path:** `.agents/skills/vue`（另有 `agent/skills/`、`.claude/skills/` 副本）
- **Frontmatter:** `name` + `description` 合法；含 metadata
- **结构:** `references/script-setup-macros.md`、`core-new-apis.md`、`advanced-patterns.md`、`GENERATION.md` 齐全
- **仓库匹配:** 强 — Vue 3.5 Composition API / `<script setup>`；skill 偏好 `lang="ts"`，仓库为 JS
- **关键发现:**
  - 可作为本仓库主 Vue 参考 skill
  - 应用时忽略 TS/`vue-tsc` 假设
  - 存在多路径重复

### 2. vue-best-practices — PASS

- **Path:** `.agents/skills/vue-best-practices`
- **Frontmatter:** 合法（含 license / metadata）
- **结构:** `references/` 下约 22 个引用文件齐全
- **仓库匹配:** 强 — 全库 Composition API / `<script setup>`
- **关键发现:**
  - 与本仓库工作流高度匹配
  - TS 默认建议需人工过滤
  - 引用树完整可加载

### 3. vue-pinia-best-practices — PASS

- **Path:** `.agents/skills/vue-pinia-best-practices`（仅 `.agents`）
- **Frontmatter:** 合法
- **结构:** `reference/` 下 6 个文件齐全
- **仓库匹配:** 强 — `src/stores/` 含 setup/options 混用；`createPinia()` 在 `main.js`
- **关键发现:**
  - Gotcha 向内容贴合真实用法
  - setup store 全量 return 等建议可直接用
  - 结构干净

### 4. vue-router-best-practices — PASS

- **Path:** `.agents/skills/vue-router-best-practices`（仅 `.agents`）
- **Frontmatter:** 合法
- **结构:** `reference/` 下 8 个文件齐全
- **仓库匹配:** 强 — `vue-router ^4.6.4` + Hash History
- **关键发现:**
  - 守卫/生命周期陷阱对本 SPA 很有价值
  - 引用完整
  - 与 Hash 模式无冲突

### 5. pinia — PASS

- **Path:** `.agents/skills/pinia`
- **Frontmatter:** 合法
- **结构:** core / features / best-practices / advanced 引用 + `GENERATION.md` 齐全
- **仓库匹配:** 强 — skill 标注 Pinia v3.0.4 与依赖一致；Nuxt/SSR 段对本 SPA 无用
- **关键发现:**
  - 本仓库首选 Pinia 官方型参考
  - 跳过 Nuxt/SSR 即可
  - 与 `vue-pinia-best-practices` 互补

### 6. element-plus — PASS

- **Path:** `.agents/skills/element-plus`（仅 `.agents`）
- **Frontmatter:** 合法（中文触发词 `el-*`）
- **结构:** 单文件 skill，无断链
- **仓库匹配:** 强 — 广泛使用 `el-dialog` / `el-form` / `ElMessage`
- **关键发现:**
  - 简洁、可直接用
  - 建议的 `@element-plus/icons-vue` 未在 `package.json`
  - 无结构问题

### 7. vue-expert — WARN

- **Path:** `.agents/skills/vue-expert`
- **Frontmatter:** 合法，metadata 丰富
- **结构:** composition-api / components / state-management / nuxt / typescript / mobile-hybrid / build-tooling 齐全
- **仓库匹配:** 中 — Vue/Pinia/Router/Vite 有用；Nuxt/Quasar/Capacitor/PWA/Vitest/vue-tsc 不适用
- **关键发现:**
  - 限定到 Composition API + Pinia + Vite 时可用
  - 避免自动启用 Nuxt/移动端/测试章节
  - 有 `agent/skills` 副本

### 8. vite — WARN

- **Path:** `.agents/skills/vite`
- **Frontmatter:** 合法
- **结构:** core-config / features / plugin-api / build-and-ssr / environment-api / rolldown-migration 齐全
- **仓库匹配:** 中 — 仓库 Vite 7；skill 面向 Vite 8 beta / Rolldown
- **关键发现:**
  - 配置 / 插件 / HMR 仍有参考价值
  - 本仓库应优先 `vite.config.js` 模式
  - Rolldown 迁移内容视为未来参考

### 9. vite-patterns — WARN

- **Path:** `.agents/skills/vite-patterns`
- **Frontmatter:** 合法
- **结构:** 自包含，无断链
- **仓库匹配:** 部分 — proxy/env/optimizeDeps 可用；示例偏 React / Vite 8
- **关键发现:**
  - `VITE_` 安全与 proxy 段贴合本项目
  - `rolldownOptions` / Oxc minify 与 Vite 7 默认不符
  - 与 `vite` skill 重叠，用时过滤 React 示例

### 10. frontend-design — WARN

- **Path:** `.agents/skills/frontend-design`
- **Frontmatter:** 合法；`LICENSE.txt` 存在
- **结构:** SKILL + LICENSE，完整
- **仓库匹配:** 部分 — 框架无关设计指导；产品是 Element Plus 后台，非营销落地页
- **关键发现:**
  - 比 `design-taste-frontend` 更中性（无 React 默认栈）
  - 勿机械套用到密集表格/EMS 界面
  - 结构 OK

### 11. design-taste-frontend — WARN

- **Path:** `.agents/skills/design-taste-frontend`
- **Frontmatter:** 合法
- **结构:** 单文件；提及未来 `blocks/`（尚未存在，属文档约定）
- **仓库匹配:** 弱 — 默认 React/Next + Tailwind v4 + Motion；§13 排除 dashboard/admin
- **关键发现:**
  - 仅适合偶发营销/落地页，不适合核心 EMS
  - React/RSC/`motion/react` 与 Vue 栈冲突
  - 无硬性断链

### 12. unit-test-vue-pinia — WARN

- **Path:** `.agents/skills/unit-test-vue-pinia`
- **Frontmatter:** 合法
- **结构:** `references/pinia-patterns.md` 存在
- **仓库匹配:** 弱 — 无 vitest / `@vue/test-utils` / `@pinia/testing` / 测试脚本
- **关键发现:**
  - 引入测试时可复用
  - 依赖包当前未安装
  - 与 `vue-testing-best-practices`、`vitest` 重叠

### 13. vue-testing-best-practices — WARN

- **Path:** `.agents/skills/vue-testing-best-practices`（仅 `.agents`）
- **Frontmatter:** 合法
- **结构:** `reference/` 下 11 个文件齐全
- **仓库匹配:** 弱 — 当前无可测面
- **关键发现:**
  - 测试引入后参考价值高
  - Playwright E2E 对本仓库属可选愿景
  - 与 unit-test / vitest 重叠

### 14. ui-to-vue — WARN

- **Path:** `.agents/skills/ui-to-vue`
- **Frontmatter:** 合法
- **结构:** 单文件；依赖外部 `ui-to-vue-converter` + DashScope API
- **仓库匹配:** 部分 — 支持 Element Plus；默认 Vant；转换器未进项目依赖
- **关键发现:**
  - 批量截图→Vue 可用 `--ui element-plus`
  - 需 `DASHSCOPE_API_KEY` 与网络，非仓库内置流程
  - 多路径重复

### 15. grill-me — WARN

- **Path:** `.agents/skills/grill-me`
- **Frontmatter:** 合法；`disable-model-invocation: true`
- **结构:** 正文几乎是一行 stub（`Call the Skill tool with "grilling".`）；有 `agents/openai.yaml`
- **仓库匹配:** 框架无关，理论上通用
- **关键发现:**
  - 无法仅凭内容跑出 grilling 工作流
  - 需显式点名才加载
  - 多路径重复

### 16. typescript-pro — FAIL

- **Path:** `.agents/skills/typescript-pro`
- **Frontmatter:** 合法
- **结构:** advanced-types / type-guards / utility-types / configuration / patterns 齐全
- **仓库匹配:** 差 — 无 TypeScript / vue-tsc / tRPC；仅有 `jsconfig.json`
- **关键发现:**
  - 日常功能开发不应自动激活
  - 仅在明确做 TS 迁移时有价值
  - skill 本身结构完整，失败点在栈不匹配

### 17. vitest — FAIL

- **Path:** `.agents/skills/vitest`
- **Frontmatter:** 合法
- **结构:** core / features / advanced 引用 + `GENERATION.md` 齐全
- **仓库匹配:** 无 — 依赖与脚本均无 Vitest；skill 面向 Vitest 5.x beta
- **关键发现:**
  - 安装测试工具前无法落地
  - 将来引入时注意版本对齐
  - 可与 `unit-test-vue-pinia` 配对使用

### 18. frontend-patterns — FAIL

- **Path:** `.agents/skills/frontend-patterns`
- **Frontmatter:** 合法；description 明确写 React/Next.js
- **结构:** 单文件自包含
- **仓库匹配:** 差 — hooks / Context / React Query / Framer Motion / Next
- **关键发现:**
  - 对本 Vue 项目会误导 API 选择
  - a11y/perf 概念可迁移，API 面错误
  - `.agents` / `agent` / `.claude` 三份重复

### 19. frontend-dev-guidelines — FAIL

- **Path:** `.agents/skills/frontend-dev-guidelines`
- **Frontmatter:** 合法
- **结构:** `resources/` 10 个文件存在，但 SKILL.md 未索引（孤立资源）；含 TanStack Router 等
- **仓库匹配:** 差 — 强制 React、MUI v7、TanStack、`features/` 布局；本仓库是 Vue + Element Plus + 扁平 `views/components`
- **关键发现:**
  - 跟随此 skill 会违背项目约定
  - resources 与入口脱节
  - 有 `agent/skills` 副本

### 20. frontend-ui-engineering — FAIL

- **Path:** `.agents/skills/frontend-ui-engineering`
- **Frontmatter:** 合法
- **结构:** **断链** — 引用 `../../references/accessibility-checklist.md` 不存在；无本地 `references/`
- **仓库匹配:** 弱 — a11y/响应式可迁移；示例为 React/TSX + React Query + Zustand
- **关键发现:**
  - 无障碍清单路径失效
  - 会把 agent 导向错误状态库与 React API
  - Tailwind 移动优先部分与仓库有少量重叠

---

## 副本与目录说明

| 目录 | 角色 |
| --- | --- |
| `.agents/skills/` | 主清单（20 个，审计以此为准） |
| `agent/skills/` | 16 个与 `.agents` 重复；无独有 skill |
| `.claude/skills/` | 子集副本：vue、frontend-design、frontend-patterns、ui-to-vue、vite-patterns、grill-me |

建议：日常以 `.agents/skills/` 为准；清理 `agent/skills/` 与 `.claude/skills/` 重复可减少维护成本。

## 建议保留 / 停用

**日常优先启用（PASS）：** `vue`、`vue-best-practices`、`pinia`、`vue-pinia-best-practices`、`vue-router-best-practices`、`element-plus`

**按需启用（WARN）：** `vite` / `vite-patterns`（注意 Vite 7）、`frontend-design`（在 Element Plus 体系内）、`vue-expert`（限定章节）、测试类 skill（引入 Vitest 后）、`ui-to-vue`（有截图批转需求时）

**建议停用或移出项目上下文（FAIL）：** `frontend-patterns`、`frontend-dev-guidelines`、`frontend-ui-engineering`、`typescript-pro`、`vitest`（未装测试前）

---

## 相关
- [[22-Skill现有技术栈]]（按公司栈重做选型：本篇结论直接决定了前端该留哪些、停用哪些）
- [[20-后端Skill试用]]（同一套方法论在 sjz-back 后端 26 个 skill 上的体检，前后端对照）
- [[16-程序员推荐安装的Skill]]（这些 skill 的选型来源与安装清单）
- [[19-cursor内置skill]]（Cursor 内置 skill 对照）

## 来源
- `E:/guojian/01project/sjz/sjz-front/.agents/skills/`（被审计的 20 个前端 skill）
- `E:/guojian/01project/sjz/sjz-front/skill运行结果.md`（本次运行结果原始文档）
