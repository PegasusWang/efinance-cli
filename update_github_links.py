#!/usr/bin/env python3
"""
更新项目中的 GitHub 链接
使用方法: python update_github_links.py <your-github-username>
"""

import re
import sys
from pathlib import Path


def update_file(file_path: Path, username: str):
    """更新文件中的 GitHub 链接"""
    print(f"正在处理: {file_path}")

    try:
        content = file_path.read_text(encoding='utf-8')
        original_content = content

        # 替换 GitHub 链接
        patterns = [
            (r'github\.com/yourusername/efinance-cli', f'github.com/{username}/efinance-cli'),
            (r'github\.com/yourusername', f'github.com/{username}'),
        ]

        for pattern, replacement in patterns:
            content = re.sub(pattern, replacement, content)

        if content != original_content:
            file_path.write_text(content, encoding='utf-8')
            print(f"  ✅ 已更新: {file_path}")
            return True
        else:
            print(f"  ℹ️  无需更新: {file_path}")
            return False

    except Exception as e:
        print(f"  ❌ 错误: {e}")
        return False


def main():
    """主函数"""
    if len(sys.argv) != 2:
        print("使用方法: python update_github_links.py <your-github-username>")
        print("示例: python update_github_links.py johnsmith")
        sys.exit(1)

    username = sys.argv[1]

    print(f"\n{'='*70}")
    print(f"更新 GitHub 链接为: {username}")
    print(f"{'='*70}\n")

    # 需要更新的文件列表
    files_to_update = [
        'README.md',
        'README_CN.md',
        'INSTALL.md',
        'DEMO.md',
        'pyproject.toml',
        'PROJECT_SUMMARY.md',
    ]

    updated_count = 0

    for file_name in files_to_update:
        file_path = Path(file_name)
        if file_path.exists():
            if update_file(file_path, username):
                updated_count += 1
        else:
            print(f"⚠️  文件不存在: {file_name}")

    print(f"\n{'='*70}")
    print(f"更新完成！共更新 {updated_count} 个文件")
    print(f"{'='*70}\n")

    # 显示下一步操作
    print("下一步操作:")
    print("1. 检查更新的文件: git diff")
    print("2. 提交更改: git add . && git commit -m 'Update GitHub links'")
    print("3. 创建 Git 标签: git tag v0.1.0")
    print("4. 推送到 GitHub: git push origin main --tags")


if __name__ == '__main__':
    main()
