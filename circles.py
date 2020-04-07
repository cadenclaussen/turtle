import turtle
import random


fillcolors = [ "red", "green", "blue", "orange", "yellow", "purple", "white" ]

screen = turtle.Screen()
screen.bgcolor("black")

pen = turtle.Pen()
pen.hideturtle()
pen.reset()
pen.speed(0);
pen.up()

for i in range(1000):
    pen.goto(random.randint(-375, 375), random.randint(-450, 300))
    pen.color("black", random.choice(fillcolors))

    pen.down()
    pen.begin_fill();
    radius = random.randint(10, 150)
    pen.circle(radius)
    pen.end_fill();
    pen.up()


    print('Radius       : ', radius)
    print('Area         : ', round(3.1415926 * (radius * radius)))
    print('Circumference: ', round(2 * 3.1415926 * radius))
    print();
