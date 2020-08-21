#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 
@author: yzyfdf 
@title:'todo'
@file: datautil.py
@time: 2018/1/20 09:50 
"""
import requests
from requests import adapters
import time

headers = {"Cookie": "xq_a_token=4db837b914fc72624d814986f5b37e2a3d9e9944",
		   "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0"}

# 股票列表
def get_shares_list(page):
	params = {"category": 'CN', "exchange": 'sh_sz', "order_by": 'symbol', "order": 'asc', "page": page,
			  "size": 50, "only_count": 0, "_": int(time.time() * 1000)}
	return requests.get(url="https://xueqiu.com/service/screener/screen", params=params, headers=headers).text

# 股票详情
def get_shares_detail(symbol):
	params = {"symbol": symbol, "extend": 'detail', "_": int(time.time() * 1000)}
	# 设置重连次数
	requests.adapters.DEFAULT_RETRIES = 10
	s = requests.session()
	# 设置连接活跃状态为False
	s.keep_alive = False
	return requests.get("https://stock.xueqiu.com/v5/stock/quote.json", params=params, headers=headers).text
