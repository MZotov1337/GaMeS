from tkinter import *
from random import randrange as rnd, choice
from array import *

import time

root = Tk()
root.geometry('800x620')


s = input()

canv = Canvas(root, bg='white')




    

class my_object(object):
    
    def __init__(self, x, y, Vx, Vy, r):
        self.x = x
        self.y = y
        self.Vx = Vx
        self.Vy = Vy
        self.r = r
    
color = ['red','orange','yellow','green','blue']

Ob1 = my_object(300, 200, 100, 70, 20)
Ob2 = my_object(400, 100, 150, 70, 10)
Ob3 = my_object(250, 100, 100, 100, 5)

c1 = canv.create_oval(300 - 20, 200 - 20, 300 + 20, 200 + 20, fill = choice(color), width=0)
c2 = canv.create_oval(400 - 10, 100 - 10, 400 + 10, 100 + 10, fill = choice(color), width=0)
c3 = canv.create_rectangle(250 - 5, 100 - 5, 250 + 5, 100 + 5, fill = choice(color), width=0)

mass = [Ob1, Ob2, Ob3]
mass1 = [c1, c2, c3]    





dT = 0.01


l = Label(root, bg = 'white', fg = 'black', width = 800)
l1 = Label(root,bg = 'white', fg = 'black', width = 800)
l2 = Label(root,bg = 'white', fg = 'black', width = 800)

b = Button(root, text = 'Старт')


l1.pack()
l2.pack()


l.pack()
canv.pack(fill=BOTH,expand=1)

i = 0
lokmax = 0


l1['text'] = s

def click(event):
    global Xo, Yo, i
    Xo = event.x
    Yo = event.y
    flag = 0
    if ((Xo-mass[0].x) ** 2 + (Yo-mass[0].y) ** 2)  <= mass[0].r ** 2 : 
        i = i + 1
        mass[0].Vx = mass[0].Vx * 1.2
        mass[0].Vy = mass[0].Vy * 1.2
        flag = 1
    if ((Xo-mass[1].x) ** 2 + (Yo-mass[1].y) ** 2)  <= mass[1].r ** 2 : 
        i = i + 1
        mass[1].Vx = mass[1].Vx * 1.2
        mass[1].Vy = mass[1].Vy * 1.2
        flag = 1
    if Xo < mass[2].x + mass[2].r and Xo > mass[2].x - mass[2].r and Yo > mass[2].y - mass[2].r and Yo < mass[2].y + mass[2].r : 
        i = i + 5
        mass[2].Vx = mass[2].Vx * 2
        mass[2].Vy = mass[2].Vy * 2
        flag = 1
    if flag == 0 : i = 0
    
    
def new_ball():
    global i, lokmax
    
    for k in range(3):
        mass[k].x = mass[k].x + mass[k].Vx * dT
        mass[k].y = mass[k].y + mass[k].Vy * dT
        canv.move(mass1[k], mass[k].Vx * dT, mass[k].Vy * dT)
        if (mass[k].x + mass[k].r > 800 or mass[k].x - mass[k].r < 0): mass[k].Vx = - mass[k].Vx
        if (mass[k].y + mass[k].r > 510 or mass[k].y - mass[k].r < 0): mass[k].Vy = - mass[k].Vy        
    if i > lokmax: lokmax = i
    l['text'] = i
    l2['text'] = "Higth Score", lokmax
    root.after(15,new_ball)



canv.bind('<Button-1>', click)
new_ball()

mainloop()