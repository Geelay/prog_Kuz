from tkinter import *
import random
import graphics as gr
root = Tk()
root.geometry("800x600")
canvas = Canvas(root)
canvas.pack(fill=BOTH, expand=1)
schet=0
speed=100
number_of_balls=50
x=[]
y=[]
text1=canvas.create_text(400, 25, text='Счёт: '+str(schet)+'/'+str(number_of_balls),font='Arial 25')
def cliick(event):
    global schet,x,y,speed,text1,ballsy,ballsx
    
    a = event.x
    b = event.y
    for i in range (number_of_balls):
        if a in range(x[i], x[i]+50) and b in range(y[i], y[i]+50):  
            if (a-x[i])^2+(b-y[i])^2 < 2500:
                y[i]=1000
                x[i]=1000
                ballsx[i]=0
                ballsy[i]=0
                canvas.delete(ov[i])
                canvas.delete(text1)
                schet +=1
                text1=canvas.create_text(400, 25, text='Счёт: '+str(schet)+'/'+str(number_of_balls),font='Arial 25')
                if speed > 5:
                    speed-=5
                break
            
#создание текста со счётом            
def create_list_of_balls(number):
    lst = []
    while len(lst) < number:
        lst.append(random.randint(1,5))
    return(lst)


def risovach(i):
    global x,y
    #рандомим переменные red blu gre, чтобы получить цвет
    red=random.randint(0,255)
    gre=random.randint(0,255)
    blu=random.randint(0,255)
    #рандомим положение круга
    x.append(random.randint(0,740))
    y.append(random.randint(0,500))
    #создаём круг
    ovall=canvas.create_oval(x[i], y[i], x[i]+50, y[i]+50,fill=gr.color_rgb(red,gre,blu))
    return (ovall)

def tick_handler():
    global x, y,ballsx,ballsy
    for i in range (number_of_balls):

        if x[i] < 40:
            ballsx[i] = -ballsx[i]; x[i] = 40
        elif x[i] > 740-40:
            ballsx[i] = -ballsx[i]
            x[i] = 740-40
        if y[i] < 40:
            ballsy[i] = -ballsy[i]
            y[i] = 40
        elif y[i] > 500-40:
            ballsy[i] = -ballsy[i]
            y[i] = 500-40
        x[i] = x[i] + ballsx[i]; y[i] = y[i] + ballsy[i]
        canvas.move(ov[i], ballsx[i], ballsy[i])
        
        


def time_handler():
    global speed
    tick_handler()
    root.after(speed, time_handler)


ov=[]
for i in range(number_of_balls):
    bll=risovach(i)
    ov.append(bll)    
ballsx=create_list_of_balls(number_of_balls)
ballsy=create_list_of_balls(number_of_balls)
root.after(10, time_handler)
canvas.bind('<Button-1>', cliick)
root.mainloop()