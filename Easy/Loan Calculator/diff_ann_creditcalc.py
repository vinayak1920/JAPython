import math
import argparse
from collections import Counter

parser = argparse.ArgumentParser(description='Calculates differentiated or  annuity payment(principal \
number of months or payment per month)')

parser.add_argument('--type', choices=["annuity", 'diff'])
parser.add_argument('--payment')
parser.add_argument('--principal')
parser.add_argument('--periods')
parser.add_argument('--interest')

args = parser.parse_args()
g_p = args.principal
g_i = args.interest
g_n = args.periods
g_pay = args.payment

none_count = Counter([g_p, g_i, g_n, g_pay])[None]


def convert(array=None):
    if array is None:
        array = []
    for elem in range(len(array)):
        if elem == 0:
            array[elem] = float(array[elem]) / (12 * 100)
        else:
            array[elem] = float(array[elem])
    return array


if args.type == 'diff':
    if args.interest is None or (args.payment is not None) or none_count > 1:
        print('Incorrect parameters')

    else:
        if args.payment is None:
            i, p, n = convert([g_i, g_p, g_n])
            sum_pay = 0
            for m in range(1, int(n + 1)):
                pay = math.ceil((p / n) + (i * (p - (p * (m - 1) / n))))
                sum_pay += pay
                print(f'Month {m}: payment is {pay}')
            over = round(sum_pay - p)
            print(f'Overpayment = {over}')

elif args.type == 'annuity':
    if args.interest is None or none_count > 1:
        print('Incorrect parameters')
    elif args.payment is None:
        i, p, n = convert([g_i, g_p, g_n])
        pay = math.ceil(p * (i * pow(1 + i, n)) / (pow(1 + i, n) - 1))
        over = round((pay * n) - p)
        print(f'You annuity payment = {pay}!')
        print(f'Overpayment = {over}')
    elif args.principal is None:
        i, n, a = convert([g_i, g_n, g_pay])
        p = math.floor(a / ((i * pow(1 + i, n)) / (pow(1 + i, n) - 1)))
        over = round(a * n - p)
        print(f'Your loan principal = {p}!')
        print(f'Overpayment = {over}')
    elif args.periods is None:
        i, p, a = convert([g_i, g_p, g_pay])
        n = math.ceil(math.log((a / (a - i * p)), 1 + i))
        years = n // 12
        months = n % 12
        if years == 0:
            print('It will take {} month{} to repay this loan!'.format(months, 's' if months > 1 else ''))
        elif months == 0:
            print('It will take {} year{} to repay this loan!'.format(years, 's' if years > 1 else ''))
        else:
            if years == 1:
                print(
                    'It will take 1 year and {} month{} to repay this loan!'.format(months, 's' if months > 1 else ''))
            if months == 1:
                print('It will take {} year{} and 1 month to repay this loan!'.format(years, 's' if years > 1 else ''))
            else:
                print(f'It will take {years} years and {months} months to repay this loan!')
        over = round(a * n - p)
        print(f'Overpayment = {over}')

else:
    print('Incorrect parameters')
