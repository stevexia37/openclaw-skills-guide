#!/bin/bash
# ================================================
# OpenClaw 健康检查脚本
# ================================================
# 
# 功能：检查 OpenClaw 服务状态
# 
# 使用方法：
#   bash health_check.sh
#
# 作者: stevexia37
# ================================================

set -euo pipefail

echo "========================================"
echo "🦞 OpenClaw 健康检查"
echo "========================================"

# 检查 OpenClaw 是否安装
echo ""
echo "📌 检查 OpenClaw 安装..."

if command -v openclaw &> /dev/null; then
    echo "✅ OpenClaw 已安装"
    openclaw --version 2>/dev/null || echo "⚠️ 无法获取版本"
else
    echo "❌ OpenClaw 未安装"
    echo "请先安装: https://openclaw.ai"
    exit 1
fi

# 检查 OpenClaw 是否运行
echo ""
echo "📌 检查 OpenClaw 运行状态..."

if pgrep -f "openclaw" > /dev/null; then
    echo "✅ OpenClaw 正在运行"
else
    echo "⚠️ OpenClaw 未运行"
    echo "启动命令: openclaw"
fi

# 检查数据目录
echo ""
echo "📌 检查数据目录..."

DATA_DIR="$HOME/.copaw"

if [ -d "$DATA_DIR" ]; then
    echo "✅ 数据目录存在: $DATA_DIR"
    
    # 检查目录大小
    DIR_SIZE=$(du -sh "$DATA_DIR" 2>/dev/null | cut -f1)
    echo "   目录大小: $DIR_SIZE"
else
    echo "⚠️ 数据目录不存在"
fi

# 检查配置文件
echo ""
echo "📌 检查配置文件..."

CONFIG_FILE="$DATA_DIR/config.json"

if [ -f "$CONFIG_FILE" ]; then
    echo "✅ 配置文件存在"
else
    echo "⚠️ 配置文件不存在"
fi

# 检查技能目录
echo ""
echo "📌 检查技能目录..."

SKILLS_DIR="$DATA_DIR/skills"

if [ -d "$SKILLS_DIR" ]; then
    SKILL_COUNT=$(find "$SKILLS_DIR" -name "SKILL.md" 2>/dev/null | wc -l | tr -d ' ')
    echo "✅ 技能目录存在"
    echo "   已安装技能: $SKILL_COUNT 个"
else
    echo "⚠️ 技能目录不存在"
fi

# 检查日志
echo ""
echo "📌 检查最近日志..."

LOG_FILE="$DATA_DIR/copaw.log"

if [ -f "$LOG_FILE" ]; then
    echo "✅ 日志文件存在"
    echo ""
    echo "最近 5 条日志:"
    tail -5 "$LOG_FILE" 2>/dev/null || echo "⚠️ 无法读取日志"
else
    echo "⚠️ 日志文件不存在"
fi

# 总结
echo ""
echo "========================================"
echo "📋 健康检查报告总结"
echo "========================================"

echo ""
echo "如果发现问题，可以："
echo "1. 查看文档: docs/ 目录"
echo "2. 使用问答工具搜索解决方案"
echo "3. 提交 Issue: https://github.com/stevexia37/openclaw-skills-guide/issues"
echo ""
echo "========================================"