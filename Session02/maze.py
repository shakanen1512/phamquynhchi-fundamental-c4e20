from turtle import *

speed(-1)
shape("turtle")
color("red")

length = 5
for i in range(80):
    forward(length)
    left(90)
    length += 10

mainloop()