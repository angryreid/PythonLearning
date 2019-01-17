#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'derek'
# 正则表达式
#   匹配
# *     任意个字符，包括0
# +     至少一个字符
# ？     0,1个字符
# {n}   表示匹配n个字符
# {n,m} 表示匹配n-m个字符

# 案例解析
# \d{3}\s+\d{3,8}

# \d{3} 匹配三个数字
# \s 匹配一个字符 \s+ 至少一个空格
# \d{3,8}   表示3-8个字符

# 符号前面使用下划线进行转义
# \- 匹配-号

#  [] 表示范围
# [0-9a-zA-Z\_] 可以匹配一个数字，字母，下划线
# [0-9a-zA-Z\_]+ 至少一个由字母，数字，下划线生成的字符串
# [a-zA-Z\_][0-9a-zA-Z\_]* 可以匹配由字母，下划线开头，后接着任意一个由数字，字母，下划线组成的字符串

# A|B 可以匹配A或者B  (P|p)ython
# ^  表示以什么开头 ^\d 以数字开头
#  $ 表示以什么结束 \d$ 以数字结束

import re
reg = re.match(r'^\d{3}\-\d{3,8}$','001-123456')
reg2 = re.match(r'^\d{3}\-\d{3,8}$','001 123456')
print(reg)
print(reg2)

str = 'a b   c'
print(str.split(' '))
# print(re.split(r'\s+',str)) 使用re模块自带的字符串分割
print(re.split(r'\s+',str))

str2 = 'a,b   c  ,d;t;uiu,wee'
print(re.split(r'[\s\,\;]+',str2))

# 除了判断是否匹配成功之外，可以直接从匹配的字符串，提取子串的功能
# () 表示提取的分组
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m)
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))
# 正则匹配默认是贪婪匹配
#

