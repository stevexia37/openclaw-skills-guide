# 如何安装 OpenClaw？

> 🎯 本章目标：成功安装并打开 OpenClaw

---

## ✅ 目标

完成本章后，你将：
- 下载 OpenClaw 安装包
- 完成安装
- 打开 OpenClaw 应用

---

## 📝 操作：下载安装包

### 步骤 1：打开官网

浏览器打开：https://openclaw.ai

### 步骤 2：点击下载

找到「下载」按钮，点击。

### 步骤 3：选择版本

根据你的系统选择：

| 系统 | 文件格式 | 注意事项 |
|------|----------|----------|
| macOS (Intel) | .dmg | 选择 Intel 版 |
| macOS (M1/M2/M3) | .dmg | **选择 ARM 版** ⚠️ |
| Windows | .exe | 64位系统选 x64 |
| Linux | AppImage | 通用格式 |

---

## 📝 操作：安装 OpenClaw

### macOS 安装步骤

1. 找到下载的 `.dmg` 文件（在「下载」文件夹）
2. 双击打开
3. 将 OpenClaw 图标拖到「Applications」文件夹
4. 完成！

**⚠️ 如果提示「已损坏，无法打开」：**

打开终端，运行：
```bash
xattr -cr /Applications/OpenClaw.app
```

解释：这个命令移除 macOS 的安全隔离属性。

---

### Windows 安装步骤

1. 找到下载的 `.exe` 文件
2. 双击运行
3. 按安装向导完成安装

**⚠️ 如果被杀毒软件拦截：**

1. 点击「更多信息」
2. 点击「仍要运行」
3. 或暂时关闭杀毒软件后再安装

---

### Linux 安装步骤

打开终端：

```bash
# 进入下载目录
cd ~/Downloads

# 添加执行权限
chmod +x OpenClaw.AppImage

# 运行（测试）
./OpenClaw.AppImage
```

如果想安装到系统：
```bash
# 移动到应用目录
sudo mv OpenClaw.AppImage /usr/local/bin/openclaw

# 之后可以直接运行
openclaw
```

---

## 📝 操作：首次打开

### macOS

1. 打开「Finder」
2. 进入「Applications」文件夹
3. 找到 OpenClaw，双击打开

**首次打开可能提示：**
> 「无法打开，因为它来自身份不明的开发者」

**解决方法：**
1. 系统偏好设置 → 隐私与安全性
2. 找到「仍要打开」按钮并点击

---

### Windows

1. 双击桌面上的 OpenClaw 图标
2. 或从开始菜单找到 OpenClaw

---

### Linux

```bash
# 直接运行
./OpenClaw.AppImage

# 或如果已安装
openclaw
```

---

## ⚠️ 常见坑

### 常见问题 1：下载速度慢

**原因：** 网络问题或服务器繁忙

**解决：**
1. 尝试换个时间段下载
2. 使用下载工具（如 IDM）
3. 找镜像下载链接

---

### 常见问题 2：安装后打不开

**macOS：**
运行 `xattr -cr /Applications/OpenClaw.app`

**Windows：**
检查杀毒软件是否拦截

**Linux：**
检查是否有执行权限：`chmod +x OpenClaw.AppImage`

---

### 常见问题 3：版本不匹配

**症状：** macOS M1/M2 用户下载了 Intel 版

**解决：**
重新下载 **ARM 版本**（文件名通常有 arm64 或 apple-silicon）

---

## ✅ 检查清单

安装完成后确认：

- [ ] OpenClaw 应用出现在应用列表
- [ ] 双击可以打开
- [ ] 屏幕显示配对二维码或配对码
- [ ] 没有报错提示

---

## 🎯 下一步

安装成功！继续 [配置账号配对](./03-config.md)

---

## ❓ 遇到了问题？

使用问答工具搜索：
- 「安装失败」
- 「已损坏」
- 「打不开」

或查看 [常见问题](../../knowledge/faq.jsonl)

---

<div align="center">

**🦞 OpenClaw 技能指南 | 0-1 入门**

</div>