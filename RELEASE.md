# OpenClaw Skills Guide

OpenClaw 技能百科 - 小白逆袭宝典

---

## 📦 下载即用

### 方式一：问答工具（推荐）

```bash
# 一键运行（无需下载）
curl -s https://raw.githubusercontent.com/stevexia37/openclaw-skills-guide/main/scripts/qa_cli.py | python3 - "你的问题"
```

### 方式二：下载知识库

1. 下载问答库文件 `knowledge/qa.json`
2. 导入到你的 AI 工具（NotebookLM / ChatGPT / Claude）
3. 直接提问，秒得答案

### 方式三：克隆仓库

```bash
git clone https://github.com/stevexia37/openclaw-skills-guide.git
cd openclaw-skills-guide

# 交互式问答
python scripts/qa_cli.py
```

---

## 📚 内容清单

| 内容 | 数量 |
|------|------|
| 问答库 | 50+ 条 |
| 图文教程 | 30+ 篇 |
| 技能分类 | 26 类 |
| 示例技能 | 5+ 个 |

---

## ✅ 发布检查清单

每次发布新版本前，请确认以下事项：

### 内容检查

- [ ] 问答库 ID 递增且不重复
- [ ] 所有链接可访问
- [ ] README 格式正确
- [ ] CHANGELOG 已更新

### 功能检查

- [ ] qa_cli.py 可正常运行
- [ ] 一键命令可执行
- [ ] 新问答已测试

### 文件检查

- [ ] 文件编码 UTF-8
- [ ] 无多余空行
- [ ] 图片已上传 assets/

### Git 检查

- [ ] Commit message 格式正确
- [ ] 无未提交文件
- [ ] 已推送到 GitHub

### 发布步骤

1. 更新 CHANGELOG.md
2. 检查 README.md 链接
3. 测试 qa_cli.py
4. 提交所有改动
5. 创建 GitHub Release
6. 推送到 GitHub

---

## 📋 版本历史

| 版本 | 日期 | 说明 |
|------|------|------|
| v1.1.0 | 2026-03-29 | 仓库优化（问答数据化、工具升级） |
| v1.0.0 | 2026-03-28 | 首次正式发布 |

---

更新时间：2026-03-29