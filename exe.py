# print("hello,the world")
# print(100)
# print(100+200)
# print('100+200=',100+200)
# name = input('please input your name:')
# print('hello:'+name)
# a=100
# if a >= 0:
#     print(a)
# else:
#     print(-a)
# print("I'am ok")
# print('''hello
# world
# hello
# world''')

if __name__ == '__main__':
    a = 10
    print(a)
    print(type(a))

    a = '123'
    print(a)
    print(len(a))
    print(not 3 > 2)
    name = 'derek'
    age = 22
    # % can be used to output as format
    print('Dear %s,you are %d' % (name, 22))
    print('%2d-%04d' % (3, 1))
    print('%.2f' % 3.1415926)
    print('your score:%.2f' % ((90 - 80) / 80))

    # Added from here: 20241029
    print('-' * 10)

    print(f'My name is {name}, and age is {age}')

    # print('Plz input your name:')
    # name = input('name:')
    # print(type(name))
    # print(name)
