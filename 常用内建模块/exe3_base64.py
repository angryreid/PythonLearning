#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'derek'

# base64
# 二进制编码方法
# 每三个字节一组

import base64

# Base64编码会把3字节的二进制数据编码为4字节的文本数据
# 如果要编码的二进制数据不是3的倍数,Base64用\x00字节在末尾补足后，再在编码的末尾加上1个或2个=号
print(base64.b64encode(b'binary\x00string'))
print(base64.b64decode(b'YmluYXJ5AHN0cmluZw=='))

# urlsafe
# 将+ ===》 -
# 将- ===》 _
print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))
def safe_base64_decode(s):
    if isinstance(s, bytes):
        s = s + b'=' * 2
        print(s)
    else:
        s = s + '=' * 2
        print(s+'1111')
    return base64.urlsafe_b64decode(s)
# 测试:
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')