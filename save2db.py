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


def save(bean: dict, others: dict):
	connect = pymysql.connect(**environment.serviceConfig)

	try:
		with connect.cursor() as cursor:
			try:
				save_list(cursor, bean)
				save_detail(cursor, bean, others)
			except Exception as e:
				print(repr(e))
				connect.rollback()
			else:
				connect.commit()

	finally:
		connect.close()


def save_list(cursor, bean):
	ss = """
			insert into sharesdata (timestamp ,symbol,name, current, chg, percent, high, low, open, last_close, limit_up, limit_down,volume,amount) 
			values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s); 
				"""
	cursor.execute(ss, [
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


def save_detail(cursor, bean, others: dict):

	ss = """
	replace into sharedetail (symbol, name, current, chg, percent, high, low, open, last_close, limit_up, limit_down, volume,
                         amount, volume_ratio, pankou_ratio, turnover_rate, amplitude, pe_forecast, pe_lyr, pe_ttm, pb,
                         eps, navps, dividend, dividend_yield, total_shares, float_shares, market_capital,
                         float_market_capital, high52w, low52w, currency, goodwill_in_net_assets, no_profit_desc,
                         is_registration_desc, is_vie_desc, weighted_voting_rights_desc)
values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
	"""

	cursor.execute(ss, [
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
		bean['volume_ratio'],
		others['pankou_ratio'] if (others is not None and "pankou_ratio" in others) else None,
		bean['turnover_rate'],
		bean['amplitude'],
		bean['pe_forecast'],
		bean['pe_lyr'],
		bean['pe_ttm'],
		bean['pb'],
		bean['eps'],
		bean['navps'],
		bean['dividend'],
		bean['dividend_yield'],
		bean['total_shares'],
		bean['float_shares'],
		bean['market_capital'],
		bean['float_market_capital'],
		bean['high52w'],
		bean['low52w'],
		bean['currency'],
		bean['goodwill_in_net_assets'],
		bean['no_profit_desc'],
		bean['is_registration_desc'],
		bean['is_vie_desc'],
		bean['weighted_voting_rights_desc'],
	])
