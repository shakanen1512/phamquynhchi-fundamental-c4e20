n = int(input("Polygon? "))
angle = 360/n

from turtle import *

speed(-1)
shape("turtle")
color("red")

for i in range(n):
    forward(100)
    left(angle)

mainloop()