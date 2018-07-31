from turtle import *
speed(-1)
shape("turtle")
color("blue")

size = 200
left(130)

while size > 0:
    for i in range(4):
        forward(size)
        left(90)
    size -= 5
    right(10)    

mainloop()