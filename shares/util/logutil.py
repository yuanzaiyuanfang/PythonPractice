#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 
@author: yzyfdf 
@title: log
@file: Logutil.py
@time: 2018/1/20 09:50 
"""
import os
import logging


class logs(object):

	def __init__(self):
		self.logger = logging.getLogger()

		# Define a Handler and set a format which output to file
		format = '%(asctime)s  %(filename)s : %(levelname)s  %(message)s'
		logging.basicConfig(
			level=logging.DEBUG,  # 定义输出到文件的log级别，大于此级别的都被输出
			format=format,  # 定义输出log的格式
			datefmt='%Y-%m-%d %H:%M:%S',  # 时间
			filename=os.path.join(os.path.dirname(__file__), 'logging.log'),  # log文件名
			filemode='a')  # 写入模式“w”或“a”

		# Define a Handler and set a format which output to console
		console = logging.StreamHandler()  # 定义console handler
		console.setLevel(logging.INFO)  # 定义该handler级别
		console.setFormatter(logging.Formatter(format))  # 定义该handler格式
		# Create an instance
		self.logger.addHandler(console)  # 实例化添加handler

	def info(self, message):
		self.logger.info(message)

	def debug(self, message):
		self.logger.debug(message)

	def warning(self, message):
		self.logger.warning(message)

	def error(self, message):
		self.logger.error(message)
