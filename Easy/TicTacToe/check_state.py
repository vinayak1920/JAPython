inp = input('Enter cells:')

print('---------')
print(f'| {inp[0]} {inp[1]} {inp[2]} |')
print(f'| {inp[3]} {inp[4]} {inp[5]} |')
print(f'| {inp[6]} {inp[7]} {inp[8]} |')
print('---------')

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

if abs(x_len - o_len) > 1:
    print('Impossible')
else:
    if o_win > 0 and x_win > 0:
        print('Impossible')
    elif o_win > 0:
        print('O wins')
    elif x_win > 0:
        print('X wins')
    else:
        if '_' in inp:
            print('Game not finished')
        else:
            print('Draw')
