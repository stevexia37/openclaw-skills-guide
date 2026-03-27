# 附录 B：命令参考

> 📋 OpenClaw 常用命令速查表

---

## 🖥️ 基本命令

| 命令 | 功能 | 示例 |
|------|------|------|
| `openclaw` | 启动 OpenClaw | `openclaw` |
| `openclaw --version` | 查看版本 | `openclaw --version` |
| `openclaw --help` | 查看帮助 | `openclaw --help` |
| `openclaw config` | 打开配置 | `openclaw config` |
| `openclaw update` | 更新版本 | `openclaw update` |
| `openclaw doctor` | 诊断问题 | `openclaw doctor` |

---

## 📁 文件命令

| 命令 | 功能 | 示例 |
|------|------|------|
| `openclaw file read <路径>` | 读取文件 | `openclaw file read README.md` |
| `openclaw file list <路径>` | 列出文件 | `openclaw file list ~/Downloads` |
| `openclaw file organize <路径>` | 整理文件 | `openclaw file organize ~/Desktop` |

---

## 🛠️ 技能命令

| 命令 | 功能 | 示例 |
|------|------|------|
| `openclaw skill list` | 列出技能 | `openclaw skill list` |
| `openclaw skill install <名称>` | 安装技能 | `openclaw skill install pdf` |
| `openclaw skill remove <名称>` | 移除技能 | `openclaw skill remove pdf` |
| `openclaw skill update <名称>` | 更新技能 | `openclaw skill update pdf` |

---

## ⏰ 定时任务命令

| 命令 | 功能 | 示例 |
|------|------|------|
| `openclaw cron list` | 列出任务 | `openclaw cron list` |
| `openclaw cron add <时间> <内容>` | 添加任务 | `openclaw cron add "9:00" "开会"` |
| `openclaw cron remove <ID>` | 移除任务 | `openclaw cron remove 1` |

---

## 🌐 浏览器命令

| 命令 | 功能 | 示例 |
|------|------|------|
| `openclaw browser open <URL>` | 打开网页 | `openclaw browser open https://example.com` |
| `openclaw browser screenshot` | 截图 | `openclaw browser screenshot` |
| `openclaw browser close` | 关闭浏览器 | `openclaw browser close` |

---

## 📊 系统命令

| 命令 | 功能 | 示例 |
|------|------|------|
| `openclaw status` | 查看状态 | `openclaw status` |
| `openclaw logs` | 查看日志 | `openclaw logs` |
| `openclaw restart` | 重启服务 | `openclaw restart` |

---

## 🔧 配置命令

| 命令 | 功能 | 示例 |
|------|------|------|
| `openclaw config show` | 显示配置 | `openclaw config show` |
| `openclaw config set <键> <值>` | 设置配置 | `openclaw config set model gpt-4` |
| `openclaw config reset` | 重置配置 | `openclaw config reset` |

---

## 💡 使用技巧

### 命令别名

可以设置命令别名，简化输入：

```bash
# 设置别名
alias oc='openclaw'
alias ocs='openclaw skill'
alias ocf='openclaw file'
```

### 命令组合

```bash
# 组合使用
openclaw file read report.pdf && openclaw skill install pdf
```

### 管道操作

```bash
# 管道输出
openclaw file list ~/Downloads | grep ".pdf"
```

---

## 📚 相关附录

- [常见问题](./A-faq.md)
- [技能目录](./C-skills-catalog.md)
- [最佳实践](./D-best-practices.md)

---

<div align="center">

**🦞 OpenClaw 技能指南 | 附录 B**

</div>