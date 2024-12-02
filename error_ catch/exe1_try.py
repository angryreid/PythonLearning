#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'derek'
try:
    print(10/0)
except ZeroDivisionError as e:
    print("Error:",e)
finally:
    print('finally...')

# 不同类型的异常捕获
try:
    print('try...')
    r = 10 / int('a')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
finally:
    print('finally...')
print('END')

# 如果没有错误发生，可以在except语句块后面加一个else，当没有错误发生时，会自动执行else语句：
try:
    print('try...')
    r = 10 / int('2')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')
# 没有error时，会直接返回值
# Python的错误其实也是class，所有的错误类型都继承自BaseException，所以在使用except时需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽

# 出错的时候，一定要分析错误的调用栈信息，才能定位错误的位置。
from functools import reduce

def str2num(s):
    if type(eval(s)) == int:
        return int(s)
    elif type(eval(s)) == float:
        return float(s)
    else:
        return 0
def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()