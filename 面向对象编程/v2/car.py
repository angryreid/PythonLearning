"""
car - PythonLearning
Author: nick
Date: 2024/11/16
Time: 19:21

Description: 

"""


class Car:
    __date__ = 'Today'

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def __str__(self):
        return 'None'

    def __del__(self):
        print('Car is deleted')

    def depreciate(self, date, price):
        self.price = price
        print(f'Depreciated from {date}, {self.brand}, {self.price}')

    @classmethod
    def run(cls):
        print(f'Car is running, {cls}, {cls.__date__}')


def main():
    car_first = Car(brand='Toyota', price='20w')
    print(car_first)
    print(f'Car brand is {car_first.brand}, price is {car_first.price}, date is {car_first.__date__}')
    car_first.depreciate(date='2024', price='18w')
    print(f'Car brand is {car_first.brand}, price is {car_first.price}, date is {car_first.__date__}')

    car_first.run()
    Car.run()
    del car_first


if __name__ == "__main__":
    main()
