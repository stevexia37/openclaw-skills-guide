# 📁 文档目录重组计划

## 当前问题

目录混乱：
- `0-1/`、`01-getting-started/`、`02-features/`... 编号重复
- `beginner/`、`advanced/`、`appendix/` 分散
- 同一主题文件分散多处

## 新结构（参考主仓库）

```
docs/
├── README.md              # 导航入口 ⭐
│
├── install/               # 安装（合并 0-1/, installation.md）
│   ├── README.md
│   ├── env-prepare.md
│   ├── download.md
│   ├── config.md
│   └── first-run.md
│
├── start/                 # 快速开始（合并 QUICK-START.md, getting-started.md, beginner-guide.md）
│   ├── README.md
│   ├── 5-min-setup.md     # 5分钟上手 ⭐
│   ├── beginner-guide.md
│   └── first-skill.md
│
├── channels/              # 渠道配置（新建）
│   ├── README.md
│   ├── feishu.md
│   ├── telegram.md
│   ├── dingtalk.md
│   ├── wechat.md
│   └── discord.md
│
├── skills/                # 技能（合并 skills-guide.md, skill-development.md）
│   ├── README.md
│   ├── install-skills.md  # 如何安装技能 ⭐
│   ├── top-10-skills.md   # 必装 Top 10 ⭐
│   ├── develop-skills.md  # 开发技能
│   ├── soul-personality.md
│   └── self-improving.md
│
├── concepts/              # 概念（合并 features.md, comparison.md, dreaming-system.md）
│   ├── README.md
│   ├── dreaming.md        # 梦境系统 ⭐ 新功能
│   ├── memory.md          # 记忆系统
│   ├── features.md
│   └── comparison.md
│
├── tools/                 # 工具命令
│   ├── README.md
│   ├── commands.md
│   ├── cli-reference.md
│   └── tips.md
│
├── appendix/              # 附录
│   ├── faq.md
│   ├── testimonials.md
│   ├── video-tutorials.md
│   └── glossary.md
│
└── archive/               # 旧文件归档（不删除，保留历史）
    ├── 0-1/
    ├── 01-getting-started/
    ├── 02-features/
    ├── beginner/
    ├── advanced/
    └── ...
```

## 执行步骤

需要批准 mv 命令才能执行。输入 `/approve` 批准。