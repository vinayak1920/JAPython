# write your code here!
import requests
import json

code = input()
url = 'http://www.floatrates.com/daily/' + code + '.json'
rates = requests.get(url).json()
print(rates['usd'])
print(rates['eur'])
