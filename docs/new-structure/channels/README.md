# 渠道配置

> 选择你的沟通渠道

---

## 📊 渠道对比

| 渠道 | 配置难度 | 推荐人群 | 特点 |
|------|----------|----------|------|
| **飞书** | ⭐ 简单 | 企业用户 | 多维表格、文档、日历 |
| Telegram | ⭐⭐ 中等 | 技术用户 | 群组、隐私、国际 |
| 钉钉 | ⭐⭐ 中等 | 国内企业 | 企业通讯录、审批 |
| Discord | ⭐⭐ 中等 | 海外用户 | 群组、语音、游戏 |
| 微信 | ⭐⭐⭐ 复杂 | 个人用户 | 需企业微信 |

---

## 🚀 飞书配置（推荐）

### Step 1: 创建飞书应用

1. 访问 [飞书开放平台](https://open.feishu.cn)
2. 创建企业自建应用
3. 记下 **App ID** 和 **App Secret**

### Step 2: 配置权限

| 权限 | 说明 |
|------|------|
| `im:message` | 发送消息 |
| `im:message:receive_as_bot` | 接收消息 |
| `drive:drive` | 云盘访问 |

### Step 3: 配对连接

在 OpenClaw 中选择「飞书渠道」，输入 App ID + App Secret。

---

## 🚀 Telegram 配置

### Step 1: 创建 Bot

1. 打开 Telegram，搜索 `@BotFather`
2. 发送 `/newbot`
3. 记下 **Bot Token**

### Step 2: 配对连接

在 OpenClaw 中选择「Telegram 渠道」，输入 Bot Token。

---

## 🚀 钉钉配置

### Step 1: 创建钉钉应用

1. 访问 [钉钉开放平台](https://open.dingtalk.com)
2. 创建企业内部应用
3. 记下 **Client ID** 和 **Client Secret**

### Step 2: 配对连接

在 OpenClaw 中选择「钉钉渠道」，输入 Client ID + Client Secret。

---

## ❓ 常见问题

| 问题 | 解决方案 |
|------|----------|
| 飞书消息不回复 | 检查权限配置 |
| Telegram Bot 无响应 | 检查 Bot Token |
| 钉钉连接失败 | 检查企业应用状态 |

---

## 🔗 相关文档

- [快速开始](../start/README.md)
- [工具命令](../tools/README.md)

---

更新时间：2026-04-09