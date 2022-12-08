import turtle

def china():
    turtle.hideturtle()
    turtle.speed(10)
    turtle.title("Chinese National Flag.")
    n = 2
    # 旗面
    turtle.penup()
    turtle.goto(-150 * n, 100 * n)
    turtle.pendown()
    turtle.pencolor("red")
    turtle.begin_fill()
    turtle.fillcolor("red")
    turtle.fd(300 * n)
    turtle.right(90)
    turtle.fd(200 * n)
    turtle.right(90)
    turtle.fd(300 * n)
    turtle.right(90)
    turtle.fd(200 * n)
    turtle.end_fill()

    # 大星星
    turtle.penup()
    turtle.goto(-100 * n, 80 * n)
    turtle.pendown()
    turtle.pencolor("yellow")
    turtle.begin_fill()
    turtle.fillcolor("yellow")
    turtle.setheading(-72)
    for i in range(5):
        turtle.fd(57.06 * n)
        turtle.right(144)
    turtle.end_fill()

    # 小星星1
    turtle.penup()
    turtle.goto(-60 * n, 70 * n)
    turtle.pendown()
    turtle.pencolor("yellow")
    turtle.begin_fill()
    turtle.fillcolor("yellow")
    turtle.setheading(70)
    for i in range(5):
        turtle.fd(19.02 * n)
        turtle.right(144)
    turtle.end_fill()

    # 小星星2
    turtle.penup()
    turtle.goto(-40 * n, 63 * n)
    turtle.pendown()
    turtle.pencolor("yellow")
    turtle.begin_fill()
    turtle.fillcolor("yellow")
    turtle.setheading(10)
    for i in range(5):
        turtle.fd(19.02 * n)
        turtle.right(144)
    turtle.end_fill()

    # 小星星3
    turtle.penup()
    turtle.goto(-36 * n, 25 * n)
    turtle.pendown()
    turtle.pencolor("yellow")
    turtle.begin_fill()
    turtle.fillcolor("yellow")
    turtle.setheading(70)
    for i in range(5):
        turtle.fd(19.02 * n)
        turtle.right(144)
    turtle.end_fill()

    # 小星星4
    turtle.penup()
    turtle.goto(-60 * n, 20 * n)
    turtle.pendown()
    turtle.pencolor("yellow")
    turtle.begin_fill()
    turtle.fillcolor("yellow")
    turtle.setheading(-20)
    for i in range(5):
        turtle.fd(19.02 * n)
        turtle.right(144)
    turtle.end_fill()

    turtle.done()

china()
