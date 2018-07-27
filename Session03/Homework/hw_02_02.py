from turtle import *

speed(-1)
shape("turtle")
list_colors = ["red", "blue", "brown", "yellow", "grey"]

for i in range(len(list_colors)):
    begin_fill()
    color(list_colors[i])
    for a in range(4):
        forward(50)
        left(90)
    end_fill()
    forward(50)

mainloop()