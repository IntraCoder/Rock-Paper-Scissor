from tkinter import *
from tkinter import messagebox as msg
from PIL import Image, ImageTk
import random


def intro():
    intro = Tk()
    intro.geometry("500x400")
    intro.title("Rock Paper Scissor")
    intro.resizable(width=False, height=False)
    intro.config(bg="yellow")

    def play():
        intro.destroy()
        game(name_var.get(), round_var.get())

    name_var = StringVar()
    round_var = IntVar()
    Entry(intro, textvariable=name_var, font="None 17").place(x=200, y=100)
    Entry(intro, textvariable=round_var, font="None 17", width=5).place(x=200, y=200)
    Label(intro, text="Name :", font="None 17", bg="yellow").place(x=100, y=100)
    Label(intro, text="Rounds :", font="None 17", bg="yellow").place(x=100, y=200)

    Button(intro, text="Play", font="None 17", bg="cyan", width=10, command=play).place(x=200, y=250)
    round_var.set(1)
    intro.mainloop()


def game(name, rounds):
    root = Tk()
    root.geometry('500x570')
    root.config(bg="#26006f")
    root.title("Rock Paper Scissor Game")

    paper = Image.open("paper (1).png")
    rock = Image.open("rock (1).png")
    scissor = Image.open("scissor (1).png")

    paper = ImageTk.PhotoImage(paper)
    rock = ImageTk.PhotoImage(rock)
    scissor = ImageTk.PhotoImage(scissor)

    def comp_play():
        global seq, comp
        seq = {rock: scissor, paper: rock, scissor: paper}
        comp = random.choice(tuple(seq.keys()))
        comp_hand["image"] = comp

    def show_img(image):
        global user, count

        user = image
        user_hand["image"] = image
        play()
        count += 1
        if count == rounds:
            if user_score > comp_score:
                msg.showinfo("Congrats!", f"{name} Won!")
            elif user_score < comp_score:
                msg.showinfo("Sorry!", "Computer Won!")
            else:
                msg.showinfo("Close!", "Draw!")
            root.destroy()
            intro()

    def play():
        global user, seq, comp, comp_score, user_score, no_result
        comp_play()
        if user == comp:
            no_result += 1
            draw_lab["text"] = f"Draws: {no_result}"
        elif user == seq[comp]:
            comp_score += 1
            comp_score_lab["text"] += comp_score
        else:
            user_score += 1
            user_score_lab["text"] += user_score

    global count, user_score, comp_score, no_result
    user_score, comp_score, count, no_result = 0, 0, 0, 0
    user_score_lab = Label(root, text=user_score, fg="white", bg="#26006f", font="None 29")
    comp_score_lab = Label(root, text=comp_score, fg="white", bg="#26006f", font="None 29")
    draw_lab = Label(root, text=f"Draws: {no_result}", font="None 25", fg="white", bg="#26006f")
    separate_lab = Label(root, text="------------------------------------------------------------------------",
                         font="None 18", fg="white", bg="#26006f")
    comp_hand = Label(root, bg="#26006f")
    user_hand = Label(root, bg="#26006f")

    draw_lab.place(x=10, y=2)
    comp_hand.place(x=190, y=10)
    user_hand.place(x=190, y=280)
    separate_lab.place(x=0, y=240)
    user_score_lab.place(x=10, y=340)
    comp_score_lab.place(x=10, y=110)

    rock_but = Button(root, text="Rock", font="None 17", fg="black", bg="yellow", command=lambda: show_img(rock))
    paper_but = Button(root, text="Paper", font="None 17", fg="black", bg="yellow", command=lambda: show_img(paper))
    scissor_but = Button(root, text="Scissor", font="None 17", fg="black", bg="yellow",
                         command=lambda: show_img(scissor))

    rock_but.place(x=120, y=520)
    paper_but.place(x=210, y=520)
    scissor_but.place(x=310, y=520)

    root.mainloop()


intro()
