import turtle
import random
import time


fgcolors = [ "red", "green", "blue", "orange", "yellow", "purple", "white" ]

screen = turtle.Screen()
screen.bgcolor("black")

pen = turtle.Pen()
pen.reset()
pen.hideturtle()
pen.speed(0);
pen.up()


for i in range(1000):

    pen.reset()
    pen.speed(0);

    x1 = random.randint(-300, 300)
    y1 = random.randint(-300, 300)

    for j in range(50):

        # go to the origin
        pen.up()
        pen.goto(x1, y1)

        # draw a line from the origin x1, y1 to x2, y2
        pen.color(random.choice(fgcolors))
        # pen.width(random.randint(1, 3))
        pen.down()
        x2 = random.randint(x1 - 250, x1 + 250)
        y2 = random.randint(y1 - 250, y1 + 250)
        pen.goto(x2, y2)
        pen.up()
