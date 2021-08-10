# Write your code here
import random
import sqlite3

CREATE_TABLE = '''
CREATE TABLE IF NOT EXISTS card(
    id INTEGER PRIMARY KEY,
    number TEXT,
    pin TEXT,
    balance INTEGER DEFAULT 0);
'''

GET_CARDS = 'SELECT number FROM card;'

GET_PIN = 'SELECT pin FROM card WHERE number = ?'

NEW_CARD = 'INSERT INTO card(number, pin) VALUES(?, ?)'

GET_BALANCE = 'SELECT balance FROM card WHERE number = ?'

conn = sqlite3.connect('card.s3db')
cursor = conn.cursor()
cursor.execute(CREATE_TABLE)
conn.commit()


def check_card_pin(cur, card_number, pin):
    check_card_exists = False
    for nums in cur.execute(GET_CARDS).fetchall():
        if card_number == nums[0]:
            check_card_exists = True
    check_pin = False
    if cur.execute(GET_PIN, (card_number,)).fetchone():
        check_pin = cur.execute(GET_PIN, (card_number,)).fetchone()[0] == pin
    return check_card_exists and check_pin


def create_new_card(cur, number, pin):
    cur.execute(NEW_CARD, (number, pin))
    conn.commit()


def balance(cur, card_number):
    return cur.execute(GET_BALANCE, (card_number,)).fetchone()


def create_account():
    pin = ''.join([str(random.randint(0, 9)) for x in range(4)])
    card_number = '400000' + ''.join([str(random.randint(0, 9)) for x in range(9)])
    card_number += luhn(card_number)
    create_new_card(cursor, card_number, pin)
    print('Your card has been created')
    print('Your card number:\n' + card_number)
    print('Your card PIN:\n' + pin)


def login(user_card, user_pin_):
    if not check_card_pin(cursor, user_card, user_pin_):
        print('Wrong card number or PIN!')
    else:
        print('\nYou have successfully logged in!\n')
        while True:
            print('1. Balance')
            print('2. Log out')
            print('0. Exit')
            user_choice = input()
            if user_choice == '1':
                print(balance(cursor, user_card))
            elif user_choice == '2':
                print('\nYou have successfully logged out!\n')
                menu()
            elif user_choice == '0':
                print('Bye!')
                exit()


def luhn(number):
    sum_ = 0
    lst = list(number)
    for i in range(0, len(lst), 2):
        lst[i] = str(int(lst[i]) * 2)
        if int(lst[i]) > 9:
            lst[i] = str(int(lst[i]) - 9)
    for i in lst:
        sum_ += int(i)
    return str(10 - (sum_ % 10)) if (sum_ % 10) > 0 else '0'


def menu():
    while True:
        print('1. Create an account')
        print('2. Log into account')
        print('3. Get all info')
        print('0. Exit')
        choice = input()
        if choice == '1':
            create_account()
        elif choice == '2':
            cn = input('\nEnter your card number:')
            user_pin = input('Enter your PIN')
            login(cn, user_pin)
        elif choice == '3':
            print(cursor.execute('SELECT * FROM card').fetchall())
        elif choice == '0':
            print('\nBye!')
            exit()


menu()
