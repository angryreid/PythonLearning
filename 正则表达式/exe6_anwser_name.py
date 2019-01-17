#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'derek'
import re

re_emailaddr = re.compile(r'^(.+)(@)(\w[a-z]+)(.\w{2,3})$')

def name_of_email(addr):
    m = re_emailaddr.match(addr)
    if m:
        if '<' in m.group(1):
            L = re.split(r'[>\<]',m.group(1))
            return L[1]
        else:
            return m.group(1)
if __name__ == '__main__':
    assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
    assert name_of_email('tom@voyager.org') == 'tom'
    print('ok')