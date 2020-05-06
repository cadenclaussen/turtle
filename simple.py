import turtle

pen = turtle.Pen()
pen.shape("turtle")


pen.reset()
pen.speed(10);
pen.color("red")
for i in range(8):
    pen.forward(400)
    pen.left(225)
