"""
guess_number - PythonLearning
Author: nick
Date: 2024/10/31
Time: 14:48

Description: 

"""
import random


def main():
    print('-' * 50)
    while True:
        choice = input('Do you want to play this game:')
        if choice == 'yes' or choice == 'Yes' or choice == 'Y':

            number = random.randint(1, 10)
            for i in range(3):
                guess = int(input('Plz input your target number:'))
                if guess == number:
                    print('Congratulations!')
                    break
                elif i < 2:
                    print(f'Sorry, it is not the target number! only {2 - i} chances last.')
                else:
                    print(f'No good luck, all chances were used! Target is {number}')
        else:
            print('see you next time!')
            break





if __name__ == "__main__":
    main()
