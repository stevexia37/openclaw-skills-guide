# OpenClaw 常用命令速查表

> 复制即可使用，快速上手

---

## 📱 应用管理

### macOS

| 操作 | 命令 |
|------|------|
| 启动应用 | `open /Applications/OpenClaw.app` |
| 查看日志 | `tail -f ~/Library/Logs/OpenClaw/main.log` |
| 清除缓存 | `rm -rf ~/Library/Application\ Support/OpenClaw/cache` |
| 重置应用 | `rm -rf ~/Library/Application\ Support/OpenClaw` |
| 卸载 | `rm -rf /Applications/OpenClaw.app` |

### Windows

| 操作 | 命令 |
|------|------|
| 启动应用 | `Start-Process "C:\Program Files\OpenClaw\OpenClaw.exe"` |
| 查看日志 | `Get-Content "$env:APPDATA\OpenClaw\logs\main.log" -Tail 50` |
| 清除缓存 | `Remove-Item -Recurse -Force "$env:APPDATA\OpenClaw\cache"` |
| 重置应用 | `Remove-Item -Recurse -Force "$env:APPDATA\OpenClaw"` |

### Linux

| 操作 | 命令 |
|------|------|
| 启动应用 | `./openclaw.AppImage` |
| 后台运行 | `nohup ./openclaw.AppImage &` |
| 查看日志 | `tail -f ~/.config/openclaw/logs/main.log` |
| 清除缓存 | `rm -rf ~/.config/openclaw/cache` |
| 重置应用 | `rm -rf ~/.config/openclaw` |

---

## 🔧 配置管理

### 查看配置文件

```bash
# macOS/Linux
cat ~/Library/Application\ Support/OpenClaw/config.json
# 或
cat ~/.config/openclaw/config.json

# Windows
type "%APPDATA%\OpenClaw\config.json"
```

### 修改配置

```bash
# macOS/Linux - 用编辑器打开
nano ~/Library/Application\ Support/OpenClaw/config.json

# 或使用 VS Code
code ~/Library/Application\ Support/OpenClaw/config.json
```

---

## 🛠️ 技能管理

### 查看已安装技能

```bash
# 列出技能目录
ls ~/Library/Application\ Support/OpenClaw/skills/

# 或
ls ~/.copaw/workspaces/default/skills/
```

### 安装技能（从 ClawHub）

访问 https://clawhub.ai 搜索安装

### 手动安装技能

```bash
# 创建技能目录
mkdir -p ~/.copaw/workspaces/default/skills/my-skill

# 创建技能文件
echo '---
name: my-skill
description: 我的技能
---
# My Skill
' > ~/.copaw/workspaces/default/skills/my-skill/SKILL.md
```

---

## 🐛 故障排除命令

### 检查网络连接

```bash
# 测试 OpenClaw 服务器连接
ping openclaw.ai

# 测试 API 连接
curl -I https://api.openclaw.ai/health
```

### 检查进程

```bash
# macOS/Linux
ps aux | grep -i openclaw

# Windows
tasklist | findstr OpenClaw
```

### 强制关闭应用

```bash
# macOS
pkill -f OpenClaw

# Windows
taskkill /F /IM OpenClaw.exe

# Linux
pkill -f openclaw
```

### 查看错误日志

```bash
# macOS/Linux
tail -100 ~/Library/Logs/OpenClaw/main.log | grep -i error

# Windows
Get-Content "$env:APPDATA\OpenClaw\logs\main.log" | Select-String "error"
```

---

## 🔄 重置与修复

### 完全重置

```bash
# macOS - 完全重置（会清除所有数据）
rm -rf ~/Library/Application\ Support/OpenClaw
rm -rf ~/Library/Logs/OpenClaw
rm -rf ~/Library/Caches/com.openclaw.*

# Windows - 完全重置
Remove-Item -Recurse -Force "$env:APPDATA\OpenClaw"
Remove-Item -Recurse -Force "$env:LOCALAPPDATA\OpenClaw"

# Linux - 完全重置
rm -rf ~/.config/openclaw
rm -rf ~/.cache/openclaw
```

### 重新配对

```bash
# 1. 完全关闭应用
pkill -f OpenClaw

# 2. 清除配对信息
rm ~/Library/Application\ Support/OpenClaw/pairing.json

# 3. 重新启动应用
open /Applications/OpenClaw.app
```

---

## 📊 性能监控

### 查看资源占用

```bash
# macOS/Linux
top -pid $(pgrep -f OpenClaw)

# 或使用 htop
htop -p $(pgrep -f OpenClaw)

# Windows
Get-Process OpenClaw | Format-List *
```

### 查看内存使用

```bash
# macOS
ps -o rss= -p $(pgrep -f OpenClaw)

# Linux
ps -o rss= -p $(pgrep -f openclaw)

# Windows
Get-Process OpenClaw | Select-Object WorkingSet64
```

---

## 🔗 常用链接

| 名称 | 地址 |
|------|------|
| 官网 | https://openclaw.ai |
| 下载 | https://openclaw.ai/download |
| ClawHub 技能市场 | https://clawhub.ai |
| 文档 | https://github.com/stevexia37/openclaw-skills-guide |
| 技能仓库 | https://github.com/stevexia37/openclaw-skills |

---

## 📚 相关文档

- [安装教程](./installation.md)
- [常见问题](./faq.md)
- [使用技巧](./tips.md)
