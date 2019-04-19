n=int(input("So vong lap: "))
from turtle import *
shape("turtle")
speed(-1)
color("red")
bgcolor("black")
pencolor("green")
pensize(2)

for i in range(1,n+1):
    forward(50)
    left(360/n)

ht()
mainloop()