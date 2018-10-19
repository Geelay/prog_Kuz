import graphics as gr
import time
import random
window = gr.GraphWin("Gleb and Kuzz project", 400, 240)
def pixel (x,y,Rd,Be,Gn):
    px=gr.Rectangle(gr.Point(x,y), gr.Point(x+9,y+9))
    px.setOutline(gr.color_rgb(Rd,Be,Gn))
    px.setFill(gr.color_rgb(Rd,Be,Gn))
    px.draw(window)
def pixel1 (a,b,x,y,Rd,Be,Gn):
    px=gr.Rectangle(gr.Point(x,y), gr.Point(x+a,y+b))
    px.setOutline(gr.color_rgb(Rd,Be,Gn))
    px.setFill(gr.color_rgb(Rd,Be,Gn))
    px.draw(window)
def smallpixel (x,y,Rd,Be,Gn):
    px=gr.Rectangle(gr.Point(x,y), gr.Point(x+2,y+2))
    px.setOutline(gr.color_rgb(Rd,Be,Gn))
    px.setFill(gr.color_rgb(Rd,Be,Gn))
    px.draw(window)
def pchela(a,b):  
    x1=[1,2,3,4,4,4,4,5,5,5,5,6,6,6,6,6,6,6,6,7,7,7,8,8,8,8,8,8,8,8,8,9,9,9,10,10,10,10,10,11,11,12,12,12]
    y1=[7,7,7,2,6,7,8,1,3,5,9,1,4,5,6,7,8,9,10,2,4,10,1,3,4,5,6,7,8,9,10,1,4,10,2,3,4,7,10,5,9,6,7,8,]   
    for i in range(len(x1)):
        smallpixel(a+3*x1[i],b+3*y1[i],0,0,0)  
    x2=[5,5,5,7,7,7,7,7,9,9,9,9,9,10,10,10,10,11,11,11]
    y2=[6,7,8,5,6,7,8,9,5,6,7,8,9,5,6,8,9,6,7,8]
    for i in range(len(x2)):
        smallpixel(a+3*x2[i],b+3*y2[i],204,168,23)  
    x3=[5,6,6,7,8,9,9]
    y3=[2,2,3,3,2,2,3]
    for i in range(len(x3)):
        smallpixel(a+3*x3[i],b+3*y3[i],120,219,226)  
def pchela_ghost(a,b):  
    x1=[1,2,3,4,4,4,4,5,5,5,5,6,6,6,6,6,6,6,6,7,7,7,8,8,8,8,8,8,8,8,8,9,9,9,10,10,10,10,10,11,11,12,12,12]
    y1=[7,7,7,2,6,7,8,1,3,5,9,1,4,5,6,7,8,9,10,2,4,10,1,3,4,5,6,7,8,9,10,1,4,10,2,3,4,7,10,5,9,6,7,8,]   
    for i in range(len(x1)):
        smallpixel(a+3*x1[i],b+3*y1[i],144,238,144)  
    x2=[5,5,5,7,7,7,7,7,9,9,9,9,9,10,10,10,10,11,11,11]
    y2=[6,7,8,5,6,7,8,9,5,6,7,8,9,5,6,8,9,6,7,8]
    for i in range(len(x2)):
        smallpixel(a+3*x2[i],b+3*y2[i],144,238,144)  
    x3=[5,6,6,7,8,9,9]
    y3=[2,2,3,3,2,2,3]
    for i in range(len(x3)):
        smallpixel(a+3*x3[i],b+3*y3[i],144,238,144) 
def blpixel():  
    x=[1,2,2,5,6,6,7,10,10,11,13,14]
    y=[4,3,4,7,6,7,7,3,4,4,6,8]   
    for i in range(len(x)):
        time.sleep(.1)
        pixel(100+10*x[i],100+10*y[i],0,0,0)  
def wtpixel():  
    x=[1,1,1,2,2,3,3,3,3,4,4,4,4,4,4,5,5,5,5,5,5,5,5,6,6,6,6,6,7,7,7,7,7,7,8,8,8,8,8,9,9,9,9,9,10,10,10,10,10,11,11,11,11,12,13,13,13,13]
    y=[5,6,7,5,6,4,5,6,7,3,4,6,7,8,9,3,4,5,6,8,9,11,12,4,5,8,9,11,5,6,8,9,11,12,6,7,8,9,11,6,7,8,9,11,6,7,8,9,11,7,8,11,12,11,9,10,11,12]   
    for i in range(len(x)):
        time.sleep(.1)
        pixel(100+10*x[i],100+10*y[i],219,215,210)  
def ylpixel():  
    x=[1,2,2,2,3,3,6,7,7,8,8,8,9,9,9,9,10,11,12,12,14,14]
    y=[8,7,8,9,8,9,3,3,4,2,3,4,1,3,4,5,2,10,9,10,6,9]   
    for i in range(len(x)):
        time.sleep(.1)
        pixel(100+10*x[i],100+10*y[i],244,196,48) 
def brpixel():  
    x=[2,3,3,4,9,10,11,11,14]
    y=[2,1,3,2,10,5,5,6,7]   
    for i in range(len(x)):
        time.sleep(.1)
        pixel(100+10*x[i],100+10*y[i],117,51,19) 
def grpixel():  
    x=[5,6,7,8]
    y=[10,10,10,10]   
    for i in range(len(x)):
        time.sleep(.1)
        pixel(100+10*x[i],100+10*y[i],186,175,150) 
def pkpixel():  
    x=[3,9]
    y=[2,2]   
    for i in range(len(x)):
        time.sleep(.1)
        pixel(100+10*x[i],100+10*y[i],239,0,151) 
def gnpixel():  
    x=[4,8]
    y=[5,5]   
    for i in range(len(x)):
        time.sleep(.1)
        pixel(100+10*x[i],100+10*y[i],0,200,0) 
def onpixel():  
    x=[10,11]
    y=[10,9]   
    for i in range(len(x)):
        time.sleep(.1)
        pixel(100+10*x[i],100+10*y[i],247,94,37) 
#кадр открытого рта
def yazikop():
        x=6
        y=8
        pixel(100+10*x,100+10*y,155,17,30)
#кадр закрытого рта
def yazikcl():
        x=6
        y=8
        pixel(100+10*x,100+10*y,219,215,210)    
#tail animation
def xvost():  
        x=13
        y=6 
        pixel(100+10*x,100+10*y,0,0,0)
        time.sleep(1)
        pixel(100+10*x,100+10*y,144,238,144)
        x=15
        pixel(100+10*x,100+10*y,0,0,0)
        time.sleep(1)
        pixel(100+10*x,100+10*y,144,238,144)
#TODO: запилить нормальный window.getMouse
def eyes(a,b):
    x=[4,8]
    y=[5,5]   
    for i in range(len(x)):
        pixel1(a,b,109-a+10*x[i],109-b+10*y[i],0,200,0) 
        pixel1(a,b,100+10*x[i],100+10*y[i],0,200,0)
        pixel1(a,b,109-a+10*x[i],100+10*y[i],0,200,0)
        pixel1(a,b,100+10*x[i],109-b+10*y[i],0,200,0) 
#animation
def dvij(a,b):
    pchela(a,b)
    rm=random.randint(1,3)
    if rm==1:
        yazikop()
    elif rm==2 or rm==3:
        yazikcl()
    xvost()
    pchela_ghost(a,b)
def anim():
    i=True
    a=10
    b=10
    while i:
        dvij(a,b)
        a+=10
        b+=10
        dvij(a,b)
        a+=10
        b-=10
        dvij(a,b)
        a+=10
        b-=10
        dvij(a,b)
        a+=10
        b+=10
def trava():
    for x in range(0,40):
        time.sleep(.1)
        pixel(10*x,230,53,104,45)
    
def kotik():       
    wtpixel()
    onpixel()
    gnpixel()
    pkpixel()
    grpixel()
    brpixel()
    blpixel()
    ylpixel()


window.setBackground(gr.color_rgb(144,238,144))
window.getMouse()
trava()
window.getMouse()
kotik()    
anim()
window.close()