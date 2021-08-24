import random
friends = {}
try:
    num_friends = int(input('Enter the number of friends joining (including you):\n'))
    assert num_friends > 0
except Exception:
    print("\nNo one is joining for the party")
else:
    print('\nEnter the name of every friend (including you), each on a new line:')
    for i in range(num_friends):
        friends_name = input()
        friends[friends_name] = 0
    bill = float(input('\nEnter the total bill value:\n'))
    list_friends = list(friends.keys())
    lucky_choice = input('\nDo you want to use the "Who is lucky?" feature? Write Yes/No:\n')
    if lucky_choice == 'Yes':
        lucky_friend = list_friends[random.randint(0, len(list_friends) - 1)]
        print(f'\n{lucky_friend} is the lucky one')
        split_bill = bill / (num_friends - 1)
        for k in friends.keys():
            if k == lucky_friend:
                friends[k] = 0
            else:
                friends[k] = round(split_bill, 2)
    else:
        print('No one is going to be lucky')
        split_bill = bill / num_friends
        for k in friends.keys():
            friends[k] = round(split_bill, 2)
    print(f'\n{friends}')
