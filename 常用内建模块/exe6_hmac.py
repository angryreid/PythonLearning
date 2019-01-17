#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'derek'
import hmac

# 传入的key和message都是bytes类型，str类型需要首先编码为bytes。
message = b'hello world'
key = b'secret'
h = hmac.new(key, message, digestmod='MD5')
print(h.hexdigest())

# 标准的 hmac算法，验证用户口令
import random


def hmac_md5(key, s):
    print(key)
    return hmac.new(key.encode('utf-8'), s.encode('utf-8'), 'MD5').hexdigest()


class User(object):
    def __init__(self, username, password):
        self.username = username
        self.key = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = hmac_md5(self.key, password)


db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}

def login(username, password):
    user = db[username]
    return user.password == hmac_md5(user.key, password)

# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')