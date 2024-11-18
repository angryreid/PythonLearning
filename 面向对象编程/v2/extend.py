"""
extend - PythonLearning
Author: nick
Date: 2024/11/18
Time: 22:00

Description: 

"""


class Parent(object):
    def __init__(self, name):
        self.name = name
        print('Init parent...')


class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
        print('Init child...')

    def __str__(self):
        year_str = 'years' if self.age > 1 else 'year'
        return f'My name is {self.name} and im {self.age} {year_str} old'


def main():
    print(Child.__mro__)
    fries = Child(name='Shutiao', age=0.2)
    print(fries)


if __name__ == "__main__":
    main()
