from turtle import *
def triangle():
    pensize(2)
    pencolor('black')
    for i in range(3):
        fd(60)
        right(120)

def main():
    colors=['green', 'red', 'yellow', 'pink', 'purple', 'orange']
    speed(7)
    for i in range(6):
        begin_fill()
        fillcolor(colors[i])
        triangle()
        fd(60)
        left(60)
        end_fill()
    fillcolor("blue")
    begin_fill()
    for i in range(6):
        fd(60)
        left(60)
    end_fill()
    ht()
main()
done()
