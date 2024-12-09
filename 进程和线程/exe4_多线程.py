#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'derek'

# 一个进程至少包含一个线程，一个进程可以包含多个线程
import time, threading

# 新线程执行代码
# def loop():
#     print('thread %s is running ...' % threading.current_thread().name)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('thread %s >>> %s' % (threading.current_thread().name,n))
#         time.sleep(1)
#     print('thread %s ended.' % threading.current_thread().name)
# print('thread %s is running...' % threading.current_thread().name)
# t = threading.Thread(target=loop,name='LoopThread')
# t.start()
# t.join()
# print('thread %s ended.' % threading.current_thread().name)

# 线程锁 lock

# balance = 0

# def change_it(n):
#     # 先存后取，结果应该为0:
#     global balance
#     balance = balance + n
#     balance = balance - n
#
# def run_thread(n):
#     for i in range(100000):
#         change_it(n)
#
# t1 = threading.Thread(target=run_thread, args=(5,))
# t2 = threading.Thread(target=run_thread, args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)

# 我们必须确保一个线程在修改balance的时候，别的线程一定不能改。
import time, threading

money = 0


def change_it(n):
    global money
    money = money + n
    money = money - n
    print('当前进程是:%s,当前money：%s,当前n:%s' % (threading.current_thread().name, money, n))


def run_thread(n):
    for i in range(100):
        change_it(n)


t1 = threading.Thread(target=run_thread, args=(5,), name='t1')
t2 = threading.Thread(target=run_thread, args=(8,), name='t2')
t1.start()
t2.start()
t1.join()
t2.join()
print(money)

balance = 0
lock = threading.Lock()


def run_thread(n):
    for i in range(100000):
        # 先要获取锁:
        lock.acquire()
        try:
            # 放心地改吧:
            change_it(n)
        finally:
            # 改完了一定要释放锁:
            lock.release()
