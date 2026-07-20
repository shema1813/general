import tkinter as tk
import random

choices = ["Rock", "Paper", "Scissor"]

user_score = 0
computer_score = 0

def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(choices)

    result = ""

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissor") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissor" and computer_choice == "Paper")
    ):
        result = "You Win!"
        user_score += 1
    else:
        result = "Computer Wins!"
        computer_score += 1

    lbl_computer.config(text=f"Computer: {computer_choice}")
    lbl_result.config(text=result)
    lbl_score.config(text=f"Score - You: {user_score}  Computer: {computer_score}")

def reset():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    lbl_computer.config(text="Computer: ?")
    lbl_result.config(text="")
    lbl_score.config(text="Score - You: 0  Computer: 0")

root = tk.Tk()
root.title("Rock Paper Scissor")
root.geometry("400x350")
root.resizable(False, False)

title = tk.Label(root, text="Rock Paper Scissor Game",
                 font=("Arial", 18, "bold"))
title.pack(pady=10)

tk.Label(root, text="Choose your move:",
         font=("Arial", 12)).pack()

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Button(frame, text="Rock", width=10,
          command=lambda: play("Rock")).grid(row=0, column=0, padx=5)

tk.Button(frame, text="Paper", width=10,
          command=lambda: play("Paper")).grid(row=0, column=1, padx=5)

tk.Button(frame, text="Scissor", width=10,
          command=lambda: play("Scissor")).grid(row=0, column=2, padx=5)

lbl_computer = tk.Label(root, text="Computer: ?",
                        font=("Arial", 12))
lbl_computer.pack(pady=10)

lbl_result = tk.Label(root, text="",
                      font=("Arial", 14, "bold"),
                      fg="blue")
lbl_result.pack()

lbl_score = tk.Label(root,
                     text="Score - You: 0  Computer: 0",
                     font=("Arial", 12))
lbl_score.pack(pady=10)

tk.Button(root, text="Reset", command=reset,
          bg="orange").pack(pady=5)

tk.Button(root, text="Exit", command=root.destroy,
          bg="red", fg="white").pack()

root.mainloop()
