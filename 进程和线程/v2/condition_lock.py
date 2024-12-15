"""
condition_lock - PythonLearning
Author: nick
Date: 2024/12/13
Time: 18:05

Description: 

"""
from threading import Condition, Thread, current_thread

g_number = 0
sub_thread_count = 10
cur_running_thread_count = 0
lock = Condition()


def task():
    global g_number, cur_running_thread_count
    thread_name = current_thread().name
    with lock:
        print(f'{thread_name} locked...')
        lock.wait()
        print(f'{thread_name} unlocked...')
        g_number += 1
        cur_running_thread_count += 1
        print(f'The current number value is: {g_number}')


def main():
    # pass  # TODO: Implement your code here
    thread_list = []

    for i in range(sub_thread_count):
        t = Thread(target=task, name=f'sub_thread_{i + 1}')
        t.start()
        thread_list.append(t)
    # for i in range(sub_thread_count):
    #     thread_list[i].join()
    # for t in thread_list:
    #     t.join()
    print('\n')
    while cur_running_thread_count < sub_thread_count:
        n = int(input('Plz input the unlock thread size:\n'))
        with lock:
            lock.notify(n)
    print('Main thread completed.')


if __name__ == "__main__":
    main()
