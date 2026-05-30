---
name: query-fund-purchase-limit
description: 查询基金限购信息，从雪球/蛋卷基金获取每日限购金额。支持批量查询多个基金代码的申购限制。
user-invocable: true
allowed-tools: Bash, Read
---

# 查询基金限购信息

从雪球/蛋卷基金获取基金的每日限购金额信息。

## 使用方式

```bash
/query-fund-purchase-limit 基金代码1 基金代码2 ...
```

## 功能说明

1. 调用雪球 API 获取基金申购限制信息
2. 返回每日限购金额（daily_limit）
3. 支持批量查询多个基金代码

## 执行步骤

### Python 实现代码

```python
import requests

def format_limit_number(limit):
    """格式化限购金额"""
    if limit >= 100000000:  # 1亿
        return f"{limit / 100000000:.0f}亿"
    elif limit >= 10000:  # 1万
        return f"{limit / 10000:.0f}万"
    else:
        return str(limit)

def get_purchase_limit(codes):
    """雪球查询基金是否限购，返回格式
    {'009101': {'daily_limit': ''}, '001338': {'daily_limit': ''}, '040046': {'daily_limit': '1000'}}
    """
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
    }

    fund_limit_dict = {}
    for code in codes:
        params = {
            'fd_code': code,
            'type': '022',
            'channel': '',
            'transaction_account_id': '',
        }
        try:
            response = requests.get(
                'https://danjuanfunds.com/djapi/fund/order/trade_info',
                params=params,
                headers=headers,
                timeout=10
            )
            data = response.json()
            limit = int(data['data']['daily_limit'])
            limit_str = format_limit_number(limit)
        except Exception as e:
            limit_str = ''

        fund_limit_dict[code] = {
            'daily_limit': limit_str,
        }

    return fund_limit_dict
```

### 执行脚本

```bash
python3 << 'EOF'
import requests
import sys

def format_limit_number(limit):
    if limit >= 100000000:
        return f"{limit / 100000000:.0f}亿"
    elif limit >= 10000:
        return f"{limit / 10000:.0f}万"
    else:
        return str(limit)

def get_purchase_limit(codes):
    headers = {
        'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X10_15_7) AppleWebKit/537.36',
    }
    
    fund_limit_dict = {}
    for code in codes:
        params = {
            'fd_code': code,
            'type': '022',
            'channel': '',
            'transaction_account_id': '',
        }
        try:
            response = requests.get(
                'https://danjuanfunds.com/djapi/fund/order/trade_info',
                params=params,
                headers=headers,
                timeout=10
            )
            data = response.json()
            limit = int(data['data']['daily_limit'])
            limit_str = format_limit_number(limit)
        except Exception as e:
            limit_str = ''
        
        fund_limit_dict[code] = {'daily_limit': limit_str}
    
    return fund_limit_dict

# 从命令行获取基金代码
codes = sys.argv[1:] if len(sys.argv) > 1 else []
if not codes:
    print("请提供基金代码，例如: query-fund-purchase-limit 009101 001338")
    sys.exit(1)

result = get_purchase_limit(codes)
for code, info in result.items():
    print(f"{code}: 每日限购 {info['daily_limit']}")
EOF
```

## 示例

```bash
# 查询单个基金限购
/query-fund-purchase-limit 009101

# 查询多个基金限购
/query-fund-purchase-limit 009101 001338 040046

# 批量查询纳斯达克基金限购
/query-fund-purchase-limit 513100 513300 159941
```

## 输出格式

返回字典格式：
```python
{
    '009101': {'daily_limit': ''},        # 不限购
    '001338': {'daily_limit': ''},        # 不限购
    '040046': {'daily_limit': '1000'},    # 每日限购1000元
    '513100': {'daily_limit': '1万'},     # 每日限购1万元
}
```

## 注意事项

- 需要安装 requests 库：`pip install requests`
- API 来源：雪球/蛋卷基金
- 空字符串表示不限购
- 限购金额已格式化（万/亿）
- 网络请求可能有延迟，建议批量查询时控制数量