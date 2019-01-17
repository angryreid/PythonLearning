#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'derek'

def application(environ,start_response):
    start_response('200 OK',[('Content-Type','text/html')])
    return [b'<h1>Hello ,World</h1>']

