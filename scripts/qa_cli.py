#!/usr/bin/env python3
"""
OpenClaw 问答工具 - 命令行版本
================================

一个简单的问答工具，帮助用户快速找到解决方案。

使用方法：
  # 方式一：交互模式
  python qa_cli.py
  
  # 方式二：直接提问（一键运行）
  python qa_cli.py "安装时提示已损坏怎么办"
  
  # 方式三：curl 一键运行（无需下载）
  curl -s https://raw.githubusercontent.com/stevexia37/openclaw-skills-guide/main/scripts/qa_cli.py | python3 - "你的问题"
  
  # 其他命令
  python qa_cli.py --list       # 列出所有问题
  python qa_cli.py --search 关键词  # 搜索问题
  python qa_cli.py --topic 主题     # 查看某主题下的问题

作者: stevexia37
版本: 2.0.0
更新: 2026-03-29
"""

import json
import re
import sys
import os
from pathlib import Path

# ==================== 配置 ====================

# 知识库文件路径（相对于脚本位置）
SCRIPT_DIR = Path(__file__).parent.absolute()
KB_DIR = SCRIPT_DIR.parent / "knowledge"
QA_FILE = KB_DIR / "qa.json"  # 新的 qa.json 格式
FAQ_FILE = KB_DIR / "faq.jsonl"  # 兼容旧的 faq.jsonl
TOPICS_FILE = KB_DIR / "topics.json"

# 匹配阈值（低于此值视为无匹配）
MATCH_THRESHOLD = 0.1

# ==================== 数据加载 ====================

def load_qa():
    """
    加载问答知识库
    
    优先读取 qa.json，兼容 faq.jsonl
    
    返回: 问题列表，每个元素是一个字典
    """
    qa_list = []
    
    # 优先读取 qa.json
    if QA_FILE.exists():
        with open(QA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            qa_list = data.get('qas', [])
            if qa_list:
                print(f"✅ 已加载 qa.json，共 {len(qa_list)} 条问答", file=sys.stderr)
                return qa_list
    
    # 兼容 faq.jsonl
    if FAQ_FILE.exists():
        with open(FAQ_FILE, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line:
                    try:
                        item = json.loads(line)
                        # 转换 id 格式
                        if 'id' in item and isinstance(item['id'], str):
                            item['id'] = int(item['id'].replace('q', ''))
                        qa_list.append(item)
                    except json.JSONDecodeError:
                        continue
        if qa_list:
            print(f"✅ 已加载 faq.jsonl，共 {len(qa_list)} 条问答", file=sys.stderr)
            return qa_list
    
    print(f"⚠️ 知识库文件不存在", file=sys.stderr)
    return qa_list

def load_topics():
    """
    加载主题索引
    
    返回: 主题字典 {主题名: [问题ID列表]}
    """
    if not TOPICS_FILE.exists():
        return {}
    
    with open(TOPICS_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

# ==================== 搜索匹配 ====================

def simple_tokenize(text):
    """
    简单分词：提取中文词汇和英文单词
    
    参数: text - 输入文本
    返回: 词列表
    """
    # 提取中文词汇（连续的中文字符）
    chinese_words = re.findall(r'[\u4e00-\u9fa5]+', text)
    
    # 提取英文单词
    english_words = re.findall(r'[a-zA-Z]+', text.lower())
    
    # 合并
    return chinese_words + english_words

def calculate_match_score(query, question, tags):
    """
    计算匹配分数
    
    参数:
        query - 用户输入的问题
        question - FAQ 中的问题
        tags - 问题标签
    
    返回: 匹配分数 (0-1)
    """
    query_words = set(simple_tokenize(query))
    question_words = set(simple_tokenize(question))
    tag_words = set(tags)
    
    # 计算交集
    common_words = query_words & question_words
    
    # 标签匹配加分
    tag_match = query_words & tag_words
    
    # 计算分数
    if len(query_words) == 0:
        return 0
    
    base_score = len(common_words) / max(len(query_words), len(question_words))
    tag_score = len(tag_match) / max(len(query_words), 1) * 0.5
    
    return min(base_score + tag_score, 1.0)

def search_qa(query, qa_list, top_n=3):
    """
    搜索问答，返回最相关的结果
    
    参数:
        query - 用户输入
        qa_list - 问答列表
        top_n - 返回结果数量
    
    返回: 匹配结果列表 [(分数, 问题项)]
    """
    results = []
    
    for item in qa_list:
        score = calculate_match_score(
            query,
            item.get('question', ''),
            item.get('tags', [])
        )
        
        if score >= MATCH_THRESHOLD:
            results.append((score, item))
    
    # 按分数排序，取前 top_n 个
    results.sort(key=lambda x: x[0], reverse=True)
    
    return results[:top_n]

# ==================== 显示输出 ====================

def print_answer(item, score=None, brief=False):
    """
    打印单个问题的答案
    
    参数:
        item - 问题项
        score - 匹配分数（可选）
        brief - 简洁模式（只输出答案）
    """
    if brief:
        # 简洁模式：直接输出答案，适合 curl 一键运行
        print(item.get('answer', ''))
        return
    
    print("\n" + "=" * 50)
    
    if score:
        print(f"📊 匹配度: {score:.0%}")
    
    print(f"❓ 问题: {item.get('question', '')}")
    print("-" * 50)
    print(f"💡 答案:\n{item.get('answer', '')}")
    
    tags = item.get('tags', [])
    if tags:
        print(f"\n🏷️ 标签: {', '.join(tags)}")
    
    difficulty = item.get('difficulty', '')
    if difficulty:
        print(f"📈 难度: {difficulty}")
    
    print("=" * 50)

def print_all_questions(qa_list):
    """
    列出所有问题
    
    参数: qa_list - 问答列表
    """
    print("\n📚 所有问题列表:")
    print("=" * 50)
    
    for i, item in enumerate(qa_list, 1):
        qid = item.get('id', i)
        print(f"{i}. [{qid}] {item.get('question', '')}")
        tags = item.get('tags', [])
        if tags:
            print(f"   🏷️ {', '.join(tags)}")
    
    print("=" * 50)
    print(f"共 {len(qa_list)} 个问题")

def print_topics(topics, qa_list):
    """
    显示主题索引
    
    参数:
        topics - 主题字典
        qa_list - 问答列表
    """
    print("\n📂 主题分类:")
    print("=" * 50)
    
    # 创建 ID 到问题的映射
    id_to_question = {item.get('id'): item for item in qa_list}
    
    for topic, ids in topics.items():
        print(f"\n【{topic}】")
        for qid in ids:
            item = id_to_question.get(qid)
            if item:
                print(f"  • {item.get('question', '')}")
    
    print("=" * 50)

# ==================== 交互模式 ====================

def interactive_mode(qa_list, topics):
    """
    交互式问答模式
    
    参数:
        qa_list - 问答列表
        topics - 主题字典
    """
    print("\n" + "=" * 50)
    print("🦞 OpenClaw 问答工具 v2.0.0")
    print("=" * 50)
    print("输入你的问题，我来帮你找答案！")
    print("- 输入 'list' 查看所有问题")
    print("- 输入 'topics' 查看主题分类")
    print("- 输入 'quit' 或 'exit' 退出")
    print("=" * 50)
    
    while True:
        print("\n请输入问题: ")
        try:
            query = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n再见！")
            break
        
        # 处理命令
        if query.lower() in ['quit', 'exit', 'q']:
            print("再见！")
            break
        
        if query.lower() == 'list':
            print_all_questions(qa_list)
            continue
        
        if query.lower() == 'topics':
            print_topics(topics, qa_list)
            continue
        
        if not query:
            print("请输入有效的问题")
            continue
        
        # 搜索问题
        results = search_qa(query, qa_list)
        
        if results:
            print(f"\n找到 {len(results)} 个相关问题:")
            for score, item in results:
                print_answer(item, score)
        else:
            print("\n⚠️ 没找到相关问题")
            print("建议:")
            print("1. 输入 'list' 查看所有问题")
            print("2. 输入 'topics' 查看主题分类")
            print("3. 或查看文档: docs/ 目录")

# ==================== 命令行参数 ====================

def print_help():
    """打印帮助信息"""
    print(__doc__)
    print("\n更多帮助:")
    print("  - GitHub: https://github.com/stevexia37/openclaw-skills-guide")
    print("  - 文档: docs/ 目录")

def main():
    """主函数"""
    # 加载知识库
    qa_list = load_qa()
    topics = load_topics()
    
    if not qa_list:
        print("❌ 无法加载知识库，请检查文件是否存在")
        sys.exit(1)
    
    # 解析命令行参数
    args = sys.argv[1:]
    
    if not args:
        # 无参数，进入交互模式
        interactive_mode(qa_list, topics)
    
    elif args[0] == '--help' or args[0] == '-h':
        print_help()
    
    elif args[0] == '--list':
        print_all_questions(qa_list)
    
    elif args[0] == '--search':
        if len(args) < 2:
            print("请提供搜索关键词")
            print("用法: qa_cli.py --search 关键词")
            sys.exit(1)
        
        query = args[1]
        results = search_qa(query, qa_list)
        
        if results:
            print(f"搜索 '{query}' 找到 {len(results)} 个结果:")
            for score, item in results:
                print_answer(item, score)
        else:
            print(f"搜索 '{query}' 未找到结果")
    
    elif args[0] == '--topic':
        if len(args) < 2:
            print("请提供主题名称")
            print("用法: qa_cli.py --topic 主题名")
            print("可用主题:", ', '.join(topics.keys()))
            sys.exit(1)
        
        topic_name = args[1]
        
        if topic_name not in topics:
            print(f"主题 '{topic_name}' 不存在")
            print("可用主题:", ', '.join(topics.keys()))
            sys.exit(1)
        
        # 创建 ID 到问题的映射
        id_to_question = {item.get('id'): item for item in qa_list}
        
        print(f"\n【{topic_name}】相关问题:")
        for qid in topics[topic_name]:
            item = id_to_question.get(qid)
            if item:
                print_answer(item)
    
    elif args[0].startswith('--'):
        # 其他未知命令
        print(f"未知命令: {args[0]}")
        print("使用 --help 查看帮助")
        sys.exit(1)
    
    else:
        # 将所有参数作为搜索词（支持直接提问）
        query = ' '.join(args)
        results = search_qa(query, qa_list)
        
        if results:
            # 检测是否在 curl 一键模式（stdin 有数据但不是交互式）
            brief_mode = not sys.stdin.isatty()
            
            if brief_mode:
                # 简洁模式：只输出最佳答案
                print_answer(results[0][1], brief=True)
            else:
                print(f"找到 {len(results)} 个相关问题:")
                for score, item in results:
                    print_answer(item, score)
        else:
            print("⚠️ 未找到相关问题")
            print("建议:")
            print("  1. 查看所有问题: python qa_cli.py --list")
            print("  2. 查看帮助: python qa_cli.py --help")

if __name__ == '__main__':
    main()