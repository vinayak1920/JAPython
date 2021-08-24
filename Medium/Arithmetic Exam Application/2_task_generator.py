import random

num1 = random.randint(2, 9)
num2 = random.randint(2, 9)
sign = ['+', '-', '*'][random.randint(0, 2)]

result = 0
if sign == '+':
    result = num1 + num2
elif sign == '-':
    result = num1 - num2
elif sign == '*':
    result = num1 * num2

print(f'{num1} {sign} {num2}')
user_inp = int(input())
if user_inp == result:
    print('Right!')
else:
    print('Wrong!')

