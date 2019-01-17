#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'derek'
# 摘要算法又称哈希算法、散列算法
# 它通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）。

import hashlib

# MD5
# 生成结果是固定的128 bit字节 32位的16进制字符串表示。
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())
md5.update('KHadmin0592'.encode('utf-8'))
print(md5.hexdigest())
# 329de156fecb6b38ca1e1346a8c99d60

# SHA1
# SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示

sha1 = hashlib.sha1()
sha1.update('KHadmin0592'.encode('utf-8'))
print(sha1.hexdigest())

db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}

def login(user,psw):
    _user = db[user]
    if _user:
        md5.update(psw.encode('utf-8'))
        return _user == md5.hexdigest()
    else:
        return False
# 测试:
assert not login('michael', '123456')
assert not login('bob', 'abc999')
assert not login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')

md5.update('123456'.encode('utf-8'))
print(md5.hexdigest())
md5.update('888888'.encode('utf-8'))
print(md5.hexdigest())