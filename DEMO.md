# efinance-cli 演示

## 安装成功 ✅

```bash
$ pip install -e .
Successfully installed efinance-cli-0.1.0
```

## 基本功能测试

### 1. 查看帮助

```bash
$ efinance-cli --help
                                                                                
 Usage: efinance-cli [OPTIONS] COMMAND [ARGS]...                                
                                                                                
 CLI tool for efinance - Get stock, fund, bond and futures data from command    
 line                                                                           
                                                                                
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --install-completion          Install completion for the current shell.      │
│ --show-completion             Show completion for the current shell, to copy │
│                               it or customize the installation.              │
│ --help                        Show this message and exit.                    │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ───────────────────────────────────────────────────────────────────╮
│ version  Show version information                                            │
│ stock    Stock related commands                                              │
│ fund     Fund related commands                                               │
│ bond     Bond related commands                                               │
│ futures  Futures related commands                                            │
╰──────────────────────────────────────────────────────────────────────────────╯
```

### 2. 查看版本

```bash
$ efinance-cli version
efinance-cli version: 0.1.0
efinance version: unknown
```

### 3. 查看股票命令帮助

```bash
$ efinance-cli stock --help
                                                                                
 Usage: efinance-cli stock [OPTIONS] COMMAND [ARGS]...                          
                                                                                
 Stock related commands                                                         
                                                                                
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                                  │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ───────────────────────────────────────────────────────────────────╮
│ history      Get stock K-line history data                                   │
│ realtime     Get real-time quotes for all A-shares                           │
│ billboard    Get daily billboard (龙虎榜) data                               │
│ performance  Get quarterly performance of all companies                      │
│ base-info    Get basic information for stocks                                │
│ holder       Get top 10 stock holders information                            │
╰──────────────────────────────────────────────────────────────────────────────╯
```

## 可用命令

### 股票命令
- `efinance-cli stock history <股票代码>` - 获取股票历史K线数据
- `efinance-cli stock realtime` - 获取实时行情
- `efinance-cli stock billboard` - 获取龙虎榜数据
- `efinance-cli stock performance` - 获取公司业绩
- `efinance-cli stock base-info <股票代码>` - 获取基本信息
- `efinance-cli stock holder <股票代码>` - 获取前10大股东

### 基金命令
- `efinance-cli fund history <基金代码>` - 获取基金净值历史
- `efinance-cli fund position <基金代码>` - 获取基金持仓
- `efinance-cli fund base-info <基金代码>` - 获取基本信息
- `efinance-cli fund manager <基金代码>` - 获取基金经理信息
- `efinance-cli fund codes` - 获取所有基金代码

### 债券命令
- `efinance-cli bond realtime` - 获取实时行情
- `efinance-cli bond history <债券代码>` - 获取历史数据
- `efinance-cli bond all-info` - 获取所有可转债信息

### 期货命令
- `efinance-cli futures info` - 获取基本信息
- `efinance-cli futures realtime` - 获取实时行情
- `efinance-cli futures history <行情ID>` - 获取历史数据

## 使用示例

### 示例 1: 获取贵州茅台股票数据

```bash
$ efinance-cli stock history 600519 --limit 10
# 显示最近10天的K线数据
```

### 示例 2: 获取基金持仓

```bash
$ efinance-cli fund position 161725
# 显示招商中证白酒指数基金的持仓信息
```

### 示例 3: 导出数据到CSV

```bash
$ efinance-cli stock history 600519 -o moutai.csv
# 将数据保存到 moutai.csv 文件
```

### 示例 4: 获取5分钟K线

```bash
$ efinance-cli stock history 600519 --klt 5 --limit 20
# 显示最近20个5分钟K线数据
```

## 与 AI Code Agent 集成

### Claude Code CLI 示例

用户可以这样向 Claude 提问:

```
"使用 efinance-cli 获取贵州茅台(600519)最近30天的K线数据,并保存到CSV文件"
```

Claude 将执行:

```bash
efinance-cli stock history 600519 --limit 30 -o moutai_30days.csv
```

### Cursor/Copilot 示例

```
"获取当前所有A股的实时行情,并找出涨幅前10的股票"
```

执行步骤:

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

## 项目特点

1. **易于使用**: 简单的命令行接口
2. **丰富的功能**: 支持股票、基金、债券、期货
3. **美观的输出**: 使用 Rich 库进行格式化
4. **数据导出**: 支持 CSV 格式导出
5. **完善的文档**: 详细的帮助信息和文档
6. **AI 友好**: 专为 AI Code Agent 优化

## 技术栈

- **Python 3.8+**
- **Typer**: 现代 CLI 框架
- **Rich**: 终端格式化库
- **Pandas**: 数据处理
- **efinance**: 数据源

## 下一步

1. 发布到 PyPI
2. 添加更多数据源支持
3. 实现数据缓存
4. 添加数据可视化功能
5. 支持配置文件

## 许可证

MIT License

## 反馈与贡献

欢迎提交 Issue 和 Pull Request!
