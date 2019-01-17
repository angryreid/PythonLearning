#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'derek'


class Student(object):
    def __init__(self, name, score):
        # 使用两个下划线定义私有变量
        # __name__ 这样的是特殊变量，可以直接访问
        # _name 一个下划线这种变量，外面可以访问，但是不要随意访问
        self.__name = name
        self.__score = score

    # 增加get set
    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def print_score(self):
        print('%s:%s' % (self.__name, self.__score))


foo = Student('foo', 100)
bar = Student('bar', 101)
foo.print_score()
bar.print_score()
print(foo.get_name(),foo.get_score())