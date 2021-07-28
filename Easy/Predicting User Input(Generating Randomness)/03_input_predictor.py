data_string = ''

while len(data_string) < 100:
    print('Print a random string containing 0 or 1:')
    inp = input()
    user_list = [x for x in inp if x == '0' or x == '1']
    data_string += ''.join(user_list)
    print('Current data length is ' + str(len(data_string)) + ', ' + str(100 - len(data_string)) + 'symbols left')

print('Final data string \n' + data_string)

triad = {'000': [0, 0], '001': [0, 0], '010': [0, 0], '011': [0, 0], '100': [0, 0], '101': [0, 0], '110': [0, 0], '111': [0, 0]}

for i in range(len(data_string) - 3):
    if data_string[i + 3] == '0':
        triad[data_string[i: i + 3]][0] += 1
    else:
        triad[data_string[i: i + 3]][1] += 1

for k, v in triad.items():
    print(k + ': ' + str(v[0]) + ',' + str(v[1]))

input_string = input('Please enter a test string containing 0 or 1:')
prediction = input_string[:3]
for i in range(3, len(input_string)):
    prob = triad[input_string[i - 3: i]][0] / (triad[input_string[i - 3: i]][1] + triad[input_string[i - 3: i]][0])
    if prob >= 0.5:
        prediction += '0'
    else:
        prediction += '1'

print(f'\nprediction:\n{prediction}')

m = 0
for i in range(3, len(input_string)):
    if prediction[i] == input_string[i]:
        m += 1
acc = (m * 100) / (len(input_string) - 3)

print(f'Computer guessed right {m} out of {len(input_string)} symbols ({acc:0.2f} %)')
