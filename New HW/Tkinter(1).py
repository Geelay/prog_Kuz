from tkinter import *
import time


root = Tk()
root.geometry('800x600')

canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

def left_button(event):
    root.title("Left")
def right_button(event):
    root.title("Right")
def motion(event):
    x = event.x
    y = event.y
    s = "Mouse motion x = {} y = {}".format(x,y)
    root.title(s)
root.bind('<Button-1>', left_button)
root.bind('<Button-3>', right_button)
root.bind('<Motion>', motion)
root.mainloop()