# OpenClaw 小白速通指南

> 一篇搞定：安装 + 配对 + 常见问题 + 必装技能

---

## 🎯 5 分钟快速上手

### 第一步：下载安装

| 系统 | 下载地址 |
|------|----------|
| macOS | [GitHub Releases](https://github.com/openclaw/openclaw/releases) |
| Windows | [GitHub Releases](https://github.com/openclaw/openclaw/releases) |
| Linux | `curl -fsSL https://get.openclaw.ai | sh` |

### 第二步：获取配对码

1. 打开 OpenClaw
2. 点击「配对」按钮
3. 记下 **配对码**（如 `BHT9-P4UW`）
4. 在手机/网页输入配对码

### 第三步：选择渠道

| 渠道 | 配置难度 | 推荐 |
|------|----------|------|
| **飞书** | ⭐ 简单 | ⭐⭐⭐ 企业用户首选 |
| Telegram | ⭐⭐ 中等 | ⭐⭐ 技术用户 |
| 钉钉 | ⭐⭐ 中等 | ⭐ 国内企业 |
| Discord | ⭐⭐ 中等 | ⭐ 海外用户 |

---

## ❓ 常见问题速查

### 安装报错

| 报错 | 解决方案 |
|------|----------|
| `macOS提示"已损坏"` | `sudo xattr -cr /Applications/OpenClaw.app` |
| `配对失败` | 检查网络、重启 App、确认配对码正确 |
| `无法连接` | 检查防火墙、代理设置 |

### 渠道配置

| 渠道 | 关键配置 |
|------|----------|
| **飞书** | App ID + App Secret |
| Telegram | Bot Token |
| 钉钉 | Client ID + Client Secret |

---

## 🔥 必装技能 Top 10

| 技能 | 下载量 | 功能 | 安装命令 |
|------|--------|------|----------|
| **self-improving-agent** | 365k | 自我进化 ⭐⭐⭐ | `claw install self-improving-agent` |
| **cron** | 50k+ | 定时提醒 ⭐⭐⭐ | `claw install cron` |
| **pdf** | 65k | PDF 处理 ⭐⭐ | `claw install pdf` |
| **whisper** | 68k | 语音转文字 ⭐⭐ | `claw install whisper` |
| **xlsx** | 30k+ | Excel 处理 ⭐ | `claw install xlsx` |
| **browser** | 40k+ | 浏览器自动化 ⭐⭐ | `claw install browser` |
| **ai-persona-os** | 8.9k | 13个角色灵魂 ⭐⭐⭐ | `claw install ai-persona-os` |
| **soulcraft** | 3.4k | SOUL.md 编辑 ⭐⭐⭐ | `claw install soulcraft` |
| **multi-search** | 30k+ | 多引擎搜索 ⭐ | `claw install multi-search` |
| **git-helper** | 40k+ | Git 辅助 ⭐⭐ | `claw install git-helper` |

---

## 🌙 新功能：梦境系统

**让 AI 在"睡觉时"自动整理记忆**

| 阶段 | 功能 |
|------|------|
| Light（浅睡） | 整理短期记忆 |
| Deep（深睡） ⭐ | 提升长期记忆（MEMORY.md） |
| REM（快速眼动） | 反思主题和重复想法 |

**启用方法**：
```bash
/dreaming on      # 启用梦境系统
/dreaming status  # 查看状态
```

---

## 🧠 人格怔流 Skill

**让 AI 拥有灵魂和性格**

| Skill | 功能 | 包含角色 |
|-------|------|----------|
| **AI Persona OS** | 13个角色灵魂库 | Thanos、Deadpool、JARVIS、Tony Stark... |
| **SoulCraft** | 创建或改进 SOUL.md | 赋予 AI 人格 |
| **Personality Switcher** | 动态切换人格 | 工作/晚间/专注/创意模式 |

---

## 🧬 自我进化 Skill

**让 AI 从错误中学习**

| 机制 | 说明 |
|------|------|
| 错误记录 | 操作失败 → .learnings/ERRORS.md |
| 纠正学习 | 用户纠正 → .learnings/LEARNINGS.md |
| 进化升级 | 广泛适用的学习 → AGENTS.md/SOUL.md |

---

## 📊 技能库统计

| 指标 | 数值 |
|------|------|
| **总技能数** | 49,035 |
| **分类数** | 28 |
| **最热门** | self-improving-agent (365k downloads) |

---

## 📚 详细文档导航

| 主题 | 文档 |
|------|------|
| 安装详解 | [docs/install/](./docs/install/) |
| 快速开始 | [docs/start/](./docs/start/) |
| 渠道配置 | [docs/channels/](./docs/channels/) |
| 技能指南 | [docs/plugins/](./docs/plugins/) |
| 概念解释 | [docs/concepts/](./docs/concepts/) |
| 工具命令 | [docs/tools/](./docs/tools/) |

---

## 🔗 外部资源

| 资源 | 链接 |
|------|------|
| 官方仓库 | [github.com/openclaw/openclaw](https://github.com/openclaw/openclaw) |
| ClawHub 技能市场 | [clawhub.ai/skills](https://clawhub.ai/skills) |
| 技能收录仓库 | [github.com/VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) |

---

**下载问答工具** → 一键搜索 50+ 常见问题

更新时间：2026-04-09