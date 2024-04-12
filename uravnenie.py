from ctypes.wintypes import INT
from pickletools import int4
from tkinter import *
from tkinter import messagebox as mb
import math,numpy
import matplotlib.pyplot as plt



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


            
pealkiri.place(x=100,y=0)
chislo1.place(x=0,y=100)
J.place(x=80,y=100)
chislo2.place(x=160,y=100)
Jj.place(x=240,y=100)
chislo3.place(x=320,y=100)
Jjj.place(x=400,y=100)
nupp.place(x=550,y=100)
solution.place(x=300,y=210)



aken.mainloop()
