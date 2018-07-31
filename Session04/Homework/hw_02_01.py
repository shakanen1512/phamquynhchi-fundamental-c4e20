from turtle import *
speed(-1)
shape("turtle")
color("blue")

for k in range(6):
    for j in range(4):
        for i in range(4):
            forward(100)
            left(90)
        left(90)
    left(15)

mainloop()