from tkinter import *
import tkinter.messagebox

#Þegar ýtt er á radiobutton
def beenClicked():
    radioValue = relStatus.get()
    print (radioValue)
    tkinter.messagebox.showinfo("Þú ýttir á", radioValue)
    return

#Til að breita text í boxi
def changeLabel():
    name = "Takk fyrir að smella " + yourName.get()
    labelText.set(name)
    yourName.delete(0,END)
    yourName.insert(0, "Ég heiti Eva")

#Býr til glugga
gluggi=Tk()
gluggi.title("Verkefni 001")
gluggi.geometry("450x300+100+100")

#Býr til lable
labelText = StringVar()
labelText.set("sýnifæmi")
lable1 = Label(gluggi, textvariable=labelText, height=4)
lable1.pack()

#Býr til cheabok
checkBoxVal = IntVar()
cheakBox1 = Checkbutton(gluggi, variable=checkBoxVal, text="Þetta er Checkbox")
cheakBox1.pack()

#Býr til box til að skrifa
custName =  StringVar(None)
yourName = Entry(gluggi, textvariable=custName)
yourName.pack()

#Býr til radiobutton
relStatus = StringVar()
relStatus.set(None)
radio1 = Radiobutton(gluggi, text="Einhleypur", value="Einhleypur", variable=relStatus, command=beenClicked).pack()
radio1 = Radiobutton(gluggi, text="Giftur",value="Giftur", variable=relStatus, command=beenClicked).pack()

#Býr til takka
button1 = Button(gluggi, text="Smelltu hér", width=20, command=changeLabel)
button1.pack(side="bottom",padx=15,pady=15)

gluggi.mainloop()

#TEST