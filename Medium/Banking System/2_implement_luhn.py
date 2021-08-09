#Write your code here
import random

cards = {}


def create_account():
    pin = ''.join([str(random.randint(0, 9)) for x in range(4)])
    card_number = '400000' + ''.join([str(random.randint(0, 9)) for x in range(9)])
    card_number += luhn(card_number)
    cards[card_number] = [pin, 0]
    print('Your card has been created')
    print('Your card number:\n' + card_number)
    print('Your card PIN:\n' + pin)


def login(user_card, user_pin_):
    if user_card not in cards.keys() or cards[user_card][0] != user_pin_:
        print('Wrong card number or PIN!')
    else:
        print('\nYou have successfully logged in!\n')
        print('1. Balance')
        print('2. Log out')
        print('0. Exit')
        user_choice = input()
        if user_choice == '1':
            print(cards[user_card][1])
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
    print('1. Create an account')
    print('2. Log into account')
    print('0. Exit')
    choice = input()
    if choice == '1':
        create_account()
    elif choice == '2':
        cn = input('\nEnter your card number:')
        user_pin = input('Enter your PIN')
        login(cn, user_pin)
    elif choice == '0':
        print('\nBye!')
        exit()


while True:
    menu()
