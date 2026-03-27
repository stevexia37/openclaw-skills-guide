# 如何准备安装 OpenClaw？

> 🎯 本章目标：确认你的系统可以安装 OpenClaw

---

## ✅ 检查系统要求

### macOS 用户

打开「关于本机」查看你的系统版本：

| 要求 | 最低 | 推荐 |
|------|------|------|
| 系统版本 | macOS 10.15 | macOS 12+ |
| 内存 | 4GB | 8GB+ |
| 存储 | 1GB | 2GB+ |

**Apple Silicon (M1/M2/M3) 用户注意：**
下载时选择 **ARM 版本**，不是 Intel 版本！

### Windows 用户

右键「此电脑」→「属性」查看：

| 要求 | 最低 | 推荐 |
|------|------|------|
| 系统版本 | Windows 10 | Windows 11 |
| 内存 | 4GB | 8GB+ |
| 存储 | 1GB | 2GB+ |

### Linux 用户

打开终端，运行：

```bash
# 查看系统版本
cat /etc/os-release

# 查看内存
free -h
```

支持的发行版：
- Ubuntu 18.04+
- CentOS 7+
- Debian 10+

---

## 📝 操作：检查网络连接

安装前需要确认网络正常：

### macOS / Linux

```bash
# 测试网络连接
ping -c 3 openclaw.ai
```

如果看到类似输出：
```
3 packets transmitted, 3 received
```
说明网络正常 ✅

### Windows

打开命令提示符（CMD）：

```bash
ping openclaw.ai
```

---

## ⚠️ 常见坑：防火墙和杀毒软件

### Windows 用户注意

Windows Defender 或其他杀毒软件可能会拦截安装：

**解决方法：**
1. 安装前暂时关闭杀毒软件
2. 或将 OpenClaw 添加到白名单

### macOS 用户注意

macOS Gatekeeper 可能提示「无法验证开发者」：

**解决方法：**
安装后如果提示「已损坏」，执行：
```bash
xattr -cr /Applications/OpenClaw.app
```

---

## 📝 操作：确认有足够空间

### macOS / Linux

```bash
# 查看磁盘空间
df -h
```

### Windows

查看 C 盘剩余空间，至少需要 1GB。

---

## ✅ 检查清单

安装前确认：

- [ ] 系统版本符合要求
- [ ] 内存至少 4GB
- [ ] 磁盘至少有 1GB 空间
- [ ] 网络连接正常
- [ ] 知道如何暂时关闭杀毒软件（Windows）

---

## 🎯 下一步

准备好了？继续 [安装 OpenClaw](./02-install.md)

---

## ❓ 遇到了问题？

使用问答工具搜索：
- 「系统要求」
- 「网络问题」
- 「安装失败」

或查看 [常见问题](../../knowledge/faq.jsonl)

---

<div align="center">

**🦞 OpenClaw 技能指南 | 0-1 入门**

</div>