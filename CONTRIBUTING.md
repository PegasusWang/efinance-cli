# 贡献指南

感谢你考虑为 efinance-cli 做出贡献！

## 🤝 贡献方式

有很多方式可以为项目做出贡献：

- 📝 改进文档
- 🐛 报告 Bug
- 💡 提出新功能建议
- 🔧 修复 Bug
- ✨ 添加新功能
- 🌍 翻译文档
- 📢 推广项目

## 🐛 报告 Bug

如果你发现了 Bug，请：

1. 检查 [Issues](https://github.com/PegasusWang/efinance-cli/issues) 中是否已经有相关报告
2. 如果没有，创建一个新的 Issue，包含：
   - 清晰的标题和描述
   - 复现步骤
   - 期望行为
   - 实际行为
   - 环境信息（Python 版本、操作系统等）
   - 错误信息或截图

## 💡 提出新功能

如果你有新功能的想法：

1. 先在 [Issues](https://github.com/PegasusWang/efinance-cli/issues) 中讨论
2. 说明功能的使用场景
3. 提供可能的实现思路

## 🔧 开发设置

### 1. Fork 并克隆仓库

```bash
git clone https://github.com/your-username/efinance-cli.git
cd efinance-cli
```

### 2. 创建虚拟环境

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. 安装开发依赖

```bash
pip install -e ".[dev]"
```

### 4. 创建分支

```bash
git checkout -b feature/your-feature-name
```

## 📝 代码规范

### Python 代码规范

- 遵循 PEP 8 编码规范
- 使用 Black 格式化代码
- 使用类型提示
- 添加文档字符串

### 代码格式化

```bash
# 格式化代码
make format

# 或直接使用
black src/

# 代码检查
make lint

# 或直接使用
ruff check src/
```

## ✅ 测试

### 运行测试

```bash
# 运行所有测试
make test

# 或直接运行
python test_cli.py
```

### 测试你的更改

- 确保现有测试仍然通过
- 为新功能添加测试
- 测试边缘情况

## 📋 Pull Request 流程

### 1. 确保代码质量

```bash
# 格式化代码
make format

# 运行代码检查
make lint

# 运行测试
make test
```

### 2. 提交代码

```bash
git add .
git commit -m "Add: 简洁的提交信息"
```

提交信息格式：
- `Add:` 新功能
- `Fix:` Bug 修复
- `Update:` 功能更新
- `Docs:` 文档更新
- `Refactor:` 代码重构
- `Test:` 测试相关
- `Chore:` 其他杂项

### 3. 推送到你的 Fork

```bash
git push origin feature/your-feature-name
```

### 4. 创建 Pull Request

- 到 GitHub 上创建 Pull Request
- 填写 PR 模板
- 关联相关的 Issue
- 等待代码审查

## 🎯 Pull Request 检查清单

提交 PR 前，请确保：

- [ ] 代码遵循项目编码规范
- [ ] 已添加必要的测试
- [ ] 所有测试都通过
- [ ] 更新了相关文档
- [ ] 提交信息清晰明确
- [ ] 没有引入新的警告

## 📚 项目结构

```
efinance-cli/
├── src/
│   └── efinance_cli/
│       ├── __init__.py      # 包初始化
│       ├── main.py          # CLI 主入口
│       ├── stock.py         # 股票命令
│       ├── fund.py          # 基金命令
│       ├── bond.py          # 债券命令
│       └── futures.py       # 期货命令
├── tests/                   # 测试目录（待添加）
├── docs/                    # 文档目录
├── README.md                # 英文文档
├── README_CN.md             # 中文文档
├── pyproject.toml           # 项目配置
└── Makefile                 # 开发工具
```

## 🔍 代码审查

所有 Pull Request 都需要经过代码审查：

- 至少需要一位维护者的批准
- 可能需要多次迭代
- 请耐心等待回复

## 📖 文档贡献

文档改进也是重要的贡献：

- 修复拼写错误
- 改进描述清晰度
- 添加更多示例
- 翻译文档

## 🌍 翻译

欢迎帮助翻译文档：

- 目前支持：中文、英文
- 需要更多语言支持
- 保持翻译同步更新

## 💬 获取帮助

如果你在贡献过程中遇到问题：

- 查看 [Wiki](https://github.com/PegasusWang/efinance-cli/wiki)
- 在 [Discussions](https://github.com/PegasusWang/efinance-cli/discussions) 提问
- 发送邮件到维护者

## 🙏 行为准则

- 尊重所有贡献者
- 保持友好和建设性的讨论
- 接受建设性批评
- 关注对社区最有利的事情

## 📄 许可证

通过贡献代码，你同意你的代码将按照 MIT 许可证授权。

---

再次感谢你的贡献！🎉
