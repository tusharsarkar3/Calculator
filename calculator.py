from tkinter import *
from math import exp, log, sin, cos, tan, sinh, cosh, tanh

root = Tk()
root.title("Calclator")

e = Entry(root,width="50",borderwidth="5")
e.grid(row="0",column="0",columnspan="3",padx="10",pady="10")

def button(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

def add():
    global f,math
    f =int(e.get())
    math="add"
    e.delete(0,END)

def sub():
    global f,math
    f =int(e.get())
    math="sub"
    e.delete(0,END)

def mul():
    global f,math
    f =int(e.get())
    math="mul"
    e.delete(0,END)

def div():
    global f,math
    f =int(e.get())
    math="div"
    e.delete(0,END)

def e_raised():
    global f, math
    f = int(e.get())
    math = "power"
    e.delete(0, END)

def ln():
    global f, math
    f = int(e.get())
    math = "ln"
    e.delete(0, END)

def log():
    global f, math
    f = int(e.get())
    math = "ln"
    e.delete(0, END)

def sin():
    global f, math
    f = int(e.get())
    math = "ln"
    e.delete(0, END)

def cos():
    global f, math
    f = int(e.get())
    math = "ln"
    e.delete(0, END)

def tan():
    global f, math
    f = int(e.get())
    math = "ln"
    e.delete(0, END)

def sinh():
    global f, math
    f = int(e.get())
    math = "ln"
    e.delete(0, END)

def cosh():
    global f, math
    f = int(e.get())
    math = "ln"
    e.delete(0, END)

def tanh():
    global f, math
    f = int(e.get())
    math = "ln"
    e.delete(0, END)

def equal():
    s= e.get()
    e.delete(0,END)
    if math == "add":
        e.insert(0,f+int(s))
    elif math == "sub":
        e.insert(0, f- int(s))
    elif math == "mul":
        e.insert(0, f*int(s))
    elif math == "div":
        e.insert(0, f/int(s))
    elif math == "power":
        e.insert(0, exp(s))
    elif math == "ln":
        e.insert(0, log(s))
    elif math == "log":
        e.insert(0, log(s,10))
    elif math == "sin":
        e.insert(0, sin(s))
    elif math == "cos":
        e.insert(0, cos(s))
    elif math == "tan":
        e.insert(0, tan(s))
    elif math == "sinh":
        e.insert(0, sinh(s))
    elif math == "cosh":
        e.insert(0, cosh(s))
    elif math == "ln":
        e.insert(0, tanh(s))
    e.delete(0,END)
    s=0

def clear():
    e.delete(0,END)

button_1 = Button(root,text="1", padx="40",pady="20",command=lambda: button(1))
button_2 = Button(root,text="2",padx="40",pady="20",command=lambda: button(2))
button_3 = Button(root,text="3",padx="40",pady="20",command=lambda: button(3))
button_4 = Button(root,text="4",padx="40",pady="20",command=lambda: button(4))
button_5 = Button(root,text="5",padx="40",pady="20",command=lambda: button(5))
button_6 = Button(root,text="6",padx="40",pady="20",command=lambda: button(6))
button_7 = Button(root,text="7",padx="40",pady="20",command=lambda: button(7))
button_8 = Button(root,text="8",padx="40",pady="20",command=lambda: button(8))
button_9 = Button(root,text="9",padx="40",pady="20",command=lambda: button(9))
button_0 = Button(root,text="0",padx="40",pady="20",command=lambda: button(0))
button_add = Button(root,text="+",padx="40",pady="20",command=add)
button_equal = Button(root,text="=",padx="80",pady="20",command=equal)
button_clear = Button(root,text="Clear",padx="80",pady="20",command=clear)
button_mutiply = Button(root,text="*",padx="80",pady="20",command=mul)
button_divide = Button(root,text="/",padx="40",pady="20",command=div)
button_substract = Button(root,text="-",padx="40",pady="20",command=sub)
button_exp = Button(root,text="e raised",padx="40",pady="20",command=exp)
button_ln = Button(root,text="ln",padx="40",pady="20",command=ln)
button_log = Button(root,text="log",padx="40",pady="20",command=log)
button_sin = Button(root,text="sin",padx="40",pady="20",command=sin)
button_cos = Button(root,text="cos",padx="40",pady="20",command=cos)
button_tan = Button(root,text="tan",padx="40",pady="20",command=tan)
button_sinh = Button(root,text="sinh",padx="40",pady="20",command=sinh)
button_cosh = Button(root,text="cosh",padx="40",pady="20",command=cosh)
button_tanh = Button(root,text="tanh",padx="40",pady="20",command=tanh)

button_7.grid(row="1", column="0")
button_8.grid(row="1", column="1")
button_9.grid(row="1", column="2")
button_4.grid(row="2", column="0")
button_5.grid(row="2", column="1")
button_6.grid(row="2", column="2")
button_1.grid(row="3", column="0")
button_2.grid(row="3", column="1")
button_3.grid(row="3", column="2")
button_0.grid(row="4", column="0")
button_add.grid(row="5",column="0")
button_equal.grid(row="4",column="1",columnspan="2")
button_clear.grid(row="5",column="1",columnspan="2")
button_divide.grid(row="1",column="3")
button_mutiply.grid(row="6",column="1",columnspan="2")
button_substract.grid(row="6",column="0")
button_exp.grid(row=2,column=3)
button_ln.grid(row=3,column=3)
button_log.grid(row=4,column=3)
button_sin.grid(row=5,column=3)
button_cos.grid(row=6,column=3)
button_tan.grid(row=7,column=0)
button_sinh.grid(row=7,column=1)
button_cosh.grid(row=7,column=2)
button_tanh.grid(row=7,column=3)

root.mainloop()