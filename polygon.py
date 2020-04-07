import turtle
import random

fillcolors = [ "red", "green", "blue", "orange", "yellow", "purple" ]

screen = turtle.Screen()
screen.bgcolor("black")

pen = turtle.Pen()
pen.hideturtle()
pen.reset()
pen.speed(0);
pen.up()


def drawPolygon(sides, length):
    if (sides < 3):
        return

    pen.color("white", random.choice(fillcolors))

    pen.down();
    pen.begin_fill()
    for i in range(sides):
        pen.forward(length)
        pen.left(360 // sides);
    pen.end_fill()
    pen.up();


for i in range(1000):
    pen.goto(random.randint(-450, 400), random.randint(-450, 400))
    sides = random.randint(3, 12)
    length = random.randint(10, 75)

    if (sides != 7 and sides != 11):
        drawPolygon(sides, length)
