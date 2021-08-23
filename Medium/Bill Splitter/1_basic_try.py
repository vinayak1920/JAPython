# write your code here
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
    split_bill = bill / num_friends
    for k in friends.keys():
        friends[k] = round(split_bill, 2)
    print(friends)
