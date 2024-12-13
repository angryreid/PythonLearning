"""
thread - PythonLearning
Author: nick
Date: 2024/12/13
Time: 17:17

Description: 

"""
import os
import time
from threading import Thread


def sum_task(n):
    s = 0
    for i in range(n + 1):  # safe check
        s += i
    print(f'Sum task {os.getpid()} result is {s}')
    return s


def main():
    # pass  # TODO: Implement your code here
    start_time = time.time()
    target = 100000000
    # print(sum_task(target)) # Cost time: 2.4096908569335938ms
    t1 = Thread(target=sum_task, args=(int(target / 2),))
    t2 = Thread(target=sum_task, args=(int(target / 2),))
    t1.start()
    t2.start()
    t1.join()
    t2.join()  # Cost time: 2.283440113067627s
    # print(f'Sum: {t1 + t2}')
    end_time = time.time()
    print(f'Cost time: {(end_time - start_time)}s')


if __name__ == "__main__":
    main()
