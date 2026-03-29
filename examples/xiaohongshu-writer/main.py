#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
小红书文案生成器
一键生成小红书爆款文案，标题、正文、标签全搞定
"""

import random
from typing import List, Dict, Optional
from dataclasses import dataclass


@dataclass
class StyleConfig:
    """风格配置"""
    name: str
    emoji_start: str
    emoji_end: str
    structure: str


class XiaohongshuWriter:
    """小红书文案生成器"""

    # 风格配置
    STYLES = {
        "starter": StyleConfig(
            name="种草",
            emoji_start="🔥",
            emoji_end="🦞",
            structure="痛点 -> 产品介绍 -> 使用体验 -> 推荐理由"
        ),
        "review": StyleConfig(
            name="测评",
            emoji_start="📝",
            emoji_end="✅",
            structure="产品信息 -> 使用过程 -> 优缺点分析 -> 总结建议"
        ),
        "tutorial": StyleConfig(
            name="教程",
            emoji_start="💡",
            emoji_end="📌",
            structure="问题引入 -> 解决步骤 -> 注意事项 -> 总结"
        ),
        "share": StyleConfig(
            name="分享",
            emoji_start="✨",
            emoji_end="❤️",
            structure="背景故事 -> 核心内容 -> 个人感悟 -> 互动引导"
        ),
        "roast": StyleConfig(
            name="吐槽",
            emoji_start="😤",
            emoji_end="💀",
            structure="触发事件 -> 情绪表达 -> 分析吐槽 -> 结尾反转"
        )
    }

    # 爆款标题模板
    TITLE_TEMPLATES = [
        "{emoji}我终于搞懂了{topic}！",
        "{emoji}小白必看！{topic}全攻略",
        "{emoji}哭了😭{topic}终于有人讲清楚了",
        "{emoji}从零到精通🔥{topic}入门指南",
        "{emoji}{topic}新手踩坑实录⚠️",
        "{emoji}我花{x}天搞定了{topic}🔥",
        "{emoji}{topic}保姆级教程来了！",
        "{emoji}别再找了！{topic}都在这里",
    ]

    # 结尾引导模板
    CLOSING_TEMPLATES = [
        "\n\n---\n\n点我主页，拿走🦞",
        "\n\n---\n\n觉得有用就收藏吧！点我主页更多干货🦞",
        "\n\n---\n\n有问题评论区问我！点我主页拿走🦞",
    ]

    def __init__(self):
        pass

    def generate(
        self,
        topic: str,
        style: str = "tutorial",
        keywords: Optional[List[str]] = None,
        word_count: int = 300,
        emoji_density: str = "medium"
    ) -> Dict[str, str]:
        """
        生成完整文案

        Args:
            topic: 主题
            style: 风格 (starter/review/tutorial/share/roast)
            keywords: 关键词列表
            word_count: 目标字数
            emoji_density: emoji密度 (low/medium/high)

        Returns:
            包含 title, content, tags 的字典
        """
        style_config = self.STYLES.get(style, self.STYLES["tutorial"])

        # 生成标题
        title = self._generate_title(topic, style_config)

        # 生成正文
        content = self._generate_content(
            topic, style_config, keywords, word_count, emoji_density
        )

        # 生成标签
        tags = self._generate_tags(topic, keywords)

        return {
            "title": title,
            "content": content,
            "tags": tags
        }

    def generate_titles(
        self,
        topic: str,
        count: int = 5,
        style: str = "tutorial"
    ) -> List[str]:
        """
        批量生成标题

        Args:
            topic: 主题
            count: 生成数量
            style: 风格

        Returns:
            标题列表
        """
        style_config = self.STYLES.get(style, self.STYLES["tutorial"])
        templates = random.sample(
            self.TITLE_TEMPLATES,
            min(count, len(self.TITLE_TEMPLATES))
        )

        titles = []
        for template in templates:
            title = template.format(
                emoji=style_config.emoji_start,
                topic=topic,
                x=random.randint(1, 30)
            )
            titles.append(title)

        return titles

    def _generate_title(
        self,
        topic: str,
        style_config: StyleConfig
    ) -> str:
        """生成单个标题"""
        template = random.choice(self.TITLE_TEMPLATES)
        return template.format(
            emoji=style_config.emoji_start,
            topic=topic,
            x=random.randint(1, 30)
        )

    def _generate_content(
        self,
        topic: str,
        style_config: StyleConfig,
        keywords: Optional[List[str]],
        word_count: int,
        emoji_density: str
    ) -> str:
        """生成正文"""
        # 构建正文框架
        structure = style_config.structure.split(" -> ")

        content_parts = []

        # 开头
        content_parts.append(f"{style_config.emoji_start} {topic}来了！\n")

        # 主体内容（根据结构生成）
        for i, section in enumerate(structure):
            if i == 0:
                content_parts.append(f"\n**{section}**\n")
            else:
                content_parts.append(f"\n**{section}**\n")

            # 添加示例内容
            if keywords:
                content_parts.append(f"关键词：{', '.join(keywords[:3])}\n")

        # 结尾引导
        closing = random.choice(self.CLOSING_TEMPLATES)
        content_parts.append(closing)

        # 添加emoji结尾
        content_parts.append(f"\n\n{style_config.emoji_end}")

        return "".join(content_parts)

    def _generate_tags(
        self,
        topic: str,
        keywords: Optional[List[str]]
    ) -> List[str]:
        """生成标签"""
        base_tags = ["OpenClaw", "AI助手", "效率神器", "教程", "小白逆袭"]

        # 添加主题相关标签
        topic_tag = topic.replace(" ", "")
        if topic_tag not in base_tags:
            base_tags.insert(0, topic_tag)

        # 添加关键词标签
        if keywords:
            for kw in keywords[:2]:
                kw_tag = kw.replace(" ", "")
                if kw_tag not in base_tags:
                    base_tags.append(kw_tag)

        return base_tags[:5]


def main():
    """命令行入口"""
    import argparse

    parser = argparse.ArgumentParser(description="小红书文案生成器")
    parser.add_argument("--topic", "-t", required=True, help="主题")
    parser.add_argument("--style", "-s", default="tutorial",
                        choices=["starter", "review", "tutorial", "share", "roast"],
                        help="风格")
    parser.add_argument("--keywords", "-k", nargs="+", help="关键词")
    parser.add_argument("--count", "-c", type=int, default=1, help="生成数量")

    args = parser.parse_args()

    writer = XiaohongshuWriter()

    for i in range(args.count):
        result = writer.generate(
            topic=args.topic,
            style=args.style,
            keywords=args.keywords
        )

        print(f"\n{'='*50}")
        print(f"文案 {i+1}:")
        print(f"{'='*50}")
        print(f"\n标题：{result['title']}")
        print(f"\n正文：\n{result['content']}")
        print(f"\n标签：{' '.join(result['tags'])}")


if __name__ == "__main__":
    main()