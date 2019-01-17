#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'derek'

import os

# print('Process (%s) start...' % os.getpid())
# # Only works on Unix/Linux/Mac:
# pid = os.fork()
# if pid == 0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

# 有了fork调用，一个进程在接到新任务时就可以复制出一个子进程来处理新任务，常见的Apache服务器就是由父进程监听端口，每当有新的http请求时，就fork出子进程来处理新的http请求。
# Windows没有fork调用，

# 从一个模块导入一个雷
from multiprocessing import Process
# 直接导入该模块
import os

def run_proc(name):
    print('Run child process %s (%s)...' % (name,os.getpid()))

if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc,args=('test',))
    print('Child process will start')
    p.start()
    p.join()#方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
    print('Child process end.')