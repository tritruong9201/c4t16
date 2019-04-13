n=int(input())
from turtle import *

shape("turtle")
shapesize(1.2)
speed(-1)
pencolor("green")
fillcolor("red")
for j in range(3,n+1):
    for i in range(j):
        forward(50)
        left(360/j) 

mainloop()
