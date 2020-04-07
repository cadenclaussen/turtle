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

screen = turtle.Screen()
screen.bgcolor("black")

for i in range(1000):

    pen.color(random.choice(fgcolors))
    pen.down()
    x = random.randint(-450, 450)
    y = random.randint(-450, 450)
    pen.goto(x, y)
    pen.up()
