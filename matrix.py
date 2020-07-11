import turtle
import random
import time


fgcolors = [ "red", "green", "blue", "orange", "yellow", "purple" ]
fillcolors = [ "red", "green", "blue", "orange", "yellow", "purple", "white" ]


screen = turtle.Screen()
pen = turtle.Pen()


def main():
    global screen, pen
    screen.bgcolor("black")
    pen.reset()
    pen.hideturtle()
    pen.speed(0);
    pen.up()

    for pattern in range(2):

        if pattern == 0:
            twinkleOnRandom(2, 10)
            continue

        if pattern == 1:
            twinkle(20)
            continue


def twinkle(number):
    # setAllOff()
    for i in range(number):

        row = random.randint(0, 16)
        column = random.randint(0, 16)
        set(row, column, random.choice(fgcolors))
        setOff(row, column)


def twinkleOnRandom(number, count):
    # setAllOff()


    # Do some "number" of "twinkle sets"
    for i in range(number):

        pixels = []

        # Each "twinkle set" will turn on "count" pixels
        for i in range(count):

            row = random.randint(0, 16)
            column = random.randint(0, 16)
            set(row, column, random.choice(fgcolors))

            pixels.append([ row, column])


        # Delay for a second before turning them all off
        time.sleep(1)


        for pixel in pixels:
            print(pixel)
            row = pixel[0]
            column = pixel[1]
            setOff(row, column)


def set(row, column, color):
    global screen, pen
    side = 30
    x = (column * side) - 300
    y = (row * -(side)) + 300
    pen.color(color)
    pen.goto(x, y)
    pen.down()
    pen.begin_fill()
    pen.goto(x, y + side)
    pen.goto(x + side, y + side)
    pen.goto(x + side, y)
    pen.goto(x, y)
    pen.end_fill()
    pen.up()


def setAllOff():
    for row in range(16):
        for column in range(16):
            setOff(row, column)


def setOff(row, column):
    set(row, column, "black")


main()
