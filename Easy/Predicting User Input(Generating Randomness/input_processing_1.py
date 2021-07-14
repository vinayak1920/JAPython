data_string = ''

while len(data_string) < 100:
    print('Print a random string containing 0 or 1:')
    inp = input()
    user_list = list()
    user_list = [x for x in inp if x == '0' or x == '1']
    data_string += ''.join(user_list)
    print('Current data length is ' + str(len(data_string)) + ', ' + str(100 - len(data_string)) + 'symbols left')

print('Final data string \n' + data_string)
