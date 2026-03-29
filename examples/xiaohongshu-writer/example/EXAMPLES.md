# 示例输入输出

## 示例 1：教程风格

### 输入

```python
from main import XiaohongshuWriter

writer = XiaohongshuWriter()
result = writer.generate(
    topic="OpenClaw安装教程",
    style="tutorial",
    keywords=["小白", "入门", "效率"]
)
```

### 输出

```
标题：💡小白必看！OpenClaw安装教程全攻略

正文：
💡 OpenClaw安装教程来了！

**问题引入**
关键词：小白, 入门, 效率

**解决步骤**
关键词：小白, 入门, 效率

**注意事项**
关键词：小白, 入门, 效率

**总结**
关键词：小白, 入门, 效率

---

点我主页，拿走🦞

📌

标签：OpenClaw AI助手 效率神器 教程 小白逆袭
```

---

## 示例 2：种草风格

### 输入

```python
result = writer.generate(
    topic="小红书文案生成器",
    style="starter",
    keywords=["AI", "效率", "博主"]
)
```

### 输出

```
标题：🔥我花了7天搞定了小红书文案生成器🔥

正文：
🔥 小红书文案生成器来了！

**痛点**
关键词：AI, 效率, 博主

**产品介绍**
关键词：AI, 效率, 博主

**使用体验**
关键词：AI, 效率, 博主

**推荐理由**
关键词：AI, 效率, 博主

---

觉得有用就收藏吧！点我主页更多干货🦞

🦞

标签：小红书文案生成器 OpenClaw AI 效率 博主
```

---

## 示例 3：批量生成标题

### 输入

```python
titles = writer.generate_titles(
    topic="OpenClaw技能推荐",
    count=5
)
```

### 输出

```
1. 💡我终于搞懂了OpenClaw技能推荐！
2. 💡小白必看！OpenClaw技能推荐全攻略
3. 💡OpenClaw技能推荐新手踩坑实录⚠️
4. 💡我花15天搞定了OpenClaw技能推荐🔥
5. 💡别再找了！OpenClaw技能推荐都在这里
```