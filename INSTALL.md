# Installation and Usage Guide

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Installation Steps

### Option 1: Install from Source (Recommended for Development)

1. Clone the repository:
```bash
git clone https://github.com/PegasusWang/efinance-cli
cd efinance-cli
```

2. Install in development mode:
```bash
pip install -e .
```

3. Verify installation:
```bash
efinance-cli --help
efinance-cli version
```

### Option 2: Build and Install Package

1. Build the package:
```bash
pip install build
python -m build
```

2. Install the built package:
```bash
pip install dist/efinance_cli-0.1.0-py3-none-any.whl
```

## Testing the Installation

Run the test script to verify all functionality:

```bash
python test_cli.py
```

## Common Issues and Solutions

### Issue 1: Command not found

If you get "command not found" error:

```bash
# Make sure the package is installed
pip install -e .

# Or use Python module directly
python -m efinance_cli.main --help
```

### Issue 2: Import errors

If you get import errors:

```bash
# Install dependencies
pip install efinance typer rich pandas
```

### Issue 3: Permission errors

If you get permission errors:

```bash
# Use --user flag
pip install --user -e .
```

## Usage Examples

### Basic Usage

```bash
# Get help for main command
efinance-cli --help

# Get help for a subcommand
efinance-cli stock --help

# Get help for a specific command
efinance-cli stock history --help
```

### Stock Examples

```bash
# Get贵州茅台 (600519) stock history
efinance-cli stock history 600519

# Get 5-minute K-line data
efinance-cli stock history 600519 --klt 5 --limit 20

# Get stock data for a date range
efinance-cli stock history 600519 --start 2024-01-01 --end 2024-12-31

# Save stock data to CSV
efinance-cli stock history 600519 -o moutai.csv

# Get real-time quotes (first 20 stocks)
efinance-cli stock realtime --limit 20

# Get today's billboard (龙虎榜)
efinance-cli stock billboard

# Get company performance data
efinance-cli stock performance --limit 30

# Get top 10 holders for a stock
efinance-cli stock holder 600519
```

### Fund Examples

```bash
# Get fund history (招商中证白酒指数)
efinance-cli fund history 161725

# Get fund position
efinance-cli fund position 161725

# Get fund manager info
efinance-cli fund manager 161725

# Get multiple funds info
efinance-cli fund base-info 161725 005827
```

### Bond Examples

```bash
# Get real-time convertible bonds quotes
efinance-cli bond realtime --limit 20

# Get specific bond history
efinance-cli bond history 123111

# Get all convertible bonds info
efinance-cli bond all-info --limit 20
```

### Futures Examples

```bash
# Get futures basic info
efinance-cli futures info --limit 20

# Get futures real-time quotes
efinance-cli futures realtime --limit 20

# Get futures history (动力煤主力)
efinance-cli futures history 115.ZCM
```

## Integration with AI Code Agents

### Claude Code CLI

Example prompts for Claude:

```
"Get the last month of stock data for 贵州茅台 (600519) and save it to a CSV file"

"Show me the current top gainers in the stock market"

"Get the fund position for 招商中证白酒指数 (161725)"
```

Claude will execute the appropriate efinance-cli commands.

### Programmatic Usage

You can also use the library programmatically in Python:

```python
from efinance_cli.main import app
from typer.testing import CliRunner

runner = CliRunner()

# Get stock history
result = runner.invoke(app, ["stock", "history", "600519"])
print(result.stdout)

# Get fund position
result = runner.invoke(app, ["fund", "position", "161725"])
print(result.stdout)
```

## Output Formatting

All commands display data in formatted tables. You can:

- Use `--limit` to control the number of rows displayed
- Use `--output` to save data to CSV files
- Use `--help` on any command to see available options

## Data Export

Export data to CSV for further analysis:

```bash
# Export stock data
efinance-cli stock history 600519 -o stock_data.csv

# Export fund data
efinance-cli fund history 161725 -o fund_data.csv

# Export bond data
efinance-cli bond realtime -o bond_data.csv
```

Then analyze in Python:

```python
import pandas as pd

# Load the exported data
df = pd.read_csv('stock_data.csv')

# Analyze
print(df.head())
print(df.describe())
print(df.info())
```

## Advanced Usage

### Combining with Unix Tools

```bash
# Get stock data and filter with grep
efinance-cli stock realtime | grep "涨幅"

# Save and analyze
efinance-cli stock history 600519 -o temp.csv && python analyze.py temp.csv
```

### Automation Scripts

Create automation scripts:

```bash
#!/bin/bash
# daily_report.sh

# Get today's stock data
efinance-cli stock realtime -o daily_stocks.csv

# Get fund positions
efinance-cli fund position 161725 -o fund_position.csv

# Get billboard data
efinance-cli stock billboard -o daily_billboard.csv

echo "Daily report generated at $(date)"
```

## Tips for AI Code Agents

1. **Use --limit for large datasets**: Prevents overwhelming output
2. **Use --output for data persistence**: Saves data for later analysis
3. **Check --help first**: Understand available options
4. **Combine commands**: Use multiple commands for comprehensive analysis
5. **Handle errors**: Check exit codes and error messages

## Performance Considerations

- Use `--limit` to limit output size
- For large datasets, export to CSV instead of displaying
- Real-time data commands may take longer due to network latency
- Consider caching strategies for frequently accessed data

## Security and Privacy

- No authentication required (uses public data)
- No sensitive data is stored locally
- All data is fetched from public sources via efinance library
- Respect rate limits and terms of service of data providers
