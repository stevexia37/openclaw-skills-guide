# 附录 B：常用命令速查表

> 📋 OpenClaw 命令大全，一键复制使用

---

## 🖥️ 基本命令

### 启动和停止

| 命令 | 功能 | 示例 |
|------|------|------|
| `openclaw` | 启动 OpenClaw | `openclaw` |
| `openclaw --version` | 查看版本 | `openclaw --version` |
| `openclaw --help` | 查看帮助 | `openclaw --help` |
| `openclaw stop` | 停止运行 | `openclaw stop` |
| `openclaw restart` | 重启服务 | `openclaw restart` |

### 配置命令

| 命令 | 功能 | 示例 |
|------|------|------|
| `openclaw config` | 打开配置 | `openclaw config` |
| `openclaw config show` | 显示配置 | `openclaw config show` |
| `openclaw config set <键> <值>` | 设置配置 | `openclaw config set model gpt-4` |
| `openclaw config reset` | 重置配置 | `openclaw config reset` |

---

## 🛠️ 技能命令

### 安装和管理

| 命令 | 功能 | 示例 |
|------|------|------|
| `openclaw skill list` | 列出技能 | `openclaw skill list` |
| `openclaw skill install <名称>` | 安装技能 | `openclaw skill install pdf` |
| `openclaw skill remove <名称>` | 移除技能 | `openclaw skill remove pdf` |
| `openclaw skill update <名称>` | 更新技能 | `openclaw skill update pdf` |
| `openclaw skill update --all` | 更新全部 | `openclaw skill update --all` |

### 技能搜索

| 命令 | 功能 | 示例 |
|------|------|------|
| `openclaw skill search <关键词>` | 搜索技能 | `openclaw skill search pdf` |
| `openclaw skill info <名称>` | 技能详情 | `openclaw skill info cron` |

---

## ⏰ 定时任务命令

### 任务管理

| 命令 | 功能 | 示例 |
|------|------|------|
| `openclaw cron list` | 列出任务 | `openclaw cron list` |
| `openclaw cron add <时间> <内容>` | 添加任务 | `openclaw cron add "09:00" "开会"` |
| `openclaw cron remove <ID>` | 移除任务 | `openclaw cron remove 1` |
| `openclaw cron clear` | 清空任务 | `openclaw cron clear` |

### 时间格式

| 格式 | 说明 | 示例 |
|------|------|------|
| `HH:MM` | 每天指定时间 | `09:00` |
| `daily HH:MM` | 每天 | `daily 09:00` |
| `weekly X HH:MM` | 每周X | `weekly 5 17:00` |
| `monthly D HH:MM` | 每月D日 | `monthly 1 09:00` |

---

## 📁 文件命令

### 文件操作

| 命令 | 功能 | 示例 |
|------|------|------|
| `openclaw file read <路径>` | 读取文件 | `openclaw file read README.md` |
| `openclaw file write <路径> <内容>` | 写入文件 | `openclaw file write test.txt "hello"` |
| `openclaw file list <路径>` | 列出文件 | `openclaw file list ~/Downloads` |
| `openclaw file copy <源> <目标>` | 复制文件 | `openclaw file copy a.txt b.txt` |
| `openclaw file move <源> <目标>` | 移动文件 | `openclaw file move a.txt ~/Desktop/` |
| `openclaw file delete <路径>` | 删除文件 | `openclaw file delete test.txt` |

### 文件整理

| 命令 | 功能 | 示例 |
|------|------|------|
| `openclaw file organize <路径>` | 整理文件 | `openclaw file organize ~/Downloads` |
| `openclaw file search <关键词>` | 搜索文件 | `openclaw file search "报告"` |

---

## 🌐 浏览器命令

| 命令 | 功能 | 示例 |
|------|------|------|
| `openclaw browser open <URL>` | 打开网页 | `openclaw browser open https://example.com` |
| `openclaw browser screenshot` | 截图 | `openclaw browser screenshot` |
| `openclaw browser close` | 关闭浏览器 | `openclaw browser close` |
| `openclaw browser fill <表单>` | 填表 | `openclaw browser fill "姓名:张三"` |

---

## 📊 系统命令

### 状态和诊断

| 命令 | 功能 | 示例 |
|------|------|------|
| `openclaw status` | 查看状态 | `openclaw status` |
| `openclaw logs` | 查看日志 | `openclaw logs` |
| `openclaw logs --tail N` | 最后N行日志 | `openclaw logs --tail 50` |
| `openclaw doctor` | 诊断问题 | `openclaw doctor` |

### 更新和备份

| 命令 | 功能 | 示例 |
|------|------|------|
| `openclaw update` | 更新版本 | `openclaw update` |
| `openclaw backup` | 备份数据 | `openclaw backup` |
| `openclaw backup restore <文件>` | 恢复数据 | `openclaw backup restore backup.tar.gz` |

---

## 💻 快速复制

### 一键安装常用技能

```bash
openclaw skill install cron pdf xlsx file-organizer translator
```

### 一键查看系统状态

```bash
openclaw status && openclaw doctor && openclaw skill list
```

### 一键备份

```bash
openclaw backup --output ~/backup/
```

---

## 📚 相关附录

- [官方自带技能](./E-official-skills.md)
- [ClawHub 热门技能](./F-clawhub-skills.md)
- [技能目录](./C-skills-catalog.md)

---

<div align="center">

**🦞 OpenClaw 技能指南 | 附录 B**

</div>
