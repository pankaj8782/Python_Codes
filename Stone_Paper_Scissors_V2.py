import tkinter as tk
import random as r

computer_choice = None

def play_game(user_choice):
    global computer_choice
    
    if computer_choice is None:
        computer_choice = r.choice(["stone", "paper", "scissors"])

    if user_choice == computer_choice:
        result = "It's a draw!"
        root.config(bg="#ADD8E6")
    elif (user_choice == "stone" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "stone") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        result = "You Won! Congratulations!"
        root.config(bg="green")
    else:
        result = "You Lost! Better luck next time."
        root.config(bg="red")

    result_label.config(text=result)
    user_choice_label.config(text=f"You Chose: {user_choice.title()}")
    computer_choice_label.config(text=f"Computer Chose: {computer_choice.title()}")

def user_choice(choice):
    play_game(choice)

def create_button(frame, text, command):
    return tk.Button(frame, text=text, command=command, relief="flat", width=4, height=2, 
                     font=("Roboto", 50), bg="#f0f0f0", activebackground="#e0e0e0", bd=0)

def show_hint():
    if computer_choice:
        hint_label.config(text=f"Computer Chose: {computer_choice.title()}")
        hint_label.grid(row=5, column=0, columnspan=3, pady=10)
        root.after(1000, hide_hint)

def hide_hint():
    hint_label.grid_forget()

def restart_game():
    global computer_choice
    computer_choice = r.choice(["stone", "paper", "scissors"])
    result_label.config(text="")
    user_choice_label.config(text="You Chose: ")
    computer_choice_label.config(text="Computer Chose: ")
    root.config(bg="#ADD8E6")

stone_unicode = "🗿"
paper_unicode = "📜"
scissors_unicode = "✂️"
bulb_unicode = "💡"
restart_unicode = "🔄"

root = tk.Tk()
root.title("Stone Paper Scissors Game")
root.config(bg="#ADD8E6")

root.option_add("*Font", "Roboto 14")

frame = tk.Frame(root)
frame.pack(pady=20)

title_label = tk.Label(frame, text="Stone Paper Scissors Game", font=("Roboto", 20, "bold"))
title_label.grid(row=0, column=0, columnspan=3, pady=10)

user_choice_label = tk.Label(frame, text="You Chose: ", font=("Roboto", 14))
user_choice_label.grid(row=1, column=0, columnspan=3, pady=5)

computer_choice_label = tk.Label(frame, text="Computer Chose: ", font=("Roboto", 14))
computer_choice_label.grid(row=2, column=0, columnspan=3, pady=5)

result_label = tk.Label(frame, text="", font=("Roboto", 16, "bold"))
result_label.grid(row=3, column=0, columnspan=3, pady=10)

stone_button = create_button(frame, stone_unicode, lambda: user_choice("stone"))
stone_button.grid(row=4, column=0, padx=15)

paper_button = create_button(frame, paper_unicode, lambda: user_choice("paper"))
paper_button.grid(row=4, column=1, padx=15)

scissors_button = create_button(frame, scissors_unicode, lambda: user_choice("scissors"))
scissors_button.grid(row=4, column=2, padx=15)

def on_enter(event):
    event.widget.config(bg="#e0e0e0")

def on_leave(event):
    event.widget.config(bg="#f0f0f0")

stone_button.bind("<Enter>", on_enter)
stone_button.bind("<Leave>", on_leave)

paper_button.bind("<Enter>", on_enter)
paper_button.bind("<Leave>", on_leave)

scissors_button.bind("<Enter>", on_enter)
scissors_button.bind("<Leave>", on_leave)

hint_button = tk.Button(frame, text=bulb_unicode, command=show_hint, relief="flat", 
                        width=4, height=2, font=("Roboto", 20), bg="#f0f0f0", activebackground="#e0e0e0", bd=0)
hint_button.grid(row=0, column=2, padx=15, pady=5, sticky="ne")

restart_button = tk.Button(frame, text=restart_unicode, command=restart_game, relief="flat", 
                           width=4, height=2, font=("Roboto", 20), bg="#f0f0f0", activebackground="#e0e0e0", bd=0)
restart_button.grid(row=0, column=0, padx=15, pady=5, sticky="nw")

hint_label = tk.Label(frame, text="", font=("Roboto", 14), bg="#ADD8E6", fg="black")

computer_choice = r.choice(["stone", "paper", "scissors"])

root.mainloop()
