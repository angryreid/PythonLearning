#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'derek'
print(type(1123))
print(type(None))

print(type(213) == int)
print(type('213') == str)

# 如果要判断一个对象是否是函数

import types


def fn():
    pass


print(type(fn) == types.FunctionType)
print(type(lambda X: X) == types.LambdaType)
print(type(x for x in range(10)) == types.GeneratorType)
# 总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。
isinstance([1, 2, 3], (list, tuple))
# 还可以判断一个变量是否是某些类型中的一种
# 使用dir 方法，获得一个对象的所有属性和方法
# print(dir('abs'))

class MyObj(object):
    name = 'oh~~ en~~'
    def __init__(self):
        self.x = 9
        self.__y = 0
    def power(self):
        return self.x*self.x
obj = MyObj()

print(obj.power())

print(hasattr(obj,'x'))
print(hasattr(obj,'y'))
print(getattr(obj,'x'))
# getattr 可以传入一个默认参数
print(getattr(obj,'y',404))

# 实例属性的优先级比类属性的优先级要高
# 删除实例的属性要用 del
print(obj.name)
obj.name = 'ooo~~enenen~~~'
print(obj.name)
del obj.name
print(obj.name)

class Student(object):
    count = 0
    def __init__(self,name):
        self.name = name
        Student.count += 1
# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')
