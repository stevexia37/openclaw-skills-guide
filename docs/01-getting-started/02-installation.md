# 第二章：安装 OpenClaw

> 📦 5分钟完成安装，开始你的 AI 助手之旅

---

## 📋 安装前准备

### 系统要求

| 系统 | 最低版本 | 推荐配置 |
|------|----------|----------|
| **macOS** | 10.15 (Catalina) | macOS 12+ / Apple Silicon |
| **Windows** | Windows 10 | Windows 11 |
| **Linux** | Ubuntu 18.04 | Ubuntu 22.04 |

### 硬件要求

- **内存**: 最低 4GB，推荐 8GB+
- **存储**: 至少 1GB 空间
- **网络**: 稳定的网络连接

---

## 🖥️ 安装方法

### macOS 安装

#### 方法一：官网下载（推荐）

```
步骤 1: 打开 https://openclaw.ai
步骤 2: 点击「下载」
步骤 3: 选择 macOS 版本（注意 M1/M2 选 ARM 版）
步骤 4: 双击 .dmg 文件安装
```

#### ⚠️ macOS 常见问题

**问题 1: 提示「已损坏，无法打开」

```bash
# 解决方案：移除隔离属性
xattr -cr /Applications/OpenClaw.app
```

**问题 2: M1/M2 芯片提示「无法验证开发者」

```
解决方案：
1. 系统偏好设置 → 隐私与安全性
2. 找到「仍要打开」并点击
```

---

### Windows 安装

#### 官网下载安装

```
步骤 1: 打开 https://openclaw.ai
步骤 2: 点击「下载」
步骤 3: 选择 Windows 版本
步骤 4: 双击 .exe 文件安装
```

#### ⚠️ Windows 常见问题

**问题 1: 被杀毒软件拦截**

```
解决方案：
1. 暂时关闭杀毒软件
2. 或将 OpenClaw 添加到白名单
```

**问题 2: 需要管理员权限**

```
解决方案：右键 → 以管理员身份运行
```

---

### Linux 安装

#### AppImage（推荐）

```bash
# 下载 AppImage
wget https://openclaw.ai/download/linux -O OpenClaw.AppImage

# 添加执行权限
chmod +x OpenClaw.AppImage

# 运行
./OpenClaw.AppImage
```

#### Debian/Ubuntu 包

```bash
# 下载 .deb 包
wget https://openclaw.ai/download/debian -O openclaw.deb

# 安装
sudo dpkg -i openclaw.deb

# 如果缺少依赖
sudo apt-get install -f
```

---

## 📱 配对账号

### 二维码配对（推荐）

```
步骤 1: 打开 OpenClaw
步骤 2: 屏幕显示二维码
步骤 3: 用手机扫描
步骤 4: 确认配对
```

### 配对码配对

如果手机摄像头不方便：

```
步骤 1: 记下显示的配对码（如：ABCD-1234）
步骤 2: 在手机 App 中输入配对码
步骤 3: 确认配对
```

---

## ✅ 验证安装

打开终端，运行：

```bash
# 检查版本
openclaw --version

# 查看帮助
openclaw --help
```

---

## 🔧 常用命令速查

| 命令 | 功能 |
|------|------|
| `openclaw` | 启动 OpenClaw |
| `openclaw --version` | 查看版本 |
| `openclaw --help` | 查看帮助 |
| `openclaw config` | 打开配置 |
| `openclaw update` | 更新版本 |
| `openclaw doctor` | 诊断问题 |

---

## 📚 本章小结

- ✅ macOS/Windows/Linux 三平台安装教程
- ✅ 常见问题解决方案
- ✅ 配对账号方法
- ✅ 常用命令速查

---

## 📖 下一章

👉 [快速上手](./03-quick-start.md) - 开始使用 OpenClaw

---

<div align="center">

**🦞 OpenClaw 技能指南 | 第二章**

</div>