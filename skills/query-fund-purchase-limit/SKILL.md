---
name: query-fund-purchase-limit
description: 查询基金限购信息，使用 akshare 获取基金申购状态、限购金额等购买信息。支持批量查询多个基金代码。
user-invocable: true
allowed-tools: Bash, Read
---

# 查询基金限购信息

使用 akshare 获取基金的申购状态、限购金额等购买信息。

## 使用方式

```bash
/query-fund-purchase-limit 基金代码1 基金代码2 ...
```

## 功能说明

1. 调用 akshare 获取基金购买信息
2. 返回申购状态、限购金额、暂停申购等信息
3. 支持批量查询多个基金代码

## 执行步骤

### Python 实现代码

```python
import akshare as ak

def get_fund_purchase_info(fund_codes: list[str]) -> list[dict]:
    """获取指定基金代码列表的购买信息

    Args:
        fund_codes: 基金代码列表，如 ['010923', '000001']

    Returns:
        list[dict]: 每个基金的购买信息字典列表，如果未找到则为空字典
    """
    # 获取全部基金购买信息
    fund_purchase_em_df = ak.fund_purchase_em()
    
    result = []
    for code in fund_codes:
        filtered_df = fund_purchase_em_df[fund_purchase_em_df['基金代码'] == code]
        if not filtered_df.empty:
            result.append(filtered_df.iloc[0].to_dict())
        else:
            result.append({})
    
    return result
```

### 执行脚本

```bash
python3 << 'EOF'
import sys

# 检查 akshare 是否安装
try:
    import akshare as ak
except ImportError:
    print("请先安装 akshare: pip install akshare")
    sys.exit(1)

def get_fund_purchase_info(fund_codes: list[str]) -> list[dict]:
    """获取指定基金代码列表的购买信息"""
    fund_purchase_em_df = ak.fund_purchase_em()
    
    result = []
    for code in fund_codes:
        filtered_df = fund_purchase_em_df[fund_purchase_em_df['基金代码'] == code]
        if not filtered_df.empty:
            result.append(filtered_df.iloc[0].to_dict())
        else:
            result.append({})
    
    return result

# 从命令行获取基金代码
codes = sys.argv[1:] if len(sys.argv) > 1 else []
if not codes:
    print("请提供基金代码，例如: /query-fund-purchase-limit 009101 001338")
    sys.exit(1)

print(f"正在查询 {len(codes)} 个基金的购买信息...")
results = get_fund_purchase_info(codes)

for i, info in enumerate(results):
    code = codes[i]
    if info:
        print(f"\n{code}: {info.get('基金简称', 'N/A')}")
        print(f"  申购状态: {info.get('申购状态', 'N/A')}")
        print(f"  限购金额: {info.get('限制申购金额', 'N/A')}")
        print(f"  暂停申购: {info.get('暂停申购', 'N/A')}")
    else:
        print(f"\n{code}: 未找到购买信息")
EOF
```

## 示例

```bash
# 查询单个基金限购
/query-fund-purchase-limit 009101

# 查询多个基金限购
/query-fund-purchase-limit 009101 001338 040046

# 批量查询纳斯达克基金限购
/query-fund-purchase-limit 513100 513300 159941 270042

# 结合筛选基金使用
# 先筛选纳斯达克基金，再查询限购
```

## 输出格式

返回字典列表，每个字典包含：

```python
[
    {
        '基金代码': '009101',
        '基金简称': '...',
        '申购状态': '开放申购',      # 或 '暂停申购'
        '限制申购金额': '1000',      # 每日限购金额
        '暂停申购': '...',           # 暂停申购说明
        '最小申购金额': '1',         # 最小申购金额
        # 其他字段...
    },
    {...}
]
```

## 数据字段说明

| 字段 | 说明 |
|------|------|
| 基金代码 | 6位基金代码 |
| 基金简称 | 基金名称 |
| 申购状态 | 开放申购/暂停申购 |
| 限制申购金额 | 每日限购金额限制 |
| 暂停申购 | 暂停申购的具体说明 |
| 最小申购金额 | 单笔最小申购金额 |

## 注意事项

- 需要安装 akshare 库：`pip install akshare`
- 数据来源：东方财富网
- 空字典表示未找到该基金的购买信息
- 批量查询时会获取全部基金购买信息后再过滤，效率较高
- ETF 场内基金通常不在此数据中显示（场内交易无申购限制）


# 使用示例
- 提示词：帮我查一下 纳斯达克基金的代码和限购金额信息，导出到一个表格 csv 里
- 提示词：筛选出所有标普500 的基金和限购金额信息，导出 csv 文件
- 提示词：筛选出所有 QDII 基金和限购金额信息，导出 csv 文件
