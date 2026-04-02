from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
root = Tk()
root.title("Rock, Paper, Scissors")
root.geometry("700x700")
root.config(bg="#fde8c5")
title = Label(root,font=("Comic Sans",20), text="Welcome!" ,fg="black",bg="white")
source = Image.open("bgimg.png")
source.resize((300,300))
img = ImageTk.PhotoImage(source)
bgimg = Label(root,image=img)
title.place(x=310,y=30)
bgimg.place(x=200,y=100)
root.mainloop()