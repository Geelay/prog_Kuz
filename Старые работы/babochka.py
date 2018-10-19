import turtle
a=True
x=0
l=1
turtle.shape('turtle')
turtle.right(90)
while a:
    
    for x in range(360):
        turtle.forward(l)
        turtle.left(1)
    for x in range(360):
        turtle.forward(l)
        turtle.right(1)
    l+=0.2