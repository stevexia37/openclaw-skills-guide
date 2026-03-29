# 贡献指南

感谢你考虑为 OpenClaw 技能指南做出贡献！

---

## 🤝 贡献方式

### 方式一：新增问答到知识库 ⭐ 推荐

帮助完善问答知识库，让更多人受益。

#### 快速开始

1. 打开 [`knowledge/qa.json`](knowledge/qa.json)
2. 按以下格式添加新问答
3. 提交 PR

#### 问答格式

```json
{
  "id": 51,
  "question": "你的问题内容",
  "answer": "答案内容\n\n详细说明...",
  "tags": ["标签1", "标签2"],
  "difficulty": "简单/中等/困难"
}
```

#### 字段说明

| 字段 | 必填 | 说明 |
|------|------|------|
| `id` | ✅ | 问题编号，按顺序递增（当前最新 ID 为 50） |
| `question` | ✅ | 问题内容，简洁明了 |
| `answer` | ✅ | 答案内容，支持换行（使用 `\n`） |
| `tags` | ✅ | 标签列表，用于搜索匹配 |
| `difficulty` | ⚠️ | 难度等级：简单/中等/困难 |

#### 可用标签

| 标签 | 说明 |
|------|------|
| 安装 | 安装相关问题 |
| macOS | macOS 系统特定 |
| Windows | Windows 系统特定 |
| Linux | Linux 系统特定 |
| 配对 | 配对相关问题 |
| 技能 | 技能安装/使用 |
| 文件 | 文件处理相关 |
| 定时 | 定时任务相关 |
| 错误 | 错误排查 |
| 网络 | 网络连接问题 |
| 模型 | 模型配置 |
| 高级 | 高级功能 |

#### 示例：添加一个新问答

```json
{
  "id": 51,
  "question": "如何切换不同的 AI 模型？",
  "answer": "OpenClaw 支持多种 AI 模型。\n\n切换方法：\n1. 打开设置\n2. 选择「模型配置」\n3. 选择你想用的模型\n4. 保存配置\n\n目前支持：Claude、GPT、Gemini、本地模型等。",
  "tags": ["模型", "配置"],
  "difficulty": "简单"
}
```

#### 测试你的问答

添加后，可使用问答工具测试：

```bash
# 本地测试
python scripts/qa_cli.py "你的问题"

# 或使用交互模式
python scripts/qa_cli.py --list
```

---

### 方式二：补充教程文档

在 `docs/` 目录下添加新教程。

#### 步骤

1. 选择合适的目录：
   - `docs/0-1/` - 入门教程
   - `docs/1-n/` - 进阶教程
   - `docs/skills/` - 技能教程

2. 创建新的 `.md` 文件

3. 遵循文档格式：
   ```markdown
   # 问题标题
   
   ## ✅ 目标
   完成后能达到什么效果
   
   ## 📝 步骤
   1. 第一步
   2. 第二步
   
   ## ⚠️ 常见问题
   - 问题1 → 解决方案1
   - 问题2 → 解决方案2
   
   ## 📚 相关资料
   - [链接](url)
   ```

4. 提交 PR

---

### 方式三：贡献技能示例

在 `examples/` 目录下添加技能示例。

#### 步骤

1. 在 `examples/` 下创建技能目录
2. 添加必要文件：
   - `README.md` - 技能说明
   - `skill.json` - 技能元数据（可选）
   - `main.py` 或 `main.js` - 技能代码（可选）

3. 提交 PR

**注意：** 本目录仅存放演示用的技能示例。用户如需安装完整技能，请访问 [awesome-openclaw-skills](https://github.com/openclaw/awesome-openclaw-skills) 或技能市场。

---

### 方式四：改进问答工具

优化 `scripts/qa_cli.py` 的搜索算法或功能。

#### 建议改进方向

- 更智能的搜索匹配（语义搜索）
- 添加新功能（如语音问答）
- 优化界面显示
- 支持更多输出格式

---

## 📋 PR 检查清单

提交 PR 前确认：

- [ ] 内容准确无误
- [ ] 格式符合规范
- [ ] ID 递增且不重复
- [ ] 标签与已有标签一致
- [ ] 文件编码为 UTF-8
- [ ] 提交信息清晰描述改动

---

## 📝 提交信息规范

使用以下格式：

```
类型: 简短描述 (#任务编号)

详细说明（可选）
```

类型：
- `feat` - 新功能/新内容
- `fix` - 修复错误
- `docs` - 文档更新
- `refactor` - 重构代码

示例：
- `feat: 新增 5 个问答 (#1)`
- `fix: 修复 qa_cli.py 搜索错误 (#4)`
- `docs: 更新贡献指南 (#6)`

---

## 🔍 行为准则

- 友好、尊重的交流
- 内容准确、有帮助
- 不发布敏感信息
- 遵循文档格式规范

---

## 💬 联系方式

- GitHub Issues: https://github.com/stevexia37/openclaw-skills-guide/issues
- Discussions: https://github.com/stevexia37/openclaw-skills-guide/discussions
- 官网: https://openclaw.ai

---

感谢你的贡献！🎉