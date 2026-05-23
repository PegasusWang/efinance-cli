---
name: filter-fund-by-name
description: 根据基金名称关键词筛选基金，支持多个关键词，输出 CSV 文件。使用 efinance-cli 获取所有基金列表并过滤匹配的基金代码。
user-invocable: true
allowed-tools: Bash(efinance-cli fund:*), Read
---

# 根据名称筛选基金

根据用户提供的基金名称关键词，从所有基金中筛选出匹配的基金，输出 CSV 文件到当前目录。

## 使用方式

```bash
/filter-fund-by-name 关键词1 关键词2 ...
```

## 功能说明

1. 调用 `efinance-cli fund codes` 获取所有基金代码和名称
2. 根据用户提供的多个关键词进行筛选（OR 逻辑，任意一个关键词匹配即可）
3. 输出 CSV 文件到当前目录，文件名格式：`filtered_funds_YYYYMMDD_HHMMSS.csv`

## 执行步骤

### 1. 获取所有基金代码

```bash
efinance-cli fund codes -o /tmp/all_funds.csv
```

### 2. 根据关键词过滤

使用 pandas 或 grep 过滤包含关键词的基金：

```python
import pandas as pd
import sys
from datetime import datetime

# 读取基金列表
df = pd.read_csv('/tmp/all_funds.csv')

# 获取关键词
keywords = sys.argv[1:]  # 从命令行获取关键词

# 过滤（OR 逻辑）
if keywords:
    pattern = '|'.join(keywords)
    filtered = df[df['基金简称'].str.contains(pattern, na=False, case=False)]
else:
    filtered = df

# 输出到 CSV
output_file = f"filtered_funds_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
filtered.to_csv(output_file, index=False, encoding='utf-8-sig')
print(f"已保存到 {output_file}，共 {len(filtered)} 条记录")
```

### 3. 输出结果

CSV 文件包含以下字段：
- 基金代码
- 基金简称
- 其他 efinance-cli 返回的字段

## 示例

```bash
# 筛选包含"富国"或"易方达"的基金
/filter-fund-by-name 富国 易方达

# 筛选债券型基金
/filter-fund-by-name 债券

# 筛选沪深300相关基金
/filter-fund-by-name 沪深300
```

## 注意事项

- 关键词匹配不区分大小写
- 多个关键词之间是 OR 关系（任意匹配）
- 基金列表数据来自 efinance-cli，可能不是最新的
- 输出文件使用 UTF-8-BOM 编码，Excel 可正确打开
