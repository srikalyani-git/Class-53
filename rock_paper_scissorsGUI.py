from tkinter import *
from PIL import ImageTk,Image
import random
root = Tk()
root.title("Rock, Paper, Scissors")
root.geometry("700x550")
root.config(bg="#1A255F")
title = Label(root,font=("Franklin Gothic Medium",30), text="Welcome!" ,fg="#FFEFCC",bg="#3E83A8",width=10)
source = Image.open("bgimg.png")
source = source.resize((300,300))
img = ImageTk.PhotoImage(source)
bgimg = Label(root,image=img)
title.place(x=246,y=30)
bgimg.place(x=200,y=110)

def check_result(player_choice):
    op = ("r","p","s")
    global com
    com = random.choice(op)
    if player_choice=="r" and com=="r" or player_choice=="p" and com=="p" or player_choice=="s" and com=="s":
        draw()
    elif player_choice=="r" and com=="p" or player_choice=="p" and com=="s" or player_choice=="s" and com=="r":
        loss()
    elif player_choice=="r" and com=="s" or player_choice=="p" and com=="r" or player_choice=="s" and com=="p":
        winning()

rocki = Image.open("rock.png")
rocki = rocki.resize((200,200))
rocki = ImageTk.PhotoImage(rocki)
paperi = Image.open("paper.png")
paperi = paperi.resize((200,200))
paperi = ImageTk.PhotoImage(paperi)
scissori = Image.open("scissor.png")
scissori = scissori.resize((200,200))
scissori = ImageTk.PhotoImage(scissori)

def play():
    global win
    win = Toplevel(root)
    win.title("Playing screen")
    win.geometry("1000x500")
    win.config(bg="#B9D1F0")
    wlabel = Label(win, text="Choose:", font=("Franklin Gothic Medium",50), bg="#E2B354", fg="#3A4A68")
    rock = Button(win,image=rocki,command = lambda: check_result("r"))
    paper = Button(win,image=paperi,command = lambda: check_result("p"))
    scissor = Button(win,image=scissori,command = lambda: check_result("s"))
    wlabel.place(x=380,y=30)
    rock.place(x=100,y=200)
    paper.place(x=420,y=200)
    scissor.place(x=740,y=200)

def winning():
    global win
    won = Toplevel()
    won.title("You won!")
    won.geometry("500x70")
    won.config(bg="#b1ff01")
    wintext = Label(won,text=f"Congrats you won! Computer chose:{com}",font=("Franklin Gothic Medium",20),fg="Black")
    wintext.place(x=20,y=20)
    if win.winfo_exists():
        win.destroy()

def loss():
    loose = Toplevel()
    loose.title("You lost...")
    loose.geometry("500x70")
    loose.config(bg="#ff685d")
    losstext = Label(loose,text=f"Oh no,you've lost, computer chose:{com}",font=("Franklin Gothic Medium",20),fg="Black")
    losstext.place(x=20,y=20)
    if win.winfo_exists():
        win.destroy()

def draw():
    drawwin = Toplevel()
    drawwin.title("You drawed")
    drawwin.geometry("500x70")
    drawwin.config(bg="#faff04")
    drawtext = Label(drawwin,text=f"You've drawed, computer chose:{com}",font=("Franklin Gothic Medium",20),fg="Black")
    drawtext.place(x=20,y=20)
    if win.winfo_exists():
        win.destroy()

button = Button(root,text="Let's get started",bg="#62C4C3",relief="raised",fg="#3D4B58",font=("Franklin Gothic Medium",16),command=play)
button.place(x=275,y=440)

root.mainloop()