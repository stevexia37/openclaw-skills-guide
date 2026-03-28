# 小红书文案生成器

> 一键生成小红书爆款文案，标题、正文、标签全搞定

## 功能介绍

- **标题生成**：根据主题生成3-5个爆款标题
- **正文生成**：小红书风格正文，emoji丰富，段落清晰
- **标签推荐**：自动推荐相关标签
- **多种风格**：支持种草、测评、教程、分享等多种风格

## 安装命令

```bash
# 克隆到本地
git clone https://github.com/stevexia37/openclaw-skills-guide.git
cd openclaw-skills-guide/skills/xiaohongshu-writer

# 或直接复制 main.py 到你的项目
```

## 使用示例

### 基础用法

```python
from main import XiaohongshuWriter

# 初始化
writer = XiaohongshuWriter()

# 生成文案
result = writer.generate(
    topic="OpenClaw新手教程",
    style="tutorial",  # 教程风格
    keywords=["小白", "入门", "效率"]
)

print(result["title"])  # 标题
print(result["content"])  # 正文
print(result["tags"])  # 标签
```

### 批量生成

```python
# 批量生成多个标题
titles = writer.generate_titles(
    topic="OpenClaw技能推荐",
    count=5
)

for i, title in enumerate(titles, 1):
    print(f"{i}. {title}")
```

## 适用场景

- **博主**：日常笔记文案生成
- **运营**：批量生产内容
- **新手**：快速上手小红书
- **测试**：A/B测试不同标题

## 常见问题

### Q: 生成的文案会重复吗？
A: 每次生成都是基于最新语境，不会完全重复。

### Q: 支持哪些风格？
A: 目前支持：种草(starter)、测评(review)、教程(tutorial)、分享(share)、吐槽(roast)

### Q: 可以自定义字数吗？
A: 可以，使用 `word_count` 参数控制。

## 更新日志

- **v1.0.0** (2024-03-28): 首次发布，支持基础文案生成

---

📌 **想学更多技能封装？点这里看我的完整教程仓库**: [OpenClaw技能指南](https://github.com/stevexia37/openclaw-skills-guide)