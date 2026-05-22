#!/usr/bin/env python3
"""
Simple test script for efinance-cli functionality
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

import efinance as ef
from efinance_cli.main import display_dataframe

print("=== 测试: 股票历史数据 ===")
try:
    df = ef.stock.get_quote_history('600519')
    print(f"✅ 成功获取股票数据: {len(df)} 行")
    display_dataframe(df.head(5), title="贵州茅台股票数据")
except Exception as e:
    print(f"❌ 错误: {e}")

print("\n=== 测试: 基金数据 ===")
try:
    df = ef.fund.get_quote_history('161725')
    print(f"✅ 成功获取基金数据: {len(df)} 行")
    display_dataframe(df.head(5), title="基金数据")
except Exception as e:
    print(f"❌ 错误: {e}")

print("\n=== 测试完成 ===")
