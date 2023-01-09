#importar gögn sem þarf til að búa til takka
from tkinter import *
root = Tk()


Button(root, text="A").pack(side=LEFT, expand=YES, fill=Y) #takkinn er vinstar megin með billi og fillir up y-ásinn
Button(root, text="B").pack(side=TOP, expand=YES, fill=BOTH) #takkinn er uppi með billi og fillir báða ásana (expand gerir ekkert því fill virkar á báða ásana)
Button(root, text="C").pack(side=RIGHT, expand=NO, fill=NONE, anchor=NE) #takkinn er hægra megin og er norðaustan megin á skjánnum (upp og hægri) 
Button(root, text="D").pack(side=LEFT, expand=NO, fill=Y) #takkinn er vinstar megin og fillir up y-ásinn
Button(root, text="E").pack(side=TOP, expand=NO, fill=BOTH) #takkinn er uppi og fillir báða ásana
Button(root, text="F").pack(side=RIGHT, expand=NO, fill=NONE) #takkinn er hægra megin (expand=NO, fill=NONE eru sjálfgefnir)
Button(root, text="G").pack(side=BOTTOM, expand=YES, fill=Y) #takkinn er niðri með billi og fillir y-ásinn
Button(root, text="H").pack(side=TOP, expand=NO, fill=BOTH) #takkinn er uppi og fillir báð ásana
Button(root, text="I").pack(side=RIGHT, expand=NO) #takkinn er hægra megin (sama og F)
Button(root, text="J").pack(anchor=SE)  #takkinn er suðaustan megin (hægri og niðri)

#lætur tóðan spilast aftur og aftur
root.mainloop()