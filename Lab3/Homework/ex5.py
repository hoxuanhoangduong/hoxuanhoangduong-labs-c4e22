from turtle import *

def draw_star(x,y,length):#,color):
#     colormode()
#     pencolor(color)
    penup()
    setx(x)
    sety(y)
    pendown()
    for i in range(5):
        forward(length)
        right(144)
draw_star(20,250,100)
# draw_star(20,250,100,"blue")
mainloop()