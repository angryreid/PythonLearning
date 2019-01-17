#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'derek'

class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s:%s' % (self.name,self.score))

foo = Student('foo',100)
bar = Student('bar',101)
foo.print_score()
bar.print_score()