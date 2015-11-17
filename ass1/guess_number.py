"""
Write a program that generates a secret random number and asks the user to guess it.
It should count how many attempts were made before the number is guessed.
The program must also give hints to the user.
Example:
    python guess_a_number.py
    > Guess your number
    > 3
    > Wrong! Try with a larger one
    > 5
    > Wrong! Try with a smaller one
    > 4
    > You guessed correctly! The number was 4 indeed!
"""
from random import randint

def guess_a_number():
    answer = randint(1,100)
    guess = int(raw_input('Guess your number: '))
    while guess != answer:
        if guess > answer:
            print 'Wrong! Try a smaller one'
            guess = int(raw_input('Guess your number: '))
        elif guess < answer:
            print 'Wrong! Try a larger one'
            guess = int(raw_input('Guess your number: '))
    else:
        print 'You guessed correctly!. The number was {0} indeed'.format(guess)
