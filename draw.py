import turtle

speed = 0
lengthInitial = 150
lengthDiff = .8
angleInitial = 90
angleDiff = 15
branches = 7

def main():
    global pen
    pen = turtle.Pen()
    pen.reset()
    pen.speed(speed)
    pen.color('red')
    pen.up()
    pen.setpos((0, -250))
    pen.left(90)
    draw(0, lengthInitial, 1)

def draw(angle, length, branch):
    print('draw', angle, length, branch)
    if branch == branches:
        return

    pen.down()
    pen.right(angle)
    pen.forward(length)
    pen.up()

    heading = pen.heading()
    position = pen.position()

    branchWeight = (branches - branch) * 10

    branch += 1
    draw((1 - angleDiff) - branchWeight, length * lengthDiff, branch)
    pen.setheading(heading)
    pen.setpos(position)
    draw(angleDiff + branchWeight, length * lengthDiff, branch)

main()
