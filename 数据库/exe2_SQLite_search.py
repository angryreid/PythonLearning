#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'derek'

import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

cursor.execute('select * from user where id=?', ('1',))

# 获取查询结果
values = cursor.fetchall()
print(values)

cursor.close()
conn.close()
