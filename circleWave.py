import turtle
import time
import random


t = turtle.Pen()
t.shape("turtle")
t.reset()
t.speed(0)
t.penup
t.color("Blue")
t.right(90)
t.forward(250)
t.left(90)
circle_size = 50
negative = False
t.pendown
for i in range (500):
    for circle_size in range (250):
        if negative == False:
            t.circle(circle_size)
            circle_size = circle_size + 5
        else:
            t.color("Red")
            circle_size = -50
            negative = True
            t.circle(circle_size)
            circle_size = circle_size - 5