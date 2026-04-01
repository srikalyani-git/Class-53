from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
root = Tk()
root.title("Denomination Calculator")
root.geometry("1000x700")
root.config(bg="blue")
source = Image.open("img.jpg")
source = source.resize((400,400))
img = ImageTk.PhotoImage(source)
pic = Label(root,image=img)
pic.place(x=300,y=100)
welc = Label(root,text="Welcome to the Denomination Calculator!",bg="black",fg="white")
welc.place(x=400,y=550)

def topwin():
    win = Toplevel()
    win.title("Notes calculator")
    win.geometry("500x700")
    win.config(bg="grey")
    Title = Label(win,text="Enter Amount", font=("Arial",30), fg="black",bg="grey")
    input = Entry(win)
    l500 = Label(win,text="Rs.500:")
    en500 = Entry(win)
    l200 = Label(win,text="Rs.200:")
    en200 = Entry(win)
    l100 = Label(win,text="Rs.100:")
    en100 = Entry(win)
    l50 = Label(win,text="Rs.50:")
    en50 = Entry(win)
    l10 = Label(win,text="Rs.10:")
    en10 = Entry(win)
    l5 = Label(win,text="Rs.5:")
    en5 = Entry(win)
    l1 = Label(win,text="Rs.1:")
    en1 = Entry(win)
    
    def calculator():
        global amount
        amount = int(input.get())
        n500 = amount//500
        amount%= 500
        n200 = amount//200
        amount%= 200
        n100 = amount//100
        amount%= 100
        n50 = amount//50
        amount%= 50
        n10 = amount//10
        amount%= 10
        n5 = amount//5
        amount%= 5
        n1 = amount

        en500.delete(0,END)
        en200.delete(0,END)
        en100.delete(0,END)
        en50.delete(0,END)
        en10.delete(0,END)
        en5.delete(0,END)
        en1.delete(0,END)

        en500.insert(END,str(n500))
        en200.insert(END,str(n200))
        en100.insert(END,str(n100))
        en50.insert(END,str(n50))
        en10.insert(END,str(n10))
        en5.insert(END,str(n50))
        en1.insert(END,str(n1))
    button = Button(win, command=calculator, text="Calculate",fg="white",bg="black")

    l500.place(x=200,y=50)
    l200.place(x=200,y=200)
    l100.place(x=200,y=230)
    l50.place(x=200,y=260)
    l10.place(x=200,y=290)
    l5.place(x=200,y=320)
    l1.place(x=200,y=350)

    input.place(x=200,y=80)
    en500.place(x=200,y=50)
    en200.place(x=200,y=200)
    en100.place(x=200,y=230)
    en50.place(x=200,y=260)
    en10.place(x=200,y=290)
    en5.place(x=200,y=320)
    en1.place(x=200,y=350)

    button.place(x=240,y=120)

def info():
    msg = messagebox.showinfo("Alert","Do you want to calculate the notes?")
    if msg == "ok":
        topwin()

button = Button(root,text="Let's get started!",command=info,bg="yellow",fg="Black")
button.place(x=455,y=600)
root.mainloop()
