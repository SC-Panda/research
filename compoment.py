import turtle
t = turtle.Pen()

def draw_star(x, y, size):
    turtle.color("white", "#C8102E")
    turtle.pensize(5)
    turtle.begin_fill()
    turtle.penup()
    turtle.goto(x, y)
    for i in range(5):
        turtle.forward(size)
        turtle.right(180 - 180 / 5)
    turtle.end_fill()

def draw_yingyang(x, y, n):
    # 画大圆
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("black")
    t.begin_fill()
    t.circle(175*n, -180)
    t.circle(350*n, -180)
    t.end_fill()

    t.fillcolor("white")
    t.begin_fill()
    t.circle(175*n, 180)
    t.end_fill()
    t.circle(-175*n, 180)
    t.circle(-350*n, -180)

    # 画小圆  半圆半径的一半为小圆半径
    t.up()
    t.circle(-43.75*n, -180)
    t.down()
    t.fillcolor("black")
    t.begin_fill()
    t.circle(87.5*n)
    t.end_fill()
    t.up()
    t.circle(175*n, 180)
    t.down()
    t.fillcolor('white')
    t.begin_fill()
    t.circle(-87.5*n)
    t.end_fill()
