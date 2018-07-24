from turtle import *

speed(-1)
shape("turtle")

for i in range(3, 7):
    if i == 3 or i == 5:
        color("blue")
        for a in range(i):
            forward(100)
            left(360/i)
    else:
        color("red")
        for b in range(i):
            forward(100)
            left(360/i)

mainloop()