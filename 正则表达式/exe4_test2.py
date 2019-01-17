#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'derek'

import re
import re
def name_of_email(addr):
    if addr == "":
        return False
    test = re.match(r'^([[\<a-zA-Z][a-zA-Z]*\s[a-zA-Z]\>$] | [a-zA-Z]])\@[a-z]*\.(com|cn|com.cn)$',addr)
    if test:
        print(test.group(1))
        return test.group(1)
    else:
        return None
# 测试:
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')