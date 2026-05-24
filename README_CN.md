# efinance-cli

[English](https://github.com/PegasusWang/efinance-cli/blob/master/README.md) | [中文文档](README_CN.md)

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg?style=flat)](https://pypi.python.org/pypi/efinance-cli)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

[efinance](https://github.com/Micro-sheep/efinance) 的命令行工具 - 从命令行获取股票、基金、债券和期货数据。

专为 AI code agent（Claude Code CLI、Cursor、Copilot CLI 等）和终端用户设计。

## 功能特性

- 🚀 **简单易用**: 直观的命令行界面
- 📊 **丰富的数据**: 支持股票、基金、债券、期货
- 🎨 **美观的输出**: 使用 Rich 库进行表格格式化
- 💾 **数据导出**: 支持 CSV 格式导出
- 📚 **完善的文档**: 详细的帮助信息和文档
- 🤖 **AI 友好**: 专为 AI Code Agent 优化

## 安装

### 从源码安装（推荐用于开发）

```bash
git clone https://github.com/PegasusWang/efinance-cli
cd efinance-cli
pip install -e .
```

### 从 PyPI 安装（即将发布）

```bash
pip install efinance-cli
```

## 快速开始

安装完成后，你就可以使用 `efinance-cli` 命令：

```bash
# 显示帮助信息
efinance-cli --help

# 显示版本
efinance-cli version

# 查看股票命令帮助
efinance-cli stock --help
```

## 使用指南

### 股票命令

#### 获取股票历史K线数据

```bash
# 获取贵州茅台（600519）历史数据
efinance-cli stock history 600519

# 指定日期范围
efinance-cli stock history 600519 --start 2024-01-01 --end 2024-12-31

# 获取5分钟K线数据
efinance-cli stock history 600519 --klt 5

# 保存到CSV文件
efinance-cli stock history 600519 -o stock_data.csv

# 限制显示行数
efinance-cli stock history 600519 --limit 20
```

#### 获取实时行情

```bash
# 获取所有A股实时行情
efinance-cli stock realtime

# 限制显示数量
efinance-cli stock realtime --limit 50

# 保存到CSV
efinance-cli stock realtime -o realtime_quotes.csv
```

#### 获取龙虎榜数据

```bash
# 获取最新龙虎榜
efinance-cli stock billboard

# 指定日期范围
efinance-cli stock billboard --start 2024-01-01 --end 2024-01-31

# 保存数据
efinance-cli stock billboard -o billboard.csv
```

#### 获取公司业绩

```bash
# 获取所有公司季度业绩
efinance-cli stock performance

# 保存数据
efinance-cli stock performance -o performance.csv
```

#### 获取股票基本信息

```bash
# 获取单只股票基本信息
efinance-cli stock base-info 600519

# 获取多只股票信息
efinance-cli stock base-info 600519 000001 000002
```

#### 获取股东信息

```bash
# 获取前10大股东
efinance-cli stock holder 600519

# 保存数据
efinance-cli stock holder 600519 -o holders.csv
```

### 基金命令

#### 获取基金净值历史

```bash
# 获取基金历史净值（招商中证白酒指数 161725）
efinance-cli fund history 161725

# 保存数据
efinance-cli fund history 161725 -o fund_history.csv

# 限制显示行数
efinance-cli fund history 161725 --limit 30
```

#### 获取基金持仓

```bash
# 获取基金持仓信息
efinance-cli fund position 161725

# 保存持仓数据
efinance-cli fund position 161725 -o fund_position.csv
```

#### 获取基金基本信息

```bash
# 获取单只基金信息
efinance-cli fund base-info 161725

# 获取多只基金信息
efinance-cli fund base-info 161725 005827
```

#### 获取基金经理信息

```bash
# 获取基金经理信息
efinance-cli fund manager 161725
```

#### 获取所有基金代码

```bash
# 获取所有基金代码列表
efinance-cli fund codes
```

### 债券命令

#### 获取可转债实时行情

```bash
# 获取所有可转债实时行情
efinance-cli bond realtime

# 限制显示数量
efinance-cli bond realtime --limit 30

# 保存数据
efinance-cli bond realtime -o bond_quotes.csv
```

#### 获取可转债历史数据

```bash
# 获取可转债历史数据（东财转3 123111）
efinance-cli bond history 123111

# 保存数据
efinance-cli bond history 123111 -o bond_history.csv
```

#### 获取所有可转债信息

```bash
# 获取所有可转债基本信息
efinance-cli bond all-info

# 保存数据
efinance-cli bond all-info -o all_bonds.csv
```

### 期货命令

#### 获取期货基本信息

```bash
# 获取所有期货基本信息
efinance-cli futures info

# 保存数据
efinance-cli futures info -o futures_info.csv
```

#### 获取期货实时行情

```bash
# 获取期货实时行情
efinance-cli futures realtime

# 保存数据
efinance-cli futures realtime -o futures_realtime.csv
```

#### 获取期货历史数据

```bash
# 获取单个期货历史数据（动力煤主力 115.ZCM）
efinance-cli futures history 115.ZCM

# 获取多个期货历史数据
efinance-cli futures history 115.ZCM 115.ZC109

# 保存数据
efinance-cli futures history 115.ZCM -o futures_history.csv
```

## 命令参考

### 全局命令

| 命令 | 描述 |
|------|------|
| `--help` | 显示帮助信息 |
| `version` | 显示版本信息 |

### 股票命令

| 命令 | 描述 |
|------|------|
| `history` | 获取股票历史K线数据 |
| `realtime` | 获取所有A股实时行情 |
| `billboard` | 获取龙虎榜数据 |
| `performance` | 获取公司季度业绩 |
| `base-info` | 获取股票基本信息 |
| `holder` | 获取前10大股东信息 |

### 基金命令

| 命令 | 描述 |
|------|------|
| `history` | 获取基金净值历史 |
| `position` | 获取基金持仓信息 |
| `base-info` | 获取基金基本信息 |
| `manager` | 获取基金经理信息 |
| `codes` | 获取所有基金代码 |

### 债券命令

| 命令 | 描述 |
|------|------|
| `realtime` | 获取可转债实时行情 |
| `history` | 获取可转债历史数据 |
| `all-info` | 获取所有可转债信息 |

### 期货命令

| 命令 | 描述 |
|------|------|
| `info` | 获取期货基本信息 |
| `realtime` | 获取期货实时行情 |
| `history` | 获取期货历史数据 |

## 选项说明

### 通用选项

- `--output, -o`: 输出文件路径（CSV 格式）
- `--limit, -l`: 最大显示行数（默认：50）

### 股票历史数据选项

- `--start, -s`: 开始日期（YYYY-MM-DD）
- `--end, -e`: 结束日期（YYYY-MM-DD）
- `--klt, -k`: K线类型
  - `101`: 日K线（默认）
  - `102`: 周K线
  - `103`: 月K线
  - `5`: 5分钟K线
  - `15`: 15分钟K线
  - `30`: 30分钟K线
  - `60`: 60分钟K线
- `--fqt, -f`: 复权类型
  - `0`: 不复权
  - `1`: 前复权（默认）
  - `2`: 后复权

## 与 AI Code Agent 集成

本 CLI 工具专为 AI code agent 优化设计，提供结构化的数据输出和完善的错误处理机制。

### 为什么需要 AI Agent 集成？

- **降低使用门槛**: 用户无需记忆复杂命令，用自然语言描述需求即可
- **自动化工作流**: AI 可以组合多个命令完成复杂任务
- **智能分析**: AI 可以对获取的数据进行深入分析和解读
- **错误恢复**: AI 可以根据错误信息自动调整命令参数

### 核心优势

#### 1. 结构化输出

使用 Rich 库进行表格格式化，输出清晰易读，便于 AI 解析和理解。

#### 2. 完善的错误处理

清晰的错误信息和退出码，便于 AI 理解问题原因并自动调整策略。

#### 3. 详细的帮助系统

每个命令都有 `--help` 选项，提供完整的使用说明，AI 可以自主学习命令用法。

#### 4. CSV 导出功能

支持数据导出到 CSV 文件，便于后续处理和分析，适合多步骤工作流。

#### 5. 输出行数控制

使用 `--limit` 选项防止输出过长，避免超过 AI 的上下文窗口限制。

### Claude Code CLI 使用指南

Claude Code CLI 是 Anthropic 官方的命令行工具，非常适合与 efinance-cli 配合使用。

#### 基础使用场景

**场景 1: 简单数据查询**

```
用户: "查询贵州茅台的最新股价和基本信息"

Claude 执行:
efinance-cli stock base-info 600519

输出:
基金代码  基金简称    成立日期    涨跌幅  最新净值  基金公司
600519   贵州茅台    2001-08-27  +1.2%  1850.00  贵州茅台酒股份有限公司
```

**场景 2: 数据导出和分析**

```
用户: "获取最近一个月的茅台股票数据，保存为CSV，并分析趋势"

Claude 执行步骤:
1. efinance-cli stock history 600519 --start 2026-04-21 --end 2026-05-21 -o moutai_month.csv
2. python -c "
import pandas as pd
df = pd.read_csv('moutai_month.csv')
print('平均收盘价:', df['收盘'].mean())
print('最高价:', df['最高'].max())
print('最低价:', df['最低'].min())
print('总涨跌幅:', (df['收盘'].iloc[-1] - df['收盘'].iloc[0]) / df['收盘'].iloc[0] * 100, '%')
"
```

**场景 3: 批量数据获取**

```
用户: "获取茅台、五粮液、泸州老窖三只股票的基本信息并比较"

Claude 执行:
efinance-cli stock base-info 600519 000858 000568

输出对比表格，Claude 会自动分析并给出投资建议
```

#### 高级使用场景

**场景 4: 基金研究**

```
用户: "帮我分析富国久利债券基金（003877）的投资价值"

Claude 工作流:
1. 获取基本信息: efinance-cli fund base-info 003877
2. 查看历史业绩: efinance-cli fund history 003877 --limit 30
3. 分析持仓结构: efinance-cli fund position 003877
4. 综合分析并给出投资建议
```

**场景 5: 市场监控**

```
用户: "帮我找出今天涨幅最大的前10只股票"

Claude 执行:
1. efinance-cli stock realtime -o today_stocks.csv
2. python -c "
import pandas as pd
df = pd.read_csv('today_stocks.csv')
top_10 = df.nlargest(10, '涨跌幅')
print(top_10[['股票代码', '股票名称', '涨跌幅', '最新价', '成交额']])
"
```

**场景 6: 投资组合分析**

```
用户: "我持有茅台(600519)、平安(601318)、招商银行(600036)，帮我分析这几只股票的近期表现"

Claude 工作流:
1. 获取各股票历史数据
2. 分析涨跌幅、波动率
3. 计算相关性
4. 给出投资组合建议
```

#### AI Agent 工作模式

**模式 1: 单命令执行**

```
用户指令 → Claude 理解意图 → 选择合适的 efinance-cli 命令 → 执行并返回结果
```

**模式 2: 多命令组合**

```
用户指令 → Claude 拆解任务 → 执行多个命令 → 整合数据 → 分析和解读
```

**模式 3: 数据驱动分析**

```
用户指令 → 获取数据 → 保存到文件 → 使用 Python 分析 → 可视化展示 → 投资建议
```

### 最佳实践

#### 1. 明确指定参数

✅ **好的提问方式**:
```
"获取贵州茅台(600519)从2024-01-01到2024-12-31的日K线数据，保存到CSV文件"
```

❌ **不明确的提问**:
```
"查一下茅台的数据"  # 不明确的时间范围、数据类型、输出方式
```

#### 2. 分步骤处理复杂任务

✅ **推荐方式**:
```
"第一步：获取茅台最近30天的股票数据
 第二步：分析价格趋势
 第三步：给出买入/卖出建议"
```

#### 3. 利用 CSV 导出功能

```
"获取数据并保存到文件，然后进行深度分析"
```

这样可以让 AI 在后续步骤中复用数据，避免重复请求。

#### 4. 指定数据量限制

```
"获取最近100条数据"  # 避免数据过多导致分析困难
```

### 实际案例演示

#### 案例 1: Claude Code CLI 快速查询

**用户提问**:
```
"使用 efinance-cli 获取贵州茅台(600519)最近30天的K线数据，并保存到CSV文件"
```

**Claude 执行**:
```bash
efinance-cli stock history 600519 --limit 30 -o moutai_30days.csv
```

**Claude 分析**:
```
已成功获取贵州茅台最近30个交易日的数据并保存到 moutai_30days.csv。
数据显示：
- 最新收盘价：1850.00元
- 区间涨跌幅：+2.3%
- 区间最高价：1875.00元
- 区间最低价：1810.00元
建议：近期走势稳健，可关注...
```

#### 案例 2: 多步骤数据分析

**用户提问**:
```
"帮我分析一下招商中证白酒指数基金(161725)的投资价值"
```

**Claude 完整工作流**:

**步骤1: 获取基本信息**
```bash
efinance-cli fund base-info 161725
```

**步骤2: 查看历史业绩**
```bash
efinance-cli fund history 161725 --limit 60 -o fund_history.csv
```

**步骤3: 分析持仓结构**
```bash
efinance-cli fund position 161725 -o fund_position.csv
```

**步骤4: 综合分析**
```python
import pandas as pd

# 分析历史净值走势
history = pd.read_csv('fund_history.csv')
performance = {
    '近期收益率': f"{((history['单位净值'].iloc[0] - history['单位净值'].iloc[-1]) / history['单位净值'].iloc[-1] * 100):.2f}%",
    '波动率': f"{history['单位净值'].std():.4f}",
    '最大净值': history['单位净值'].max(),
    '最小净值': history['单位净值'].min()
}

# 分析持仓集中度
position = pd.read_csv('fund_position.csv')
top10_ratio = position['持仓占比'].sum()

print("基金投资价值分析报告：")
print("1. 历史业绩：", performance)
print("2. 持仓集中度：前十大重仓股占比", top10_ratio, "%")
print("3. 投资建议：...")
```

#### 案例 3: 实时市场监控

**用户提问**:
```
"获取当前所有A股的实时行情，并找出涨幅前10的股票"
```

**Claude 执行步骤**:

```bash
# 第一步：获取实时数据
efinance-cli stock realtime -o realtime_stocks.csv

# 第二步：筛选涨幅前10
python -c "
import pandas as pd
df = pd.read_csv('realtime_stocks.csv')
top_gainers = df.nlargest(10, '涨跌幅')
print('📈 今日涨幅前10股票：')
print(top_gainers[['股票代码', '股票名称', '涨跌幅', '最新价', '成交额']].to_string(index=False))
"
```

**输出结果**:
```
📈 今日涨幅前10股票：
股票代码  股票名称  涨跌幅  最新价  成交额
688xxx  XXX科技  +10.02%  50.00  1.2亿
000xxx  XXX电子   +9.98%  30.50  0.8亿
...
```

### 其他 AI Agent 集成

#### Cursor/Copilot 集成示例

```
"获取当前所有A股的实时行情，并找出涨幅前10的股票"
```

执行步骤：

```bash
# 1. 获取实时数据
efinance-cli stock realtime -o realtime_stocks.csv

# 2. 使用 Python 分析
python -c "
import pandas as pd
df = pd.read_csv('realtime_stocks.csv')
top_gainers = df.nlargest(10, '涨跌幅')
print(top_gainers[['股票代码', '股票名称', '涨跌幅', '最新价']])
"
```

### 数据分析示例

```bash
# 获取股票数据
efinance-cli stock history 600519 -o stock.csv --limit 100

# 使用 Python 进行分析
python -c "import pandas as pd; df = pd.read_csv('stock.csv'); print(df.describe())"
```

### 自动化脚本示例

```bash
#!/bin/bash
# daily_report.sh - 每日报告生成脚本

# 获取今日股票数据
efinance-cli stock realtime -o daily_stocks.csv

# 获取基金持仓
efinance-cli fund position 161725 -o fund_position.csv

# 获取龙虎榜数据
efinance-cli stock billboard -o daily_billboard.csv

echo "每日报告已生成于 $(date)"
```

## Skills（技能）

本项目包含 Claude Code 技能，用于常见任务：

### 根据名称筛选基金

根据基金名称关键词筛选基金并导出到 CSV：

```bash
# 筛选包含特定关键词的基金
/filter-fund-by-name 富国 易方达

# 筛选量化相关基金
/filter-fund-by-name 量化 多因子 多策略

# 筛选债券型基金
/filter-fund-by-name 债券
```

该技能会：
1. 从 efinance 获取所有基金代码
2. 根据关键词过滤（OR 逻辑，任意匹配）
3. 导出结果到 CSV 文件

**使用示例**：
```
用户: 帮我筛选出所有名字包含 "多策略" "多因子" "量化" 的基金代码
Claude: 执行 /filter-fund-by-name 多策略 多因子 量化，输出 CSV 文件
```

## 输出格式

所有命令都使用 Rich 库进行表格格式化输出，例如：

```
                              贵州茅台股票数据
┏━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━┳━━━━━━┳━━━━━━┳━━━━━━┓
┃ 股票 ┃ 股票代 ┃ 日期       ┃ 开盘 ┃ 收盘 ┃ 最高 ┃ 最低 ┃
┡━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━╇━━━━━━╇━━━━━━╇━━━━━━┩
│ 贵州 │ 600519 │ 2024-01-01 │ 1850 │ 1860 │ 1870 │ 1840 │
│ 贵州 │ 600519 │ 2024-01-02 │ 1860 │ 1855 │ 1865 │ 1850 │
└──────┴────────┴────────────┴──────┴──────┴──────┴──────┘
```

## AI Agent 高级用法

### 智能错误处理

AI Agent 可以自动处理常见错误：

```
场景：用户请求获取股票数据时网络超时

AI Agent 自动处理流程:
1. 检测到网络错误
2. 等待后重试（最多3次）
3. 如果仍失败，建议用户稍后再试
4. 提供替代方案（如使用缓存数据）
```

### 上下文感知推理

AI Agent 可以根据对话上下文智能推断：

```
用户: "帮我分析茅台"
AI Agent 推断:
- 上下文中曾提到股票代码 600519
- 默认获取日K线数据
- 默认显示最近30天

用户: "和五粮液比较一下"
AI Agent 推断:
- 需要获取 000858（五粮液）的数据
- 对比两只股票的涨跌幅、成交量等指标
```

### 多维度综合分析

AI Agent 可以整合多个维度进行深度分析：

```
用户: "全面分析贵州茅台的投资价值"

AI Agent 执行流程:
1. 获取基本信息 → 了解公司基本面
2. 获取历史K线 → 分析技术面走势
3. 获取资金流向 → 分析主力动向
4. 获取股东信息 → 了解股权结构
5. 获取龙虎榜 → 查看机构交易
6. 整合数据生成综合报告
```

### 自动化工作流

AI Agent 可以创建自动化脚本：

```bash
# 创建每日监控脚本
cat > daily_monitor.sh << 'EOF'
#!/bin/bash
# 每日股票监控脚本

echo "=== 每日股票监控报告 $(date) ==="

# 监控列表
stocks=("600519" "000858" "000568")

for stock in "${stocks[@]}"; do
    echo "正在获取 $stock 数据..."
    efinance-cli stock history $stock --limit 1
    echo ""
done

# 获取龙虎榜
echo "=== 今日龙虎榜 ==="
efinance-cli stock billboard --limit 10

echo "报告生成完成！"
EOF

chmod +x daily_monitor.sh
```

### 数据导出与可视化

AI Agent 可以导出数据并创建可视化：

```python
# AI Agent 自动生成的分析脚本
import pandas as pd
import matplotlib.pyplot as plt

# 1. 获取数据
# efinance-cli stock history 600519 -o stock.csv

# 2. 读取数据
df = pd.read_csv('stock.csv')

# 3. 计算指标
df['MA5'] = df['收盘'].rolling(5).mean()
df['MA20'] = df['收盘'].rolling(20).mean()

# 4. 可视化
plt.figure(figsize=(12, 6))
plt.plot(df['日期'], df['收盘'], label='收盘价')
plt.plot(df['日期'], df['MA5'], label='5日均线')
plt.plot(df['日期'], df['MA20'], label='20日均线')
plt.legend()
plt.title('贵州茅台股价走势')
plt.savefig('stock_analysis.png')
plt.show()
```

### 使用注意事项

#### 数据时效性
- ⚠️ 股票行情数据有延迟（通常15分钟）
- ⚠️ 基金净值每天更新一次（收盘后）
- ⚠️ 龙虎榜数据T+1公布

#### 数据量控制
- ✅ 使用 `--limit` 限制输出行数
- ✅ 使用 `--start` 和 `--end` 指定时间范围
- ✅ 导出CSV后分批处理大量数据

#### 网络依赖
- ⚠️ 所有数据获取需要网络连接
- ⚠️ API 可能有频率限制
- ✅ 建议使用CSV缓存避免重复请求

#### 数据准确性
- ⚠️ 数据仅供参考，不构成投资建议
- ⚠️ 建议交叉验证重要数据
- ✅ 投资决策前请咨询专业顾问

## 系统要求

- Python >= 3.8
- efinance >= 0.5.8
- typer >= 0.9.0
- rich >= 13.0.0
- pandas >= 1.3.0

## 相关项目

- [efinance](https://github.com/Micro-sheep/efinance) - 底层 Python 金融数据库
- [typer](https://typer.tiangolo.com/) - CLI 应用开发框架
- [rich](https://rich.readthedocs.io/) - Python 终端格式化库

## 开发

### 运行测试

```bash
python test_cli.py
```

### 代码格式化

```bash
make format
```

### 代码检查

```bash
make lint
```

### 构建发布包

```bash
make build
```

## 常见问题

### 1. 命令找不到

如果遇到 "command not found" 错误：

```bash
# 确认包已安装
pip install -e .

# 或直接使用 Python 模块
python -m efinance_cli.main --help
```

### 2. 导入错误

如果遇到导入错误：

```bash
# 安装依赖
pip install efinance typer rich pandas
```

### 3. 网络连接问题

数据获取需要网络连接，如果遇到网络错误：

- 检查网络连接
- 稍后重试
- 使用 `--limit` 减少数据量

### 4. 权限错误

如果遇到权限错误：

```bash
# 使用 --user 标志
pip install --user -e .
```

## 许可证

MIT License

## 贡献

欢迎提交 Issue 和 Pull Request！

## 免责声明

本项目仅供学习和研究使用，不得用于商业目的。在做出投资决策前，请务必进行独立研究。

## 更新日志

### v0.1.0 (2026-05-21)
- 初始版本发布
- 支持股票、基金、债券、期货数据获取
- CSV 导出功能
- Rich 表格格式化
- 完整的帮助系统

## 联系方式

- GitHub: https://github.com/PegasusWang/efinance-cli
- 问题反馈: https://github.com/PegasusWang/efinance-cli/issues

---

**⭐ 如果这个项目对你有帮助，请给一个 Star！**
