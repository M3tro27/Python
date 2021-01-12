from GUI import *
from tkinter import * 
from tkinter.ttk import *
from .root import * 

def alarm():
    """Display alarm clock labels and button"""
    global e1,e2
    alarm_clock=Label(root,text="Alarm clock",font=('arial',30,'bold'),background="dimgray",foreground='black').place(x=60,y=520)
    hours = Label(root,text="Hours: ",font=('arial',10,'bold'),background="lightgreen")
    hours.place(x=100,y=580)
    e1=Entry(root,width=10)
    e1.place(x=170,y=580)
    minutes=Label(root,text="Minutes: ",font=('arial',10,'bold'),background="lightgreen")
    minutes.place(x=100,y=600)
    e2 = Entry(root,width=10)
    e2.place(x=170,y=600)
    begin=Button(root,text="Start alarm")
    begin.place(x=120,y=630)
    begin.bind("<Button-1>",alarm_begin)