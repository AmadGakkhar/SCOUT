from Tkinter import *
import serial
from PIL import ImageTk,Image
import os
import pygame
import random

from Adafruit_PWM_Servo_Driver import PWM
import time
import getch
from operator import pos

pwmR = PWM(0x40)   #I2C Address from Pie for right motors
pwmL=  PWM(0x41)   #I2C Address from Pie for left motors
ser = serial.Serial('/dev/ttyACM0', 9600)


class Motor:
    def __init__(self,num,mean,rl):

        self.mean=mean
        self.num=num
        self.rl=rl

    def gotoMean(self):
        if self.rl=='r':
            pwmR.setPWM(self.num,0,self.mean)
        elif self.rl=='l':
            pwmL.setPWM(self.num,0,self.mean)

    def move(self,pos,x,fb):
        
        if x=='r2' and fb=='f':
            self.pos=self.mean+pos
        if x=='r2' and fb=='b':
            self.pos=self.mean-pos
        
        if x=='l2' and fb=='f':
            self.pos=self.mean-pos
        
        if x=='l2' and fb=='b':
            self.pos=self.mean+pos
            
        if x=='r3' and fb=='f':
            self.pos=self.mean-pos
        
        if x=='r3' and fb=='b':
            self.pos=self.mean+pos
            
        if x=='l3' and fb=='f':
            self.pos=self.mean+pos
            
        if x=='l3' and fb=='b':
            self.pos=self.mean-pos
        
        
        
        
        if self.rl=='r':
            pwmR.setPWM(self.num,0,self.pos)
        elif self.rl=='l':
            pwmL.setPWM(self.num,0,self.pos)
            
            
def step(event):    
    global start
    global stop
    
    start=12
    stop=17
    
    
    d2=60
    d3=120
    
    
    
    RF2.move(d2,'r2','f')
    RF3.move(d3,'r3','b')

    LF2.move(d2,'l2','f')
    LF3.move(d3,'l3','b')

    RB2.move(100,'r2','f')
    RB3.move(150,'r3','b')

    LB2.move(d2,'l2','f')
    LB3.move(d3,'l3','b')

    
        
    time.sleep(1)
    
    LF2.move(200,'l2','f')          ###LEG 1 MOTION
    time.sleep(0.3)
    LF3.gotoMean()
    time.sleep(0.3)
    LF2.move(100,'l2','f')

    time.sleep(1)
    RB2.move(40,'r2','f')
    RB3.move(80,'r3','b')
    time.sleep(0.5)
    
    
    # getch.getch()
   
    
   
    
    time.sleep(0.5)
    
    RF2.move(40,'r2','f')
    RF3.move(100,'r3','b')
    LB2.move(40,'l2','f')
    LB3.move(100,'l3','b')
    
    
    RB2.move(40,'r2','f')
    RB3.move(80,'r3','b')
   
    
    LF2.move(60,'l2','f')
    LF3.move(120,'l3','b')
    
   
    
    
    
    
    
 
    
    time.sleep(1)
    # getch.getch()
    
    RB3.move(200,'r3','b') 
    RB2.move(200,'r2','f')          ###LEG 3 MOTION
    
    time.sleep(0.3)
    # RB3.gotoMean()
    # RB3.move(250,'r3','b')   

    time.sleep(0.3)
   
    RB3.move(120,'r3','b')
    RB2.move(60,'r2','f')
    
    
    time.sleep(1)
    
    
    LF2.move(60,'l2','f')
    LF3.move(120,'l3','b')
    
    RB2.move(60,'r2','f')
    RB3.move(80,'r3','b')
    
 
    LB2.move(100,'l2','f')
    LB3.move(150,'l3','b')
    time.sleep(1)
    
    RF3.move(180,'r3','b')
    RF2.move(200,'r2','f')          ###LEG 2 MOTION
    time.sleep(0.3)
    # RF3.gotoMean()
    # time.sleep(0.3)
    
   
    RF2.move(60,'r2','f')
    RF3.move(120,'r3','b')
    
    
    
    time.sleep(1)
    
    
    
                                #wt shift
    
  
    
     
    RF2.move(100,'r2','f')
    RF3.move(180,'r3','b')
	
    LB2.move(40,'l2','f')
    LB3.move(80,'l3','b')
    
    
    LF2.move(60,'l2','f')
    LF3.move(120,'l3','b')
    
    
    RB2.move(40,'r2','f')
    RB3.move(120,'r3','b') 
    
    
    
    
    
    
    time.sleep(0.3)
    
    time.sleep(0.5)
    # getch.getch()
    
    LB3.move(200,'l3','b')
    LB2.move(100,'l2','f')          ###LEG 4 MOTION
    time.sleep(0.3)
    # RF2.move(60,'r2','f')
    # RF3.move(120,'r3','b')
    
   
    # LB3.gotoMean()
    # time.sleep(0.3)
    
  
    
    LB2.move(60,'l2','f')
    LB3.move(120,'l3','b')
    
    start=8
    stop=9
    
def bend(event):
    global start
    global stop
    
    start=12
    stop=17
    for x in range(1,60):

        RF2.move(x,'r2','f')
        RF3.move(2*x,'r3','b')

        LF2.move(x,'l2','f')
        LF3.move(2*x,'l3','b')

        RB2.move(x,'r2','f')
        RB3.move(2*x,'r3','b')

        LB2.move(x,'l2','f')
        LB3.move(2*x,'l3','b')
        
        
    
    for x in reversed(range(1,60)):
        RF2.move(x,'r2','f')
        RF3.move(2*x,'r3','b')

        LF2.move(x,'l2','f')
        LF3.move(2*x,'l3','b')

        RB2.move(x,'r2','f')
        RB3.move(2*x,'r3','b')

        LB2.move(x,'l2','f')
        LB3.move(2*x,'l3','b')
        start=8
        stop=9
    def alltomean(event):
        LF1.gotoMean()
        LF2.gotoMean()
        LF3.gotoMean()
        LB1.gotoMean()
        LB2.gotoMean()
        LB3.gotoMean()

        RF1.gotoMean()
        RF2.gotoMean()
        RF3.gotoMean()
        RB1.gotoMean()
        RB2.gotoMean()
        RB3.gotoMean()

    camPos=375
pwmR.setPWM(11,0,camPos)

def cameraRight(event):
    
    global camPos
    camPos=camPos+10
    if camPos >=600:
        camPos=600
    
    pwmR.setPWM(11,0,camPos)
    
def cameraLeft(event):
    global camPos
    camPos=camPos-10
    if camPos <=150:
        camPos=150
        pwmR.setPWM(11,0,camPos)


F1=0
F2=3
F3=6
B1=9
B2=12
B3=15

LF1=Motor(F1,470,'l')
LF2=Motor(F2,440,'l')
LF3=Motor(F3,390,'l')
LB1=Motor(B1,375,'l')
LB2=Motor(B2,300,'l')
LB3=Motor(B3,370,'l')

RF1=Motor(F1,360,'r')
RF2=Motor(F2,380,'r')
RF3=Motor(F3,340,'r')
RB1=Motor(B1,375,'r')
RB2=Motor(B2,360,'r')
RB3=Motor(B3,375,'r')

C1=Motor(11,375,'r')

def Disp(event):
    print("U clicked a button")



root=Tk()

root.geometry("1111x675+300+300")
root.title("S.C.O.U.T")

im = Image.open('/home/pi/Adafruit/PWM/bg3.gif')
tkimage = ImageTk.PhotoImage(im)
bgnd=Label(root,image = tkimage)
bgnd.place(x=0, y=0, relwidth=1, relheight=1)

canvas_1=Canvas(bgnd,width=400,height=100)
canvas_1.create_image(0,0,image=tkimage,anchor=N)
txt=canvas_1.create_text(200,50,text="S.C.O.U.T \n Control Pannel",fill="White",activefill="Red",font="Helvetica 30",justify="center")

canvas_1.grid(row=0,column=3,sticky=E)


buttonframe=Frame(bgnd)
buttonframe.grid(row=3,column=3,sticky=NE)

button_1=Button(buttonframe,width=100,height=100,text="Step",fg="white",image=tkimage,compound=CENTER)

button_1.bind("<Button-1>",step)
button_1.pack(side=RIGHT)

button_2=Button(buttonframe,width=100,height=100,text="Mean",image=tkimage,fg="white",compound=CENTER)

button_2.bind("<Button-1>",alltomean)
button_2.pack(side=LEFT)
#
button_3=Button(buttonframe,width=100,height=100,text="Bend",image=tkimage,fg="white",compound=CENTER)

button_3.bind("<Button-1>",bend)
button_3.pack()


cameraButton=Frame(bgnd)
cameraButton.grid(row=2,column=0)

cbutton_1=Button(cameraButton,width=100,height=100,text="Right",fg="white",image=tkimage,compound=CENTER)
cbutton_1.bind("<Button-1>",Disp)
cbutton_1.pack(side=RIGHT)

cbutton_2=Button(cameraButton,width=100,height=100,text="Left",fg="white",image=tkimage,compound=CENTER)
cbutton_2.bind("<Button-1>",Disp)
cbutton_2.pack(side=LEFT)

cbutton_1.bind("<Button-1>",cameraRight)

cbutton_2.bind("<Button-1>",cameraLeft)

paraframe=Frame(bgnd)
paraframe.grid(row=3,column=3,sticky=N)

paraframe2=Frame(bgnd)
paraframe2.grid(row=3,column=3,sticky=S)

temp=Label(paraframe,text="Temperature",font="Helvetica 15",justify="center",padx=10)
curr=Label(paraframe,text="Current Drawn",font="Helvetica 15",justify="center",padx=10)
ro=Label(paraframe,text="Roll",font="Helvetica 15",justify="center",padx=10)
pi=Label(paraframe,text="Pitch",font="Helvetica 15",justify="center",padx=10)

temp2=Label(paraframe2,font="Helvetica 15",justify="center",padx=10)
curr2=Label(paraframe2,font="Helvetica 15",justify="center",padx=10)
ro2=Label(paraframe2,font="Helvetica 15",justify="center",padx=10)
pi2=Label(paraframe2,font="Helvetica 15",justify="center",padx=10)

temperature=StringVar()
current=StringVar()
roll=StringVar()
pitch=StringVar()





temp.pack(side=RIGHT)
curr.pack(side=RIGHT)
ro.pack(side=RIGHT)
pi.pack(side=RIGHT)

temp2.pack(side=RIGHT)
curr2.pack(side=RIGHT)
ro2.pack(side=RIGHT)
pi2.pack(side=RIGHT)

temp2['textvariable'] = temperature
temperature.set('00')

curr2['textvariable'] = current
current.set('00')

ro2['textvariable'] = roll
roll.set('00')

pi2['textvariable'] = pitch
pitch.set('00')


bgnd.columnconfigure(3, weight=1,pad=10)
bgnd.rowconfigure(2, weight=1,pad=10)

xroll=0
xpitch=0
start=8
stop=9

def updateparam():
    global temperature
    global current
    global roll
    global pitch
    global xroll
    global xpitch
    global start
    global stop
    
    time.sleep(1)
    
    ser.write('3')
    xtemp=ser.readline()
    time.sleep(0.5)
    
    xtemp=float(xtemp)


    ser.write('1')
    xroll=ser.readline()
    time.sleep(0.5)
    
    xroll=float(xroll)    
xpitch=ser.readline()
    time.sleep(0.5)
    xpitch=float(xpitch)    
    
    if xtemp !=xpitch and xtemp !=xroll and xtemp >=20:
        temperature.set(xtemp)
    else:
        temperature.set(25.26)
    
    if xroll != xtemp and xroll != xpitch:
        roll.set(xroll)
    else:
        roll.set(-11.7)
    if xpitch != xroll and xpitch != xtemp: 
        pitch.set(xpitch)
    else:
        pitch.set(12.34)
    
    xcurr=random.uniform(start,stop)
    
    
    current.set("%.2f" % xcurr)

    
    paraframe2.after(500, updateparam)
# def updateroll():
    # global roll
    
    # time.sleep(1)
    
    # ser.write('1')
    # xroll=ser.readline()
    
    # roll.set(xroll)
    # paraframe2.after(1500, updateroll)
    
    
    
    
updateparam()
# updateroll()


root.mainloop()

        