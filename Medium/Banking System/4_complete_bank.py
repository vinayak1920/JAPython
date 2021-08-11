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

GET_PIN = 'SELECT pin FROM card WHERE number = ?;'

NEW_CARD = 'INSERT INTO card(number, pin) VALUES(?, ?);'

GET_BALANCE = 'SELECT balance FROM card WHERE number = ?;'

CHANGE_BALANCE = 'UPDATE card SET balance = ? WHERE  number = ?;'

DELETE_ACCOUNT = 'DELETE FROM card WHERE number = ?;'

CHECK_CARD = 'SELECT EXISTS(SELECT * FROM card WHERE number = ?)'

conn = sqlite3.connect('card.s3db')
cursor = conn.cursor()
cursor.execute('DROP TABLE IF EXISTS card')
conn.commit()
cursor.execute(CREATE_TABLE)
conn.commit()


def change_bal(cur, con, card_number, amount):
    cur.execute(CHANGE_BALANCE, (amount, card_number))
    con.commit()


def add_income(cur, con, card_number, income):
    bal = balance(cur, card_number) + income
    change_bal(cur, con, card_number, bal)
    print('Income was added!')


def close_account(cur, con, card_number):
    cur.execute(DELETE_ACCOUNT, (card_number,))
    con.commit()
    print('\nThe account has been closed!')


def transfer(cur, con, user_number):
    print('\nTransfer')
    card_number = input('Enter card number:')
    if user_number == card_number:
        print("You can't transfer money to the same account!")
    elif card_number[-1] != luhn(card_number[:15]):
        print('Probably you made a mistake in the card number. Please try again!')
    elif not cur.execute(CHECK_CARD, (card_number,)).fetchone()[0]:
        print('Such a card does not exist.')
    else:
        amount = int(input('Enter how much money you want to transfer:'))
        if balance(cur, user_number) < amount:
            print('Not enough money!')
        else:
            user_bal = balance(cur, user_number) - amount
            payee_bal = balance(cur, card_number) + amount
            change_bal(cur, con, user_number, user_bal)
            change_bal(cur, con, card_number, payee_bal)
            print('Success!')


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
    return int(cur.execute(GET_BALANCE, (card_number,)).fetchone()[0])


def create_account():
    pin = ''.join([str(random.randint(0, 9)) for x in range(4)])
    card_number = '400000' + ''.join([str(random.randint(0, 9)) for x in range(9)])
    card_number += luhn(card_number)
    create_new_card(cursor, card_number, pin)
    print('\nYour card has been created')
    print('Your card number:\n' + card_number)
    print('Your card PIN:\n' + pin + '\n')


def login(user_card, user_pin_):
    if not check_card_pin(cursor, user_card, user_pin_):
        print('\nWrong card number or PIN!')
    else:
        print('\nYou have successfully logged in!\n')
        while True:
            print('\n1. Balance')
            print('2. Add income')
            print('3. Do transfer')
            print('4. Close account')
            print('5. Log out')
            print('0. Exit')
            user_choice = input()
            if user_choice == '1':
                print(balance(cursor, user_card))
            elif user_choice == '2':
                income = int(input('\nEnter income:'))
                add_income(cursor, conn, user_card, income)
            elif user_choice == '3':
                transfer(cursor, conn, user_card)
            elif user_choice == '4':
                close_account(cursor, conn, user_card)
            elif user_choice == '5':
                print('\nYou have successfully logged out!\n')
                menu()
            elif user_choice == '0':
                print('\nBye!')
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
        print('0. Exit')
        choice = input()
        if choice == '1':
            create_account()
        elif choice == '2':
            cn = input('\nEnter your card number: ')
            user_pin = input('Enter your PIN: ')
            login(cn, user_pin)
        elif choice == '0':
            print('\nBye!')
            exit()


menu()
