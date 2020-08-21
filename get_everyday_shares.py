#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 
@author: yzyfdf 
@title: 每天收盘后数据
@file: get_everyday_shares.py
@time: 2018/1/20 09:50 
"""

import time
import math
import json

import datautil
import save2db

totalShares = 4469

if __name__ == '__main__':

	print("开始")
	start = int(time.time())

	for page in range(1, math.ceil(totalShares / 50) + 1):
		# 获取列表
		shares_list = json.loads(datautil.get_shares_list(page))["data"]["list"]

		# 遍历
		for shares in shares_list:
			# 去掉没用的
			symbol: str = shares["symbol"]
			if symbol.startswith("SH171"):
				continue

			# 获取详情
			sharesDetail: dict = json.loads(datautil.get_shares_detail(symbol))
			if sharesDetail['error_code'] != 0:
				print(sharesDetail['error_description'])

			# 写入
			data = sharesDetail.get("data")
			if data is not None:
				try:
					save2db.save(data["quote"])
				except:
					continue

			time.sleep(0.4)

	print("耗时%d秒" % (int(time.time()) - start))
