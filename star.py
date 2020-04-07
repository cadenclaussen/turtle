import turtle 
import random
import time

pen = turtle.Pen()
pen.shape("turtle")
pen.speed(0)

screen = turtle.Screen()
screen.bgcolor("black") 

fill_colors = ["red", "green", "blue", "yellow", "purple"]

def drawStar(length):
    pen.penup()
    pen.color(random.choice(fill_colors))

    pen.goto(random.randint(-300, 300), random.randint(-300, 300))

    # Draw the first triangle
    # Begins at the bottom left, draw pyramid
    pen.pendown()
    for _ in range(3):
        pen.forward(length)
        pen.left(120)

    # Move to the position to draw the second triangle
    # Second triangle is and upside down pyramid, that
    # starts at the upper right.
    pen.penup()
    pen.forward(length)    
    pen.left(90)
    pen.forward(length/2)
    pen.left(90)

    # Draw the second triangle
    pen.pendown()
    for _ in range(3):
        pen.forward(length)
        pen.left(120)

for _ in range (1000):
    drawStar(random.randint(15, 150))
