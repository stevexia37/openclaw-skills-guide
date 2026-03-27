# OpenClaw 技能指南 🦞

> **全网最详细、最友好的 OpenClaw 百科全书**
> 
> 每一步都有具体命令，复制即可执行

---

## 🦞 这是什么？

OpenClaw 是一个**本地运行的 AI 助手平台**，拥有 **30,000+ 技能库**。

| 特点 | 说明 |
|------|------|
| 🔒 **隐私安全** | 数据在你自己电脑里，不上云 |
| 💰 **完全免费** | 开源项目，无订阅费 |
| 🌍 **无需翻墙** | 支持多种 AI 模型 |
| 🛠️ **技能丰富** | 30,000+ 技能可安装 |
| 💪 **真正能干** | 能操作你的电脑，不只是聊天 |

---

## 🚀 快速开始（复制粘贴即可）

### macOS

```bash
# 一键安装
curl -L -o ~/Downloads/OpenClaw.dmg https://openclaw.ai/download/mac && \
hdiutil attach ~/Downloads/OpenClaw.dmg && \
cp -R /Volumes/OpenClaw/OpenClaw.app /Applications/ && \
xattr -cr /Applications/OpenClaw.app && \
open /Applications/OpenClaw.app
```

### Linux

```bash
# 一键安装
wget https://openclaw.ai/download/linux -O openclaw.AppImage && \
chmod +x openclaw.AppImage && \
./openclaw.AppImage
```

### Windows

1. 访问 https://openclaw.ai
2. 下载 Windows 安装包
3. 双击安装

---

## 📚 完整文档

### 🌟 新手必读

| 文档 | 说明 | 推荐指数 |
|------|------|----------|
| [小白入门指南](./docs/beginner-guide.md) | 从零开始，每一步都有命令 | ⭐⭐⭐⭐⭐ |
| [什么是 OpenClaw](./docs/beginner/what-is-openclaw.md) | 一句话讲清楚 | ⭐⭐⭐⭐⭐ |
| [安装教程](./docs/installation.md) | 详细安装步骤 | ⭐⭐⭐⭐ |
| [第一个技能](./docs/beginner/first-skill.md) | 安装和使用技能 | ⭐⭐⭐⭐ |

### 🔧 命令速查

| 文档 | 说明 |
|------|------|
| [常用命令速查表](./docs/commands.md) | 所有命令，复制即用 |
| [故障排除](./docs/faq.md) | 问题解答和修复方法 |

### 📖 功能介绍

| 文档 | 说明 |
|------|------|
| [功能大全](./docs/features.md) | 所有功能详细介绍 |
| [使用技巧](./docs/tips.md) | 提问技巧和场景示例 |
| [技能使用指南](./docs/skills-guide.md) | 技能安装和使用 |

### 🔍 了解更多

| 文档 | 说明 |
|------|------|
| [与其他工具对比](./docs/comparison.md) | OpenClaw vs ChatGPT/文心一言 |

---

## ⚡ 常用命令

### 启动应用

```bash
# macOS
open /Applications/OpenClaw.app

# Linux
./openclaw.AppImage

# Windows (PowerShell)
Start-Process "C:\Program Files\OpenClaw\OpenClaw.exe"
```

### 故障排除

```bash
# macOS - 允许运行（解决"未验证开发者"问题）
xattr -cr /Applications/OpenClaw.app

# macOS - 查看日志
tail -f ~/Library/Logs/OpenClaw/main.log

# macOS - 清除缓存
rm -rf ~/Library/Application\ Support/OpenClaw/cache

# macOS - 完全重置
rm -rf ~/Library/Application\ Support/OpenClaw
```

---

## ❓ 常见问题

<details>
<summary>点击展开</summary>

### macOS 提示"无法打开"

```bash
xattr -cr /Applications/OpenClaw.app
```

### 配对失败

```bash
# macOS
rm ~/Library/Application\ Support/OpenClaw/pairing.json
open /Applications/OpenClaw.app
```

### 应用卡住

```bash
# macOS
pkill -f OpenClaw
open /Applications/OpenClaw.app
```

</details>

---

## 🔗 相关链接

| 链接 | 地址 |
|------|------|
| OpenClaw 官网 | https://openclaw.ai |
| ClawHub 技能市场 | https://clawhub.ai |
| 技能仓库 | https://github.com/stevexia37/openclaw-skills |

---

## 🤝 贡献

欢迎提交 PR 完善文档！

---

## 📄 许可证

MIT License

---

<div align="center">

**⭐ 觉得有用就点个 Star 吧！**

Made with ❤️ for OpenClaw users

</div>
