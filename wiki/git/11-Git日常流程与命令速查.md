---
title: Git 日常流程与命令速查
type: term
created: 2026-08-31
updated: 2026-08-31
tags: [Git, 命令, 最佳实践, 速查, rebase]
sources: [https://git-scm.com/docs, https://git-scm.com/book/zh/v2, https://www.conventionalcommits.org/]
---

# Git 日常流程与命令速查

## 摘要
按「一天真实的工作流」组织 Git 命令：开工同步 → 开分支 → 小步提交 → 提交前自检 → 追平主干 → 整理历史 → 推送提 PR → 评审修改 → 合入清理 → 冲突处理 → 事故救急。**每一节都明确标注"此刻本地应处在哪个分支、命令执行后分支会变成什么样"**，并专门拆解 `rebase` 的「三方关系」与执行期间的游离 HEAD 状态。最后附撤销矩阵、速查表、推荐别名，以及 AI 辅助编程场景下的额外纪律。

## 正文

> ### 阅读约定
> 每一节开头的「本地位置 / 执行后」标记含义：
> - **本地位置**：敲命令前，`HEAD` 应该停在哪个分支上
> - **执行后**：命令跑完，`HEAD` 和分支指针停在哪
>
> 记不住分支指针含义的，先回看 [[02-Git核心概念]]；只想知道"我现在在哪"，看下面第〇节。

---

### 〇、先搞清楚：我现在到底在哪个分支

**本地位置**：任意状态

```bash
git status                  # 第一行就写着 "On branch xxx"
git branch --show-current    # 只输出当前分支名，适合脚本
git branch -vv               # 看所有分支 + 各自跟踪的远端分支 + 领先/落后多少
git log --oneline --decorate -3   # 看 HEAD 指着谁、附近有哪些分支指针
```

#### 三种「不在正常分支上」的状态（新手最容易懵的地方）

| `git status` 首行显示 | 含义 | 你现在该做什么 |
|------------------------|------|----------------|
| `On branch feature/xxx` | 正常，站在一个分支上 | 正常操作 |
| `HEAD detached at <sha>` | **游离 HEAD**：HEAD 直接指着某个提交，不属于任何分支 | 只是查看就 `git switch 分支名` 回去；要保留改动则 `git switch -c 新分支` |
| `interactive rebase in progress; onto <sha>` | **rebase 进行中**（可能卡在冲突） | 解决冲突 → `git add` → `git rebase --continue`；或 `git rebase --abort` 全退 |
| `You have unmerged paths` / `All conflicts fixed...` | **merge 进行中**（卡在冲突） | 解决冲突 → `git add` → `git commit`；或 `git merge --abort` |

> 关键区别：**rebase 期间 `git branch --show-current` 会返回空**（因为 HEAD 是游离的）。这时不要慌，也不要新建分支，按提示 `--continue` 或 `--abort` 即可。
> 判断口诀：**`git status` 的第一行就是你的 GPS。**

#### 三条容易混淆的分支（rebase 的三方之一）

| 名字 | 是什么 | 更新时机 |
|------|--------|----------|
| `main` | **本地**的主干分支指针 | 只有你本地 `commit` / `merge` / `reset` 才会动 |
| `origin/main` | **本地缓存的**远端主干快照（远端引用） | 只有 `git fetch` / `git pull` 才会更新 |
| `origin/main`（服务器上的真身） | 远端仓库的真实分支 | 别人 push 时更新 |

> 所以「`git log` 看不到同事的新提交」通常不是没推送，而是**你没 `fetch`**——`origin/main` 还停在昨天。

---

### 一、rebase 到底在干什么（读懂这节，后面全通）

**本地位置**：`feature/user-login`（你自己的功能分支）

假设当前仓库长这样（你在 `feature`，主干已经往前走了）：

```
提交历史（箭头方向 = 时间的先后，右边更新）

        A---B---C---D---E      ← origin/main（同事刚推的 D、E）
                 \
                  X---Y        ← feature/user-login（你的两个提交，基点还停在 C）
                     ↑
                    HEAD（你现在站着的地方）
```

执行 `git rebase origin/main`，Git 内部做五件事：

```
① 找分叉点：git merge-base feature origin/main → 得到 C
② 把 C 之后 feature 独有的提交摘下来：X、Y（存成补丁）
③ 把 HEAD 挪到 origin/main 的最新提交 E 上  ← 此刻进入「游离 HEAD」，不在任何分支
④ 依次把 X、Y 重放到 E 后面，生成全新的提交 X'、Y'（内容一样，哈希变了）
⑤ 把 feature 指针从 Y 移到 Y'，HEAD 重新指回 feature  ← 回到正常分支状态
```

结果：

```
        A---B---C---D---E          ← origin/main（没动过）
                         \
                          X'---Y'  ← feature/user-login（换了新爹，哈希变了）
                               ↑
                              HEAD
```

#### 三方关系速查（rebase 命令填空用）

| 角色 | 本例取值 | 说明 |
|------|----------|------|
| **当前分支**（被重放的分支） | `feature/user-login` | 就是你现在 `HEAD` 所在，`git status` 第一行 |
| **新基点 upstream** | `origin/main` | 你想"接在谁后面"，就是 rebase 后面跟的参数 |
| **被重放的提交** | `X`、`Y` | 当前分支有、而 upstream 没有的提交（`origin/main..HEAD`） |
| **没被碰的** | `origin/main` 上的 `D`、`E` | rebase **永远不改动 upstream**，只改你自己的分支 |

完整语法（平时用不到，但出问题时很有用）：

```bash
git rebase --onto <新基点> <从哪个提交之后开始> <重放哪个分支>

# 例：只把最后 2 个提交搬到 main 上，丢掉前面的
git rebase --onto main HEAD~2 feature/user-login

# 例：本地 main 没更新，直接拿远端做基点
git rebase --onto origin/main main feature/user-login
```

#### merge 与 rebase 的区别（同一场景两种结局）

```
用 git merge main：              用 git rebase main：
  A---B---C---D---E                 A---B---C---D---E
           \     \                               \
            X---Y---M  ← merge提交                 X'---Y'
                                                    ↑ 历史是一条直线，没有多余节点
  ↑ 多出一个 M，分支图开始打结
```

| 维度 | `merge` | `rebase` |
|------|---------|----------|
| 历史 | 保留真实分叉，多一个 merge 提交 | 线性、干净 |
| 提交哈希 | 不变 | **变**（X→X'、Y→Y'） |
| 适用 | 公共分支合入、`main` 上操作 | 自己的、未推送的分支 |
| 风险 | 无 | 改写历史，**绝不要对别人在用的分支做** |

> 一句话：**merge 是把别人的东西娶进来；rebase 是把自己嫁到别人最新的后面。**
> 更详细的分支与合并模型见 [[04-Git分支模型]]，历史改写的边界见 [[06-Git变基与历史改写]]。

---

### 二、七条铁律（先把这个记住，命令都是次要的）

**本地位置**：任意

| # | 铁律 | 原因 |
|---|------|------|
| 1 | **一个提交只做一件事**，且能独立编译通过 | 出问题好 bisect、好 revert |
| 2 | **提交前必看 `git diff --staged`** | 90% 的误提交（调试代码、密钥、大文件）都在这里被拦下 |
| 3 | **只 rebase 自己的本地分支**，不碰共享分支 | 别人的提交历史被改写是协作灾难 |
| 4 | **已推送的提交不改写**，用 `revert` 而不是 `reset` | 重写公共历史会坑所有同事 |
| 5 | **同步优先用 `pull --rebase`**，保持线性 | 减少无意义的 merge commit |
| 6 | **强推只用 `--force-with-lease`** | 别人先推了就会拒绝，避免覆盖他人代码 |
| 7 | **敲任何不确定命令前先 `git status`** | 免费、无损、能救命 |

> 判断口诀：**动本地随便试，动远端先问一遍；rebase 前看一眼 `git status` 第一行。**

---

### 三、晨间同步：开工前先对齐主干

**本地位置**：任意分支（可能在昨天的 `feature/xxx` 上）
**执行后**：停在 `main`，且本地 `main` = `origin/main`

```bash
git switch main              # ① 先切回主干（有未提交改动会拒绝，先 stash 或 commit）
git status                   # ② 确认第一行是 On branch main，且工作区干净
git pull --rebase            # ③ fetch + 以 rebase 方式把本地改动接到 origin/main 之后
git log --oneline -5         # ④ 看一眼别人昨晚合了什么
```

**为什么这里也要 rebase**：如果你昨天在本地 `main` 上误提交过，`pull --rebase` 会把它重放到远端之后；用普通 `pull` 则会多出一个 merge 提交，污染主干历史。

**分支位置变化**

| 时刻 | `main` | `origin/main` | `HEAD` |
|------|--------|---------------|--------|
| 执行前 | 昨天的 C | 昨天的 C | `feature/xxx` |
| `switch main` 后 | C | C | `main` |
| `pull --rebase` 后 | E（追平远端） | E（fetch 更新） | `main` |

**坑点**
- `git pull` 时不加参数、也没配 `pull.rebase`，默认走 merge → 主干出现多余 merge 提交。
- 工作区有未提交改动时 `pull --rebase` 会拒绝执行；配了 `rebase.autoStash` 会自动存、自动恢复。

一次配好：
```bash
git config --global pull.rebase true
git config --global rebase.autoStash true
```

---

### 四、领任务：开分支

**本地位置**：`main`（刚同步完、最新的主干）
**执行后**：新分支 `feature/xxx`，`HEAD` 随之切过去

```bash
git switch main && git pull --rebase   # 确认基点是最新主干（很重要，否则从旧点分叉）
git switch -c feature/user-login       # 新建并切换（旧写法 git checkout -b）
git branch --show-current              # 确认：输出 feature/user-login
git push -u origin feature/user-login  # 可选：立刻推空分支建远端跟踪，之后可直接 git push
```

**为什么必须站在最新的 `main` 上开分支**：分支的「基点」决定你将来 rebase 时要重放多少提交。基点越旧，冲突越多。

**分支位置变化**：`main` 和 `origin/main` 都不动；新指针 `feature/user-login` 指向与 `main` 相同的提交。

**命名建议**：`feature/xxx`、`fix/xxx`、`hotfix/xxx`、`refactor/xxx`、`docs/xxx`，带上需求或 issue 编号。
分支要**短命**（1~3 天），活得越久合并时冲突越多。分支策略详见 [[04-Git分支模型]]。

---

### 五、编码循环：小步提交

**本地位置**：`feature/user-login`（自己的功能分支，始终不要切走）
**执行后**：分支不变，`HEAD` 前进一个新的提交

```bash
git status               # 改了什么
git diff                 # 看未暂存的改动（工作区 vs 暂存区）
git add <file>           # 暂存指定文件
git add -p               # 交互式按"块"暂存，把调试代码和正事拆开
git commit -m "feat(auth): 新增短信验证码登录"
```

**分支位置变化**：`feature/user-login` 指针前移一格，`main` / `origin/main` 原地不动。

```
        A---B---C---D---E---F   ← main / origin/main（始终没动）
                         \
                          X---Y  ← feature/user-login 前进（本例当前分支）
```

**要点**
- 拒绝 `git add .` 一把梭；`git add -p` 是保证「一个提交一件事」的关键工具。
- 新文件必须先 `git add` 才被跟踪；忽略规则见 [[07-Git暂存与忽略]]。

---

### 六、提交前自检（最值钱的一步）

**本地位置**：`feature/user-login`，已有改动待提交
**执行后**：产生一个干净的提交，分支指针前移

```bash
git status -s            # 精简状态：有没有漏 add / 多余文件
git diff --staged        # 确认"即将提交的内容"正是你想提交的
git diff --check         # 找出空白字符错误、残留的冲突标记 <<<<<<<
```

**自检清单**
- [ ] 没有 `console.log` / `printf` / `TODO` 调试残留
- [ ] 没有密钥、密码、内网地址、证书（用 `.env` + `.gitignore`）
- [ ] 没有大文件、编译产物、日志
- [ ] 没有把别人的改动一并提交进来
- [ ] 提交后能编译 / 测试能过

> 密钥一旦推到远端，删提交也没用（历史仍在），必须**立刻轮换密钥**。

---

### 七、写提交信息

**本地位置**：`feature/user-login`

```
<type>(<scope>): <subject>

<body>    # 为什么改、怎么改
<footer>  # 关联 issue、破坏性变更
```

```bash
git commit -m "fix(order): 修复并发下订单号重复" \
           -m "使用数据库序列替代时间戳拼接，压测 500 并发下不再冲突。Closes #1234"
```

常用 type：`feat` `fix` `docs` `refactor` `perf` `test` `chore` `revert`。
规范详见 [[09-Git工作流与最佳实践]]。

---

### 八、追平主干：rebase 详解（每天至少一次）

**本地位置**：`feature/user-login` ← **必须是你的功能分支，不是 main**
**执行后**：分支名字不变，但**基点从旧的 `origin/main` 挪到了最新的 `origin/main`，你的提交变成全新哈希的 X'、Y'**

```bash
git branch --show-current     # ① 确认第一行是 feature/user-login（rebase 前必做！）
git fetch origin              # ② 只下载不合并，先更新本地的 origin/main 快照
git log --oneline HEAD..origin/main   # ③ 主干比我多了哪些提交
git log --oneline origin/main..HEAD   # ④ 我比主干多了哪些提交（这就是即将被重放的）
git rebase origin/main        # ⑤ 把 ④ 的那些提交重放到 ③ 之后
git log --oneline --graph -8  # ⑥ 确认历史是直线、我的提交在最上面
```

**分支位置变化（配合第一节的图看）**

| 时刻 | `feature/user-login` | `origin/main` | `HEAD` 状态 |
|------|----------------------|---------------|-------------|
| ① 执行前 | 指向 `Y`（基点 C） | 指向 `E` | 正常分支 `feature/user-login` |
| ② `fetch` 后 | 不动 | 更新到 `E`（若同事又推了 F、G，则到 G） | 正常 |
| ⑤ `rebase` 期间 | 指针暂时不动 | 不动 | **游离 HEAD**，逐个生成 X'、Y' |
| ⑤ 完成后 | 指向 `Y'`（基点 = E） | 不动 | 回到正常分支 `feature/user-login` |

**如果卡在冲突**（此时 `git status` 显示 `interactive rebase in progress`）：

```bash
git status                    # 看 both modified 的文件
# 手工编辑，搜索 <<<<<<<  =======  >>>>>>>
git add <冲突文件>             # 标记已解决（注意：不是 commit）
git rebase --continue         # 继续重放剩下的提交
git rebase --abort            # 想反悔：整体回到 rebase 之前的状态（X、Y 原样）
git rebase --skip             # 放弃当前这个提交（慎用，等于丢弃它）
```

> 重点：**冲突可能不止一次**。三个提交要重放，就可能冲突三次，每次都 `add` + `--continue`。

**等价写法（理解用）**
```bash
git rebase origin/main
# 等价于：
git rebase --onto origin/main $(git merge-base HEAD origin/main) feature/user-login
```

**常见坑**
- **站在 `main` 上执行 `git rebase origin/main`**：等于什么都没做（自己的提交集合为空），白忙一场。
- **站在 `main` 上执行 `git rebase feature/xxx`**：灾难——会把主干重放到功能分支后面，改写了公共分支。**方向反了。**
- **rebase 了已经 push 过的提交**：之后再 `git push` 会被拒绝，只能 `--force-with-lease`；若别人已基于你的旧提交工作，会直接坑到对方。

---

### 九、整理本地历史（仅限「还没推送」的提交）

**本地位置**：`feature/user-login`
**执行后**：分支名不变，本地提交被压缩/改写，哈希变化

```bash
git commit --amend                   # 补进上一次提交（改信息 / 补漏文件）
git commit --amend --no-edit         # 只补文件，不改提交信息
git rebase -i HEAD~3                 # 交互式整理最近 3 个提交
git rebase -i origin/main            # 整理"本次分支的全部提交"（更推荐，自动算范围）
```

`rebase -i` 打开的是一个**待办清单**（顺序为从旧到新），把每行前面的 `pick` 改成：

| 动作 | 作用 |
|------|------|
| `pick` | 保留 |
| `reword` | 保留但改提交信息 |
| `squash` / `s` | 并入上一个提交，合并提交信息 |
| `fixup` / `f` | 并入上一个提交，丢弃本次信息 |
| `drop` / `d` | 删掉这个提交 |
| `edit` | 停在这个提交（此时 HEAD 游离），可拆分或改内容后 `git rebase --continue` |

```bash
git commit --fixup <原提交sha>        # 先打个"这是修复某某提交"的补丁提交
git rebase -i --autosquash origin/main  # 自动把 fixup 归位并合并
```

**判断能不能整理**：`git log origin/feature/user-login..HEAD` 有输出 = 有未推送的提交 = 可以随便整理；无输出 = 已全部推送 = 不要再改写。

---

### 十、推送与提 PR / MR

**本地位置**：`feature/user-login`（整理完毕）
**执行后**：远端出现同名分支，本地建立上游跟踪

```bash
git push -u origin feature/user-login   # 首次推送，绑定上游
git push                                # 之后直接推
```

**若你整理过历史**（rebase / amend 之后，远端分支已存在旧哈希）：

```bash
git push --force-with-lease   # 安全强推：远端若被别人更新过则拒绝
# 绝不用 --force；绝不对 main / develop 等共享分支强推
```

**分支位置变化**：本地 `feature/user-login` 不动；远端 `origin/feature/user-login` 追平；`main` / `origin/main` 不受影响——**PR 没合并前，主干一根毛都不会变**。

**提 PR 前自查**：提交数量合理（别让人一次 review 3000 行）、自测通过、描述写清「改了什么 / 为什么 / 怎么验证」、关联 issue。

---

### 十一、评审后改代码

**本地位置**：`feature/user-login`（与第 10 节同一个分支，继续在上面对话式修改）
**执行后**：分支名不变，追加提交或收敛为原提交

```bash
# 方式 A：小改 → 追加提交（便于 reviewer 看增量）
git add -p && git commit -m "refactor: 按评审意见拆分校验逻辑"
git push

# 方式 B：想保持"一个 PR 一个提交" → fixup 收进原提交
git commit --fixup <原提交sha>
git rebase -i --autosquash origin/main
git push --force-with-lease
```

> 若 PR 基于的是 `main` 且期间主干又前进了：`git fetch origin && git rebase origin/main`，再 `--force-with-lease` 推。

---

### 十二、合入后收尾清理

**本地位置**：`feature/user-login`（PR 已合并到远端 `main`）
**执行后**：切回 `main` 并追平远端，删除本地功能分支

```bash
git switch main              # ① 切回主干
git pull --rebase            # ② 拉回刚被合入的那个提交
git branch -d feature/user-login   # ③ 删本地分支（已合并才允许删；-D 强制删）
git fetch --prune            # ④ 清理远端已删除分支的本地残留引用
git branch -vv               # ⑤ 复查
```

顺手清理工作区：
```bash
git clean -n      # 先预览将删除的未跟踪文件（永远先 -n）
git clean -fd     # 确认无误再真删
```

**分支位置变化**：`main` 从 E → M（合并提交或 squash 提交）；`origin/main` 同步到 M；`feature/user-login` 被删除。

---

### 十三、冲突处理标准流程（含"我现在在哪个分支"）

**本地位置**：取决于触发方式

| 触发命令 | 冲突时 `git status` 首行 | 结束后怎么收尾 | 全程分支变化 |
|----------|--------------------------|----------------|--------------|
| `git merge main`（在 feature 上） | `On branch feature/xxx` + `You have unmerged paths` | `git add` → **`git commit`** | 分支不变，多一个 merge 提交 |
| `git rebase main`（在 feature 上） | **`interactive rebase in progress`**，HEAD 游离 | `git add` → **`git rebase --continue`** | 分支名不变，提交被重放成新哈希 |
| `git cherry-pick <sha>` | `On branch xxx` + `You are currently cherry-picking` | `git add` → `git cherry-pick --continue` | 分支不变，追加一个提交 |
| `git stash pop` | `On branch xxx` + 冲突提示 | 手工解决后 `git add`，无需 commit | 分支不变 |

```bash
git status                    # 第一步永远是这个：看首行判断处在哪种流程里
# 编辑冲突文件，搜索 <<<<<<< ======= >>>>>>>，保留正确的一侧或融合两侧
git add <冲突文件>             # 标记已解决
# 按上表收尾：merge 用 commit，rebase 用 --continue
git merge  --abort            # 全退（merge 场景）
git rebase --abort            # 全退（rebase 场景）
```

**要点**
- 冲突是「信息」不是错误，看清两边意图再合并，别无脑选一边。
- 三路合并更清晰：`git config --global merge.conflictStyle diff3`，能同时看到「共同祖先」版本。
- 图形化：`git mergetool`。详见 [[08-Git冲突解决]]。

---

### 十四、救急手册：常见事故与解法

> 每条都标注了**操作时的分支位置**，因为"在哪个分支上执行"往往决定是救命还是闯祸。

#### 1. 代码写错分支了

```bash
# 场景 A：改了文件但还没 commit，当前在 main（不该在的地方）
git branch --show-current          # 确认：main
git stash push -u -m "临时存放"     # 存起来（-u 含未跟踪文件）
git switch feature/user-login      # 切到正确的分支
git stash pop                      # 取回来

# 场景 B：已经 commit 了，但还没 push
git reset --soft HEAD~1            # 撤销提交，改动回到暂存区
git stash push -u && git switch feature/user-login && git stash pop
```

#### 2. 撤销上一次提交

**本地位置**：`feature/user-login`（未推送的提交）

```bash
git reset --soft  HEAD~1   # 改动留在暂存区（想重提）
git reset --mixed  HEAD~1  # 改动回到工作区（默认，想重改重提）
git reset --hard   HEAD~1  # 彻底丢弃分支指针和改动（危险，先看 git reflog 留后路）
```

| 模式 | 分支指针 | 暂存区 | 工作区 |
|------|----------|--------|--------|
| `--soft` | 回退 | 保留 | 保留 |
| `--mixed`（默认） | 回退 | 清空 | 保留 |
| `--hard` | 回退 | 清空 | **清空（丢失！）** |

#### 3. 提交已经推到远端（公共分支）

**本地位置**：`main`（或任何共享分支）

```bash
git revert <sha>            # 生成一个"反向提交"，历史可追溯，安全
git revert -m 1 <merge-sha> # 撤销一个 merge 提交（-m 1 表示保留主线）
git revert --no-commit <sha1>~1..<sha2>  # 撤销一段提交后一次性提交
git push                    # 普通推送即可，不需要强推
```

> **永远不要对公共分支 `reset --hard` + 强推。** 唯一例外：全团队知情且协调一致的紧急事故处理。

#### 4. 找回"丢掉"的提交

**本地位置**：任意（`reflog` 是本地 HEAD 的移动日志）

```bash
git reflog                  # 找到误操作前的那个 sha
git reset --hard <旧sha>    # 整体跳回去（确认没有要保留的未提交改动）
git cherry-pick <sha>       # 或者只把某一个提交拣回当前分支
```

`reflog` 默认保留 90 天（gc 之前），`reset --hard` 过头、误删分支都能救。

#### 5. 误删分支

```bash
git reflog                              # 找到该分支最后一个提交的 sha
git switch -c <分支名> <sha>             # 从该提交重建分支（本地位置：新建分支即为当前分支）
```

#### 6. 临时切换任务 / 半成品不想提交

**本地位置**：`feature/user-login`（有未完成的改动）

```bash
git stash push -u -m "做到一半的登录页"   # 存起来，工作区变干净，分支不变
git switch main                          # 可以随便切去干别的
git switch feature/user-login            # 回来
git stash list                           # 看看存了哪些
git stash pop                            # 恢复并删除该条
git stash apply stash@{1}                # 恢复但保留记录（可在多个分支复用）
```

> `stash` 是跨分支的公共栈，恢复时注意分支对不对；`pop` 到错分支同样会冲突。

#### 7. 撤销矩阵（查这张表就够了）

| 想撤销的东西 | 状态 | 当前分支 | 命令 |
|--------------|------|----------|------|
| 工作区某个文件的改动 | 未暂存 | 任意 | `git restore <file>` |
| 已 `git add` 的暂存 | 已暂存 | 任意 | `git restore --staged <file>` |
| 上一次提交（保留改动） | 已提交·未推送 | 自己的分支 | `git reset --soft HEAD~1` |
| 上一次提交（彻底丢弃） | 已提交·未推送 | 自己的分支 | `git reset --hard HEAD~1` |
| 某次提交（已推送） | 已推送 | 通常 `main` | `git revert <sha>` |
| 回到某个历史版本看看 | 任意 | 任意 | `git switch --detach <sha>`（看完 `git switch -` 回来） |
| 误删的提交 / 分支 | 任意 | 任意 | `git reflog` → `git cherry-pick` / `git reset --hard` |

#### 8. 找出"是谁把这段代码改成这样的"

```bash
git blame <file>              # 逐行看最后修改者与提交
git log -S "关键字"            # 搜索引入/删除该字符串的提交
git bisect start              # 二分法定位引入 bug 的提交
git bisect bad && git bisect good <旧sha>   # 按提示逐轮测试
git bisect reset              # 结束后复位到原分支
```

> `bisect` 期间同样处于**游离 HEAD**，务必记得 `git bisect reset`。

---

### 十五、命令速查表

| 场景 | 命令 |
|------|------|
| 我在哪 | `git status` `git branch --show-current` `git branch -vv` |
| 初始化 | `git init` / `git clone <url>` |
| 看差异 | `git diff` `git diff --staged` `git diff <a> <b>` |
| 看历史 | `git log --oneline --graph --all --decorate` |
| 切分支 | `git switch <name>` `git switch -c <name>` `git switch -` |
| 暂存 | `git add <file>` `git add -p` |
| 提交 | `git commit -m "..."` `git commit --amend` |
| 同步 | `git fetch` `git pull --rebase` `git push` `git push --force-with-lease` |
| 整理 | `git rebase -i HEAD~n` `git rebase --onto A B C` `git cherry-pick <sha>` |
| 暂存栈 | `git stash push -u` `git stash pop` `git stash list` |
| 撤销 | `git restore` `git reset` `git revert` |
| 排查 | `git blame` `git log -S` `git bisect` `git reflog` |

**最推荐记住的一条**：
```bash
git log --oneline --graph --all --decorate
```

---

### 十六、推荐全局配置（一次配好，长期受益）

```bash
git config --global user.name "你的名字"
git config --global user.email "你的邮箱"

git config --global pull.rebase true          # git pull 默认走 rebase
git config --global rebase.autoStash true     # rebase 前自动 stash，结束自动恢复
git config --global push.default current      # 推送到同名远端分支
git config --global fetch.prune true          # 自动清理已删除的远端分支引用
git config --global merge.conflictStyle diff3 # 冲突时显示共同祖先
git config --global init.defaultBranch main
git config --global core.autocrlf input       # 跨平台团队统一换行（Windows 客户端用 true）

git config --global alias.st "status -s"
git config --global alias.br "branch -vv"
git config --global alias.lg "log --oneline --graph --all --decorate"
git config --global alias.last "log -1 --stat"
git config --global alias.unstage "restore --staged"
git config --global alias.amend "commit --amend --no-edit"
```

---

### 十七、AI 辅助编程场景下的额外纪律

用 Cursor / Copilot / 各类 code agent 产出代码时，风险从"写错"变成"看着对但其实没审"：

1. **先 diff 后提交**：AI 一次改十几个文件是常态，必须 `git diff --staged` 逐文件过。
2. **小步分批提交**：让 AI 一次只做一件事，一个提交对应一个意图，出问题好回退。
3. **别照抄 AI 写的提交信息**：自己核对描述与实际改动是否一致。
4. **敏感信息二次确认**：AI 可能把真实配置、内网地址、测试账号写进代码或注释。
5. **生成的代码走独立分支**：`git switch -c ai/refactor-xxx`，评审通过再合入，便于整体放弃。
6. **AI 改写大面积代码前先打点**：`git branch backup/before-ai-<日期>` 或记住当前 sha，一键回退。

---

### 十八、习惯清单

**每天**
- 开工 `git switch main && git pull --rebase`；收工前 `git push`（本地未推送的代码等于没有备份）
- 每天至少 `git fetch origin && git rebase origin/main` 一次，别攒到 PR 那天

**每次提交**
- `git status` → `git diff` → `git diff --staged` → `commit`
- 一个提交一件事，信息写清「为什么」

**每次 rebase 前**
- 看 `git status` 第一行：是不是自己的功能分支？有没有未提交改动？
- 看 `git log --oneline origin/main..HEAD`：即将被重放的是哪些？

**每次强推前**
- 三问：这是公共分支吗？有没有人基于它工作？用 `--force-with-lease` 了吗？

**每周**
- 清理已合并的本地分支与 stash 残留（`git branch -vv` / `git stash list`）
- `git gc` 保持仓库健康（大仓库尤其）

---

### 附录：一次完整任务的分支迁移轨迹

| 步骤 | 命令 | 本地位置（HEAD 所在） | `main` | `feature/x` |
|------|------|----------------------|--------|-------------|
| 1 | `git switch main && git pull --rebase` | `main` | → E | —— |
| 2 | `git switch -c feature/x` | `feature/x` | E | → 新建于 E |
| 3 | 编码 + `git commit` ×2 | `feature/x` | E | E → X → Y |
| 4 | `git fetch origin` | `feature/x` | E | Y（`origin/main` 更新到 G） |
| 5 | `git rebase origin/main` | `feature/x`（中途游离 HEAD） | E | Y → X' → Y'（基点 G） |
| 6 | `git push -u origin feature/x` | `feature/x` | E | Y'（远端同步） |
| 7 | 评审修改 + `--fixup` + `rebase -i` | `feature/x` | E | Y'' |
| 8 | `git push --force-with-lease` | `feature/x` | E | Y''（远端同步） |
| 9 | 远端合并 PR | `feature/x` | E | Y''（`origin/main` → M） |
| 10 | `git switch main && git pull --rebase` | `main` | E → M | Y'' |
| 11 | `git branch -d feature/x` | `main` | M | 已删除 |

> 全程 `main` 只在第 1、10 步动过，**功能开发期间主干零改动**——这就是分支工作流的核心。

## 相关
- [[01-Git概览]]
- [[02-Git核心概念]]
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
