# 🧬 自我进化 Skill（Self-Improving）

> 让 AI 从错误中学习，持续进化提升

---

## 📊 分类概览

| 指标 | 数值 |
|------|------|
| **技能数** | 10+ |
| **总下载量** | 600k+ |
| **最热门** | self-improving-agent (365k downloads) ⭐ |

---

## 🔥 Top 5 自我进化 Skill

| 排名 | 技能名 | 下载量 | Stars | 功能 |
|------|--------|--------|-------|------|
| 1 | **self-improving-agent** ⭐⭐⭐ | 365k | 3.1k | 自我进化框架（ClawHub 第一名） |
| 2 | **Self-Improving + Proactive Agent** ⭐⭐⭐ | 152k | - | 进化 + 主动型 Agent |
| 3 | **Proactive Agent** ⭐⭐ | 137k | - | 主动型 Agent（不需用户触发） |
| 4 | **Self** ⭐ | 1.4k | - | 自我观察人格发展 |
| 5 | **Learning Journal** | 890 | - | 学习日志记录 |

---

## 🎯 self-improving-agent 详解

### 核心功能

**ClawHub 下载量第一的技能，3.1k stars**

**四大核心机制**：

| 机制 | 触发条件 | 记录位置 | 作用 |
|------|----------|----------|------|
| **错误记录** | 操作失败 | .learnings/ERRORS.md | 避免重复踩坑 |
| **纠正学习** | 用户纠正我 | .learnings/LEARNINGS.md | 吸收用户反馈 |
| **知识空白** | 发现不懂的 | .learnings/LEARNINGS.md | 标记待学习内容 |
| **洞察提炼** | 新洞察 | .learnings/LEARNINGS.md | 记录深刻认知 |

### 进化升级规则

```
广泛适用的学习 → 提升到 AGENTS.md（工作流改进）
工具陷阱 → 提升到 MEMORY.md（教训 section）
行为模式 → 提升到 SOUL.md（风格定义）
```

### 安装命令

```bash
claw install self-improving-agent
```

### 目录结构

```
.learnings/
├── LEARNINGS.md         # 纠正、洞察、最佳实践、知识空白
├── ERRORS.md            # 命令失败、API错误、集成问题
└── FEATURE_REQUESTS.md  # 用户请求的功能
```

### 记录格式

```markdown
## [LRN-YYYYMMDD-XXX] category

**Logged**: ISO-8601 timestamp
**Priority**: low | medium | high | critical
**Status**: pending | integrated
**Area**: frontend | backend | infra | tools | docs | config

### Summary
One-line description

### Details
Full context

### Suggested Action
Specific fix

### Metadata
- Source: conversation | error | user_feedback
- Related Files: path/to/file.ext
- Tags: tag1, tag2
```

---

## 🎯 Proactive Agent 详解

### 核心功能

**主动型 Agent，不需要用户触发也能行动**

**核心能力**：
- 监控系统状态
- 主动发现问题
- 自主执行修复
- 主动提供建议

**安装命令**：
```bash
claw install proactive-agent
```

---

## 📋 快速安装指南

### 小白必装

```bash
claw install self-improving-agent  # 自我进化（必装）⭐⭐⭐
claw install proactive-agent       # 主动型 Agent ⭐⭐
```

### 进阶推荐

```bash
claw install self-improving-proactive-agent  # 进化 + 主动
```

---

## 🔄 自我进化工作流

```text
┌─────────────────────────────────────────────────────────────┐
│                    自我进化完整工作流                    │
├─────────────────────────────────────────────────────────────┤
│                                                            │
│   ┌─────────┐      ┌─────────────┐      ┌─────────────┐    │
│   │ 任务执行 │ ───→ │ 成功/失败？ │ ───→ │ 记录结果    │    │
│   └─────────┘      └─────────────┘      └─────────────┘    │
│        │                  │                    │           │
│        │                  │ 失败               │           │
│        │                  ↓                    ↓           │
│        │            ┌─────────────┐      ┌─────────────┐   │
│        │            │ 记录到      │      │ 分析原因    │   │
│        │            │ ERRORS.md   │      │             │   │
│        │            └─────────────┘      └─────────────┘   │
│        │                                        │          │
│        │ 用户纠正                               │ 洞察     │
│        ↓                                        ↓          │
│   ┌─────────────┐                        ┌─────────────┐   │
│   │ 记录到      │                        │ 提升到      │   │
│   │ LEARNINGS.md│                        │ AGENTS.md   │   │
│   └─────────────┘                        └─────────────┘   │
│                                                            │
└─────────────────────────────────────────────────────────────┘
```

---

## ⚠️ 注意事项

1. **定期清理** — .learnings/ 目录会积累，建议每月清理已集成的记录
2. **隐私保护** — 不要在 .learnings/ 中记录敏感信息
3. **进化频率** — 默认每天检查一次，可在 Heartbeat 中调整
4. **备份** — 重要学习记录应备份到 MEMORY.md

---

## 🔗 相关资源

- [Self-Improving Agent GitHub](https://github.com/peterskoett/self-improving-agent) (414 stars)
- [Proactive Agent 文档](https://clawhub.ai/skills/proactive-agent)
- [ClawHub 自我进化分类](https://clawhub.ai/skills?search=self-improving)

---

更新时间：2026-04-09