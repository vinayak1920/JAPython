# Write your code here
import random

print('H A N G M A N')


def game():
    answers = ['python', 'java', 'kotlin', 'javascript']

    answer = random.choice(answers)
    word = list('-' * len(answer))
    attempts = set()

    counter = 0
    while counter < 8:
        print()
        print(''.join(word))
        guess = input('Input a letter:')
        if len(guess) != 1:
            print('You should input a single letter')
            continue
        if not 'a' <= guess <= 'z':
            print('Please enter a lowercase English letter')
            continue
        if guess in attempts:
            print("You've already guessed this letter")
            continue
        if guess in answer:
            attempts.add(guess)
            for i, ele in enumerate(answer):
                if ele == guess:
                    word[i] = guess
        else:
            print("That letter doesn't appear in the word")
            counter += 1
            attempts.add(guess)
        if ''.join(word) == answer:
            print('''You guessed the word! 
                    You survived!''')
            break

    if ''.join(word) != answer:
        print('You lost!')

while True:
    user_choice = input('Type "play" to play the game, "exit" to quit:')
    if user_choice == 'play':
        game()
    else:
        break
