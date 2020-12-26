from tkinter import *
from tkinter import messagebox as msg
import random

root = Tk()
root.geometry('500x400')
paper = PhotoImage(file="paper.png")
rock = PhotoImage(file="stone.png")
scissor = PhotoImage(file="scissor.png")


def comp_play():
    global seq, comp
    seq = {rock: scissor, paper: rock, scissor: paper}
    comp = random.choice(tuple(seq.keys()))
    comp_lab = Label(root, image=comp)
    comp_lab.place(x=190, y=0)


def show_img(image):
    global user
    user = image
    user_lab = Label(root, image=image)
    user_lab.place(x=190, y=180)
    play()


def play():
    global user, seq, comp
    comp_play()
    if user == comp:
        msg.showinfo("Draw", "Same!")
    elif user == seq[comp]:
        comp_score_lab["text"]+=1
        msg.showinfo("Lost!", "Comp won!")
    else:
        user_score_lab["text"]+=1
        msg.showinfo("Won!", "You won!")

user_score, comp_score = 0, 0
user_score_lab = Label(root, text=user_score, font="None 18")
comp_score_lab = Label(root, text=comp_score, font="None 18")
user_score_lab.place(x=10, y=100)
comp_score_lab.place(x=10, y=130)

rock_but = Button(root, text="Rock", font="None 17", command=lambda: show_img(rock))
paper_but = Button(root, text="Paper", font="None 17", command=lambda: show_img(paper))
scissor_but = Button(root, text="Scissor", font="None 17", command=lambda: show_img(scissor))

rock_but.place(x=120, y=350)
paper_but.place(x=210, y=350)
scissor_but.place(x=310, y=350)

root.mainloop()
