# OpenClaw 技能指南 🦞

<div align="center">

**OpenClaw 小白宝典：从部署到精通，还有随身的问答助手**

![GitHub release](https://img.shields.io/github/v/release/stevexia37/openclaw-skills-guide?include_prereleases)
![GitHub stars](https://img.shields.io/github/stars/stevexia37/openclaw-skills-guide?style=social)
![文档数量](https://img.shields.io/badge/问答库-24+-blue)
![更新频率](https://img.shields.io/badge/更新-持续-green)

**像查字典一样解决部署问题 | 下载一个文件，就能问问题**

</div>

---

## ✨ 特色亮点

| 特色 | 说明 |
|------|------|
| 🚀 **零基础友好** | 每一步都有详细说明，小白也能轻松上手 |
| 💡 **内置 24+ 常见问题** | 覆盖安装、配置、技能、故障等场景 |
| 🖥️ **免安装问答工具** | 下载即可运行，无需 Python 环境 |
| 🔄 **持续更新** | 社区驱动，欢迎贡献问题与答案 |
| 📚 **完整学习路径** | 从入门到进阶，循序渐进 |

---

## 🚀 快速开始

### 方式一：直接阅读文档

👉 [开始学习：环境准备](./docs/0-1/01-env-prepare.md)

适合：想详细了解 OpenClaw 的用户

---

### 方式二：下载问答工具

👉 [前往 Releases 下载](https://github.com/stevexia37/openclaw-skills-guide/releases)

适合：遇到问题想快速查找答案的用户

**使用方法：**

```bash
# macOS/Linux
chmod +x qa_tool_macos
./qa_tool_macos

# Windows
双击 qa_tool_windows.exe
```

**问答示例：**

```
请输入问题:
> 安装失败怎么办

📊 匹配度: 85%
❓ 问题: 安装时提示「已损坏，无法打开」怎么办？
💡 答案:
这是 macOS 的安全机制导致的。

解决方法：
1. 打开终端
2. 执行命令：xattr -cr /Applications/OpenClaw.app
3. 重新打开应用
```

---

## 📚 文档目录

### 0-1 入门教程

| 文档 | 内容 |
|------|------|
| [环境准备](./docs/0-1/01-env-prepare.md) | 如何检查系统是否满足要求？ |
| [安装教程](./docs/0-1/02-install.md) | 如何安装 OpenClaw？ |
| [配对账号](./docs/0-1/03-config.md) | 如何配对账号并开始使用？ |
| [首次运行](./docs/0-1/04-first-run.md) | 第一次使用 OpenClaw |

### 1-N 进阶运维

| 文档 | 内容 |
|------|------|
| [安全设置](./docs/1-n/01-security.md) | 如何保护隐私和数据安全？ |
| [备份恢复](./docs/1-n/02-backup.md) | 如何备份和恢复数据？ |
| [性能监控](./docs/1-n/03-monitor.md) | 如何监控 OpenClaw 运行状态？ |
| [扩展技能](./docs/1-n/04-scale.md) | 如何安装更多技能？ |

### 技能相关

| 文档 | 内容 |
|------|------|
| [推荐技能](./docs/plugins/recommended.md) | 新手必备技能推荐 |

---

## 💬 问答知识库

### 按主题浏览

| 主题 | 问题数 | 常见问题 |
|------|--------|----------|
| **部署安装** | 5 | 系统要求、安装失败、配对问题 |
| **技能使用** | 6 | 安装技能、PDF处理、Excel处理 |
| **定时任务** | 2 | 设置提醒、提醒不生效 |
| **隐私安全** | 1 | 数据保护 |
| **模型配置** | 2 | 切换模型、支持哪些模型 |
| **维护管理** | 3 | 更新、备份、卸载 |

### 使用问答工具

```bash
# 列出所有问题
qa_tool --list

# 搜索问题
qa_tool --search 安装

# 查看主题
qa_tool --topic 技能
```

---

## 📦 下载问答工具

前往 [Releases](https://github.com/stevexia37/openclaw-skills-guide/releases) 页面下载：

| 系统 | 文件 | 说明 |
|------|------|------|
| Windows | `qa_tool_windows.exe` | 双击运行 |
| macOS | `qa_tool_macos` | chmod +x 后运行 |
| Linux | `qa_tool_linux` | chmod +x 后运行 |

**注意：** 需要同时下载 `knowledge/` 目录中的文件。

---

## 🛠️ 工具脚本

| 脚本 | 功能 |
|------|------|
| [health_check.sh](./tools/health_check.sh) | 检查 OpenClaw 运行状态 |

---

## 🤝 贡献指南

欢迎贡献问题和答案！

### 如何贡献

1. **新增问题**：编辑 `knowledge/faq.jsonl`
2. **补充教程**：在 `docs/` 下新建文件
3. **改进工具**：优化 `scripts/qa_cli.py`

👉 [详细贡献指南](./CONTRIBUTING.md)

---

## ⭐ Star & Fork

如果觉得有用，请：

- ⭐ 点击右上角 Star 支持项目
- 🔀 Fork 到你的账号进行改进
- 📢 分享给更多需要的人

---

## 📞 求助渠道

| 渠道 | 地址 |
|------|------|
| 问答工具 | [下载](https://github.com/stevexia37/openclaw-skills-guide/releases) |
| GitHub Issues | [提问](https://github.com/stevexia37/openclaw-skills-guide/issues) |
| 官方网站 | https://openclaw.ai |
| 技能市场 | https://clawhub.ai |

---

## 📄 许可证

MIT License - 自由使用、修改和分享

---

<div align="center">

**🦞 Made with ❤️ for OpenClaw users**

**分享给朋友，一起学习！**

</div>