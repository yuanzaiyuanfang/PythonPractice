#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 
@author: yzyfdf 
@title: 保存到mysql
@file: save2db.py
@time: 2018/1/20 09:50 
"""
import pymysql
import environment


def save(bean: dict):
	connect = pymysql.connect(**environment.serviceConfig)

	try:
		with connect.cursor() as cursor:
			ss = """
			insert into sharesdata (timestamp ,symbol,name, current, chg, percent, high, low, open, last_close, limit_up, limit_down,volume,amount) 
			values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s); 
				"""
			execute = cursor.execute(ss, [
				bean['timestamp'],
				bean['symbol'],
				bean['name'],
				bean['current'],
				bean['chg'],
				bean['percent'],
				bean['high'],
				bean['low'],
				bean['open'],
				bean['last_close'],
				bean['limit_up'],
				bean['limit_down'],
				bean['volume'],
				bean['amount'],
			])
			connect.commit()

	finally:
		connect.close()
