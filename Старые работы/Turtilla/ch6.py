import turtle
a=True
b=1
print('Enter the number of legs')
x=int(input())
y=360/x
turtle.shape('turtle')
for i in range (x):
    turtle.forward(100)
    turtle.stamp()  
    turtle.backward(100)   
    turtle.left(y)

    
