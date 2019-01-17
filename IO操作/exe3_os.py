#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'derek'

import os
print(os.name)
# nt windows 操作系统
# 要获取详细的系统信息，可以调用uname()函数：
# print(os.uname())
# 环境变量
print(os.environ)
# 要获取某个环境变量的值，可以调用os.environ.get('key')：
print(os.environ.get('PATH'))
# 可以传入容错参数
print(os.environ.get('ooo','fengyoujing'))
# 操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，这一点要注意一下。查看、创建和删除目录可以这么调用：
# 查看当前的文件的绝对路劲
print(os.path.abspath('.'))
# 在某一个目录下面创建一个新目录，首先把新目录的完整路径表示出来
# os.path.join('C:/Users/admin/Desktop','python')
# 然后开始创建目录
# os.mkdir('C:/Users/admin/Desktop/python')
# 删除目录功能
# os.rmdir('C:/Users/admin/Desktop/python')

# 要拆分路径时，不需要直接拆分字符串，os.path.split()
# os.path.split('C:/Users/admin/Desktop/ads.txt')
# print(os.path.split('C:/Users/admin/Desktop/ads.txt'))
# ('C:/Users/admin/Desktop', 'ads.txt')
# os.path.splitext() 直接获得文件的扩展名
# print(os.path.splitext('C:/Users/admin/Desktop/ads.txt'))
# ('C:/Users/admin/Desktop/ads', '.txt')
# 对文件重命名:
# os.rename('C:/Users/admin/Desktop/ads.txt', 'C:/Users/admin/Desktop/ads.py')
# 删掉文件:
# os.remove('C:/Users/admin/Desktop/ads.py')

# 列出当前目录下面的所有目录
print([x for x in os.listdir('.') if os.path.isdir(x)])
# 列出当前文件夹下面的所有.py文件
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])

# shutil模块提供了copyfile()的函数
print(type({}))
d = dict()
l = list()
t = tuple()
print(type(l))
print(type(d))
print(type(t))
print(type([]))
print(type(()))
