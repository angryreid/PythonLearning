#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'derek'

# class 的类型就是type 而他的实例的类型是class
# class 的定义是运行时动态创建的，而创建class的方法就是type函数

# type函数 既可以返回类型，也可以创建类型
# 直接通过type函数创建类，而无需使用class SSS（）的定义
def fn(self,name='world'):
    print('Hello, %s' % name)
Hello = type('Hello',(object,),dict(hello=fn))
# 定义传入三个参数
# class的名称；
# 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
h = Hello()
h.hello()
print(type(Hello))
print(type(h))

# metaclass 控制创建类的创建行为
# 正常情况来说，先创建类，在创建实例
# 所以，先创建metaclass，在创建class
# 所以，metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”。
