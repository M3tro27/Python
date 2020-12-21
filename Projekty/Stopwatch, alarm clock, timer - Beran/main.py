from tkinter import * 
from tkinter.ttk import *
from time import strftime 
import tkinter
import winsound
import time
import datetime
import math

  
"""Clock - vypise aktualni cas, AM/PM, den,mesic a rok"""
def time(): 
    string = strftime('%H:%M:%S %p \n %d.%m.%Y')
    lbl.config(text = string) 
    lbl.after(1000, time) 

"""Start stopwatch"""
def start():
    global second,minute,hour
    second = second + 1
    if(second==60):
        minute=minute+1
        second=0
    if(minute==60):
        hour=hour+1
        minute=0
    if(stp==0):
        label=Label(root,text='%i:%i:%i'%(hour,minute,second),font=('arial',30,'bold'),
        foreground='white',background="black",width=6)
        label.after(1000,start)
        label.place(x=140,y=260)

"""Stop stopwatch"""
def stop():
    global stp
    stp = 1

"""Timer countdown - odecita 1 od celkoveho souctu do 0"""

def countdown(count): 
	#math.floor - vraci x - nejvetsi cislo, ale ne vetsi nez x 
    seconds=math.floor(count%60)		
    minutes=math.floor((count/60)%60)
    hours=math.floor((count/3600))
    label['text'] = "Hours: "+ str(hours)+ " Minutes:  " +str(minutes)+ " Seconds: " +str(seconds)

    if count >= 0:
        root.after(1000, countdown,count-1)

    else:
    	#Alert okno o vyprseni casu
        alert = tkinter.Tk()
        alert.title('Timer alert')
        alert.geometry("240x160")
        alert.resizable(False,False)
        alert.configure(bg="white")
        labeltimer = Label(alert, text = "Time is up!",font=('arial',15,'bold'),foreground='red')
        labeltimer.place(x=65,y=60) 	

        #Zvukovy signal	
        for x in range(3):
         winsound.Beep(500,1000)

        alert.mainloop()

"""Start timer"""
#isdigit - metoda vraci true, pokud jsou všechny znaky číslice
#get - vraci hodnoty polozky
def updateButton():
    hr,mn,sec = hoursE.get(),minuteE.get(),secondE.get()
    if hr.isdigit() and mn.isdigit() and sec.isdigit():
           time=int(hr)*3600+int(mn)*60+int(sec)
           countdown(time)

#Stopwatch - definování proměnných
second=0
minute=0
hour=0
stp=0

#Hlavni dialogove okno
root = tkinter.Tk() 
root.title('Clock,alarm,stopwatch,timer') 
root.geometry("420x600")
root.resizable(False,False)
root.configure(bg="white")

#Clock labels
clock = Label(root, text="Clock",font=('arial',30,'bold'),foreground='red').pack(anchor = 'n')
lbl = Label(root, font = ('arial', 40, 'bold'), background = 'black', foreground = 'white') 
lbl.pack(anchor = 'n') 

time() 

#Stopwatch labels
stopwatch = Label(root, text="Stopwatch",font=('arial',30,'bold'),foreground='red').pack(anchor = 'center')
stopwatchlabel = Label(root, text='0:0:0',font=('arial',30,'bold'),foreground='white',background="black",width=6).place(x=140,y=260)
button1=Button(root,text="Start",command=start).place(x=130,y=230)
button2=Button(root,text="Stop",command=stop).place(x=210,y=230)

#Timer labels
timer = Label(root, text="Timer",font=('arial',30,'bold'),foreground='red').place(x=140,y=340)

enter = Label(text="Enter all values:", font=('arial',14,'bold')).place(x=10,y=400)
hoursT=tkinter.Label(root, text="Hours:",font=('arial',12,'bold')).place(x=20,y=425)
hoursE=tkinter.Entry(root)
hoursE.place(x=100,y=430)

minuteT=tkinter.Label(root, text="Minutes:",font=('arial',12,'bold')).place(x=20,y=445)
minuteE=tkinter.Entry(root)
minuteE.place(x=100,y=450)

secondT=tkinter.Label(root, text="Seconds:",font=('arial',12,'bold')).place(x=20,y=465)
secondE=tkinter.Entry(root)
secondE.place(x=100,y=470)

button=tkinter.Button(root,text="Start Timer",command=updateButton).place(x=20,y=510)

#label pro otestování jestli zbytek funguje
label = tkinter.Label(root)
label.place(x=100,y=490)

root.mainloop() 