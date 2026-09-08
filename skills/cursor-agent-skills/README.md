# Cursor Agent Skills · 团队起始包 v1.0

面向**强合规企业（政府 / 工业 / 水务，代码与数据不出境）**的 Cursor Agent Skills 六件套。

## 技能清单

| 技能 | 目录 | 作用 | 触发方式 |
|------|------|------|---------|
| 数据合规守卫 | `data-compliance-guard/` | 扫描数据出境与敏感信息风险 | 提交前 / 引依赖前 / 评审 AI 代码前 |
| 代码评审门禁 | `code-review-gate/` | 六维评审清单 + 留痕报告 | 要求评审、PR 前 |
| AI 代码留痕 | `ai-code-provenance/` | AI 生成代码的标注与留痕 | AI 产出代码后、提交前 |
| 规范化提交 | `commit-and-pr/` | commit message + PR 描述 | 要提交 / 要开 PR |
| 系统化排障 | `debug-systematically/` | 复现→定位→最小修复→回归 | 遇到 bug / 报错 |
| 安全重构 | `refactor-safely/` | 小步、行为不变、可回滚 | 要重构 / 要大改 |

## 安装

### 全局（个人机器，所有项目可用）

```powershell
Copy-Item -Recurse -Force "E:\999知识库\skills\cursor-agent-skills\*" "$env:USERPROFILE\.cursor\skills\"
```

安装后路径：`C:\Users\<用户名>\.cursor\skills\<技能名>\SKILL.md`

### 项目级（团队共享，推荐）

```powershell
cd <你的项目根目录>
New-Item -ItemType Directory -Force -Path .cursor\skills
Copy-Item -Recurse -Force "E:\999知识库\skills\cursor-agent-skills\*" ".cursor\skills\"
git add .cursor/skills && git commit -m "chore(skills): 引入团队 Agent Skills 起始包"
```

> **团队规范必须放项目级**：Cursor 不会把全局技能同步到 Cloud Agents / 远程 SSH 会话 / self-hosted worker。

### Git Bash / macOS / Linux

```bash
cp -r /e/999知识库/skills/cursor-agent-skills/* ~/.cursor/skills/
```

## 验证

装完**开新会话**（技能在启动时扫描），然后在 Agent 聊天里问：

> 你现在有哪些可用的 skill？把每个的 name 和 description 原样列出来。

列得出来就说明加载成功。

## 使用

| 方式 | 操作 |
|------|------|
| 显式执行 | 输入 `/data-compliance-guard` |
| 附加上下文 | 输入 `@code-review-gate` |
| 自动匹配 | 直接描述任务，Agent 自行判断 |
| 常驻会话 | `Alt+Enter` 变成 Custom Mode |

## 校验

```bash
skills-ref validate ./data-compliance-guard
```

## 安全说明

- 本包中仅 `data-compliance-guard/scripts/scan-egress.py` 含可执行脚本，**纯 stdlib、无网络请求、无外部依赖**，可放心审读。
- 引入任何**第三方**技能前，请按「指令层 + 代码层」双重评审，详见 wiki 条目 `12-Skill安全与企业合规`。

## 维护

- 修改技能走 **PR**，与改 ESLint 配置同等对待。
- 版本号写在每个 `SKILL.md` 的 `metadata.version`。
