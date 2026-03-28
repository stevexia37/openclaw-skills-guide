# OpenClaw 自研技能

> 由 OpenClaw 小白逆袭百科团队开发的实用技能

---

## 📦 已发布技能

| 技能名称 | 功能 | 状态 | 版本 |
|----------|------|------|------|
| [xiaohongshu-writer](./xiaohongshu-writer/) | 小红书文案生成器 | ✅ 已发布 | v1.0.0 |

---

## 🚧 开发中技能

| 技能名称 | 功能 | 状态 | 预计发布 |
|----------|------|------|----------|
| git-commit-helper | Git commit 消息生成器 | 🔧 开发中 | 2024年4月 |
| todo-sync | 待办清单同步工具 | 📋 计划中 | 2024年5月 |

---

## 📥 安装方法

### 方法一：直接下载

```bash
# 克隆仓库
git clone https://github.com/stevexia37/openclaw-skills-guide.git

# 进入技能目录
cd openclaw-skills-guide/skills/xiaohongshu-writer

# 运行
python main.py --topic "你的主题"
```

### 方法二：复制文件

直接复制 `main.py` 到你的项目中使用。

---

## 🤝 贡献技能

欢迎贡献你的技能！

1. Fork 本仓库
2. 在 `skills/` 目录下创建你的技能文件夹
3. 按照 [技能模板](./SKILL-TEMPLATE.md) 编写代码和文档
4. 提交 Pull Request

---

## 📝 技能开发规范

每个技能必须包含：

- `README.md` - 功能介绍、安装方法、使用示例
- `skill.json` - 技能元数据（名称、版本、作者、依赖）
- `main.py` - 核心代码
- `example/` - 示例输入输出
- `assets/` - 封面图、演示录屏（可选）

---

📌 **想学更多技能封装？点这里看我的完整教程仓库**: [返回主页](../README.md)