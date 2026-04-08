# 🌙 OpenClaw 梦境系统（Dreaming）

> 让 AI 在"睡觉时"自动整理记忆，第二天更聪明

---

## 🎯 什么是梦境系统？

**梦境系统**是 OpenClaw 的后台记忆整合功能。

就像人类睡觉时会整理白天的记忆一样，AI 也可以在后台自动：
- ✅ 整理短期记忆素材
- ✅ 评分决定哪些值得长期保留
- ✅ 提升重要内容到长期记忆（MEMORY.md）
- ✅ 反思主题和重复出现的想法

---

## 🔄 三阶段模型

| 阶段 | 功能 | 写入位置 |
|------|------|----------|
| **Light（浅睡）** | 整理短期记忆素材 | 不写入 MEMORY.md |
| **Deep（深睡）** ⭐ | 评分并提升长期记忆 | **MEMORY.md** |
| **REM（快速眼动）** | 反思主题和重复想法 | 不写入 MEMORY.md |

---

## 📊 Deep 评分信号

Deep 阶段用 **6 个加权信号**决定哪些记忆值得保留：

| 信号 | 权重 | 说明 |
|------|------|------|
| **频率** | 24% | 出现次数 |
| **相关性** | 30% | 检索质量 |
| **查询多样性** | 15% | 不同场景触发次数 |
| **新鲜度** | 15% | 时间衰减分数 |
| **巩固度** | 10% | 多天重复强度 |
| **概念丰富度** | 6% | 概念标签密度 |

---

## 📝 输出文件

| 文件 | 内容 | 人类可读？ |
|------|------|------------|
| `memory/.dreams/` | 机器状态（recall store、phase signals） | ❌ |
| `DREAMS.md` | 梦境日记 | ✅ ⭐ |
| `MEMORY.md` | 长期记忆 | ✅ ⭐ |

---

## 🚀 如何启用

### 方法一：配置文件

在 `~/.copaw/config.json` 中添加：

```json
{
  "plugins": {
    "entries": {
      "memory-core": {
        "config": {
          "dreaming": {
            "enabled": true
          }
        }
      }
    }
  }
}
```

### 方法二：Slash 命令

```bash
/dreaming on      # 启用梦境系统
/dreaming off     # 关闭梦境系统
/dreaming status  # 查看状态
/dreaming help    # 查看帮助
```

### 方法三：CLI 命令

```bash
# 预览记忆提升候选
openclaw memory promote

# 执行记忆提升
openclaw memory promote --apply

# 限制提升数量
openclaw memory promote --limit 5

# 查看记忆状态
openclaw memory status --deep
```

---

## ⏰ 默认运行时间

默认每天凌晨 3:00 自动运行：

```json
{
  "dreaming": {
    "frequency": "0 3 * * *"  // 每天 3:00
  }
}
```

可自定义（如每 6 小时）：

```json
{
  "dreaming": {
    "frequency": "0 */6 * * *"  // 每 6 小时
  }
}
```

---

## 🎨 Dreams UI

启用后，Gateway 网页界面会显示 **Dreams 标签页**：

- 当前梦境系统状态
- 各阶段状态
- 短期/长期/今日提升数量
- 下次运行时间
- 梦境日记阅读器

---

## 💡 小白常见问题

### Q1: 梦境系统会占用很多资源吗？

**不会**。它是后台轻量级任务，默认凌晨 3 点运行，不影响日常使用。

### Q2: 我能看到 AI "梦见"了什么吗？

**可以**！查看 `DREAMS.md` 文件，里面是人类可读的梦境日记。

### Q3: 梦境系统会把隐私内容写入 MEMORY.md 吗？

**不会**。敏感内容会被过滤，只保留有价值的信息。

### Q4: 我可以手动触发梦境系统吗？

**可以**！使用命令：

```bash
openclaw memory promote --apply
```

### Q5: 梦境系统默认启用吗？

**默认关闭**。需要手动启用（`/dreaming on`）。

---

## 🔗 相关资源

- [主仓库文档](https://github.com/openclaw/openclaw/blob/main/docs/concepts/dreaming.md)
- [Memory 配置参考](https://github.com/openclaw/openclaw/blob/main/docs/reference/memory-config.md)
- [Memory CLI](https://github.com/openclaw/openclaw/blob/main/docs/cli/memory.md)

---

更新时间：2026-04-09