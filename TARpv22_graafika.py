
from tkinter import *
from webbrowser import *

def tab(event): 
    en=ent.get()
    url=open(en)
k=0
def klikker(event):
    global k
    k+=1
    btn.configure(text=k)
    en=ent.get()
    if k%2==0:
        tahvel.itemconfig(img_kast,image=img1)
        ent.configure(show="")
    else:
        tahvel.itemconfig(img_kast,image=img)
        ent.configure(show="*")

def klikkermaha(event):
    global k
    k-=1
    btn.configure(text=k)
def tekst_to_lbl(event):
    t=ent.get()
    lbl.configure(text=t)
    ent.delete(0,END) #2,7
def valik():
    val=var.get()
    ent.insert(END,val)
def checklist_to_l(event):
    v1=var1.get()
    v2=var2.get()
    jarjend=[v1,v2]
    l.delete(0,1)# read
    for item in jarjend:
        l.insert(END,item)


aken=Tk()
#aken.geometry("400x500")
aken.title("Minu esimene aken")
aken.iconbitmap("Poke-Ball.ico")
f=Frame(aken,bg="blue")
lbl=Label(f,text="Elemendid",bg="gold",fg="#AA4A44",font="Arial 20",height=5,width=15)
btn=Button(f,text="Vajuta siia",font="Arial 24",relief=GROOVE,width=15)#SUNKEN, RAISED
pas=Entry(f,show="*",fg="blue",bg="lightblue",width=15,font="Arial 20",justify=CENTER)
ent=Entry(f,fg="blue",bg="lightblue",width=15,font="Arial 20",justify=CENTER)
ent.insert(0, "password")
def clear_all(event):
    ent.delete(0,END)
ent.bind("<Button-1>",clear_all)
var=IntVar() #StringVar()
r1=Radiobutton(f,text="Esimene",font="Algerian 14",variable=var,value=1,command=valik)
r2=Radiobutton(f,text="Teine",font="Algerian 14",variable=var,value=2,command=valik)
r3=Radiobutton(f,text="Kolmas",font="Algerian 14",variable=var,value=3,command=valik)
var1=StringVar()
var2=StringVar()
c1=Checkbutton(f,text="Esimene",font="Arial 20",variable=var1,onvalue="Esimene on valitud",offvalue="Esimene on peidetud")
c2=Checkbutton(f,text="Teine",font="Arial 20",variable=var2,onvalue="Teine on valitud",offvalue="Teine on peidetud")
l=Listbox(f,height=2,width=20)

tahvel=Canvas(aken,width=260,height=260,bg="gold",bd=0)
img=PhotoImage(file="Premier-Ball-256.png")#.subsample(2)
img1=PhotoImage(file="Poke-Ball-256.png")
img_kast=tahvel.create_image(2,2,image=img,anchor=NW)

btn.bind("<Button-1>",klikker) #lkm
btn.bind("<Double-1>",tab) #Button-2 rattas
btn.bind("<Button-3>",klikkermaha) #pkm
ent.bind("<Return>",tab)#Enter
c1.deselect()
c2.deselect()
ob=[lbl,btn,ent,r1,r2,r3,l,c1,c2]
for i in range(len(ob)):
    ob[i].pack()
f.grid(row=0,column=0)
tahvel.grid(row=0, column=1)

aken.mainloop()
