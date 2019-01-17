#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'derek'
import re

time = '15:38:56'
time2 = '1:8:6'
t = re.match(
    r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$',
    time)
t2 = re.match(
    r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$',
    time2)
print(t.group(0))
print(t.group(1))
print(t.group(2))
print(t.group(3))

# print(t2.group(0))
# print(t2.group(1))
# print(t2.group(2))
# print(t2.group(3))

date = '04-31'
d = re.match(r'^(0[0-9]|1[0-2]|[0-9])-(1[0-9]|2[0-9]|3[0-1]|[0-9])',date)
print(d.group(0))
print(d.group(1))
print(d.group(2))

tanlan = re.match(r'^(\d+)(0*)$', '102300').groups()
print(tanlan)

tanlan2 = re.match(r'^(\d+?)(0*)$', '102300').groups()
print(tanlan2)