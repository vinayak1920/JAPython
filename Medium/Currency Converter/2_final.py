import requests

curr = input()
rates = requests.get(f'http://www.floatrates.com/daily/{curr}.json').json()
cache = dict()
if curr != 'usd':
    cache['usd'] = rates['usd']['rate']
if curr != 'eur':
    cache['eur'] = rates['eur']['rate']
while True:
    exchange = input()
    if not exchange:
        break
    amount = float(input())
    print('Checking the cache...')
    if exchange in cache:
        print('Oh! It is in the cache!')
        amt_exchange = amount * cache[exchange]
        print(f'You recieved {amt_exchange:.2f} {exchange}')
    else:
        print('Sorry, but it is not in the cache!')
        cache[exchange] = rates[exchange]['rate']
        amt_exchange = amount * cache[exchange]
        print(f'You recieved {amt_exchange:.2f} {exchange}')
