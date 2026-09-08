# 六维评审清单（详细版）

> 供 `code-review-gate` 技能在评审时按需读取。
> 每一维给出「检查项 + 反例 + 正例」，评审时逐条对照。

---

## 🔴 维度一：安全

### 检查项

- [ ] **注入类**：SQL / NoSQL / 命令 / 模板 / LDAP 注入——是否使用参数化查询或预编译语句？
- [ ] **越权**：是否校验了当前用户对资源的操作权限（水平越权 + 垂直越权）？
- [ ] **XSS**：输出到 HTML / DOM 的用户数据是否转义？`innerHTML`、`dangerouslySetInnerHTML`、`v-html` 是否有白名单？
- [ ] **CSRF**：状态变更接口是否有 token / SameSite / 自定义头校验？
- [ ] **认证鉴权**：是否有未鉴权的接口、硬编码的绕过逻辑（`if (user === 'admin')`）？
- [ ] **反序列化**：是否反序列化不可信数据？是否有类型白名单？
- [ ] **文件上传**：是否校验类型、大小、路径（防 `../` 穿越）、是否重命名？
- [ ] **随机数**：安全相关场景（token、盐、session id）是否用了密码学安全随机源？
- [ ] **加密**：是否用了已废弃算法（MD5、SHA1、DES、ECB 模式）？IV 是否随机？

### 反例 / 正例

```js
// ❌ SQL 注入
const sql = `SELECT * FROM users WHERE name = '${req.query.name}'`;

// ✅ 参数化
const sql = 'SELECT * FROM users WHERE name = ?';
db.query(sql, [req.query.name]);
```

```js
// ❌ 越权：只验证登录，不验证资源归属
app.get('/orders/:id', auth, (req, res) => Order.findById(req.params.id));

// ✅ 校验归属
app.get('/orders/:id', auth, async (req, res) => {
  const order = await Order.findOne({ _id: req.params.id, userId: req.user.id });
  if (!order) return res.status(404).end();
});
```

```js
// ❌ XSS
el.innerHTML = userInput;

// ✅ 转义 / 白名单
el.textContent = userInput;
```

---

## 🔴 维度二：敏感信息泄露

### 检查项

- [ ] **密钥凭据**：是否硬编码 AK/SK、token、私钥、连接串？（应走环境变量或配置中心）
- [ ] **日志**：是否打印了完整请求体、响应体、用户对象、token？
- [ ] **错误信息**：生产环境是否把堆栈、SQL、内网 IP 返回给前端？
- [ ] **个人信息**：身份证、手机号、银行卡、住址、生物特征是否明文存储或输出？
- [ ] **前端泄露**：`localStorage` / cookie 里是否存了不该存的敏感数据？
- [ ] **注释与文档**：是否有把真实账号密码写进注释或 README 的样例？
- [ ] **调试代码**：是否遗留了 `console.log`、调试接口、测试后门？

### 反例 / 正例

```js
// ❌ 打印完整请求体（可能含身份证号）
logger.info('收到请求', req.body);

// ✅ 白名单 + 脱敏
logger.info('收到请求', { userId: req.body.userId, action: req.body.action });
logger.info('手机号', maskPhone(req.body.phone));
```

```js
// ❌ 堆栈直达前端
catch (e) { res.status(500).json({ error: e.stack }); }

// ✅ 对内记录、对外脱敏
catch (e) {
  logger.error('[reqId=%s] 处理失败', reqId, e);
  res.status(500).json({ error: '服务异常，请联系管理员', reqId });
}
```

---

## 🔴 维度三：合规

### 检查项

- [ ] **数据出境**：是否调用境外 API、加载境外 CDN / 字体 / SDK、上报遥测到境外？
- [ ] **云服务区域**：是否指定了境外 region？
- [ ] **第三方依赖来源**：是否来自内网源？新增依赖是否经过审批？
- [ ] **行业规定**：是否违反所在行业（政府 / 工业 / 水务）的等保、数据安全要求？
- [ ] **数据留存**：是否按规定的期限与方式存储和销毁数据？
- [ ] **审计留痕**：关键操作是否有日志记录、是否可追溯？
- [ ] **AI 生成内容标注**：AI 产出的代码是否按规范留痕？

> 本维度建议配合 `data-compliance-guard` 技能自动扫描。

---

## 🟠 维度四：性能

### 检查项

- [ ] **N+1 查询**：循环里查数据库 / 调接口？应批量查询或预加载
- [ ] **循环内 IO**：循环里读写文件、发网络请求、开事务？
- [ ] **无界内存**：一次性 `SELECT *` 大表、把大文件读进内存、无限增长的缓存（无 TTL / 无上限）
- [ ] **索引**：新增查询条件的字段是否有索引？是否索引失效（函数包裹、隐式转换、`LIKE '%x'`）？
- [ ] **前端渲染**：长列表是否虚拟滚动？是否有不必要的全量重渲染？
- [ ] **包体积**：是否引入了大库却只用了一个函数？（应按需引入）
- [ ] **并发**：是否有竞态、是否需要加锁、是否重复请求（缺防抖节流）？
- [ ] **超时与重试**：外部调用是否有超时？重试是否有退避与上限？

### 反例 / 正例

```js
// ❌ N+1
for (const u of users) {
  u.orders = await db.orders.find({ userId: u.id });
}

// ✅ 批量 + 内存聚合
const ids = users.map(u => u.id);
const orders = await db.orders.find({ userId: { $in: ids } });
const byUser = groupBy(orders, 'userId');
users.forEach(u => { u.orders = byUser[u.id] ?? []; });
```

```js
// ❌ 循环内 await IO
for (const f of files) await fs.writeFile(f.path, f.content);

// ✅ 并发
await Promise.all(files.map(f => fs.writeFile(f.path, f.content)));
```

---

## 🟡 维度五：可维护性

### 检查项

- [ ] **命名**：是否见名知义？布尔值是否用 `is/has/should` 前缀？是否避免了 `data`、`info`、`temp`、`flag` 这类空洞词
- [ ] **函数长度与复杂度**：单个函数是否过长？嵌套是否过深（>4 层考虑早返回）？
- [ ] **单一职责**：一个函数/类是否做了多件事？
- [ ] **重复代码**：是否出现三次以上相同逻辑？（三次原则）
- [ ] **错误处理**：是否吞掉异常（空 `catch`）？是否区分可恢复与不可恢复错误？
- [ ] **魔法值**：硬编码的数字/字符串是否提为常量或配置？
- [ ] **注释**：注释是否解释「为什么」而非重复「做了什么」？是否有过期注释？
- [ ] **边界处理**：空值、空数组、极值、非法输入是否处理？
- [ ] **类型**：是否滥用 `any` / 类型断言？公共 API 是否有类型注解？
- [ ] **测试**：改动是否可测？是否补充了测试？

### 反例 / 正例

```js
// ❌ 嵌套地狱 + 魔法值
function check(u) {
  if (u) { if (u.age) { if (u.age > 18) { if (u.type === 3) { return true; } } } }
  return false;
}

// ✅ 早返回 + 常量
const ADULT_AGE = 18;
const USER_TYPE_ENTERPRISE = 3;

function isEnterpriseAdult(user) {
  if (!user?.age) return false;
  if (user.age <= ADULT_AGE) return false;
  return user.type === USER_TYPE_ENTERPRISE;
}
```

```js
// ❌ 吞异常
try { risky(); } catch (e) {}

// ✅ 至少记录
try { risky(); } catch (e) {
  logger.warn('清理缓存失败，不影响主流程', e);
}
```

---

## 🟡 维度六：依赖

### 检查项

- [ ] **必要性**：这个依赖真的需要吗？能否用标准库或几十行代码解决？
- [ ] **健康度**：是否还在维护？最近一次发布是什么时候？issue 是否堆积？
- [ ] **已知漏洞**：是否有 CVE？（跑 `npm audit` / `pnpm audit` / `pip-audit`）
- [ ] **许可证**：是否与公司政策冲突？（GPL 系需谨慎）
- [ ] **体积**：是否过大？是否支持 tree-shaking / 按需引入？
- [ ] **传递依赖**：它拖进来了多少间接依赖？
- [ ] **来源**：是否来自内网源？能否锁定版本？
- [ ] **幻觉依赖**（评审 AI 代码时重点）：包是否真实存在？API 签名是否正确？

### 检查命令

```bash
# Node
npm audit --production
npm ls <package-name>

# Python
pip-audit
pip show <package-name>
```

---

## 评审 AI 生成代码的额外检查项

AI 产出有固定的失效模式，**评审时必须额外看**：

| 风险 | 检查方式 |
|------|---------|
| **幻觉依赖** | 引用的包/API 是否真实存在？版本是否存在？ |
| **幻觉 API** | 调用的方法签名是否与当前版本一致？ |
| **过度设计** | 是否引入了用不上的抽象、配置、扩展点？ |
| **静默兜底** | 是否用 `?? []`、`catch {}` 掩盖了真实错误？ |
| **合规引入** | 是否顺手引了境外 CDN、字体、遥测？ |
| **假装验证** | 声称「已测试」但实际没跑——**要求给出真实执行输出** |
| **上下文错位** | 是否改了不该改的文件、是否偏离需求范围？ |
