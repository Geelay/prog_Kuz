import turtle
a=True
x=0
y=0
b=10
turtle.shape('turtle')
def fignya(g):       
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
    fignya(b)
    b+=20
    x-=10
    y-=10
    