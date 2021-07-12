ini_game = '         '
game_matrix = []
count = 0
player = 'X'


for i in range(3):
    row = []
    for j in range(3):
        row.append(ini_game[count].replace('_', ' '))
        count += 1
    game_matrix.append(row)


def con_mat():
    inp = ''
    for i in range(3):
        for j in range(3):
            inp += game_matrix[i][j]
    return inp



def print_matrix():
    inp = con_mat()
    print('---------')
    for i in range(3):
        for j in range(3):
            inp += game_matrix[i][j]
    print(f'| {inp[0]} {inp[1]} {inp[2]} |')
    print(f'| {inp[3]} {inp[4]} {inp[5]} |')
    print(f'| {inp[6]} {inp[7]} {inp[8]} |')

    print('---------')


print_matrix()

while True:
    x, y = input('Enter the coordinates:').split()
    if not (x.isnumeric() and y.isnumeric()):
        print('You should enter numbers!')
        continue
    elif int(x) not in [1, 2, 3] or int(y) not in [1, 2, 3]:
        print('Coordinates should be from 1 to 3!')
        continue
    elif game_matrix[int(x) - 1][int(y) - 1] != ' ':
        # x, y = int(x), int(y)
        print('This cell is occupied! Choose another one!')
        continue
    else:
        game_matrix[int(x) - 1][int(y) - 1] = player
        if player == 'X':
            player = 'O'
        else:
            player = 'X'

        inp = con_mat()
        print_matrix()
        x_len = len([i for i in inp if i == 'X'])
        o_len = len([i for i in inp if i == 'O'])


        def h_win(i):
            for n in (0, 3, 6):
                if inp[n] == i and inp[n + 1] == i and inp[n + 2] == i:
                    return 1
            return 0


        def v_win(i):
            for n in (0, 1, 2):
                if inp[n] == i and inp[n + 3] == i and inp[n + 6] == i:
                    return 1
            return 0


        def d_win(i):
            if inp[0] == i and inp[4] == i and inp[8] == i:
                return 1
            elif inp[2] == i and inp[4] == i and inp[6] == i:
                return 1
            return 0


        o_win = h_win('O') + v_win('O') + d_win('O')
        x_win = h_win('X') + v_win('X') + d_win('X')

        if o_win > 0:
            print('O wins')
            break
        elif x_win > 0:
            print('X wins')
            break
        else:
            if ' ' in inp:
                continue
            else:
                print('Draw')
                break
        break
