"""
my_process - PythonLearning
Author: nick
Date: 2024/12/9
Time: 20:23

Description: 

"""
import os
import time
from multiprocessing import Process


class MyProcess(Process):

    def __init__(self, name, wait):
        super().__init__()
        self.name = name
        self.wait = wait

    def run(self):
        print(f'Sub process {self.name} is running!, pid is {os.getpid()}')
        time.sleep(self.wait)
        print(f'Sub process {self.name} end!, pid is {os.getpid()}')


def main():
    main_pic = os.getpid()
    print(f'Main process id: {main_pic}')
    process_list = []
    for i in range(3):
        sub_process_name = f'subProcess_{i}'
        p = MyProcess(sub_process_name, i + 1)
        p.start()
        process_list.append(p)
    for p in process_list:
        p.join()
    print(f'Main process {main_pic} end!')


if __name__ == "__main__":
    main()
