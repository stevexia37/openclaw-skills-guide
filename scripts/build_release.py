#!/usr/bin/env python3
"""
OpenClaw 问答工具 - 打包脚本
============================

使用 PyInstaller 将 qa_cli.py 打包成独立可执行文件。

使用方法:
  python build_release.py

注意:
  - 需要先安装 PyInstaller: pip install pyinstaller
  - 打包后的文件在 releases/ 目录
  - 会根据系统生成对应的可执行文件

作者: stevexia37
版本: 1.0.0
"""

import os
import sys
import platform
import shutil
import subprocess
from pathlib import Path

# ==================== 配置 ====================

SCRIPT_DIR = Path(__file__).parent.absolute()
PROJECT_DIR = SCRIPT_DIR.parent

QA_CLI_SCRIPT = SCRIPT_DIR / "qa_cli.py"
RELEASES_DIR = PROJECT_DIR / "releases"
KB_DIR = PROJECT_DIR / "knowledge"

# 输出文件名（根据系统不同）
OUTPUT_NAMES = {
    'Windows': 'qa_tool_windows.exe',
    'Darwin': 'qa_tool_macos',
    'Linux': 'qa_tool_linux'
}

# ==================== 检查环境 ====================

def check_pyinstaller():
    """检查 PyInstaller 是否安装"""
    try:
        subprocess.run(['pyinstaller', '--version'], capture_output=True)
        return True
    except FileNotFoundError:
        print("❌ PyInstaller 未安装")
        print("请先安装: pip install pyinstaller")
        return False

def get_system_name():
    """获取系统名称"""
    system = platform.system()
    return system

# ==================== 打包函数 ====================

def build_executable():
    """执行打包"""
    system = get_system_name()
    output_name = OUTPUT_NAMES.get(system, 'qa_tool')
    
    print(f"正在为 {system} 系统打包...")
    print(f"输出文件: {output_name}")
    
    # 确保 releases 目录存在
    RELEASES_DIR.mkdir(exist_ok=True)
    
    # PyInstaller 命令
    cmd = [
        'pyinstaller',
        '--onefile',              # 打包成单文件
        '--name', output_name,    # 输出文件名
        '--distpath', str(RELEASES_DIR),  # 输出目录
        '--workpath', str(RELEASES_DIR / 'build'),
        '--specpath', str(RELEASES_DIR),
        '--clean',                # 清理临时文件
        str(QA_CLI_SCRIPT)
    ]
    
    # 运行打包
    result = subprocess.run(cmd, capture_output=True)
    
    if result.returncode == 0:
        print(f"✅ 打包成功!")
        print(f"文件位置: {RELEASES_DIR / output_name}")
        
        # 复制知识库到 releases 目录（可选）
        copy_knowledge_to_releases()
        
        return True
    else:
        print(f"❌ 打包失败")
        print(result.stderr.decode())
        return False

def copy_knowledge_to_releases():
    """复制知识库到 releases 目录"""
    print("正在复制知识库...")
    
    release_kb_dir = RELEASES_DIR / 'knowledge'
    release_kb_dir.mkdir(exist_ok=True)
    
    # 复制 faq.jsonl
    faq_src = KB_DIR / 'faq.jsonl'
    faq_dst = release_kb_dir / 'faq.jsonl'
    if faq_src.exists():
        shutil.copy(faq_src, faq_dst)
        print(f"  ✅ {faq_dst}")
    
    # 复制 topics.json
    topics_src = KB_DIR / 'topics.json'
    topics_dst = release_kb_dir / 'topics.json'
    if topics_src.exists():
        shutil.copy(topics_src, topics_dst)
        print(f"  ✅ {topics_dst}")
    
    print("知识库复制完成!")

# ==================== 创建说明文件 ====================

def create_readme_release():
    """创建 Release 说明文件"""
    readme_content = """# OpenClaw 问答工具 - 使用说明

## 📦 文件列表

根据你的操作系统，下载对应的文件：

- **Windows**: `qa_tool_windows.exe`
- **macOS**: `qa_tool_macos`
- **Linux**: `qa_tool_linux`

## 🚀 使用方法

### Windows

1. 双击 `qa_tool_windows.exe` 运行
2. 或在命令行中运行：`qa_tool_windows.exe`

### macOS

1. 打开终端
2. 进入文件所在目录
3. 添加执行权限：`chmod +x qa_tool_macos`
4. 运行：`./qa_tool_macos`

### Linux

1. 打开终端
2. 进入文件所在目录
3. 添加执行权限：`chmod +x qa_tool_linux`
4. 运行：`./qa_tool_linux`

## 📖 功能说明

### 交互模式（默认）

直接运行程序，进入问答模式：

```
请输入问题:
> 安装失败怎么办
```

### 命令行参数

- `--list` 或 `-l`: 列出所有问题
- `--search 关键词`: 直接搜索问题
- `--topic 主题名`: 查看某主题下的问题
- `--help` 或 `-h`: 显示帮助信息

### 示例

```bash
# 列出所有问题
qa_tool --list

# 搜索问题
qa_tool --search 安装

# 查看主题
qa_tool --topic 技能
```

## 📂 知识库位置

问答工具需要 `knowledge/` 目录中的文件：
- `faq.jsonl` - 问题知识库
- `topics.json` - 主题索引

请确保这些文件与可执行文件在同一目录下。

## ❓ 遇到问题？

1. 确保知识库文件存在
2. 检查是否有执行权限（macOS/Linux）
3. 查看 GitHub Issues: https://github.com/stevexia37/openclaw-skills-guide/issues

---

Made with ❤️ for OpenClaw users
"""
    
    readme_path = RELEASES_DIR / 'README_RELEASE.md'
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    print(f"✅ 创建说明文件: {readme_path}")

# ==================== 主函数 ====================

def main():
    """主函数"""
    print("=" * 50)
    print("🦞 OpenClaw 问答工具打包脚本")
    print("=" * 50)
    
    # 检查 PyInstaller
    if not check_pyinstaller():
        sys.exit(1)
    
    # 检查源文件
    if not QA_CLI_SCRIPT.exists():
        print(f"❌ 源文件不存在: {QA_CLI_SCRIPT}")
        sys.exit(1)
    
    # 执行打包
    success = build_executable()
    
    if success:
        # 创建说明文件
        create_readme_release()
        
        print("\n" + "=" * 50)
        print("🎉 打包完成!")
        print("=" * 50)
        print(f"文件位置: {RELEASES_DIR}")
        print("\n下一步:")
        print("1. 测试打包的可执行文件")
        print("2. 上传到 GitHub Releases")
    
    sys.exit(0 if success else 1)

if __name__ == '__main__':
    main()