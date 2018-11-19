import turtle
turtle.speed(1000)
x=0
turtle.shape('turtle')
for i in range (3):
    for x in range(360):
        turtle.forward(1)
        turtle.left(1)
    for x in range(360):
        turtle.forward(1)
        turtle.right(1)
    turtle.left(60)