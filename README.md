# OpenClaw 技能指南 🦞

> **全网最详细、最友好的 OpenClaw 百科全书**
> 
> 让每个人都能轻松使用 AI 助手

---

## 🦞 这是什么？

OpenClaw 是一个**本地运行的 AI 助手平台**，拥有 **30,000+ 技能库**。

### 为什么选择 OpenClaw？

| 特点 | 说明 |
|------|------|
| 🔒 **隐私安全** | 数据在你自己电脑里，不上云 |
| 💰 **完全免费** | 开源项目，无订阅费 |
| 🌍 **无需翻墙** | 支持多种 AI 模型 |
| 🛠️ **技能丰富** | 30,000+ 技能可安装 |
| 💪 **真正能干** | 能操作你的电脑，不只是聊天 |

---

## 🚀 5分钟上手

### 第一步：下载

访问 https://openclaw.ai 下载安装包

### 第二步：安装

```bash
# macOS 一键安装
curl -L -o ~/Downloads/OpenClaw.dmg https://openclaw.ai/download/mac
hdiutil attach ~/Downloads/OpenClaw.dmg
cp -R /Volumes/OpenClaw/OpenClaw.app /Applications/
xattr -cr /Applications/OpenClaw.app
```

### 第三步：配对

扫描二维码，完成配对

### 第四步：开始使用

```
帮我总结这份文档
每天早上9点提醒我开会
帮我把这个PDF转成文字
```

---

## 📚 完整文档

### 🌟 新手必读

| 文档 | 说明 |
|------|------|
| [快速入门指南](./docs/getting-started.md) | 5分钟学会使用 |
| [安装教程](./docs/installation.md) | 详细安装步骤，每步都有命令 |
| [第一个技能](./docs/beginner/first-skill.md) | 安装和使用技能 |

### 📖 功能介绍

| 文档 | 说明 |
|------|------|
| [功能大全](./docs/features.md) | 所有功能详细介绍 |
| [使用技巧](./docs/tips.md) | 提问技巧和场景示例 |
| [技能使用指南](./docs/skills-guide.md) | 技能安装和使用 |

### 🔧 命令速查

| 文档 | 说明 |
|------|------|
| [常用命令速查表](./docs/commands.md) | 所有命令，复制即用 |
| [故障排除](./docs/faq.md) | 问题解答和修复方法 |

### 🔍 了解更多

| 文档 | 说明 |
|------|------|
| [与其他工具对比](./docs/comparison.md) | OpenClaw vs ChatGPT/文心一言 |

### ⚡ 进阶内容

| 文档 | 说明 |
|------|------|
| [技能开发指南](./docs/skill-development.md) | 开发自己的技能 |
| [自定义模型](./docs/advanced/custom-models.md) | 配置不同的 AI |

---

## 🎯 我能用它做什么？

### 💼 工作场景

```
✅ 自动整理邮件
✅ 处理 Excel/Word/PDF
✅ 写周报、总结
✅ 数据分析
```

### 💻 开发场景

```
✅ 代码辅助
✅ 自动化脚本
✅ 浏览器自动化
✅ API 测试
```

### 🏠 生活场景

```
✅ 日程管理
✅ 提醒事项
✅ 学习辅导
✅ 投资分析
```

---

## ⚡ 快速命令

### 启动应用

```bash
# macOS
open /Applications/OpenClaw.app

# Windows
Start-Process "C:\Program Files\OpenClaw\OpenClaw.exe"

# Linux
./openclaw.AppImage
```

### 故障排除

```bash
# macOS - 允许运行
xattr -cr /Applications/OpenClaw.app

# macOS - 查看日志
tail -f ~/Library/Logs/OpenClaw/main.log

# macOS - 清除缓存
rm -rf ~/Library/Application\ Support/OpenClaw/cache
```

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

### 贡献方式

1. Fork 本仓库
2. 创建新分支
3. 添加或修改内容
4. 提交 PR

---

## 📄 许可证

MIT License

---

<div align="center">

**⭐ 觉得有用就点个 Star 吧！**

Made with ❤️ for OpenClaw users

</div>
