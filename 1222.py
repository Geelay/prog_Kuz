import turtle
a=True
x=0
turtle.shape('turtle')
while a:
    
    for x in range(360):
        turtle.forward(1)
        turtle.left(1)
    for x in range(360):
        turtle.forward(1)
        turtle.right(1)
    turtle.left(60)