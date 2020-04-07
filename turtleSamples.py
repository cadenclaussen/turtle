import turtle
import random

pen = turtle.Pen()
pen.shape("turtle")


colors = [ "red", "green", "blue", "orange", "black" ]


pen.reset()
pen.speed(10);
pen.color(random.choice(colors))
for i in range(8):
    pen.forward(400)
    pen.left(225)


pen.reset()
pen.speed(0)
pen.color(random.choice(colors))
for i in range(50):
    pen.forward(i * 2)
    pen.circle(i * 2, 90)
    pen.right(20)



pen.reset()
pen.speed(10)
pen.color(random.choice(colors))
for i in range(50):
    pen.forward(i * 10)
    pen.left(90)



pen.reset()
pen.speed(15)
pen.color(random.choice(colors))
for i in range(500):
    pen.forward(i * 1.25)
    pen.left(70)



pen.reset()
pen.speed(15)
pen.color(random.choice(colors))
for i in range(400):
    pen.circle(i + 10 * 1.1, 360)
    pen.left(30)


pen.reset()
pen.speed(15)
pen.color(random.choice(colors))
for i in range(300):
    pen.circle(i + 10 * 1.2, 360)
    pen.left(i + (i * 2) + 30)


pen.reset()
pen.speed(15)
pen.color(random.choice(colors))
for i in range(300):
    pen.circle((i * 1.5) + 10, 360)
    pen.left((i * 2) + 30)
    pen.forward(30)


pen.reset()
pen.speed(0)
pen.color(random.choice(colors))
sides = 6
length = 200
movement = 8
loops = 360 // movement
for i in range(loops):
    pen.left(movement)
    for side in range(sides):
        pen.forward(length)
        pen.left(360 / sides)



pen.reset()
pen.speed(0)
pen.color(random.choice(colors))
sides = 6
length = 10
movement = 1
loops = 100 // movement
for i in range(loops):
    pen.left(8)
    length = length * 1.02
    movement = movement * 1.1
    for side in range(sides):
        pen.forward(length)
        pen.left(360 / sides)
