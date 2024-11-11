"""
copy_py_file - PythonLearning
Author: nick
Date: 2024/11/11
Time: 21:43

Description: 

"""

import os


def copy_task(source, destination):
    """
    :param source: Copy folder source
    :param destination: Copy folder target
    :return: None
    """
    if not os.path.exists(source) or not os.path.isdir(source):
        return

    file_list = os.listdir(source)
    for f in file_list:
        f_path = os.path.join(source, f)
        t_path = os.path.join(destination, f)

        if os.path.isfile(f_path) and f.endswith('.py'):
            if not os.path.exists(destination):
                os.makedirs(destination)
            copy_py(f_path, t_path)
        elif os.path.isdir(f_path):
            copy_task(f_path, t_path)


def copy_py(source_py, target_py):
    file_source = open(source_py, 'r')
    file_target = open(target_py, 'w')
    while True:
        content = file_source.read(1024 * 10)
        if content == '' or content is None:
            break
        file_target.write(content)
    file_source.close()
    file_target.close()


if __name__ == "__main__":
    copy_task('/Users/nick/Documents/github/PythonLearning/IO操作/v2', '/Users/nick/Documents/github/PythonLearning/IO操作/assets/copy_task')
