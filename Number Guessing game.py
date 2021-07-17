import tkinter as tk
import random

window = tk.Tk()
window.geometry("600x400")
window.config(bg="#808080")
window.resizable(width=False, height=False)
window.title("Number Guessing Game")


Target = 1
Retries = 0

def updateResult(text):
    result.configure(text=text)

def new_game():
    guess_button.config(state="normal")
    global Target, Retries
    Target = random.randint(0, 10)
    Retries = 0
    updateResult(text="Guess a number between 1 to 10")


def play_game():
    global Retries

    choice = int(num_form.get())
    if choice != Target:
        Retries +=1
        result = "Wrong guess"

        if Target < choice:
             hint = "The num lies between 0 and {}".format(result)
        else:
            hint = "The num lies between {} and 10".format(choice)
        result += "\n\nHint:\n " +hint

    else:
        result = "Yay.....its crct after {} retries".format(Retries)
        guess_button.configure(state="disabled")
        result += "\n" + "Start new game"

    updateResult(result)

play_button = tk.Button(window, text="Play Game", font=("Arial", 10), fg="Black", bg="#29c70a", command=new_game)

guess_button = tk.Button(window, text="Guess", font=("Arial", 14), fg="White", bg="#b82741", command=play_game)


exit_button = tk.Button(window, text="Exit", font=("Arial", 14), fg="White", bg="#b82741", command=exit)
exit_button.place(x=340, y=320)

title = tk.Label(window, text="Guessing Number", font=("Arial", 24), fg="#fffcbd", bg="#808080")
result = tk.Label(window, text="click to play", font=("Arial", 14), fg="White", bg="#808080", justify=tk.LEFT)
title.place(x=170, y=50)
result.place(x=260, y=125)

guessed_num = tk.StringVar()
num_form = tk.Entry(window, font=("Arial", 11), textvariable=guessed_num)
num_form.place(x=225, y=290)

play_button.place(x=270, y=97)
guess_button.place(x=220, y=320)

window.mainloop()
