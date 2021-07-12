initial_state = input('Enter cells:')

game_matrix = []
count = 0

for i in range(3):
    row = []
    for j in range(3):
        row.append(initial_state[count].replace('_', ' '))
        count += 1
    game_matrix.append(row)


def print_matrix():
    print('_' * 9)
    for i in range(3):
        row = '| '
        for j in range(3):
            row = row + game_matrix[i][j] + ' '
        row += '|'
        print(row)

    print('_' * 9)


print_matrix()

while True:
    x, y = input('Enter the coordinates:').split()
    if not (x.isnumeric() and y.isnumeric()):
        print('You should enter numbers!')
    elif int(x) not in [1, 2, 3] or int(y) not in[1, 2, 3]:
        print('Coordinates should be from 1 to 3!')
    elif game_matrix[int(x) - 1][int(y) - 1] != ' ':
        # x, y = int(x), int(y)
        print('This cell is occupied! Choose another one!')
    else:
        game_matrix[int(x) - 1][int(y) - 1] = 'X'
        print_matrix()
        break
