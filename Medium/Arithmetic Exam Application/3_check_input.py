# write your code here
import random


def assign_ques():
    num1 = random.randint(2, 9)
    num2 = random.randint(2, 9)
    sign = ['+', '-', '*'][random.randint(0, 2)]
    print(f'{num1} {sign} {num2}')
    return num1, sign, num2


def return_result(num1, sign, num2):
    result = 0
    if sign == '+':
        result = num1 + num2
    elif sign == '-':
        result = num1 - num2
    elif sign == '*':
        result = num1 * num2
    return result


def question():
    while True:
        try:
            user_inp = int(input())
        except ValueError:
            print('Incorrect format.')
            continue
        else:
            return user_inp


count = 0
mark = 0
while count < 5:
    num_1, op, num_2 = assign_ques()
    answer = return_result(num_1, op, num_2)
    inp = question()
    if answer == inp:
        print('Right!')
        mark += 1
    else:
        print('Wrong!')
    count += 1

print(f'You mark is {mark}/5')
