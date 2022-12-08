from turtle import *
def triangle(x):
    pensize(2)
    pencolor('black')
    for i in range(3):
        fd(x)
        right(120)

def main():
    speed(8)
    colors=['green','red','yellow','blue']
    for j in range(1,7):
        for i in range(4):
            if j >= 2:
                triangle(160 + j * 10)
                left(90)
            else:
                fillcolor(colors[i])
                begin_fill()
                triangle(160)
                left(90)
                end_fill()
    ht()
main()
done()
