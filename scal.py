#Importing tkinter module
from tkinter import*
#window named root
root=Tk()
root.title("Scal")
root.iconbitmap(r"c.ico")

#Creating a box named e to input
e=Entry(root,width=10,borderwidth=5,font="Times 25")
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

#Simple arithmatic function
def badd(number):	
	current=e.get()
	e.delete(0,END)
	e.insert(0, str(current) + str(number))

def clear():
	e.delete(0,END)
def add():
	global fn
	global math
	math="add"
	fn=int(e.get())
	e.delete(0,END)

def minu():
	global fn
	global math
	math="minu"
	fn=int(e.get())
	e.delete(0,END)

def mul():
	global fn
	global math
	math="mul"
	fn=int(e.get())
	e.delete(0,END)

def div():
	global fn
	global math
	math="div"
	fn=int(e.get())
	e.delete(0,END)

#Condition
def equal():
	if math == "add":
		sn=e.get()
		e.delete(0,END)
		e.insert(0,fn+int(sn))
	if math == "minu":
		sn=e.get()
		e.delete(0,END)
		e.insert(0,fn-int(sn))
	if math == "mul":
		sn=e.get()
		e.delete(0,END)
		e.insert(0,fn*int(sn))
	if math == "div":
		sn=e.get()
		e.delete(0,END)
		e.insert(0,fn/int(sn))	

#BUTTION
b1=Button(root,text="1",padx=25,pady=1,command=lambda:badd(1),font="Times 14")
b2=Button(root,text="2",padx=25,pady=1,command=lambda:badd(2),font="Times 14")
b3=Button(root,text="3",padx=25,pady=1,command=lambda:badd(3),font="Times 14")
b4=Button(root,text="4",padx=25,pady=1,command=lambda:badd(4),font="Times 14")
b5=Button(root,text="5",padx=25,pady=1,command=lambda:badd(5),font="Times 14")
b6=Button(root,text="6",padx=25,pady=1,command=lambda:badd(6),font="Times 14")
b7=Button(root,text="7",padx=25,pady=1,command=lambda:badd(7),font="Times 14")
b8=Button(root,text="8",padx=25,pady=1,command=lambda:badd(8),font="Times 14")
b9=Button(root,text="9",padx=25,pady=1,command=lambda:badd(9),font="Times 14")
b0=Button(root,text="0",padx=25,pady=1,command=lambda:badd(0),font="Times 14")
bp=Button(root,text="+",padx=25,pady=1,command=add,font="Times 14")
bminu=Button(root,text="-",padx=25,pady=1,command=minu,font="Times 14")
bmul=Button(root,text="*",padx=25,pady=1,command=mul,font="Times 14")
bdiv=Button(root,text="/",padx=25,pady=1,command=div,font="Times 14")
be=Button(root,text="=",padx=60,pady=1,command=equal,font="Times 15")
bc=Button(root,text="Clear",padx=50,pady=1,command=clear,font="Times 13")

#Button position

b1.grid(row=3,column=0)
b2.grid(row=3,column=1)
b3.grid(row=3,column=2)

b4.grid(row=2,column=0)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)

b7.grid(row=1,column=0)
b8.grid(row=1,column=1)
b9.grid(row=1,column=2)

bp.grid(row=5,column=0)
b0.grid(row=4,column=0)
be.grid(row=5,column=1,columnspan=2)
bc.grid(row=4,column=1,columnspan=2)

bminu.grid(row=6,column=0)
bmul.grid(row=6,column=1)
bdiv.grid(row=6,column=2)

#Loop ender
root.mainloop()
