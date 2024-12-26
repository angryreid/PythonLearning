"""
decorator - PythonLearning
Author: nick
Date: 2024/12/26
Time: 20:30

Description: 

"""
import os
import sys
from functools import wraps

user_login_state = False


def login_decorator(user_info_file):
    def wrapper(func):
        users = []
        if os.path.exists(user_info_file):
            with open(user_info_file, encoding='utf8') as f:
                lines = f.readlines()
                for line in lines:
                    user = eval(line)  # Dict
                    users.append(user)
        else:
            choice = input('Do you want to create a new account, plz input Y:')
            if choice == 'Y' or choice == 'y':
                user_name = input('Plz input user name:')
                psw = input('Plz input your password:')
                user_info = {'user_name': user_name, 'psw': psw}
                users.append(user_info)
                with open(user_info_file, mode='w', encoding='utf8') as f:
                    f.write(str(user_info))
            else:
                sys.exit(0)

        @wraps(func)
        def inner(*args, **kwargs):
            print(f'Validating user information now...')
            global user_login_state
            if user_login_state is False:
                _name = input('Plz input user name:')
                _psw = input('Plz input password:')
                for _user in users:
                    if _name == _user['user_name'] and _psw == _user['psw']:
                        print(f'Hi {_name}, welcome.')
                        user_login_state = True
                        break
                else:
                    print('No existing user')
                    sys.exit(0)

            return func(*args, **kwargs)

        return inner

    return wrapper


@login_decorator('./assets/user_info.txt')
def login():
    print('User is logining now...')


def main():
    login()


if __name__ == "__main__":
    main()
