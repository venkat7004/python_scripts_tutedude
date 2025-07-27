from tkinter import *
# This script creates a simple GUI application using Tkinter in Python.

wnd= Tk()
wnd.title("Simple Calculator")
wnd.geometry("320x270")

e1 = Entry(wnd, width=25,borderwidth=5, font=("Arial", 14) )   

b1 = Button(wnd, text=" 1 ",width=10,borderwidth=5,command=lambda: click(1))
b2 = Button(wnd, text=" 2 ",width=10,borderwidth=5,command=lambda: click(2))
b3 = Button(wnd, text=" 3 ",width=10,borderwidth=5,command=lambda: click(3))

b4 = Button(wnd, text=" 4 ",width=10,borderwidth=5,command=lambda: click(4))
b5 = Button(wnd, text=" 5 ",width=10,borderwidth=5,command=lambda: click(5))
b6 = Button(wnd, text=" 6 ",width=10,borderwidth=5,command=lambda: click(6))

b7 = Button(wnd, text=" 7 ",width=10,borderwidth=5,command=lambda: click(7))
b8 = Button(wnd, text=" 8 ",width=10,borderwidth=5,command=lambda: click(8))
b9 = Button(wnd, text=" 9 ",width=10,borderwidth=5,command=lambda: click(9))

b0 = Button(wnd, text=" 0 ",width=10,borderwidth=5,command=lambda: click(0))

def add():
    num1 = e1.get()
    global n1
    global math_op
    math_op = "add"
    n1 = float(num1)
    e1.delete(0, END)

b10 = Button(wnd, text=" + ",width=10,borderwidth=5,command=add)
def subtract():
    num1 = e1.get()
    global n1
    global math_op
    math_op = "sub"
    n1 = float(num1)
    e1.delete(0, END)

b11 = Button(wnd, text=" - ",width=10,borderwidth=5,command=subtract)
def multiply():
    num1 = e1.get()
    global n1
    global math_op
    math_op = "mul"
    n1 = float(num1)
    e1.delete(0, END)

b12 = Button(wnd, text=" * ",width=10,borderwidth=5,command=multiply)
def divide():
    num1 = e1.get()
    global n1
    global math_op
    math_op = "div"
    n1 = float(num1)
    e1.delete(0, END)

b13 = Button(wnd, text=" / ",width=10,borderwidth=5,command=divide)
def equal():
    try:
        n2   = e1.get()
        e1.delete(0, END)
        if math_op == "add":
            e1.insert(0, n1 + float(n2))
        elif math_op == "sub":
            e1.insert(0, n1 - float(n2))
        elif math_op == "mul":
            e1.insert(0, n1 * float(n2))
        elif math_op == "div":
            if float(n2) != 0:
                e1.insert(0, round(n1 / float(n2),2))
            else:
                e1.insert(0, "Error")
    except ValueError:
        e1.insert(0, "Error")    

b14 = Button(wnd, text=" = ",width=10,height=3,borderwidth=5,command=equal)
b15 = Button(wnd, text=" Clear ",width=24,borderwidth=5,command=lambda: clear())

e1.place(x=15, y=10)
b1.place(x=15, y=50)
b2.place(x=110, y=50)
b3.place(x=210, y=50)
b4.place(x=15, y=80)
b5.place(x=110, y=80)
b6.place(x=210, y=80)
b7.place(x=15, y=110)
b8.place(x=110, y=110)
b9.place(x=210, y=110)
b0.place(x=15, y=140)
b10.place(x=110, y=140)
b11.place(x=210, y=140)
b12.place(x=15, y=170)
b13.place(x=110, y=170)
b14.place(x=210, y=170)
b15.place(x=15, y=200)

# e1.pack()
# e2.pack()
# wnd.pack()

def click(num):
    result = e1.get() 
    e1.delete(0, END)
    e1.insert(0, str(result)+str(num))

def clear():
    e1.delete(0, END)
mainloop()
