# 🦞 OpenClaw 技能百科 — 小白逆袭宝典

> **50+ 精选问答 · 30+ 实战教程 · 一键安装即用**  
> 从零基础到进阶玩家，一站式掌握 OpenClaw 的全部能力。

[![Stars](https://img.shields.io/github/stars/stevexia37/openclaw-skills-guide?style=flat-square&logo=github)](https://github.com/stevexia37/openclaw-skills-guide/stargazers)
[![License](https://img.shields.io/github/license/stevexia37/openclaw-skills-guide?style=flat-square)](LICENSE)
[![Topics](https://img.shields.io/github/topics/stevexia37/openclaw-skills-guide?style=flat-square)](https://github.com/stevexia37/openclaw-skills-guide)
[![Last Commit](https://img.shields.io/github/last-commit/stevexia37/openclaw-skills-guide?style=flat-square&color=orange)](https://github.com/stevexia37/openclaw-skills-guide/commits/main)
[![Languages](https://img.shields.io/github/languages/top/stevexia37/openclaw-skills-guide?style=flat-square&color=blue)](https://github.com/stevexia37/openclaw-skills-guide)
[![Repo Size](https://img.shields.io/github/repo-size/stevexia37/openclaw-skills-guide?style=flat-square&color=green)](https://github.com/stevexia37/openclaw-skills-guide)

---

## 🚀 为什么选这份指南？

| 特色 | 说明 |
|------|------|
| 🎯 **零基础友好** | 从安装到第一个技能，5分钟快速上手 |
| 🧠 **知识体系完整** | 覆盖入门→核心概念→进阶→实战全链路 |
| 💡 **独家深度内容** | 梦境系统、人格技能、自我进化 — 别处看不到的干货 |
| 🔧 **工具即装即用** | 内置问答工具，命令行直接搜索50条精选问答 |
| 📱 **多平台覆盖** | macOS / Windows / Linux 三大系统安装指南 |
| 🌐 **开放共享** | MIT 开源协议，欢迎 Fork / Star / PR |

---

## 📖 快速导航

### 🟢 新手入门

| 文档 | 内容 |
|------|------|
| [📦 安装指南](docs/start/installation.md) | macOS / Windows / Linux 三系统安装教程 |
| [⚡ 5分钟速通](docs/start/quick-start.md) | 从安装到运行第一个技能 |
| [🤔 OpenClaw 是什么？](docs/start/introduction.md) | 工具介绍与核心能力 |

### 🔵 核心概念

| 文档 | 内容 |
|------|------|
| 🌙 [梦境系统详解](docs/concepts/dreaming-system.md) | 三阶段模型 · 评分信号 · 启用方法 |
| 👤 [人格技能](docs/concepts/soul-personality-skills.md) | 13个角色灵魂库 · 人格注入指南 |
| 🔄 [自我进化](docs/concepts/self-improving-skills.md) | 工作流 · 反馈循环 · 持续优化 |

### 🟡 进阶提升

| 文档 | 内容 |
|------|------|
| 🧩 [技能开发指南](docs/advanced/skill-development.md) | 从零开始创建自定义技能 |
| 🎨 [自定义模型](docs/advanced/custom-models.md) | 接入第三方 LLM 模型 |
| 📊 [用户实战案例](docs/advanced/user-cases.md) | 真实场景下的使用案例 |

### 🔴 参考手册

| 文档 | 内容 |
|------|------|
| ⌨️ [命令速查表](docs/reference/commands.md) | 全部命令参数与用法 |
| ❓ [常见问题 FAQ](docs/reference/faq.md) | 50条精选问答 |
| 💡 [使用技巧](docs/reference/tips.md) | 提升效率的隐藏技巧 |
| 🆚 [竞品对比](docs/reference/comparison.md) | 与同类工具的对比分析 |

---

## 🛠️ 三种使用方式

### 方式一：在线阅读
直接浏览本仓库的 `docs/` 目录，按分类查找所需内容。

### 方式二：命令行问答工具
```bash
# 安装问答工具（无需依赖）
pip install -r requirements.txt 2>/dev/null || true

# 交互式问答
python3 scripts/qa_cli.py

# 按主题浏览
python3 scripts/qa_cli.py --topic 安装

# 一键搜索
python3 scripts/qa_cli.py --search "macOS"
```

### 方式三：技能目录
```bash
# 查看技能总览
cat SKILLS-CATALOG.md

# 查看学习路线
cat LEARNING-PATH.md
```

---

## 🗺️ 学习路线图

```
零基础 ──────────────────────────────→ 进阶玩家
  │
  ├─ 1️⃣ 安装 OpenClaw  → docs/start/installation.md
  ├─ 2️⃣ 5分钟速通       → docs/start/quick-start.md
  ├─ 3️⃣ 理解核心概念     → docs/concepts/
  ├─ 4️⃣ 尝试第一个技能   → docs/start/first-skill.md
  ├─ 5️⃣ 进阶：自定义模型 → docs/advanced/
  └─ 6️⃣ 实战案例学习     → docs/advanced/user-cases.md
```

> 📋 完整学习路线详见 → [LEARNING-PATH.md](LEARNING-PATH.md)

---

## 📦 项目结构

```
openclaw-skills-guide/
├── README.md                  ← 你在看的这个文件
├── LEARNING-PATH.md           ← 学习路线图
├── QUICK-GUIDE.md             ← 5分钟速通指南
├── SKILLS-CATALOG.md          ← 技能总览
├── CHANGELOG.md               ← 版本历史
├── CONTRIBUTING.md            ← 贡献指南
├── docs/                      ← 📚 文档库
│   ├── start/                 ← 入门指南
│   ├── concepts/              ← 核心概念
│   ├── reference/             ← 参考手册
│   └── advanced/              ← 进阶内容
├── knowledge/                 ← 📊 知识库
│   └── qa.jsonl               ← 50条精选问答（单一数据源）
├── examples/                  ← 💻 示例代码
├── scripts/                   ← 🔧 工具脚本
│   └── qa_cli.py              ← 命令行问答工具
└── tools/                     ← 🛡️ 运维工具
    └── health_check.sh        ← 健康检查
```

---

## 🌟 精选内容

### 🏆 Top 3 必读文档

1. **[梦境系统详解](docs/concepts/dreaming-system.md)** — 三阶段梦境模型，独家评分信号分析
2. **[人格技能](docs/concepts/soul-personality-skills.md)** — 13个角色灵魂库，人格注入实战
3. **[自我进化](docs/concepts/self-improving-skills.md)** — 让 AI Agent 持续优化的工作流

### 🔥 最实用工具

- **[qa_cli.py](scripts/qa_cli.py)** — 命令行问答工具，支持交互/搜索/主题浏览三种模式
- **[SKILLS-CATALOG.md](SKILLS-CATALOG.md)** — 技能分类目录，49,035 个技能索引

---

## 🤝 参与贡献

我们欢迎任何形式的贡献！详见 [CONTRIBUTING.md](CONTRIBUTING.md)

- 📝 补充文档内容
- 🔧 修复错误或遗漏
- 💡 添加新的实战案例
- 🌍 翻译成其他语言

---

## 📄 许可证

本项目采用 [MIT 许可证](LICENSE) 开源。欢迎 Fork、Star、分享！

---

<p align="center">
  ⭐ 如果这份指南对你有帮助，别忘了给个 Star 支持一下！
</p>
