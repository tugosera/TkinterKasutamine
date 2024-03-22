from tkinter import *
k=0
def vajuta():
    global k
    k+=1
    nupp.configure(text=k)
def vajuta_(event):
    global k
    k-=1
    nupp.configure(text=k)
def tst_psse(event):
    textbox.get()
    pealkiri.configure(text=t,
                       width=len(t))
    textbox.delete(0,END)
def valik():
    arv=var.get()
    textbox.insert(arv)




aken=Tk()
aken.geometry("300x300")
aken.iconbitmap('tiktok.ico')
aken.title("TikTok")
tekst="HUI HUI HUI HUI"
pealkiri=Label(aken,
              text=tekst,
              bg="#7c02b4",
              fg="#7ba5fd",
              font="Chiller",
              height=3,
              width=len(tekst))
textbox=Entry(aken,
              bg="#7ba5fd",
              fg="#7c02b4",
              font="Chiller",
              width=20,
              justify=CENTER)
nupp=Button(aken,
            text="Vajuta mind",
            font="Algerian",
            height=3, 
            width=10,
            relief=RAISED,
            bg="lightblue",
            command=vajuta)
f=Frame(aken)
var=IntVar()
e=Radiobutton(f,text="Esimine",variable=var,value=1,command=valik)
t=Radiobutton(f,text="teine",variable=var,value=2,command=valik)
kk=Radiobutton(f,text="kolmas",variable=var,value=3,command=valik)
nupp.bind("<Button-3>",vajuta_)
textbox.bind("<Return>",tst_psse)

obj=[pealkiri,textbox,nupp,f]
for i in obj:
    i.pack()
aken.mainloop()
obj2=[e,t,kk]
for i in range(len(obj2)):
    obj2[i].grid(row=0,column=1)
pealkiri.pack()
textbox.pack()
nupp.pack()
aken.mainloop()
