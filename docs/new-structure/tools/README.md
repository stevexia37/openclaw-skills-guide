# 工具命令

> OpenClaw CLI 命令速查

---

## 🛠️ 常用命令

### 技能管理

| 命令 | 说明 |
|------|------|
| `claw search 关键词` | 查找技能 |
| `claw install skill-name` | 安装技能 |
| `claw list` | 查看已安装 |
| `claw update skill-name` | 更新技能 |
| `claw remove skill-name` | 删除技能 |

### 记忆管理

| 命令 | 说明 |
|------|------|
| `openclaw memory status` | 查看记忆状态 |
| `openclaw memory promote` | 预览提升候选 |
| `openclaw memory promote --apply` | 执行提升 |

### 梦境系统

| 命令 | 说明 |
|------|------|
| `/dreaming on` | 启用梦境系统 |
| `/dreaming off` | 关闭梦境系统 |
| `/dreaming status` | 查看状态 |

### 渠道管理

| 命令 | 说明 |
|------|------|
| `openclaw channel list` | 查看渠道 |
| `openclaw channel add` | 添加渠道 |

---

## 💡 命令技巧

### 技能安装批量

```bash
# 安装必装技能
claw install self-improving-agent cron pdf whisper browser
```

### 记忆提升限制

```bash
# 限制提升数量
openclaw memory promote --limit 5
```

---

## 🔗 相关文档

- [技能指南](../skills/README.md)
- [概念解释](../concepts/README.md)

---

更新时间：2026-04-09