# 更新日志

所有重要的变更都会记录在这个文件中。

格式基于 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)，
并且本项目遵循 [语义化版本](https://semver.org/lang/zh-CN/)。

## [未发布]

### 计划中
- 添加数据缓存机制
- 支持更多数据源
- 添加数据可视化功能
- 性能优化

## [0.2.0] - 2026-05-22

### ✨ 新功能

#### Stock 模块（新增 10 个命令）
- `report-dates` - 获取所有报告日期
- `board` - 获取股票所属板块
- `deal` - 获取成交明细
- `history-bill` - 获取历史资金流向
- `holder-number` - 获取最新股东人数
- `ipo` - 获取最新IPO信息
- `latest-quote` - 获取最新行情
- `members` - 获取板块成员
- `snapshot` - 获取行情快照
- `today-bill` - 获取今日资金流向

#### Fund 模块（新增 7 个命令）
- `industry` - 获取行业分布
- `pdf-reports` - 获取PDF报告
- `period-change` - 获取周期变化
- `public-dates` - 获取公开日期
- `history-multi` - 批量获取历史净值
- `realtime-rate` - 获取实时涨跌幅
- `types` - 获取类型百分比

#### Bond 模块（新增 4 个命令）
- `base-info` - 获取基本信息
- `deal` - 获取成交明细
- `history-bill` - 获取历史资金流向
- `today-bill` - 获取今日资金流向

#### Futures 模块（新增 1 个命令）
- `deal` - 获取成交明细

### 📊 统计
- 命令总数：从 17 个增加到 **39 个**
- Stock 命令：从 6 个增加到 **16 个**
- Fund 命令：从 5 个增加到 **12 个**
- Bond 命令：从 3 个增加到 **7 个**
- Futures 命令：从 3 个增加到 **4 个**

### 🎯 改进
- 完整覆盖 efinance 库的所有功能
- 新增资金流向分析功能
- 新增板块分析功能
- 新增基金深度分析功能

## [0.1.0] - 2026-05-21

### ✨ 新功能

#### 股票命令
- `stock history` - 获取股票历史K线数据
- `stock realtime` - 获取A股实时行情
- `stock billboard` - 获取龙虎榜数据
- `stock performance` - 获取公司季度业绩
- `stock base-info` - 获取股票基本信息
- `stock holder` - 获取前10大股东信息

#### 基金命令
- `fund history` - 获取基金净值历史
- `fund position` - 获取基金持仓信息
- `fund base-info` - 获取基金基本信息
- `fund manager` - 获取基金经理信息
- `fund codes` - 获取所有基金代码

#### 债券命令
- `bond realtime` - 获取可转债实时行情
- `bond history` - 获取可转债历史数据
- `bond all-info` - 获取所有可转债信息

#### 期货命令
- `futures info` - 获取期货基本信息
- `futures realtime` - 获取期货实时行情
- `futures history` - 获取期货历史数据

### 📚 文档
- README.md - 英文文档
- README_CN.md - 中文文档（含 AI Agent 详细指南）
- INSTALL.md - 安装指南
- DEMO.md - 功能演示
- CONTRIBUTING.md - 贡献指南

### 🎨 改进
- 使用 Rich 库进行美观的表格输出
- 完善的错误处理和提示
- 支持 CSV 数据导出
- 输出行数控制 (--limit)
- 完整的帮助系统

### 🛠️ 开发工具
- Makefile - 开发任务自动化
- GitHub Actions - CI/CD 配置
- Issue 模板 - Bug 报告和功能请求
- PR 模板 - Pull Request 模板

### 📦 依赖
- efinance >= 0.5.8
- typer >= 0.9.0
- rich >= 13.0.0
- pandas >= 1.3.0

## 版本说明

- **主版本号**: 不兼容的 API 变更
- **次版本号**: 向后兼容的功能新增
- **修订号**: 向后兼容的问题修复

[未发布]: https://github.com/PegasusWang/efinance-cli/compare/v0.2.0...HEAD
[0.2.0]: https://github.com/PegasusWang/efinance-cli/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/PegasusWang/efinance-cli/releases/tag/v0.1.0
