n=int(input("So vong lap: "))
from turtle import *
shape("turtle")
speed(-1)
color("red")
bgcolor("black")
pencolor("green")
pensize(2)
begin_fill()
for j in range(3,n+1):
    for i in range (j):
        forward(75)
        left(360/j)
color("yellow")
end_fill()
ht()
mainloop()