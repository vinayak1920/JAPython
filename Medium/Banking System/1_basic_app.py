# Write your code here
import random

cards = {}


def create_account():
    pin = str(random.randint(0000, 9999))
    card_number = '400000' + str(random.randint(0000000000, 9999999999)
    cards[card_number] = [pin, 0]
    print('Your card has been created')
    print('Your card number:\n' + card_number)
    print('Your card PIN:\n' + pin)


def login(user_card, user_pin_):
    if user_card not in cards.keys() or cards[user_card][0] != user_pin_:
        print('Wrong card number or PIN!')
    else:
        print('You have successfully logged in!')
        print('1. Balance')
        print('2. Log out')
        print('0. Exit')
        user_choice = input()
        if user_choice == '1':
            print(cards[user_card][1])
        elif user_choice == '2':
            menu()
        elif user_choice == '0':
            print('Bye!')
            exit()



def menu():
    print('1. Create an account')
    print('2. Log into account')
    print('0. Exit')
    choice = input()
    if choice == '1':
        create_account()
    elif choice == '2':
        cn = input('Enter your card number:')
        user_pin = input('Enter your PIN')
    elif choice == '0':
        print('Bye!')
        exit()


while True:
    menu()
