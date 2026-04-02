import random

print("Welcome to Rock, Paper Scissors !!")
print("----------------------------------------------------------------")
inp = input("Your choice (r,p,s):")
op = ("r","p","s")
com = random.choice(op)
win = "You won computer chose:"
loss = "You loose computer chose:"
draw = "You draw computer also chose:"
if inp=="r" and com=="r":
    print(draw,com)
elif inp=="p" and com=="p":
    print(draw,com)
elif inp=="s" and com=="s":
    print(draw,com)
elif inp=="r" and com=="p":
    print(loss,com)
elif inp=="p" and com=="s":
    print(loss,com)
elif inp=="s" and com=="r":
    print(loss,com)
elif inp=="r" and com=="s":
    print(win,com)
elif inp=="p" and com=="r":
    print(win,com)
elif inp=="s" and com=="p":
    print(win,com)
else:
    print("Wrong input")