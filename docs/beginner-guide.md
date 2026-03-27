# 小白入门完整指南

> 从零开始，一步一步教你使用 OpenClaw

---

## 📋 你需要准备什么？

| 准备项 | 要求 |
|--------|------|
| 电脑 | macOS / Windows / Linux |
| 内存 | 4GB 以上 |
| 磁盘 | 500MB 以上空间 |
| 网络 | 能访问互联网 |

**不需要**：编程基础、翻墙工具、付费账号

---

## 🚀 第一步：下载安装

### macOS 用户

**复制以下命令到终端执行：**

```bash
# 打开官网下载页面
open https://openclaw.ai
```

或者使用命令行一键安装：

```bash
# 下载
curl -L -o ~/Downloads/OpenClaw.dmg https://openclaw.ai/download/mac

# 挂载镜像
hdiutil attach ~/Downloads/OpenClaw.dmg

# 安装
cp -R /Volumes/OpenClaw/OpenClaw.app /Applications/

# 允许运行（解决"未验证开发者"问题）
xattr -cr /Applications/OpenClaw.app

# 启动
open /Applications/OpenClaw.app
```

### Windows 用户

**步骤：**

1. 打开 https://openclaw.ai
2. 点击"下载 Windows 版本"
3. 双击下载的安装包
4. 一路"下一步"完成安装

**PowerShell 一键安装：**

```powershell
# 下载（需要手动访问网页下载）
# 运行安装包
Start-Process ~/Downloads/OpenClaw-Setup.exe
```

### Linux 用户

**复制以下命令到终端执行：**

```bash
# 下载
wget https://openclaw.ai/download/linux -O openclaw.AppImage

# 添加执行权限
chmod +x openclaw.AppImage

# 安装依赖（Ubuntu/Debian）
sudo apt-get update
sudo apt-get install -y libgtk-3-0 libnotify4 libnss3 libxss1 libxtst6 xdg-utils

# 运行
./openclaw.AppImage
```

---

## 🔧 第二步：配对账号

### 步骤

1. 打开 OpenClaw 应用
2. 屏幕显示二维码
3. 用手机扫描二维码
4. 在手机上确认配对
5. 完成！

---

## 💬 第三步：开始对话

### 试试这些命令

```
你好，请介绍一下你自己
```

```
帮我看看今天有什么待办事项
```

```
每天早上9点提醒我喝水
```

---

## 🛠️ 第四步：安装技能

技能是 OpenClaw 的"超能力"。

### 从 ClawHub 安装

```bash
# 打开 ClawHub
open https://clawhub.ai
```

1. 搜索你想要的技能
2. 点击"安装"按钮
3. 完成！

### 推荐新手安装的技能

| 技能名 | 能做什么 | 一句话说明 |
|--------|----------|------------|
| cron | 定时任务、提醒 | 帮你设置提醒 |
| pdf | PDF 处理 | 读取、转换 PDF |
| xlsx | Excel 表格处理 | 分析表格数据 |
| browser | 浏览器自动化 | 自动打开网页 |

---

## ❓ 遇到问题怎么办？

### 问题1：macOS 提示"无法打开"

**原因**：macOS 安全限制

**解决**：复制以下命令执行

```bash
xattr -cr /Applications/OpenClaw.app
```

### 问题2：Windows 提示"已保护你的电脑"

**解决**：

1. 点击"更多信息"
2. 点击"仍要运行"

### 问题3：配对失败

**解决**：复制以下命令执行

```bash
# macOS
rm ~/Library/Application\ Support/OpenClaw/pairing.json
open /Applications/OpenClaw.app

# Linux
rm ~/.config/openclaw/pairing.json
./openclaw.AppImage

# Windows
Remove-Item "$env:APPDATA\OpenClaw\pairing.json"
Start-Process "C:\Program Files\OpenClaw\OpenClaw.exe"
```

### 问题4：应用卡住或无响应

**解决**：强制重启

```bash
# macOS
pkill -f OpenClaw
open /Applications/OpenClaw.app

# Linux
pkill -f openclaw
./openclaw.AppImage

# Windows
taskkill /F /IM OpenClaw.exe
Start-Process "C:\Program Files\OpenClaw\OpenClaw.exe"
```

### 问题5：技能不生效

**解决**：检查并重启

```bash
# 查看技能是否安装
ls ~/.copaw/workspaces/default/skills/

# 重启应用
pkill -f OpenClaw
open /Applications/OpenClaw.app
```

---

## 📚 常用命令速查表

### 应用管理

```bash
# ============ macOS ============
# 启动
open /Applications/OpenClaw.app

# 关闭
pkill -f OpenClaw

# 查看日志
tail -f ~/Library/Logs/OpenClaw/main.log

# 清除缓存
rm -rf ~/Library/Application\ Support/OpenClaw/cache

# 完全重置
rm -rf ~/Library/Application\ Support/OpenClaw

# ============ Linux ============
# 启动
./openclaw.AppImage

# 后台运行
nohup ./openclaw.AppImage &

# 关闭
pkill -f openclaw

# 查看日志
tail -f ~/.config/openclaw/logs/main.log

# 清除缓存
rm -rf ~/.config/openclaw/cache

# 完全重置
rm -rf ~/.config/openclaw

# ============ Windows ============
# 启动
Start-Process "C:\Program Files\OpenClaw\OpenClaw.exe"

# 关闭
taskkill /F /IM OpenClaw.exe

# 查看日志
Get-Content "$env:APPDATA\OpenClaw\logs\main.log" -Tail 50

# 清除缓存
Remove-Item -Recurse -Force "$env:APPDATA\OpenClaw\cache"

# 完全重置
Remove-Item -Recurse -Force "$env:APPDATA\OpenClaw"
```

### 故障排除

```bash
# ============ macOS/Linux ============
# 检查网络
ping openclaw.ai

# 检查进程
ps aux | grep -i openclaw

# 查看错误日志
tail -100 ~/Library/Logs/OpenClaw/main.log | grep -i error

# 查看资源占用
top -pid $(pgrep -f OpenClaw)

# ============ Windows ============
# 检查网络
ping openclaw.ai

# 检查进程
tasklist | findstr OpenClaw

# 查看错误日志
Get-Content "$env:APPDATA\OpenClaw\logs\main.log" | Select-String "error"

# 查看资源占用
Get-Process OpenClaw | Format-List *
```

---

## 🎯 接下来做什么？

1. **学会提问** → [使用技巧](./tips.md)
2. **了解更多功能** → [功能大全](./features.md)
3. **遇到问题** → [常见问题](./faq.md)
4. **开发技能** → [技能开发](./skill-development.md)

---

## 📞 获取帮助

- 📖 文档：本站
- 🐛 问题反馈：https://github.com/openclaw/issues
- 💬 社区讨论：https://github.com/openclaw/discussions

---

<div align="center">

**🎉 恭喜你完成了 OpenClaw 入门！**

开始享受 AI 助手带来的便利吧！

</div>
