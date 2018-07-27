from turtle import *

speed(-1)
shape("turtle")
list_colors = ["red", "blue", "brown", "yellow", "grey"]

for i in range(3, 8):
    color(list_colors[i-3])
    for a in range(i):
        forward(100)
        left(360/i)

mainloop()