---
title: "20-Skill后端试用：在 sjz-back 项目上套用推荐 Skill"
created: 2026-09-09
updated: 2026-09-09
tags: [AI, Agent, Skill, Cursor, 试用, 代码审查, SQL注入, 事务, sjz-back, MySQL, Redis]
sources: [E:/guojian/01project/sjz/sjz-back/.agents/skills, https://www.skills.sh/]
---

# 20-Skill后端试用：在 sjz-back 项目上套用推荐 Skill

> 目的：验证 [[16-程序员推荐安装的Skill]] 里推荐、并已实际安装到 `E:\guojian\01project\sjz\sjz-back` 的技能，能否在真实代码上发现问题、指导修复。

## 一、关于"调用 Cursor"的说明（重要）

用户要求"调用 Cursor 在 sjz-back 使用这些 skill 完成工作"。实测本机环境后结论：

- Cursor 安装目录 `D:\apps\cursor` 下**只有 IDE 内部 agent 运行时扩展**（`cursor-agent-exec` / `cursor-agent-host` / `cursor-agent-worker` / `cursor-local-agent-runtime`），**没有可程序化拉起的非交互 CLI 入口**。
- `cursor` 主命令是 IDE 启动器，参数仅支持 `diff` / `merge` / 打开文件，**不支持** `--agent` / `--ask` / `--run` / `--headless` / `--non-interactive`。
- 因此**无法从命令行让 Cursor 自动跑 agent 审查代码**。

**替代做法（等价且更可审计）**：直接读取项目 `.agents/skills/` 下已安装的 21 个 SKILL.md **规则原文**，逐条套到 sjz-back 真实代码做静态分析。这等同于"让 agent 按 skill 规则审查"，且结果可复现、可定位。

> 若要在你的环境真正跑起来：在 Cursor IDE 内打开 sjz-back，用 Chat 输入"按 mysql-patterns / code-quality 审查 alarm_major_rule 相关代码"，或在 `.cursorrules`/`.agents` 里引用这些 skill，由 IDE 内的 agent 调用。本文件记录的是不依赖 IDE 的离线验证结果。

## 二、已安装技能（取自 sjz-back/skills-lock.json，共 21 个）

| 来源仓库 | 技能 |
|---------|------|
| **affaan-m/ecc**（⭐253k） | `backend-patterns`、`mysql-patterns`、`redis-patterns`、`java-coding-standards`、`database-migrations`、`database-optimizer`、`springboot-patterns`、`springboot-security`、`springboot-verification` |
| **piomin/claude-ai-spring-boot**（⭐1.3k） | `code-quality`、`design-patterns`、`java-architect`、`logging-patterns`、`spring-boot` |
| **jeffallan/claude-skills**（⭐11.4k） | `java-architect`、`spring-boot-engineer`、`database-optimizer`、`sql-pro` |
| **github/awesome-copilot**（⭐38.8k） | `create-spring-boot-java-project`、`java-springboot`、`sql-code-review`、`sql-optimization` |
| **wshobson/agents**（⭐39.5k） | `sql-optimization-patterns` |

> 后端项目故只装了后端/SQL 类技能，未装前端（vue/antfu 等）系列。要不要补前端技能用于 sjz 前端仓库，见 [[16-程序员推荐安装的Skill]]。

## 三、试用方法

1. 从 `skills-lock.json` 导出已装技能清单（21 个）。
2. 读取每个 SKILL.md 的 frontmatter `description` 与正文规则（已读 `mysql-patterns` / `redis-patterns` / `code-quality` / `java-architect` 全文）。
3. 用规则逐项扫描代码：
   - `mysql-patterns` → SQL 注入、SELECT *、深分页、索引、长事务
   - `code-quality` / `java-coding-standards` → 日志、异常处理、空安全、复杂度
   - `java-architect` → 事务与数据一致性、多写无事务
   - `redis-patterns` → 键命名、TTL、连接池、防击穿
4. 对每条"命中"记录**文件:行号**证据链，区分"真实缺陷"与"合规建议"。

## 四、试用结果

### 4.1 🔴 严重：SQL 注入风险（mysql-patterns / sql-code-review 命中）

`mysql-patterns` 规则明确：值位置必须用预编译 `#{}`，`${}` 仅用于动态表名/排序字段这类**标识符**场景，绝不用于值。

扫描发现 **2 处值在 `where`/`delete` 中直接 `${}` 拼接**：

| 文件:行 | 代码 | 风险 |
|--------|------|------|
| `hi-libs/hi-lib-alarm/.../dao/MajorAlarmMapper.xml:247` | `delete from alarm_major_rule where id = ${id}` | id 直接拼 SQL |
| `hi-libs/hi-lib-alarm/.../dao/MajorAlarmMapper.xml:318` | `delete from alarm_major_broadcast where id = ${id}` | 同上 |

**证据链（247 行那条）**：
```
MajorAlarmServiceImpl.java:261  public int deleteAlarmConfig(Map<String,Object> param) {
MajorAlarmServiceImpl.java:262      Long id = Long.valueOf((Integer) param.get("id"));  // id 来自外部请求参数
MajorAlarmServiceImpl.java:263      int i = majorAlarmMapper.deleteMajorAlarmConfigById(id);
MajorAlarmServiceImpl.java:264      pointService.remove(...getRuleId, id);   // 第二步：删关联点表
MajorAlarmServiceImpl.java:265      return i;
MajorAlarmMapper.xml:247            delete from alarm_major_rule where id = ${id}   // 字符串拼接
```
- `id` 由 `param.get("id")` 取得（外部可控）。
- 虽然此处做了 `Long.valueOf` 强转，但 **`${}` 在 MyBatis 中是纯字符串替换**，绕过预编译；一旦调用方改为传 String 或去掉强转（重构、新 Controller 复用该方法），即构成可注入点。
- 正确写法应为 `#{id}`，`parameterType="java.lang.Long"` 已声明，无需 `${}`。

> 注：全项目 `${}` 共 236 处，绝大多数是 `order by ${column}`、`${tableName}` 这类**合法标识符**用法，只有这 2 处是值位置，须整改。

### 4.2 🟠 高：多步写操作无事务（java-architect / code-quality 命中）

`java-architect` 规则：跨多表/多步写操作必须用 `@Transactional` 保证原子性，否则中间失败会留孤儿数据。

- 全项目 `ServiceImpl` 共 **142** 个，**完全无 `@Transactional` 的 131** 个。
- 其中**多写操作（≥2 次写）却无 `@Transactional` 的 16** 个，`MajorAlarmServiceImpl` 是典型（7 次写操作无事务）。

上面 4.1 的 `deleteAlarmConfig` 正是反面教材：先删 `alarm_major_rule`、再删关联 `AlarmMajorPoint`，两步**无 `@Transactional`**——若第二步 `pointService.remove` 抛异常，规则表已删而点表残留，产生数据不一致。

### 4.3 🟡 中：SELECT * 与深分页（mysql-patterns 命中）

| 问题 | 数量 | 规则依据 |
|------|------|---------|
| `select *`（Mapper XML） | **24 个文件** | 返回多余列、索引失效、DTO 映射脆弱 |
| `LIMIT offset, size` 深分页手写 | **3 处** | `mysql-patterns` 推荐 keyset/游标分页（`LIMIT ?,?` 大 offset 全表扫描） |

深分页位置：`ConstVariableTypeMapper.xml`、`BaseDictTypeMapper.xml`、`EmpEnergyPriceMapper.xml`。

### 4.4 🟡 中：代码质量（code-quality / java-coding-standards 命中）

| 反模式 | 文件数 | 建议 |
|--------|--------|------|
| `System.out.println` | **30** | 改用 SLF4J/Logback（项目已引入 `logging-patterns`） |
| `printStackTrace()` | **38** | 包装为业务异常 + 日志，禁止吞栈 |

`code-quality` 审查策略要求按 **Critical → Minor → Good** 分级，`System.out`/栈打印属 Minor，但 30/38 的高散落度说明缺乏统一日志门禁。

### 4.5 🟢 良好：Redis 使用收口（redis-patterns 评估）

`redis-patterns` 规则：键命名 `resource:id:field`、必须设 TTL、连接池、防击穿。

- Redis 使用仅 **4 个文件**，全部集中在 `hi-libs-redis` 模块的 `RedisConfig` / `RedisUtil`，说明项目**已对 Redis 访问做了统一封装**（符合"集中管理"思想，优于散落各处的 `RedisTemplate`）。
- 建议后续核查 `RedisUtil` 的 key 是否带**业务命名空间前缀**（如 `sjz:xxx:123`），以及缓存写入是否 `setex` 带 TTL（防 `redis-patterns` 列出的 "Keys with no TTL" 反模式）。

### 4.6 分页现状

- `MyBatis-Plus Page/IPage`：**86 个文件**（主流）
- `PageHelper.startPage`：**0**（未用）
- 结论：项目已统一走 MyBatis-Plus 分页，深分页 4.3 应改用 `IPage` + 索引游标，而非手写 `LIMIT ?,?`。

## 五、修复建议（直接可落）

```xml
<!-- 1) SQL 注入：MajorAlarmMapper.xml:247 / :318 -->
<!-- 改前 --> delete from alarm_major_rule where id = ${id}
<!-- 改后 --> delete from alarm_major_rule where id = #{id}
```

```java
// 2) 事务：MajorAlarmServiceImpl.deleteAlarmConfig
@Override
@Transactional(rollbackFor = Exception.class)   // 补事务，两步写原子化
public int deleteAlarmConfig(Map<String, Object> param) {
    Long id = Long.valueOf((Integer) param.get("id"));
    int i = majorAlarmMapper.deleteMajorAlarmConfigById(id);
    pointService.remove(Wrappers.<AlarmMajorPoint>lambdaQuery().eq(AlarmMajorPoint::getRuleId, id));
    return i;
}
```

```sql
-- 3) 深分页：EmpEnergyPriceMapper 等改用 keyset 游标
-- 改前：SELECT ... FROM t ORDER BY id LIMIT #{offset}, #{size}
-- 改后：WHERE id > #{lastId} ORDER BY id ASC LIMIT #{size}
```

```
4) 日志：30 处 System.out / 38 处 printStackTrace → 统一 SLF4J
5) SELECT *（24 文件）→ 显式列名，配合 resultMap
```

## 六、结论

1. **这批 skill 真实可用**。规则原文（ECC 的 mysql/redis-patterns、piomin 的 code-quality/java-architect）能在你们 1397 个 Java 文件、100 个 Mapper 的真实代码上**精准命中问题**：最严重的是 2 处 SQL 注入 + 16 处多写无事务，都是合规审计重点。
2. **最高优先修**：`MajorAlarmMapper.xml` 两处 `${id}` 注入（改 `#{}`）+ `deleteAlarmConfig` 补 `@Transactional`。
3. **方法论建议**：把 `code-quality` / `java-architect` 设为 **Cursor 评审门禁**（PR 前自动跑），把 `mysql-patterns` 的 `#{}` / 禁 `SELECT *` 写成 **MyBatis 检查规则**（Checkstyle/自定义 lint），比人工审查稳。
4. **未验证项**：前端技能（vue/antfu）未在此后端项目试用；`design-patterns` / `sql-optimization` 等偏设计/性能优化的技能，本次只做了存在性确认，未逐条生成重构方案（可作为下一轮"设计评审"试用）。

> ⚠️ 数据时点：2026-09-09，基于 sjz-back 当前代码静态扫描。注入点已确认 `id` 来自外部参数，建议上线前修复。
