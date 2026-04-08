# 核心概念

> 理解 OpenClaw 的底层逻辑

---

## 🎯 核心概念速览

| 概念 | 说明 | 文档 |
|------|------|------|
| **梦境系统** | AI 后台整理记忆 | [dreaming.md](./dreaming.md) ⭐ 新功能 |
| **记忆系统** | 三层记忆架构 | [memory.md](./memory.md) |
| **技能系统** | 49,035 技能库 | [../skills/README.md](../skills/README.md) |
| **渠道系统** | 多渠道沟通 | [../channels/README.md](../channels/README.md) |

---

## 🌙 梦境系统（Dreaming）

**让 AI 在"睡觉时"自动整理记忆**

### 三阶段模型

| 阶段 | 功能 | 写入位置 |
|------|------|----------|
| **Light（浅睡）** | 整理短期记忆 | 不写入 MEMORY.md |
| **Deep（深睡）** ⭐ | 评分并提升长期记忆 | **MEMORY.md** |
| **REM（快速眼动）** | 反思主题和重复想法 | 不写入 MEMORY.md |

### 启用方法

```bash
/dreaming on      # 启用梦境系统
/dreaming status  # 查看状态
```

详细文档: [dreaming.md](./dreaming.md)

---

## 💾 记忆系统（Memory）

### 三层记忆架构

| 层级 | 存储 | 用途 |
|------|------|------|
| **第一层** | Mem0 向量记忆 | 快速检索 |
| **第二层** | 文件记忆（MEMORY.md） | 长期保留 |
| **第三层** | 关系图谱 | 跨时间检索 |

详细文档: [memory.md](./memory.md)

---

## 🧠 人格怔流（Soul）

**让 AI 拥有独特人格**

| Skill | 功能 |
|-------|------|
| AI Persona OS | 13个角色灵魂 |
| SoulCraft | SOUL.md 编辑 |
| Personality Switcher | 人格切换 |

详细文档: [../skills/soul-personality.md](../skills/soul-personality.md)

---

## 🧬 自我进化（Self-Improving）

**让 AI 从错误中学习**

| 机制 | 说明 |
|------|------|
| 错误记录 | .learnings/ERRORS.md |
| 纠正学习 | .learnings/LEARNINGS.md |
| 进化升级 | AGENTS.md/SOUL.md |

详细文档: [../skills/self-improving.md](../skills/self-improving.md)

---

## 🔗 相关文档

- [技能指南](../skills/README.md)
- [工具命令](../tools/README.md)

---

更新时间：2026-04-09