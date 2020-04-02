import turtle
import random

pen = turtle.Pen()
pen.shape("turtle")
pen.color("green")

def drawPolygon(sides, length):
    if (sides < 3):
        return

    for i in range(sides):
        pen.forward(length)
        pen.left(360 // sides);

drawPolygon(3, 100)
drawPolygon(4, 100)
drawPolygon(5, 100)
drawPolygon(6, 100)
drawPolygon(7, 100)
drawPolygon(8, 100)
drawPolygon(9, 100)
drawPolygon(10, 100)
input('Hit a key...')
