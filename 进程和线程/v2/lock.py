"""
lock - PythonLearning
Author: nick
Date: 2024/12/13
Time: 17:58

Description: 

"""

# 一个进程至少包含一个线程，一个进程可以包含多个线程
import threading

# 我们必须确保一个线程在修改money的时候，别的线程一定不能改。
import threading

money = 0
lock = threading.Lock()


def change_it(n):
    global money
    money = money + n
    money = money - n 
    print('当前进程是:%s,当前money：%s,当前n:%s' % (threading.current_thread().name, money, n))


def run_thread2(n):
    for i in range(5):
        change_it(n)


def run_thread(n):
    for i in range(5):
        # 先要获取锁:
        lock.acquire()
        try:
            # 放心地改吧:
            change_it(n)
        finally:
            # 改完了一定要释放锁:
            lock.release()


def main():
    t1 = threading.Thread(target=run_thread, args=(5,), name='t1')
    t2 = threading.Thread(target=run_thread, args=(8,), name='t2')
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(money)


if __name__ == "__main__":
    main()
