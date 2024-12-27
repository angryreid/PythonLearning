#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'derek'

import re

re_emailaddr = re.compile(r'^(\w[a-zA-Z.]+)(@)(\w[a-z]+)(.com)$')


def is_valid_email(addr):
    if re_emailaddr.match(addr):
        return True
    else:
        print('%s is a wrong email addr' % addr)


if __name__ == '__main__':
    assert is_valid_email('someone@gmail.com')
    assert is_valid_email('bill.gates@microsoft.com')
    assert not is_valid_email('bob#example.com')
    assert not is_valid_email('mr-bob@example.com')
    print('ok')
