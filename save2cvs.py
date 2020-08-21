#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 
@author: yzyfdf 
@title:'todo'
@file: save2cvs.py
@time: 2018/1/20 09:50 
"""

from datetime import datetime
import csv

date = datetime.now().strftime('%Y%m%d')


def save_shares(bean: dict):
	if bean["symbol"].startswith("SH688"):
		# 科创板格式不一样单独保存一个
		with open('%s%skcb.csv' % (dir, date), 'a', newline='') as file:
			global first_kcb
			b = save(bean, file, first_kcb)
			first_kcb = b
	else:
		with open('%s%sa.csv' % (dir, date), 'a', newline='') as file:
			global first_a
			b2 = save(bean, file, first_a)
			first_a = b2


def save(bean, file, first):
	writer = csv.writer(file)
	if first:
		writer.writerow(bean)

	values = bean.values()
	for value in values:
		if isinstance(value, int) | isinstance(value, float):
			value = str(value) + " \t"
	writer.writerow(values)
	return False
