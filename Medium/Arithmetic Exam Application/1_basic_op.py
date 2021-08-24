# write your code here
num1, sign, num2 = input().split()
result = 0
num1 = int(num1)
num2 = int(num2)
if sign == '+':
    result = num1 + num2
elif sign == '-':
    result = num1 - num2
elif sign == '*':
    result = num1 * num2

print(result)
