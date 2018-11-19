#импортируем библиотеки random для числа graphics для цвета
from tkinter import *
import time
import random
import graphics as gr
#создаем интерфейс для рисования
root = Tk()
root.geometry('1000x700')
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)
#обнуляем счёт и задаём начальное время
schet=0
tt=2000


#функция рисует кружки с рандомным цветом и положением
def risovach():
    global a,b
    #рандомим переменные red blu gre, чтобы получить цвет
    #любой цвет состоит из 3х переменных с диапозоном (0.255)
    red=random.randint(0,255)
    gre=random.randint(0,255)
    blu=random.randint(0,255)
    #рандомим положение круга
    a=random.randint(0,950)
    b=random.randint(0,650)
    #создаём круг
    canv.create_oval(a, b, a+50, b+50,fill=gr.color_rgb(red,gre,blu))
    
    
def cliick(event):
    global schet,a,b,tt
    #ситываем положение курсора по x и по y
    x = event.x
    y = event.y
    #смотрим находится ли курсор в нарисованном круге при щелчке
    if x in range(a, a+50) and y in range(b, b+50):  
        canv.delete(ALL)
        a=10000
        b=10000
        schet +=2
        #создание текста со счётом
        canv.create_text(500, 25, text='Счёт: '+str(schet),font='Arial 25')
        #увеличение сложности(скорости появления шарика) при удачном клике
        if tt>200:    
            tt-=100
    else:
        canv.delete(ALL)
        a=10000
        b=10000
        canv.create_text(500, 25, text='Счёт: '+str(schet),font='Arial 25')
        
        
def tick(): 
    global tt,schet
    #очищаем экран
    canv.delete(ALL)
    #создаём счётчик
    canv.create_text(500, 25, text='Счёт: '+str(schet),font='Arial 25')
    #магия цикла
    root.after(tt, tick)
    #рисуем круги
    risovach()
    schet-=1
#заставляем программу после клика ЛКМ проигрывать event 
canv.bind('<Button-1>', cliick)
root.after_idle(tick)
root.mainloop()