import turtle
import random
import time


fgcolors = [ "red", "green", "blue", "orange", "yellow", "purple", "black" ]
fillcolors = [ "red", "green", "blue", "orange", "yellow", "purple", "white" ]

screen = turtle.Screen()
screen.bgcolor("black")

pen = turtle.Pen()
pen.reset()
pen.hideturtle()
pen.speed(0);
pen.up()

for i in range(1000):

    pen.color("black", random.choice(fillcolors))
    # pen.width(random.randint(1, 3))
    x = random.randint(-450, 350)
    y = random.randint(-450, 350)
    length = random.randint(10, 300)
    height = random.randint(10, 300)

    pen.goto(x, y)

    pen.down()
    pen.begin_fill()
    pen.goto(x, y + height)
    pen.goto(x + length, y + height)
    pen.goto(x + length, y)
    pen.goto(x, y)
    pen.end_fill()
    pen.up()

    print('Length & Height: ', length, height)
    print('Perimeter: ', length * 2 + height * 2)
    print('Area     : ', length * height)
    print();
