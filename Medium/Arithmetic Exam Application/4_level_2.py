# write your code here
import random


def level1():
    num1 = random.randint(2, 9)
    num2 = random.randint(2, 9)
    sign = ['+', '-', '*'][random.randint(0, 2)]
    print(f'{num1} {sign} {num2}')
    return num1, sign, num2


def level2():
    num = random.randint(11, 29)
    print(num)
    square = num ** 2
    return square


def l1_result(num1, sign, num2):
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
            print('Wrong format! Try again.')
            continue
        else:
            return user_inp


def level_choice():
    while True:
        print('Which level do you want? Enter a number:')
        print('1 - simple operations with numbers 2-9')
        print('2 - integral squares of 11-29')
        user_choice = input()
        if user_choice == '1' or user_choice == '2':
            return user_choice
        else:
            print('Incorrect format')
            continue


count = 0
mark = 0
choice = level_choice()
level_description = ''
while count < 5:
    if choice == '1':
        num_1, op, num_2 = level1()
        answer = l1_result(num_1, op, num_2)
        level_description = '(simple operations with numbers 2-9)'
    elif choice == '2':
        answer = level2()
        level_description = '(integral squares of 11-29)'
    else:
        print('Incorrect format')
        continue
    inp = question()
    if answer == inp:
        print('Right!')
        mark += 1
    else:
        print('Wrong!')
    count += 1

print(f'You mark is {mark}/5. Would you like to save the result?')
print('Enter yes or no.')
save_choice = input()
if save_choice in {'Yes', 'yes', 'YES', 'y'}:
    print('What is your name?')
    name = input()
    with open('results.txt', 'a') as f:
        f.write(f'{name}: {mark}/5 in level {choice} {level_description}\n')
    print('The results are saved in "results.txt".')
