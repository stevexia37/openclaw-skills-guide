# OpenClaw 安装教程（完整版）

## 📋 安装前准备

### 系统要求

| 系统 | 最低版本 | 推荐配置 |
|------|----------|----------|
| **macOS** | 10.15 (Catalina) | macOS 12+ / M1/M2 芯片 |
| **Windows** | Windows 10 | Windows 11 |
| **Linux** | Ubuntu 18.04+ | Ubuntu 22.04 |

### 硬件要求

- **内存**: 最低 4GB，推荐 8GB+
- **存储**: 至少 1GB 可用空间
- **网络**: 稳定的网络连接

---

## 🖥️ 方法一：图形界面安装（推荐新手）

### macOS 安装步骤

#### 步骤 1：下载安装包

1. 打开浏览器，访问 https://openclaw.ai
2. 点击「下载」按钮
3. 选择 macOS 版本（注意 M1/M2 芯片选择 ARM 版本）

#### 步骤 2：安装应用

1. 找到下载的 `.dmg` 文件（通常在「下载」文件夹）
2. 双击打开
3. 将 OpenClaw 图标拖拽到「Applications」文件夹

#### 步骤 3：首次打开

**⚠️ 如果提示「无法打开，因为它来自身份不明的开发者」：**

1. 打开「系统偏好设置」→「安全性与隐私」
2. 点击「仍要打开」按钮
3. 或者在终端运行：
   ```bash
   xattr -cr /Applications/OpenClaw.app
   ```

#### 步骤 4：配对账号

1. 打开 OpenClaw 应用
2. 屏幕显示二维码
3. 用手机扫描二维码
4. 在手机上确认配对

---

### Windows 安装步骤

#### 步骤 1：下载安装包

1. 访问 https://openclaw.ai
2. 点击「下载」
3. 选择 Windows 版本

#### 步骤 2：运行安装程序

1. 双击下载的 `.exe` 文件
2. 如果 Windows 安全中心提示，点击「更多信息」→「仍要运行」
3. 按照安装向导完成安装

#### ⚠️ 常见问题：被杀毒软件拦截

**解决方案：**
1. 暂时关闭杀毒软件
2. 或将 OpenClaw 添加到白名单
3. 重新运行安装程序

---

### Linux 安装步骤

#### 方法 1：AppImage（推荐）

```bash
# 下载 AppImage
wget https://openclaw.ai/download/linux -O OpenClaw.AppImage

# 添加执行权限
chmod +x OpenClaw.AppImage

# 运行
./OpenClaw.AppImage
```

#### 方法 2：Debian/Ubuntu 包

```bash
# 下载 .deb 包
wget https://openclaw.ai/download/debian -O openclaw.deb

# 安装
sudo dpkg -i openclaw.deb

# 如果缺少依赖，运行
sudo apt-get install -f
```

---

## 💻 方法二：命令行安装（高级用户）

### macOS 使用 Homebrew

```bash
# 添加 OpenClaw 源
brew tap openclaw/tap

# 安装 OpenClaw
brew install openclaw
```

**⚠️ 可能遇到的问题：**

| 错误信息 | 解决方案 |
|----------|----------|
| `brew: command not found` | 先安装 Homebrew：`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"` |
| `Error: openclaw/tap was not found` | 暂不支持 brew 安装，使用图形界面安装 |
| `Permission denied` | 运行 `sudo chown -R $(whoami) $(brew --prefix)/*` |

### Windows 使用 Winget

```powershell
# 安装 OpenClaw
winget install OpenClaw.OpenClaw
```

**⚠️ 可能遇到的问题：**

| 错误信息 | 解决方案 |
|----------|----------|
| `winget: command not found` | 更新 Windows 或安装 App Installer |
| `No package found` | 暂不支持 winget，使用图形界面安装 |

### Windows 使用 Chocolatey

```powershell
# 安装 OpenClaw
choco install openclaw
```

### Linux 使用 Snap

```bash
# 安装 OpenClaw
sudo snap install openclaw
```

---

## 🔧 安装后配置

### 检查安装是否成功

打开终端，运行：

```bash
# 检查版本
openclaw --version

# 查看帮助
openclaw --help
```

### 常用命令速查表

| 命令 | 功能 |
|------|------|
| `openclaw` | 启动 OpenClaw |
| `openclaw --version` | 查看版本号 |
| `openclaw --help` | 查看帮助信息 |
| `openclaw config` | 打开配置文件 |
| `openclaw update` | 更新 OpenClaw |
| `openclaw doctor` | 诊断问题 |

---

## ❓ 安装常见问题

### macOS 问题

#### Q: 提示「已损坏，无法打开」

**解决方案：**
```bash
# 方法1：移除隔离属性
xattr -cr /Applications/OpenClaw.app

# 方法2：允许任何来源
sudo spctl --master-disable
```

#### Q: M1/M2 芯片提示「无法验证开发者」

**解决方案：**
1. 系统偏好设置 → 隐私与安全性
2. 找到「仍要打开」按钮并点击

#### Q: 安装后打不开

**检查步骤：**
```bash
# 检查应用是否完整
ls -la /Applications/OpenClaw.app

# 检查是否有权限
chmod +x /Applications/OpenClaw.app/Contents/MacOS/OpenClaw
```

---

### Windows 问题

#### Q: 安装时提示「需要管理员权限」

**解决方案：**
- 右键安装程序 → 「以管理员身份运行」

#### Q: 安装后找不到应用

**解决方案：**
1. 检查安装路径（默认 `C:\Program Files\OpenClaw`）
2. 搜索「OpenClaw」
3. 如果找不到，重新安装并记住安装路径

#### Q: 运行时闪退

**解决方案：**
1. 右键 → 属性 → 兼容性 → 以兼容模式运行
2. 更新显卡驱动
3. 检查是否有杀毒软件拦截

---

### Linux 问题

#### Q: AppImage 无法运行

**解决方案：**
```bash
# 检查是否有执行权限
ls -la OpenClaw.AppImage

# 添加执行权限
chmod +x OpenClaw.AppImage

# 安装 FUSE（如果缺少）
sudo apt install fuse libfuse2
```

#### Q: 缺少依赖

**解决方案：**
```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install -f

# Fedora
sudo dnf install -f
```

---

## 📱 配对账号

### 二维码配对

1. 打开 OpenClaw
2. 显示配对二维码
3. 用手机扫描
4. 确认配对

### 配对码配对

如果没有摄像头，可以使用配对码：

1. 打开 OpenClaw
2. 记下显示的配对码（如：`ABCD-1234`）
3. 在手机 OpenClaw App 中输入配对码

---

## 🔄 更新 OpenClaw

### 自动更新

OpenClaw 会在启动时自动检查更新

### 手动更新

```bash
# 命令行更新
openclaw update

# 或重新下载最新版本
```

---

## 📚 下一步

- [快速入门](./getting-started.md) - 开始使用 OpenClaw
- [第一个技能](./beginner/first-skill.md) - 安装技能
- [常见问题](./faq.md) - 更多问题解答

---

💡 **提示**：遇到问题？在 OpenClaw 中直接提问，它会帮你解答！
