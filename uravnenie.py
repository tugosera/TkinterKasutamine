from ctypes.wintypes import INT
from pickletools import int4
from tkinter import *
from tkinter import messagebox as mb
import math
import matplotlib.pyplot as plt
import numpy

def choice():
    figure_selected = var.get()
    if figure_selected == 1:
        kala()
    elif figure_selected == 2:
        prillid()

aken=Tk()
aken.geometry("800x400")
aken.iconbitmap('')
aken.title("Квадратные уравнения")
tekst="Решение квадартного уравнения"
tekst2="X**2+"
tekst3="X+"
tekst4="=0"
D=int
x1=int
x2=int
def vajuta_():
    a_=float(chislo1.get())
    b_=float(chislo2.get())
    c_=float(chislo3.get())
    D=b_*b_-4*a_+c_
    if D>0:
        x1=round((abs((b_))+math.sqrt(D))/(2*a_), 2)
        x2=round((abs((b_))-math.sqrt(D))/(2*(a_)), 2)
        solution.configure(text=f"D={D}\nX₁={x1}\nX₂={x2}")
        graph()
    elif D==0:
         x=round(abs(float(b_))/(2*float(a_)), 2)
         solution.configure(text=f"D={D}\nX={x}")
         graph()
    else:
            solution.configure(text=f"D={D}\nLahendusi pole")
         
def graph():
    """
    """
    a_=float(chislo1.get())
    b_=float(chislo2.get())
    c_=float(chislo3.get())
    x=round(abs(b_)/(2*a_),2)
    x1=numpy.arange(x-5,x+5,float(f"0.{5}"))
    y=a_*x**2+b_*x1+c_
    y1=a_*x1**2+b_*x1+c_
    fig=plt.figure()
    plt.plot(x1,y1,'b-d')
    plt.title('Ruutvõrrand')
    plt.ylabel('y')
    plt.xlabel('x')
    plt.grid(True)
    plt.show()

def kala():
    x1=numpy.arange(0,9.5,0.5)
    y1=(2/27)*x1*x1-3
    x2=numpy.arange(-10,0.5,0.5)
    y2=0.04*x2*x2-3
    x3=numpy.arange(-9,-2.5,0.5)
    y3=(2/9)*(x3+6)**2+1
    x4=numpy.arange(-3,9.5,0.5)
    y4=(-1/12)*(x4-3)**2+6
    x5=numpy.arange(5,9,0.5)
    y5=(1/9)*(x5-5)**2+2
    x6=numpy.arange(5,8.5,0.5)
    y6=(1/8)*(x6-7)**2+1.5
    x7=numpy.arange(-13,-8.5,0.5)
    y7=(-0.75)*(x7+11)**2+6
    x8=numpy.arange(-15,-12.5,0.5)
    y8=(-0.5)*(x8+13)**2+3
    x9=numpy.arange(-15,-10,0.5)
    y9=[1]*len(x9)
    x10=numpy.arange(3,4,0.5)
    y10=[3]*len(x10)
    plt.figure()
    plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10)
    plt.title('Kit')
    plt.xlabel('y')
    plt.xlabel('x')
    plt.grid(True)
    plt.show()

def prillid():
    x1 = numpy.arange(-9, -0.5, 0.5)
    y1 = -(1/16) * (x1 + 5)**2 + 2
    x2 = numpy.arange(1, 9.5, 0.5)
    y2 = -(1/16) * (x2 - 5)**2 + 2
    x3 = numpy.arange(-9, -0.5, 0.5)
    y3 = (1/4) * (x3 + 5)**2 - 3
    x4 = numpy.arange(1, 9.5, 0.5)
    y4 = (1/4) * (x4 - 5)**2 - 3
    x5 = numpy.arange(-9, -6, 0.5)
    y5 = -(x5 + 7)**2 + 5
    x6 = numpy.arange(6, 9.5, 0.5)
    y6 = -(x6 - 7)**2 + 5
    x7 = numpy.arange(-1, 1, 0.01)
    y7 = -0.5 * (x7**2) + 1.5
    plt.figure()
    plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7)
    plt.title('Prillid')
    plt.xlabel('y')
    plt.xlabel('x')
    plt.grid(True)
    plt.show()

    
pealkiri=Label(aken,
              text=tekst,
              bg="#7c02b4",
              fg="#7ba5fd",
              font="Chiller",
              height=4,
              width=100)
chislo1=Entry(aken,
              bg="#7ba5fd",
              fg="#7c02b4",
              font="Chiller",
              width=6,
              bd=10,
              justify=CENTER)
J=Label(aken,
              text=tekst2,
              bg="#7c02b4",
              fg="#7ba5fd",
              font="Chiller",
              height=2,
              width=8)
chislo2=Entry(aken,
              bg="#7ba5fd",
              fg="#7c02b4",
              font="Chiller",
              width=6,
              bd=10,
              justify=CENTER)
Jj=Label(aken,
              text=tekst3,
              bg="#7c02b4",
              fg="#7ba5fd",
              font="Chiller",
              height=2,
              width=8)
chislo3=Entry(aken,
              bg="#7ba5fd",
              fg="#7c02b4",
              font="Chiller",
              width=6,
              bd=10,
              justify=CENTER)
Jjj=Label(aken,
              text=tekst4,
              bg="#7c02b4",
              fg="#7ba5fd",
              font="Chiller",
              height=2,
              width=8)
nupp=Button(aken,
            text="решение",
            font="Algerian",
            height=3, 
            width=15,
            relief=RAISED,
            command=vajuta_,
            bg="lightblue")
solution = Label(
            bg="#7c02b4",
            fg="#7ba5fd",
            font="Chiller",
            height=6,
            width=40,
            justify=CENTER,
            text="")

var=IntVar()
kala_button = Radiobutton(aken, text="Kala", variable=var, value=1, font = "Arial 12", command=choice)
kala_button.pack(side = BOTTOM)

prillid_button = Radiobutton(aken, text="Prillid", variable=var, value=2, font = "Arial 12", command=choice)
prillid_button.pack(side = BOTTOM)

pealkiri.place(x=100,y=0)
chislo1.place(x=0,y=100)
J.place(x=80,y=100)
chislo2.place(x=160,y=100)
Jj.place(x=240,y=100)
chislo3.place(x=320,y=100)
Jjj.place(x=400,y=100)
nupp.place(x=550,y=100)
solution.place(x=300,y=210)
kala_button.place(x=400,y=350)
prillid_button.place(x=300,y=350)


aken.mainloop()
