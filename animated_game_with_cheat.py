import random as r
import time as t
import sys

# Print animation function
def animated_print(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        t.sleep(delay)
    print()

# Computer choice animation
def animate_choice():
    choices = ["Rock", "Paper", "Scissors", "Shoot..."]
    for choice in choices:
        sys.stdout.write("\r" + choice)  
        sys.stdout.flush()
        t.sleep(0.2)
    print()  

# Main logic for the game
def play_game():
    computer = r.choice([3, 1, 2]) 

    main = {1: "stone", 2: "paper", 3: "scissors"}
    you_main = {"stone": 1, "paper": 2, "scissors": 3}

    print()
    animated_print("Computer's Turn...")
    t.sleep(1)
    animate_choice()

    # user
    animated_print("Now your Turn...")
    t.sleep(0.5)

    you = input("Choose from(stone, paper, scissors): ").lower()

    computer_choice = main[computer]
    cp = you_main[main[computer]]

    your_choice = main[you_main[you]]
    yp = you_main[you]

    animated_print(f"\nYou Chose: {your_choice.title()}")
    t.sleep(0.5)
    animated_print(f"Computer Chose: {computer_choice.title()}")
    print()

    # result
    t.sleep(0.5)
    if yp == cp:
        animated_print("It's a draw!")
    elif (yp == 1 and cp == 3) or (yp == 2 and cp == 1) or (yp == 3 and cp == 2):
        animated_print("You Won! Congratulations!")
    else:
        animated_print("You Lost! Better luck next time")
    print()

# retry
def game_loop():
    play_game() 
    
    retry = input("Another turn?(yes,no): ").lower()
    while retry == "yes":
        play_game() 
        retry = input("Another turn?(yes,no): ").lower()

    print("Goodbye! Well Played")

game_loop()