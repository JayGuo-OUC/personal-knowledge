---
name: data-compliance-guard
description: >-
  扫描代码、配置与依赖中的数据出境与敏感信息风险：境外 API/SDK/遥测域名、硬编码密钥与凭据、明文个人信息、
  日志与错误信息泄露。在提交代码前、引入第三方依赖前、评审 AI 生成代码前，或用户提到
  「合规 / 数据出境 / 敏感信息 / 密钥泄露 / 代码审查」时使用。
license: Proprietary
compatibility: Requires Python 3.9+ (scripts/scan-egress.py uses stdlib only)
metadata:
  author: platform-team
  version: "1.0"
  risk-level: high
---

# 数据合规守卫

## 何时使用

- 提交（commit / PR）之前，对改动做合规体检
- 引入任何第三方依赖、SDK、CDN、字体、图标库之前
- 评审 AI 生成代码之前（AI 极易引入境外 CDN 或遥测）
- 用户提到合规、数据出境、敏感信息、密钥泄露、代码审查时

## 红线（命中即阻断，无例外）

1. **代码与业务数据不得出境**——不得调用境外 API、不得加载境外 CDN/字体/SDK、不得向境外发送遥测或错误上报
2. **密钥不得进仓库**——不得硬编码 AK/SK、token、私钥、数据库连接串
3. **个人信息不得明文落盘或打日志**——身份证号、手机号、住址、人脸/声纹等
4. **客户现场数据不得回传公司或第三方**
5. **不得在错误信息/日志中暴露堆栈、内网地址、SQL、客户信息**

## 步骤

### 1. 确定扫描范围

- 未提交改动：先 `git status --porcelain` 与 `git diff --name-only` 拿到改动文件清单
- 指定路径：用用户给的路径
- **不要全量扫描整个仓库**（慢且噪音大），优先扫改动文件

### 2. 跑自动扫描

```bash
python scripts/scan-egress.py <路径1> <路径2> ...
```

退出码：`0` = 无高危；`1` = 发现高危，必须处理。

脚本覆盖**机器可判定**的四类：境外域名、硬编码凭据、个人信息模式、外发指令。

### 3. 人工补充检查（脚本扫不出的部分）

脚本只能模式匹配，**以下必须人工/由你判断**：

| 检查项 | 怎么看 |
|--------|--------|
| 新引入的依赖是否合规 | 看 `package.json` / `pom.xml` / `requirements.txt` 的 **diff**，确认新增了什么包 |
| 依赖是否自带遥测 | 检查包是否含 analytics / telemetry / track / beacon 等调用 |
| 云服务区域 | 看是否指定了境外 region（如 `us-east-1`、`ap-southeast-1`） |
| 构建产物外链 | 检查 HTML 模板里的 `src`/`href` 是否指向境外 CDN |
| 字体 / 图标库 | 检查是否引入 Google Fonts、cdnjs、unpkg、jsdelivr 等 |
| 日志与上报 | 检查是否新增 `console.log` 打印敏感对象、是否新增 Sentry/GA 等上报 |

### 4. 输出报告

按下面的格式输出，**不得省略**：

```
## 合规扫描报告

**范围**：<扫描了哪些文件/路径>
**工具**：scripts/scan-egress.py + 人工检查
**结论**：✅ 通过 / ⚠️ 有告警 / ❌ 有阻断项

### 阻断项（必须修复才能提交）
| 等级 | 文件:行号 | 问题 | 建议 |
|------|----------|------|------|

### 告警项（需人工确认）
| 等级 | 文件:行号 | 问题 | 建议 |
|------|----------|------|------|

### 已检查但无问题
- 境外域名 ✅
- 硬编码凭据 ✅
- 个人信息明文 ✅
- 日志泄露 ✅
- 新增依赖 ✅
```

### 5. 给出修复方案

每个阻断项都要给**可直接执行**的替换方案，例如：

| 问题 | 替换方案 |
|------|---------|
| 引了 `cdn.jsdelivr.net` | 改为内网 npm 源安装，或 `assets/` 本地化 |
| 引了 Google Fonts | 改用内网字体服务或本地字体文件 |
| 硬编码了 AK/SK | 改为从环境变量/配置中心读取，并**立即轮换该凭据** |
| 打了 `console.log(user)` | 删除或脱敏为 `console.log(user.id)` |
| 用了境外 Sentry | 改用内网自建监控 |

## 示例

**输入**：用户说「帮我检查下这次改动能不能提交」

**执行**：

```bash
git diff --name-only
python scripts/scan-egress.py $(git diff --name-only)
```

**输出**：

```
## 合规扫描报告

**范围**：src/api/client.ts、src/utils/logger.ts、index.html
**结论**：❌ 有阻断项

### 阻断项
| 等级 | 文件:行号 | 问题 | 建议 |
|------|----------|------|------|
| 🔴 高 | index.html:12 | 引用境外 CDN `https://cdn.jsdelivr.net/npm/vue@3` | 改为内网 npm 源安装 vue，构建时打包 |
| 🔴 高 | src/api/client.ts:8 | 硬编码 `const API_KEY = "sk-live-xxxx"` | 改从 `import.meta.env.VITE_API_KEY` 读取，并轮换该密钥 |
```

## 边界（Do NOT）

- **不要因为「只是测试环境」就放行阻断项**——红线没有例外
- **不要修改被扫描的业务代码**，只报告问题与建议；修复须经用户确认
- **不要全量扫描 `node_modules/`、`.git/`、构建产物目录**（噪音巨大）
- 脚本报的是**疑似**，最终判定由人做；不要直接把脚本输出当成最终结论
- 发现已泄露的密钥，必须提示**立即轮换**，仅删除代码不够

## 相关脚本

- `scripts/scan-egress.py` — 模式扫描器（stdlib only，无网络请求，可安全审读）
