"""
process - PythonLearning
Author: nick
Date: 2024/12/9
Time: 19:54

Description:

"""
import os
from multiprocessing import Process, Queue
import time


def sub_process_run(name, q):
    v = q.get()
    print(f'Sub process {name} is running!, pid is {os.getpid()}, get value: {v}')
    time.sleep(2)
    v += 1
    q.put(v)
    print(f'Sub process {name} end!, pid is {os.getpid()}')


def main():
    # pass  # TODO: Implement your code here
    print(f'Main process id: {os.getpid()}')
    q = Queue()
    q.put(0)
    pl = []
    for i in range(10):
        sub_process_name = f'subProcess_{i}'
        p = Process(target=sub_process_run, args=(sub_process_name, q))
        p.start()
        pl.append(p)
    for p in pl:
        p.join()
    print(f'Get value in main process: {q.get()}')
    print(f'Main process end!')


if __name__ == "__main__":
    main()
