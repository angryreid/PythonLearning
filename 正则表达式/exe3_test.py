#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'derek'

import re


def is_valid_email(addr):
    if addr == "":
        return False
    elif re.match(r'^[a-zA-Z_]*\@[a-z]*\.(com|cn|com.cn)$', addr):
        return True
    else:
        return False


# test
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')
