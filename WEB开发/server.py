#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'derek'
from wsgiref.simple_server import make_server
from hello import application

httpd = make_server('192.168.69.216',8000,application)
print('Serveing HTTP on port 127.0.0.1:8000...')
httpd.serve_forever()