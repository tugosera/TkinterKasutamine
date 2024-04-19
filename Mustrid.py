from tkinter import *
from tkinter import font



raam = Tk()
raam.title("Tahvel")
tahvel = Canvas(raam, width=750, height=600, background="white")
tahvel.grid()
def estonia():
    tahvel.delete("all")
    tahvel.create_line(30, 20, 300, 20, width=50, fill="blue")
    tahvel.create_line(30, 70, 300, 70, width=50, fill="black")
    pass

def bahama():
    tahvel.delete("all")
    tahvel.create_line(30, 450, 300, 450, width=50, fill="teal")
    tahvel.create_line(30, 500, 300, 500, width=50, fill="yellow")
    tahvel.create_line(30, 550, 300, 550, width=50, fill="teal")
    tahvel.create_polygon(30, 425, 30, 575, 150, 500, width=30, fill="black")
    pass

def gruzia():
    tahvel.delete("all")
    tahvel.create_line(0, 300, 600, 300 , width=50, fill="red")
    tahvel.create_line(300, 0, 300, 600 , width=50, fill="red")
    tahvel.create_line(125, 40, 125, 225, width=30, fill="red")
    tahvel.create_line(30, 125, 220, 125, width=30, fill="red")
    tahvel.create_line(470, 40, 470, 225, width=30, fill="red")
    tahvel.create_line(30, 450, 220, 450, width=30, fill="red")
    tahvel.create_line(125, 560, 125, 350, width=30, fill="red")
    tahvel.create_line(360, 450, 570, 450, width=30, fill="red")
    tahvel.create_line(360, 125, 570, 125, width=30, fill="red")
    tahvel.create_line(470, 540, 470, 360, width=30, fill="red")
    pass

def shahmat():
    tahvel.delete("all")


    b = 8
    a = 8
    с = 50

    for j in range(b):
        for i in range(a): 
            x1 = i * с
            y1 = j * с
            x2 = x1 + с
            y2 = y1 + с
            if (i + j) % 2 == 0:
                cvet = "white"
            else:
                cvet = "black"
            tahvel.create_rectangle(x1, y1, x2, y2, fill=cvet)
    pass

def svetoforZ():
    tahvel.delete("all")
    tahvel.create_line(300, 500, 300, 310 , width=10, fill="black")
    tahvel.create_line(280, 280, 320, 280 , width=50, fill="green")
    tahvel.create_line(280, 220, 320, 220 , width=50, fill="black")
    tahvel.create_line(280, 160, 320, 160 , width=50, fill="black")
    tahvel.create_line(250, 500, 350, 500 , width=10, fill="black")
    pass

def svetoforO():
    tahvel.delete("all")
    tahvel.create_line(300, 500, 300, 310 , width=10, fill="black")
    tahvel.create_line(280, 280, 320, 280 , width=50, fill="black")
    tahvel.create_line(280, 220, 320, 220 , width=50, fill="orange")
    tahvel.create_line(280, 160, 320, 160 , width=50, fill="black")
    tahvel.create_line(250, 500, 350, 500 , width=10, fill="black")
    pass

def svetoforK():
    tahvel.delete("all")
    tahvel.create_line(300, 500, 300, 310 , width=10, fill="black")
    tahvel.create_line(280, 280, 320, 280 , width=50, fill="black")
    tahvel.create_line(280, 220, 320, 220 , width=50, fill="black")
    tahvel.create_line(280, 160, 320, 160 , width=50, fill="red")
    tahvel.create_line(250, 500, 350, 500 , width=10, fill="black")
    pass




nupp=Button(raam,
            text="Estonia",
            font="Algerian",
            height=2, 
            width=15,
            relief=RAISED,
            command=estonia,
            bg="lightblue")

nupp2=Button(raam,
            text="bahama saar",
            font="Algerian",
            height=2, 
            width=15,
            relief=RAISED,
            command=bahama,
            bg="lightblue")

nupp3=Button(raam,
            text="gruzia",
            font="Algerian",
            height=2, 
            width=15,
            relief=RAISED,
            command=gruzia,
            bg="lightblue")

nupp4=Button(raam,
            text="shahmati",
            font="Algerian",
            height=2, 
            width=15,
            relief=RAISED,
            command=shahmat,
            bg="lightblue")

nupp5=Button(raam,
            text="svetofor Z",
            font="Algerian",
            height=2, 
            width=15,
            relief=RAISED,
            command=svetoforZ,
            bg="lightblue")

nupp6=Button(raam,
            text="svetofor O",
            font="Algerian",
            height=2, 
            width=15,
            relief=RAISED,
            command=svetoforO,
            bg="lightblue")

nupp7=Button(raam,
            text="svetofor K",
            font="Algerian",
            height=2, 
            width=15,
            relief=RAISED,
            command=svetoforK,
            bg="lightblue")

nupp.place(x=0,y=550)
nupp2.place(x=150,y=550)
nupp3.place(x=300,y=550)
nupp4.place(x=450,y=550)
nupp5.place(x=600,y=550)
nupp6.place(x=600,y=500)
nupp7.place(x=600,y=450)






raam.mainloop()