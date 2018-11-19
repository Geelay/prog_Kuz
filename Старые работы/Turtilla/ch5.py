import turtle
x=0
y=0
b=10
turtle.shape('turtle')
def sqr(g):       
        turtle.forward(g)
        turtle.left(90)
        turtle.forward(g)
        turtle.left(90)
        turtle.forward(g)
        turtle.left(90)
        turtle.forward(g)
        turtle.left(90)
for _ in range(10):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    sqr(b)
    b+=20
    x-=10
    y-=10
    