from turtle import *

speed(-1)
shape("turtle")
color("red")

begin_fill()
for i in range(4):
    forward(100)
    left(90)
end_fill()

mainloop()