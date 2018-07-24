from turtle import *

speed(-1)
shape("turtle")
color("red")

begin_fill()
for i in range(3):
    forward(100)
    left(120)
end_fill()

mainloop()