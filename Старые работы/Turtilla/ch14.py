import turtle
a=True
x=0
print('Enter number of angles')
l=int(input())
b=180 + 180/l
turtle.shape('turtle')
for x in range(l):
    turtle.left(b)
    turtle.forward(300)
turtle.penup()
turtle.forward(1000)