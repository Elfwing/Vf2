import sys
from tkinter import *
root = Tk()
root.title("Reiknivél")
num1=StringVar()

#breytur
global tala1
global takn
nr=0
tala1=0
tala2=0
summa=0

#reikni kóði fyrir takkar 
def clear():
    global summa
    txtDisplay.delete(0,END)
    summa=0
    return
def ein():
    txtDisplay.insert(END,1)
    return
def tve():
    txtDisplay.insert(END,2)
    return
def thr():
    txtDisplay.insert(END,3)
    return
def fjr():
    txtDisplay.insert(END,4)
    return
def fim():
    txtDisplay.insert(END,5)
    return
def six():
    txtDisplay.insert(END,6)
    return
def sjo():
    txtDisplay.insert(END,7)
    return
def att():
    txtDisplay.insert(END,8)
    return
def niu():
    txtDisplay.insert(END,9) 
    return
def nul():
    txtDisplay.insert(END,0)
    return
def plus():
    global tala1
    global takn
    takn ="+"
    t=int(txtDisplay.get())
    tala1=t
    txtDisplay.delete(0,END)
    return
def minus():
    global tala1
    global takn
    takn ="-"
    t=int(txtDisplay.get())
    tala1=t
    txtDisplay.delete(0,END)
    return
def sinnum():
    global tala1
    global takn
    takn ="*"
    t=int(txtDisplay.get())
    tala1=t
    txtDisplay.delete(0,END)
    return
def deiling():
    global tala1
    global takn
    takn ="/"
    t=int(txtDisplay.get())
    tala1=t
    txtDisplay.delete(0,END)
    return

def jafnt ():
    global tala1
    global takn
    if takn=="+":
        tala2=int(txtDisplay.get())
        summa=tala1+tala2
    elif takn=="-":
        tala2=int(txtDisplay.get())
        summa=tala1-tala2
    elif takn=="*":
        tala2=int(txtDisplay.get())
        summa=tala1*tala2
    elif takn=="/":
        tala2=int(txtDisplay.get())
        summa=round(tala1/tala2,2)

    txtDisplay.delete(0,END)
    txtDisplay.insert(0,summa)

#Býr til frames
frame1 = Frame(root)
frame1.pack(side=TOP)
frame2 = Frame(root)
frame2.pack(side=TOP)
frame3 = Frame(root)
frame3.pack(side=TOP)
frame4 = Frame(root)
frame4.pack(side=TOP)

#Gerir top glugga
txtDisplay=Entry(frame1, textvariable = num1, bd=20, insertwidth=3, font=30)
txtDisplay.pack(side=TOP)

#Býr til taka
button1 = Button(frame1, padx=16, pady=16, bd=8, fg="black", text="1",command=ein)
button1.pack(side=LEFT)
button1.config(height=1, width=2)

button2 = Button(frame1, padx=16, pady=16, bd=8, fg="black", text="2", command=tve, height=1, width=2)
button2.pack(side=LEFT)

button3 = Button(frame1, padx=16, pady=16, bd=8, fg="black", text="3", command=thr, height=1, width=2)
button3.pack(side=LEFT)

buttonDiv = Button(frame1, padx=16, pady=16, bd=8, fg="black", text="/", command=deiling, height=1, width=2)
buttonDiv.pack(side=LEFT)

button4 = Button(frame2, padx=16, pady=16, bd=8, fg="black", text="4", command=fjr, height=1, width=2)
button4.pack(side=LEFT)

button5 = Button(frame2, padx=16, pady=16, bd=8, fg="black", text="5", command=fim, height=1, width=2)
button5.pack(side=LEFT)

button6 = Button(frame2, padx=16, pady=16, bd=8, fg="black", text="6", command=six, height=1, width=2)
button6.pack(side=LEFT)

buttonMag = Button(frame2, padx=16, pady=16, bd=8, fg="black", text="*", command=sinnum, height=1, width=2)
buttonMag.pack(side=LEFT)

button7 = Button(frame3, padx=16, pady=16, bd=8, fg="black", text="7", command=sjo, height=1, width=2)
button7.pack(side=LEFT)

button8 = Button(frame3, padx=16, pady=16, bd=8, fg="black", text="8", command=att, height=1, width=2)
button8.pack(side=LEFT)

button9 = Button(frame3, padx=16, pady=16, bd=8, fg="black", text="9", command=niu, height=1, width=2)
button9.pack(side=LEFT)

buttonSub = Button(frame3, padx=16, pady=16, bd=8, fg="black", text="-", command=minus, height=1, width=2)
buttonSub.pack(side=LEFT)

buttonC = Button(frame4, padx=16, pady=16, bd=8, fg="black", text="C", command=clear, height=1, width=2)
buttonC.pack(side=LEFT)

button0 = Button(frame4, padx=16, pady=16, bd=8, fg="black", text="0", command=nul, height=1, width=2)
button0.pack(side=LEFT)

buttonEqu = Button(frame4, padx=16, pady=16, bd=8, fg="black", text="=", command=jafnt, height=1, width=2)
buttonEqu.pack(side=LEFT)

buttonAdd = Button(frame4, padx=16, pady=16, bd=8, fg="black", text="+", command=plus, height=1, width=2)
buttonAdd.pack(side=LEFT)

#lætur tóðan spilast aftur og aftur
root.mainloop()