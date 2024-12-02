import pyjokes as joke

yes_v = ['yes', 'affirmative', 'absolutely', 'sure', 'of course', 'certainly', 'definitely', 'yep', 'yea', 'yeah', 'aye', 'indeed', 'positive', 'agreed', 'right', 'you bet', 'totally', 'sure thing', 'no doubt', 'without a doubt', 'for sure', 'by all means', 'ok', '1']

no_va = ['no', 'nope', 'negative', 'certainly not', 'absolutely not', 'definitely not', 'not at all', "i don't think so", "i don't believe so", 'not really', 'nah', 'never', 'no way', 'by no means', "not on your life", 'not a chance', "nope, not gonna happen", "i can't", "i won't", "it's not happening", 'out of the question', 'under no circumstances', '0']

jokes = joke.get_joke()
print("")
print(jokes)

#feedback
f_i = input("Did you liked the joke: ")

if (f_i.lower() in yes_v):
    print("Thanks! You Are Sweet ❤")
elif(f_i.lower() in no_va):
    print("Sorry! a New joke only for you ")
    print(jokes)
    print("")
else:
    print("Enter Valid Input")