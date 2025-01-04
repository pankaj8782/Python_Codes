from random import randint as r
computer = r(1,50) 

you = int(input(" \nSilly Game! Guess any number (1,50): "))
guess = 1
while(you!=computer):
    if(you>computer):
        print("Enter Smaller")          
    elif(you<computer):
        print('Guess Higher')  
    you = int(input("Try again: "))  # Asking for New Game
    guess += 1  
print(f'You guessed the number {you} in {guess} attempts')
