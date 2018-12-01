#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 18-11-4 下午2:14
# @Author  : KainHuck
# @Email   : kainhoo2333@gmail.com
# @File    : models.py

from ORM.orm import ORM

# 写你自己的class继承自ORM,类名与数据库中的表名相同
# 表的表头为参数,
class users(ORM):
	def __init__(self, username, password):
		self.username = username
		self.password = password
