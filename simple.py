import turtle
import random

fillcolors = [ "red", "green", "blue", "orange", "yellow", "purple", "white" ]

pen = turtle.Pen()
pen.shape("turtle")


pen.reset()
pen.speed(10);
pen.color("red")
for _ in range(8):
    pen.color("black", random.choice(fillcolors))
    pen.forward(400)
    pen.left(225)
