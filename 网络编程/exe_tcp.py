#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'derek'
import socket

# 创建一个socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 建立连接
s.connect(('www.sina.com.cn',80))