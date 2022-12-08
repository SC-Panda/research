import turtle
from compoment import *

t = turtle.Pen()
t.hideturtle()
t.speed(50)

def draw_pattren():
    draw_yingyang(100, 200, 0.2)
    draw_yingyang(-100, 200, 0.2)
    draw_yingyang(100, -200, 0.2)
    draw_yingyang(-100, -200, 0.2)
    
draw_pattren()
turtle.exitonclick()