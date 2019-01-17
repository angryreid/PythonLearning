#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'derek'

def application(environ,start_response):
    start_response('200 OK',[('Content-Type','text/html')])
    return [b'<h1 style="text-align:center;background:yellow">A JIE ZUI SHUAI!!!</h1><img src="https://ss0.bdstatic.com/94oJfD_bAAcT8t7mm9GUKT-xh_/timg?image&quality=100&size=b4000_4000&sec=1544431222&di=a64643ca0be72b5c6eb87939ed8d4620&src=http://life.southmoney.com/tuwen/UploadFiles_6871/201801/20180129110733180.jpg"/>']