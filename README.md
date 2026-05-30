# efinance-cli

[English](README.md) | [中文文档](https://github.com/PegasusWang/efinance-cli/blob/master/README_CN.md)

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg?style=flat)](https://pypi.python.org/pypi/efinance-cli)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Command line interface for [efinance](https://github.com/Micro-sheep/efinance) - Get stock, fund, bond and futures data from command line.

Designed for AI code agents (Claude Code CLI, Cursor, Copilot CLI, etc.) and terminal users.

## Installation

### From PyPI (Recommended)

```bash
pip install efinance-cli
```

### From Source

```bash
git clone https://github.com/PegasusWang/efinance-cli
cd efinance-cli
pip install -e .
```

### Install Skills (for Claude Code)

Install skills to Claude Code skills directory:

```bash
# Using uvx (recommended)
uvx --from github:PegasusWang/efinance-cli install-skills

# Using pipx
pipx run --from github:PegasusWang/efinance-cli install-skills
```

Available skills:
- `filter-fund-by-name` - Filter funds by keywords and export to CSV
- `query-fund-purchase-limit` - Query fund purchase limits from Xueqiu

## Quick Start

After installation, you can use `efinance-cli` command:

```bash
# Show version
efinance-cli version

# Get help
efinance-cli --help
```

## Usage

### Stock Commands

```bash
# Get stock K-line history
efinance-cli stock history 600519

# Get stock history with date range
efinance-cli stock history 600519 --start 2024-01-01 --end 2024-12-31

# Get 5-minute K-line data
efinance-cli stock history 600519 --klt 5

# Save to CSV file
efinance-cli stock history 600519 -o stock_data.csv

# Get real-time quotes for all A-shares
efinance-cli stock realtime

# Get daily billboard (龙虎榜)
efinance-cli stock billboard

# Get billboard for date range
efinance-cli stock billboard --start 2024-01-01 --end 2024-01-31

# Get company quarterly performance
efinance-cli stock performance

# Get stock basic information
efinance-cli stock base-info 600519 000001

# Get top 10 stock holders
efinance-cli stock holder 600519
```

### Fund Commands

```bash
# Get fund net value history
efinance-cli fund history 161725

# Save to CSV
efinance-cli fund history 161725 -o fund_data.csv

# Get fund investment position
efinance-cli fund position 161725

# Get fund basic information
efinance-cli fund base-info 161725 005827

# Get fund manager information
efinance-cli fund manager 161725

# Get all fund codes
efinance-cli fund codes
```

### Bond Commands

```bash
# Get real-time quotes for convertible bonds
efinance-cli bond realtime

# Get bond K-line history
efinance-cli bond history 123111

# Get all convertible bonds information
efinance-cli bond all-info

# Save to CSV
efinance-cli bond realtime -o bonds.csv
```

### Futures Commands

```bash
# Get futures basic information
efinance-cli futures info

# Get real-time futures quotes
efinance-cli futures realtime

# Get futures K-line history
efinance-cli futures history 115.ZCM

# Get multiple futures history
efinance-cli futures history 115.ZCM 115.ZC109

# Save to CSV
efinance-cli futures history 115.ZCM -o futures_data.csv
```

## Command Reference

### Global Options

- `--help`: Show help message
- `--version`: Show version

### Stock Commands

| Command | Description |
|---------|-------------|
| `history` | Get stock K-line history data |
| `realtime` | Get real-time quotes for all A-shares |
| `billboard` | Get daily billboard (龙虎榜) data |
| `performance` | Get quarterly performance of companies |
| `base-info` | Get basic information for stocks |
| `holder` | Get top 10 stock holders information |

### Fund Commands

| Command | Description |
|---------|-------------|
| `history` | Get fund net value history |
| `position` | Get fund investment position |
| `base-info` | Get basic information for funds |
| `manager` | Get fund manager information |
| `codes` | Get all fund codes |

### Bond Commands

| Command | Description |
|---------|-------------|
| `realtime` | Get real-time quotes for convertible bonds |
| `history` | Get bond K-line history data |
| `all-info` | Get all convertible bonds information |

### Futures Commands

| Command | Description |
|---------|-------------|
| `info` | Get futures basic information |
| `realtime` | Get real-time futures quotes |
| `history` | Get futures K-line history data |

## Options

### Common Options

- `--output, -o`: Output file path (CSV format)
- `--limit, -l`: Maximum number of rows to display (default: 50)

### Stock History Options

- `--start, -s`: Start date (YYYY-MM-DD)
- `--end, -e`: End date (YYYY-MM-DD)
- `--klt, -k`: K-line type
  - `101`: Day K-line (default)
  - `102`: Week K-line
  - `103`: Month K-line
  - `5`: 5-minute K-line
  - `15`: 15-minute K-line
  - `30`: 30-minute K-line
  - `60`: 60-minute K-line
- `--fqt, -f`: Adjustment type
  - `0`: No adjustment
  - `1`: Forward adjustment (default)
  - `2`: Backward adjustment

## For AI Code Agents

This CLI tool is designed to work well with AI code agents:

1. **Structured Output**: Data is displayed in formatted tables using `rich` library
2. **Error Handling**: Clear error messages with exit codes
3. **CSV Export**: All data can be exported to CSV for further processing
4. **Comprehensive Help**: Built-in help for all commands

Example usage with Claude Code CLI:

```bash
# Ask Claude to get stock data
"Use efinance-cli to get the last 30 days of K-line data for 贵州茅台 (600519) and save it to a CSV file"

# Claude will execute:
efinance-cli stock history 600519 -o moutai_30days.csv --limit 30
```

## Skills

This project includes Claude Code skills for common tasks:

### Filter Fund by Name

Filter funds by name keywords and export to CSV:

```bash
# Filter funds containing specific keywords
/filter-fund-by-name 富国 易方达

# Filter quantitative funds
/filter-fund-by-name 量化 多因子 多策略

# Filter bond funds
/filter-fund-by-name 债券
```

The skill will:
1. Fetch all fund codes from efinance
2. Filter by keywords (OR logic)
3. Export results to CSV file

## Examples

### Example 1: Get stock data and analyze

```bash
# Get recent stock data
efinance-cli stock history 600519 -o stock.csv --limit 100

# Then use Python to analyze
python -c "import pandas as pd; df = pd.read_csv('stock.csv'); print(df.describe())"
```

### Example 2: Monitor real-time market

```bash
# Get real-time quotes
efinance-cli stock realtime -o realtime.csv

# Filter with Python
python -c "import pandas as pd; df = pd.read_csv('realtime.csv'); print(df[df['涨跌幅'] > 5])"
```

### Example 3: Track fund performance

```bash
# Get fund history
efinance-cli fund history 161725 -o fund.csv

# Get fund position
efinance-cli fund position 161725
```

## Requirements

- Python >= 3.8
- efinance >= 0.5.8
- typer >= 0.9.0
- rich >= 13.0.0
- pandas >= 1.3.0

## Related Projects

- [efinance](https://github.com/Micro-sheep/efinance) - The underlying Python library for finance data
- [typer](https://typer.tiangolo.com/) - Library for building CLI applications
- [rich](https://rich.readthedocs.io/) - Python library for rich text and beautiful formatting

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Disclaimer

This project is for educational and research purposes only. It should not be used for commercial purposes. Always do your own research before making investment decisions.

## Changelog

### v0.1.0 (2026-05-21)
- Initial release
- Support for stock, fund, bond, and futures data
- CSV export functionality
- Rich table formatting
