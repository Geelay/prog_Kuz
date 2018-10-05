import graphics as gr

window = gr.GraphWin("Gleb and Kuzz project", 400, 400)
def pixel (x,y,Rd,Be,Gn):
    px=gr.Rectangle(gr.Point(x,y), gr.Point(x+10,y+10))
    px.setOutline(gr.color_rgb(Rd,Be,Gn))
    px.setFill(gr.color_rgb(Rd,Be,Gn))
    px.draw(window)
def blpixel():  
    x=[1,2,2,5,6,6,7,10,10,11,13,14]
    y=[4,3,4,7,6,7,7,3,4,4,6,8]   
    for i in range(len(x)):
        pixel(100+10*x[i],100+10*y[i],0,0,0)  
def wtpixel():  
    x=[1,1,1,2,2,3,3,3,3,4,4,4,4,4,4,5,5,5,5,5,5,5,5,6,6,6,6,6,7,7,7,7,7,7,8,8,8,8,8,9,9,9,9,9,10,10,10,10,10,11,11,11,11,12,13,13,13,13]
    y=[5,6,7,5,6,4,5,6,7,3,4,6,7,8,9,3,4,5,6,8,9,11,12,4,5,8,9,11,5,6,8,9,11,12,6,7,8,9,11,6,7,8,9,11,6,7,8,9,11,7,8,11,12,11,9,10,11,12]   
    for i in range(len(x)):
        pixel(100+10*x[i],100+10*y[i],219,215,210)  
def ylpixel():  
    x=[1,2,2,2,3,3,6,7,7,8,8,8,9,9,9,9,10,11,12,12,14,14]
    y=[8,7,8,9,8,9,3,3,4,2,3,4,1,3,4,5,2,10,9,10,6,9]   
    for i in range(len(x)):
        pixel(100+10*x[i],100+10*y[i],244,196,48) 
def brpixel():  
    x=[2,3,3,4,9,10,11,11,14]
    y=[2,1,3,2,10,5,5,6,7]   
    for i in range(len(x)):
        pixel(100+10*x[i],100+10*y[i],117,51,19) 
def grpixel():  
    x=[5,6,7,8]
    y=[10,10,10,10]   
    for i in range(len(x)):
        pixel(100+10*x[i],100+10*y[i],186,175,150) 
def pkpixel():  
    x=[3,9]
    y=[2,2]   
    for i in range(len(x)):
        pixel(100+10*x[i],100+10*y[i],239,0,151) 
def gnpixel():  
    x=[4,8]
    y=[5,5]   
    for i in range(len(x)):
        pixel(100+10*x[i],100+10*y[i],0,200,0) 
def onpixel():  
    x=[10,11]
    y=[10,9]   
    for i in range(len(x)):
        pixel(100+10*x[i],100+10*y[i],247,94,37) 
        
def kotik():       
    wtpixel()
    onpixel()
    gnpixel()
    pkpixel()
    grpixel()
    brpixel()
    blpixel()
    ylpixel()
    
kotik()    
window.getMouse()
window.close()