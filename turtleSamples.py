import turtle
import random


pen = turtle.Pen()
colors = [ "red", "green", "blue", "orange", "black" ]


pen.reset()
pen.speed(0);
for i in range(8):
    pen.goto(random.randint(0, 200), random.randint(0, 200))
    pen.down()
    pen.color(random.choice(colors), random.choice(colors))
    pen.circle(random.randint(30, 150), 360)
    pen.up()
