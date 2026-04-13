# 常见问题解答

> 小白最关心的问题，这里都有答案

---

## 📋 目录

- [安装问题](#安装问题)
- [使用问题](#使用问题)
- [技能问题](#技能问题)
- [安全问题](#安全问题)
- [其他问题](#其他问题)

---

## 🔧 安装问题

### Q1: macOS 提示"无法打开，因为它来自未验证的开发者"

**原因**：macOS 安全限制

**解决方法**：

```bash
# 方法一：命令行允许
xattr -cr /Applications/OpenClaw.app

# 方法二：系统设置
# 系统偏好设置 → 安全性与隐私 → 点击"仍要打开"
```

### Q2: Windows 提示"Windows 已保护你的电脑"

**原因**：Windows Defender 保护机制

**解决方法**：

1. 点击"更多信息"
2. 点击"仍要运行"
3. 或在设置中添加例外

### Q3: 安装后打不开怎么办？

**解决步骤**：

```bash
# 1. 检查是否安装成功
ls /Applications/OpenClaw.app  # macOS

# 2. 检查权限
chmod +x openclaw.AppImage  # Linux

# 3. 查看错误日志
tail -f ~/Library/Logs/OpenClaw/main.log  # macOS
```

### Q4: 卸载后重新安装失败？

**完全卸载命令**：

```bash
# macOS
rm -rf /Applications/OpenClaw.app
rm -rf ~/Library/Application\ Support/OpenClaw
rm -rf ~/Library/Logs/OpenClaw
rm -rf ~/Library/Caches/com.openclaw.*

# Windows
Remove-Item -Recurse -Force "$env:APPDATA\OpenClaw"
Remove-Item -Recurse -Force "$env:LOCALAPPDATA\OpenClaw"

# Linux
rm -rf ~/.config/openclaw
rm -rf ~/.cache/openclaw
```

---

## 💬 使用问题

### Q5: 配对失败怎么办？

**可能原因和解决方法**：

| 原因 | 解决方法 |
|------|----------|
| 网络问题 | 检查网络，确保能访问 openclaw.ai |
| 二维码过期 | 重启应用，重新扫码 |
| 缓存问题 | 清除缓存后重试 |

**解决步骤**：

```bash
# 1. 检查网络
ping openclaw.ai

# 2. 重启应用
pkill -f OpenClaw  # macOS/Linux
# 或直接关闭窗口

# 3. 清除配对缓存
rm ~/Library/Application\ Support/OpenClaw/pairing.json  # macOS

# 4. 重新打开应用并配对
```

### Q6: OpenClaw 回复很慢怎么办？

**可能原因**：

1. 网络连接问题
2. 使用的模型响应慢
3. 电脑性能问题

**解决方法**：

```bash
# 1. 切换更快的模型
# 在设置中更换 AI 模型

# 2. 检查网络
curl -I https://api.openclaw.ai/health

# 3. 关闭其他占用资源的程序
```

### Q7: OpenClaw 不理解我的指令？

**提问技巧**：

| ❌ 不好的提问 | ✅ 好的提问 |
|---------------|-------------|
| 帮我弄一下 | 帮我把这个 PDF 转成 Word |
| 看看这个 | 帮我分析这份销售数据，找出前10名 |
| 搞一下 | 每天早上9点提醒我喝水 |

**公式**：**目标 + 动作 + 细节 = 最佳效果**

### Q8: 如何查看 OpenClaw 的操作记录？

```bash
# 查看日志
tail -f ~/Library/Logs/OpenClaw/main.log  # macOS
tail -f ~/.config/openclaw/logs/main.log  # Linux

# Windows
Get-Content "$env:APPDATA\OpenClaw\logs\main.log" -Tail 50
```

---

## 🛠️ 技能问题

### Q9: 如何安装技能？

**方法一：从 ClawHub 安装（推荐）**

1. 打开 https://clawhub.ai
2. 搜索你想要的技能
3. 点击"安装"

**方法二：手动安装**

```bash
# 1. 下载技能文件夹
# 2. 放到技能目录
mkdir -p ~/.copaw/workspaces/default/skills/
# 3. 重启 OpenClaw
```

### Q10: 技能安装后不生效？

**解决方法**：

```bash
# 1. 检查技能目录
ls ~/.copaw/workspaces/default/skills/

# 2. 检查技能文件
# 确保技能文件夹里有 SKILL.md 文件

# 3. 重启应用
```

### Q11: 如何卸载技能？

```bash
# 删除技能文件夹
rm -rf ~/.copaw/workspaces/default/skills/技能名称
```

### Q12: 推荐安装哪些技能？

| 技能 | 功能 | 推荐指数 |
|------|------|----------|
| cron | 定时任务、提醒 | ⭐⭐⭐⭐⭐ |
| pdf | PDF 处理 | ⭐⭐⭐⭐⭐ |
| xlsx | Excel 表格处理 | ⭐⭐⭐⭐ |
| browser | 浏览器自动化 | ⭐⭐⭐⭐ |

---

## 🔒 安全问题

### Q13: 我的对话会被上传吗？

**不会！** OpenClaw 是本地运行：

- ✅ 所有对话存储在你电脑里
- ✅ 数据不上传云端
- ✅ 只有你能看到

### Q14: OpenClaw 会偷我的数据吗？

**不会！** OpenClaw 是开源项目：

- ✅ 代码公开，可审查
- ✅ 不收集用户信息
- ✅ 不上传任何数据

### Q15: 可以在离线环境使用吗？

**部分功能可以！**

- ✅ 本地模型：完全离线
- ⚠️ 云端模型：需要网络

---

## ❓ 其他问题

### Q16: OpenClaw 支持哪些语言？

- ✅ 中文（简体/繁体）
- ✅ 英文
- ✅ 日文、韩文等

### Q17: 需要翻墙吗？

**不需要！** OpenClaw 支持多种国内 AI 模型。

### Q18: 支持哪些系统？

| 系统 | 支持 |
|------|------|
| macOS | ✅ |
| Windows | ✅ |
| Linux | ✅ |

### Q19: 如何更新 OpenClaw？

```bash
# macOS/Linux
# 重新下载最新版本覆盖安装

# Windows
# 设置中检查更新，或重新下载安装
```

### Q20: 遇到其他问题怎么办？

1. **查看日志**：找出具体错误
2. **搜索文档**：本站可能有答案
3. **提交 Issue**：https://github.com/openclaw/issues

---

## 📚 相关文档

- [安装教程](./installation.md)
- [快速入门](./getting-started.md)
- [常用命令](./commands.md)
- [使用技巧](./tips.md)
