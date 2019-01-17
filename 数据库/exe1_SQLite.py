#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'derek'
import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute('create table user (id varchar(20) primary key,name varchar(20))')
cursor.execute('insert into user (id,name) values (\'1\',\'ooohen\')')
print(cursor.rowcount)
# 关闭cursor
cursor.close()
# 提交事务
conn.commit()
# 关闭连接
conn.close()