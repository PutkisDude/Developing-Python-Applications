#Author Lauri Putkonen
#Video of the game: https://youtu.be/RJaPppaSP_4
#Audio is free from mixkit.co

#kids math game (add prize: pic, sound or something else (negative/positive))
#Two numbers are shown on labels
#User adds the sum to a textbox
#With a button sum is checked
#Then new values are generated to labels
#Right and wrong answers are shown

from tkinter import *
from tkinter import messagebox
import random
import pygame

pygame.mixer.init()
loseSound = pygame.mixer.Sound("lose.wav")
winSound = pygame.mixer.Sound("winwin.wav")

answered = ""
num1 = 0
num2 = 0
correct_answers = 0
wrong_answers = 0

def win():
    global correct_answers
    correct_answers += 1
    winSound.play(0)
    messagebox.showinfo("Good job", "{} is correct.\n\nYou have {} correct and {} wrong answers.".format(correct, correct_answers, wrong_answers))

def lose():
    global wrong_answers
    wrong_answers += 1
    loseSound.play(0)
    messagebox.showinfo("Nice try.", "{} is wrong.\nCorrect answer was {}.\n\nYou have {} correct and {} wrong answers.".format(answered, correct, correct_answers, wrong_answers))

def reset():
    roll()
    label_num1.configure(text=num1)
    label_num2.configure(text=num2)
    
def roll():
    global num1, num2, correct
    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)
    correct = num1 + num2

def submit():
    global answered
    answered = answer.get()
    answered = int(answered)
    if int(answered) == int(correct):
        win()
    else:
        lose()
    reset()

roll()

window = Tk()
window.title("Math Game")
window.geometry("300x150")
window.configure(bg="#7fb579")
window.resizable(False, False)
# window.eval("tk::PlaceWindow . center") # opens in middle of screen but doesn't work with my dual monitor setup on linux

label_text = Label(window, text="What is the correct answer?", pady=10, bg="#7fb579")
label_text.pack()


container = Frame(window, background="#7fb579")

label_num1 = Label(window, text=num1, bg="#7fb579")
label_plus_sign = Label(window, text="+", bg="#7fb579")
label_num2 = Label(window, text=num2, bg="#7fb579")

label_num1.pack(in_=container, side="left")
label_plus_sign.pack(in_=container, side="left")
label_num2.pack(in_=container, side="left")


container.pack()

answer = Entry(window, justify="center")
answer.pack()


button_answer = Button(window, padx=80, pady=15, text="Answer", bg="#a5b8a3", command=submit)


button_answer.pack()

window.mainloop()
