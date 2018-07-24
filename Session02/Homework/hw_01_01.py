from turtle import *

speed(-1)
shape("turtle")
color("red")

left(60)

for i in range(4):
    forward(100)
    left(60)
    forward(100)
    left(120)
    forward(100)
    left(60)
    forward(100)
    left(30)

mainloop()