import math

loan = int(input('Enter the loan principal'))
print('''What do you want to calculate? 
type "m" for number of monthly payments,
type "p" for the monthly payment:''')
inp = input()
if inp == 'm':
    pay = int(input('Enter monthly payment:'))
    months = math.ceil(loan/pay)
    print('It will take ' + str(months) + ('month ' if months == 1 else 'months ' + 'to repay the loan'))
else:
    num_m = int(input('Enter the number of months:'))
    m_pay = math.ceil(loan/num_m)
    l_pay = loan - (num_m - 1) * m_pay
    print('Your monthly payment is ' + str(m_pay) + (' and the last payment is ' + str(l_pay) if l_pay > 0 else ''))
