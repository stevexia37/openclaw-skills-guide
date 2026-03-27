# 示例代码

> 📦 实用的自动化脚本和配置示例

---

## 📋 目录结构

```
examples/
├── automation/     自动化脚本
├── configs/        配置文件示例
└── skills/         技能开发示例
```

---

## 🤖 自动化脚本

### 定时任务脚本

```python
# daily_reminder.py
# 每日提醒脚本示例

import schedule
import time

def morning_reminder():
    print("早上9点：提醒开会")

def lunch_reminder():
    print("中午12点：提醒午餐")

def evening_reminder():
    print("下午5点：提醒写周报")

schedule.every().day.at("09:00").do(morning_reminder)
schedule.every().day.at("12:00").do(lunch_reminder)
schedule.every().day.at("17:00").do(evening_reminder)

while True:
    schedule.run_pending()
    time.sleep(60)
```

### 文件整理脚本

```python
# file_organizer.py
# 文件按类型整理示例

import os
import shutil

def organize_files(directory):
    categories = {
        '图片': ['.jpg', '.png', '.gif', '.webp'],
        '文档': ['.pdf', '.doc', '.docx', '.txt'],
        '视频': ['.mp4', '.mov', '.avi'],
        '音乐': ['.mp3', '.wav', '.flac']
    }
    
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            ext = os.path.splitext(file)[1].lower()
            for category, extensions in categories.items():
                if ext in extensions:
                    target_dir = os.path.join(directory, category)
                    os.makedirs(target_dir, exist_ok=True)
                    shutil.move(file_path, target_dir)
                    print(f"已移动: {file} → {category}/")
```

---

## ⚙️ 配置文件示例

### OpenClaw 基本配置

```json
{
  "model": "gpt-4",
  "language": "zh-CN",
  "storage": "local",
  "features": {
    "file_management": true,
    "schedule": true,
    "browser": true,
    "terminal": true
  },
  "skills": [
    "cron",
    "pdf",
    "xlsx"
  ]
}
```

### 定时任务配置

```json
{
  "tasks": [
    {
      "id": 1,
      "time": "09:00",
      "content": "提醒开会",
      "repeat": "daily"
    },
    {
      "id": 2,
      "time": "17:00",
      "content": "提醒写周报",
      "repeat": "weekly",
      "day": "Friday"
    }
  ]
}
```

---

## 🛠️ 技能开发示例

### 简单技能结构

```markdown
# my-skill/SKILL.md

## 功能
- 功能1
- 功能2

## 使用方法
示例对话

## 配置
JSON 配置说明
```

### 技能配置文件

```json
{
  "name": "my-skill",
  "version": "1.0.0",
  "description": "技能描述",
  "author": "你的名字",
  "dependencies": []
}
```

---

## 📚 使用方法

1. 浏览示例代码
2. 复制到你的项目
3. 根据需求修改
4. 在 OpenClaw 中测试

---

<div align="center">

**🦞 OpenClaw 技能指南 | 示例代码**

</div>