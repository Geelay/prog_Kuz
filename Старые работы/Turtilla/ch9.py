import turtle
a=True
b=1
io=50
o=18
x=0
y=0
k=0
t=3
l=360//t
turtle.shape('turtle')
for i in range (10):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    for k in range(t):
            turtle.left(360-l)
            turtle.forward(io)
    t+=1
    l=360/t
    y+=o
    x+=10
    io+=20
    o+=7