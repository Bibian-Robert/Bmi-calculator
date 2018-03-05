from tkinter import *

a=Tk()
a.title("BMI CALCULATOR")
a.geometry("500x500+100+100")
n="arial",14,"bold"
def mycalc():
    a=var1.get()
    b=var2.get()
    result= '%.2f'%(a/(b**2))
    var3.set(result)
    # e3.delete(0,END)
    # e3.insert(0,float(var3))
def myclear():
    var1.set(0)
    var2.set(0)
    var3.set(0)

var1=DoubleVar()
var2=DoubleVar()
var3=DoubleVar()
label1=Label(a,text="Weight(kg)",font=(n),padx=0)
label1.grid(row=0,sticky=W)
label2=Label(a,text="Height(m)",font=(n),padx=0)
label2.grid(row=1,sticky=W)
label3=Label(a,text="BMI",font=(n),padx=0)
label3.grid(row=2,sticky=W)
e1=Entry(a,width=15,textvariable=var1)
e1.grid(row=0,column=1)
e2=Entry(a,width=15,textvariable=var2)
e2.grid(row=1,column=1)
e3=Entry(a,width=15,textvariable=var3)
e3.grid(row=2,column=1)

but1=Button(a,text="Calculate",font=(n),command=mycalc).grid(row=4,column=1)
but2=Button(a,text="Clear",font=(n),command=myclear).grid(row=4,column=0)
but3=Button(a,text="Exit",font=(n),command=a.destroy).grid(row=5,column=1)

a.mainloop()
