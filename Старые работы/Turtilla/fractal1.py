import turtle
ltl = 3
x = 0
turtle.shape('turtle')
turtle.speed(1000)

def lr1(lt):
    turtle.forward(lt)
    turtle.left(60)
    turtle.forward(lt)    
    turtle.right(120)
    turtle.forward(lt)   
    turtle.left(60) 
    turtle.forward(lt) 
    
def lr2(lt):
    lr1(lt)
    turtle.left(60)
    lr1(lt)    
    turtle.right(120)
    lr1(lt)   
    turtle.left(60) 
    lr1(lt)
    
def lr3(lt):
    lr2(lt)
    turtle.left(60)
    lr2(lt)    
    turtle.right(120)
    lr2(lt)   
    turtle.left(60) 
    lr2(lt)
    
def lr4(lt):
    lr3(lt)
    turtle.left(60)
    lr3(lt)    
    turtle.right(120)
    lr3(lt)   
    turtle.left(60) 
    lr3(lt)
    
def lr5(lt):
    lr4(lt)
    turtle.left(60)
    lr4(lt)    
    turtle.right(120)
    lr4(lt)   
    turtle.left(60) 
    lr4(lt)
    
def lr6(lt):
    lr5(lt)
    turtle.left(60)
    lr5(lt)    
    turtle.right(120)
    lr5(lt)   
    turtle.left(60) 
    lr5(lt)
    
turtle.pen(pencolor = "red")
turtle.penup()
turtle.goto(-770, 0)
turtle.pendown()
print('fullscreen')
for i in range (10):
    lr6(ltl)
