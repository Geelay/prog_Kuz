import turtle

x=0
l=1
turtle.shape('turtle')
turtle.speed(100)
turtle.right(90)
for i in range(10):
    
    for x in range(360):
        turtle.forward(l)
        turtle.left(1)
    for x in range(360):
        turtle.forward(l)
        turtle.right(1)
    l += 0.2