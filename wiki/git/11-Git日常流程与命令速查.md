---
title: Git 日常流程与命令速查
type: term
created: 2026-08-31
updated: 2026-08-31
tags: [Git, 命令, 最佳实践, 速查]
sources: [https://git-scm.com/docs, https://git-scm.com/book/zh/v2, https://www.conventionalcommits.org/]
---

# Git 日常流程与命令速查

## 摘要
按「一天真实的工作流」组织 Git 命令：开工同步 → 开分支 → 小步提交 → 提交前自检 → 追平主干 → 整理历史 → 推送提 PR → 评审修改 → 合入清理 → 冲突处理 → 事故救急。每个流程给出**具体指令 + 为什么这么做 + 坑点**。最后附撤销矩阵、速查表、推荐别名，以及 AI 辅助编程场景下的额外纪律。

## 正文

### 〇、七条铁律（先把这个记住，命令都是次要的）

| # | 铁律 | 原因 |
|---|------|------|
| 1 | **一个提交只做一件事**，且能独立编译通过 | 出问题好 bisect、好 revert |
| 2 | **提交前必看 `git diff --staged`** | 90% 的误提交（调试代码、密钥、大文件）都在这里被拦下 |
| 3 | **只改自己的本地分支**，不碰共享分支 | 别人的提交历史被改写是协作灾难 |
| 4 | **已推送的提交不改写**，用 `revert` 而不是 `reset` | 重写公共历史会坑所有同事 |
| 5 | **同步优先用 `pull --rebase`**，保持线性 | 减少无意义的 merge commit，历史可读 |
| 6 | **强推只用 `--force-with-lease`** | 别人先推了就会拒绝，避免覆盖他人代码 |
| 7 | **任何不确定前先 `git status`** | 免费、无损、能救命 |

> 判断口诀：**动本地随便试，动远端先问一遍。**

---

### 一、晨间同步：开工前先对齐主干

```bash
git checkout main              # 回到主干（或 git switch main）
git pull --rebase              # 用 rebase 方式拉取，避免多余 merge commit
git status                     # 确认工作区干净
git log --oneline -5           # 看一眼别人昨晚合了什么
```

**说明**
- `pull = fetch + merge`；`pull --rebase = fetch + rebase`，把你的本地提交"接到"远端最新之后，历史是一条直线。
- 若工作区有未提交改动，`pull` 会拒绝。先 `git stash`（见流程十）或先提交。
- 建议一次性配好省事：
  ```bash
  git config --global pull.rebase true          # 之后 git pull 默认 rebase
  git config --global rebase.autoStash true     # rebase 前自动 stash，结束后自动恢复
  ```

---

### 二、领任务：开分支

```bash
git switch -c feature/user-login      # 新建并切换（旧写法 git checkout -b）
git switch -c fix/issue-1234 main     # 从指定基点创建
git branch --show-current             # 确认当前分支名
```

**分支命名建议**：`feature/xxx`、`fix/xxx`、`hotfix/xxx`、`refactor/xxx`、`docs/xxx`，`xxx` 带上需求或 issue 编号，方便回溯。

**要点**
- 分支要**短命**（1 天 ~ 3 天）。活得越久，合并时冲突越多。
- 不确定用什么分支模型，看 [[04-Git分支模型]] 与 [[09-Git工作流与最佳实践]]。

---

### 三、编码循环：小步提交

```bash
git status                     # 改了什么
git diff                       # 看未暂存的改动（工作区 vs 暂存区）
git add <file>                 # 暂存指定文件
git add -p                     # 交互式按"块"暂存，把调试代码和正事分开
git commit -m "feat(auth): 新增短信验证码登录"
```

**要点**
- 拒绝 `git add .` 一把梭。用 `git add -p` 可以只提交一个文件里的部分修改，这是保证「一个提交一件事」的关键工具。
- 顺手补齐：新文件必须 `git add` 后才会被跟踪；`.gitignore` 的写法见 [[07-Git暂存与忽略]]。

---

### 四、提交前自检（最值钱的一步）

```bash
git diff --staged              # 确认"即将提交的内容"正是你想提交的
git diff --check               # 找出空白字符错误、残留的冲突标记
git status -s                  # 精简状态，一眼看出有没有漏 add / 多余文件
```

**自检清单（过一遍再敲 commit）**
- [ ] 没有 `console.log` / `printf` / `TODO` 调试残留
- [ ] 没有密钥、密码、内网地址、证书（→ 用 `.env` + `.gitignore`，或 git-secrets 类钩子）
- [ ] 没有大文件、编译产物、日志（→ 确认已被 `.gitignore` 覆盖）
- [ ] 没有把别人的改动一并提交进来
- [ ] 提交后代码能编译 / 测试能过

> 一旦把密钥推到远端，删提交也没用（历史仍在）。必须立刻轮换密钥。

---

### 五、写提交信息

```
<type>(<scope>): <subject>

<body>   # 可选：为什么改、怎么改
<footer> # 可选：关联 issue、破坏性变更
```

```bash
git commit -m "fix(order): 修复并发下订单号重复" \
           -m "使用数据库序列替代时间戳拼接，压测 500 并发下不再冲突。Closes #1234"
```

常用 type：`feat` `fix` `docs` `refactor` `perf` `test` `chore` `revert`。
规范的价值：能自动生成 CHANGELOG、能按 type 过滤历史、评审时一眼看出改动性质。详见 [[09-Git工作流与最佳实践]]。

---

### 六、追平主干：每天至少一次

```bash
git fetch origin               # 只下载不合并，先看看情况
git log --oneline HEAD..origin/main   # 主干比我的分支多了哪些提交
git rebase origin/main         # 把我的提交重放到主干最新之后
```

**为什么不用 `git merge main`**
- `merge` 会额外产生一个 merge commit，分支图变成毛线团。
- `rebase` 保持线性，`git log --graph` 一眼能读懂。
- **前提**：只 rebase 你自己的、尚未共享的分支。

---

### 七、整理本地历史（仅限「还没推送」的提交）

```bash
git commit --amend                     # 补进上一次提交（改信息/补漏文件）
git commit --amend --no-edit           # 只补文件，不改提交信息

git rebase -i HEAD~3                   # 交互式整理最近 3 个提交
```

`rebase -i` 常用动作：

| 动作 | 作用 |
|------|------|
| `pick` | 保留 |
| `reword` | 保留但改提交信息 |
| `squash` / `s` | 并入上一个提交，合并提交信息 |
| `fixup` / `f` | 并入上一个提交，丢弃本次信息 |
| `drop` / `d` | 删掉这个提交 |
| `edit` | 停在这个提交，方便拆分 |

```bash
git rebase -i --autosquash origin/main   # 配合 git commit --fixup <sha> 自动归位
```

**要点**：整理完再推。已经 push 过的提交就别动了。更多细节见 [[06-Git变基与历史改写]]。

---

### 八、推送与提 PR / MR

```bash
git push -u origin feature/user-login   # 首次推送，绑定上游分支
git push                                # 之后直接推
git push --force-with-lease             # 整理过历史后强推（不用 --force）
```

**提 PR 前自查**
- 提交数量是否合理（别一次 review 3000 行）
- 自测通过，描述里写清「改了什么 / 为什么 / 怎么验证」
- 关联 issue，必要时贴截图或日志

---

### 九、评审后改代码

```bash
# 小改 → 追加提交
git add -p && git commit -m "refactor: 按评审意见拆分校验逻辑"

# 想保持"一个 PR 一个提交" → 用 fixup 收进原提交
git commit --fixup <原提交sha>
git rebase -i --autosquash origin/main
git push --force-with-lease
```

**要点**：评审意见多时，逐条建提交更利于复审（reviewer 能看增量）；合入前再 squash。

---

### 十、合入后收尾清理

```bash
git switch main && git pull --rebase
git branch -d feature/user-login        # 删本地分支（已合并才让删）
git remote prune origin                 # 清理远端已删除分支的本地引用
git branch -a                           # 复查
```

顺手清理工作区残留：
```bash
git clean -n      # 预览将删除的未跟踪文件（先 -n 再 -f，永远）
git clean -fd     # 真正删除未跟踪的文件和目录
```

---

### 十一、冲突处理标准流程

```bash
git rebase origin/main          # 或 git merge，冲突时都会停下
git status                      # 看哪些文件冲突（both modified）
# 手工编辑冲突文件，搜索 <<<<<<< ======= >>>>>>>
git add <冲突文件>               # 标记已解决（不是 commit）
git rebase --continue           # 继续；merge 冲突则用 git commit
git rebase --abort              # 想重来：整个回退到 rebase 前
```

**要点**
- 冲突是「信息」，不是错误。看清两边意图再合并，别无脑选一边。
- 只解决自己引入的冲突；看不懂就问原作者。
- 配一个 `git config --global merge.conflictStyle diff3`，能同时看到「共同祖先」，判断更准。
- 图形化工具有效：`git mergetool`。详见 [[08-Git冲突解决]]。

---

### 十二、救急手册：常见事故与解法

#### 1. 代码写错分支了
```bash
# 还没提交
git stash push -m "临时存放"      # 存起来
git switch 正确的分支
git stash pop                    # 取回来

# 已提交但没推送
git reset --soft HEAD~1          # 撤销提交，改动回到暂存区
git stash push && git switch 正确分支 && git stash pop
```

#### 2. 撤销上一次提交
```bash
git reset --soft  HEAD~1   # 改动留在暂存区（想重提）
git reset --mixed  HEAD~1  # 改动回到工作区（默认，想重改）
git reset --hard   HEAD~1  # 彻底丢弃（危险，先确认没要保留的东西）
```

#### 3. 提交已经推到远端了（公共分支）
```bash
git revert <sha>            # 生成一个"反向提交"，保留历史，安全
git revert -m 1 <merge-sha> # 撤销一个 merge 提交
git revert --no-commit <sha>~1..<sha>  # 撤销一段提交后一次性提交
```
**永远不要对公共分支用 `reset --hard` + 强推。**

#### 4. 找回"丢掉"的提交
```bash
git reflog                  # 记录 HEAD 的每一次移动，本地救命稻草
git reset --hard <旧sha>    # 跳回去
git cherry-pick <sha>       # 只把某一个提交拣回来
```
`reflog` 默认保留 90 天（未 gc 前），误删分支、`reset --hard` 过头都能救。

#### 5. 误删分支
```bash
git reflog                              # 找到该分支最后那个提交的 sha
git switch -c <分支名> <sha>             # 从该提交重建分支
```

#### 6. 临时切换任务 / 半成品不想提交
```bash
git stash push -u -m "做到一半的登录页"   # -u 含未跟踪文件
git stash list
git stash pop                            # 恢复并删除该条
git stash apply stash@{1}                # 恢复但保留记录（可多处复用）
```

#### 7. 撤销矩阵（查这张表就够了）

| 想撤销的东西 | 状态 | 命令 |
|--------------|------|------|
| 工作区某个文件的改动 | 未暂存 | `git restore <file>` |
| 已 `git add` 的暂存 | 已暂存 | `git restore --staged <file>` |
| 上一次提交（保留改动） | 已提交·未推送 | `git reset --soft HEAD~1` |
| 上一次提交（彻底丢弃） | 已提交·未推送 | `git reset --hard HEAD~1` |
| 某次提交（已推送） | 已推送 | `git revert <sha>` |
| 回到某个历史版本看看 | 任意 | `git switch --detach <sha>` |
| 误删的提交 / 分支 | 任意 | `git reflog` → `git cherry-pick` / `git reset --hard` |

#### 8. 找出"是谁把这段代码改成这样的"
```bash
git blame <file>              # 逐行看最后修改者与提交
git log -S "关键字"            # 搜包含该字符串的提交（增删都算）
git bisect start              # 二分法定位引入 bug 的提交
git bisect bad && git bisect good <旧sha>   # 按提示逐轮测试
git bisect reset              # 结束后复位
```

---

### 十三、命令速查表

| 场景 | 命令 |
|------|------|
| 初始化 | `git init` / `git clone <url>` |
| 看状态 | `git status` `git status -s` |
| 看差异 | `git diff` `git diff --staged` `git diff <a> <b>` |
| 看历史 | `git log --oneline --graph --all --decorate` |
| 暂存 | `git add <file>` `git add -p` |
| 提交 | `git commit -m "..."` `git commit --amend` |
| 分支 | `git switch -c <name>` `git switch <name>` `git branch -d <name>` |
| 同步 | `git fetch` `git pull --rebase` `git push` `git push --force-with-lease` |
| 整理 | `git rebase -i HEAD~n` `git cherry-pick <sha>` |
| 暂存栈 | `git stash push -u` `git stash pop` `git stash list` |
| 撤销 | `git restore` `git reset` `git revert` |
| 排查 | `git blame` `git log -S` `git bisect` `git reflog` |

**最推荐记住的一条**（好看的历史全靠它）：
```bash
git log --oneline --graph --all --decorate
```

---

### 十四、推荐全局配置（一次配好，长期受益）

```bash
# 身份
git config --global user.name "你的名字"
git config --global user.email "你的邮箱"

# 行为
git config --global pull.rebase true
git config --global rebase.autoStash true
git config --global push.default current
git config --global fetch.prune true          # 拉取时自动清理已删除的远端分支
git config --global merge.conflictStyle diff3
git config --global core.autocrlf input       # 跨平台团队统一换行（Windows 用 true）
git config --global init.defaultBranch main

# 别名
git config --global alias.st "status -s"
git config --global alias.lg "log --oneline --graph --all --decorate"
git config --global alias.last "log -1 --stat"
git config --global alias.unstage "restore --staged"
git config --global alias.amend "commit --amend --no-edit"
```

配好后：`git st` 看状态、`git lg` 看历史图、`git last` 看上次提交改了哪些文件。

---

### 十五、AI 辅助编程场景下的额外纪律

用 Cursor / Copilot / 各类 code agent 产出代码时，风险从"写错"变成"看着对但其实没审"：

1. **先 diff 后提交**：AI 一次改十几个文件是常态，必须 `git diff --staged` 逐文件过，再 commit。
2. **小步分批提交**：让 AI 一次只做一件事，一个提交对应一个意图，出问题好回退。
3. **别让 AI 代写提交信息就完事**：自己核对一遍描述是否与实际改动一致。
4. **敏感信息二次确认**：AI 可能把真实配置、内网地址、测试账号写进代码或注释。
5. **生成的代码单独分支**：`git switch -c ai/refactor-xxx`，评审通过再合入，便于整体放弃。

---

### 十六、习惯清单（贴在显示器上）

**每天**
- 开工 `git pull --rebase`；收工前 `git push`（本地未推送的代码等于没有备份）
- 每天至少追平一次主干，别攒到 PR 那天

**每次提交**
- `git status` → `git diff` → `git diff --staged` → `commit`
- 一个提交一件事，信息写清「为什么」

**每次强推前**
- 问自己三遍：这是不是公共分支？有没有人基于它工作？用 `--force-with-lease` 了吗？

**每周**
- 清理已合并的本地分支与 stash 残留
- `git fsck` / `git gc` 保持仓库健康（大仓库尤其）

## 相关
- [[03-Git基础命令]]
- [[04-Git分支模型]]
- [[05-Git远程协作]]
- [[06-Git变基与历史改写]]
- [[07-Git暂存与忽略]]
- [[08-Git冲突解决]]
- [[09-Git工作流与最佳实践]]
- [[git-index]]

## 来源
- https://git-scm.com/docs
- https://git-scm.com/book/zh/v2
- https://www.conventionalcommits.org/
