n = int(input("How many circles? "))
angle = 360/n

from turtle import *

speed(-1)
shape("turtle")
color("red")

for i in range(n):
    circle(50)
    left(angle)

mainloop()