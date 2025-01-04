import random
'''
1 = Stone
2 = Paper
3 = Scissors
'''
computer = random.choice([3,1,2])
# print(computer) ✅
you = input(" \nYour Turn: ").lower() #✅
main = {1: "stone",2:"paper",3:"scissors"} #✅
you_main = {"stone":1,"paper":2,"scissors":3} #✅

computer_choice = main[computer] #✅ FOR PRINT USE THIS
cp =  you_main[main[computer]] #✅

your_choice = main[you_main[you]] #✅ FOR PRINT USE THIS
yp = you_main[you] #✅
print("")

if yp == cp:
    print(f"You Chose {your_choice.title()} & Computer Chose {computer_choice.title()}\nIts a draw!")
elif (yp == 1 and cp == 3) or (yp == 2 and cp == 1) or (yp == 3 and cp == 2):
    print(f"You Chose {your_choice.title()} & Computer Chose {computer_choice.title()}\nHence! You Won, Congratulations!")
else:
    print(f"You Chose {your_choice.title()} & Computer Chose {computer_choice.title()}\nHence! You Lost, Better luck next time!")

print("")