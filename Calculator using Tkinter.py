from tkinter import *
from functools import partial

win = Tk()

def sum(label,x1,x2):
    n1 = (x1.get())
    n2 = (x2.get())
    sum =  int(n1) + int(n2)
    label.config(text='Sum : %d' %sum)

def sub(label, x1,x2):
    n1 = (x1.get())
    n2 = (x2.get())
    sub = int(n1) - int(n2)
    label.config(text='Sub : %d' %sub)

def mul(label, x1, x2):
    n1 = (x1.get())
    n2 = (x2.get())
    mul = int(n1) * int(n2)
    label.config(text='Product : %d' %mul)

def div(label, x1, x2):
    n1 = x1.get()
    n2 = x2.get()
    div = int(n1) / int(n2)
    label.config(text='Division : %d' %div)

l1 = Label(win, text='First number: ')
l1.grid(row=1, column=0)
l2 = Label(win, text='Second number: ')
l2.grid(row=2, column=0)
label = Label(win)
label.grid(row=6, column=2)

x1 = StringVar()
x2 = StringVar()

e1 = Entry(win, textvariable=x1)
e1.grid(row=1, column=2)
e2 = Entry(win, textvariable=x2)
e2.grid(row=2, column=2)
sum = partial(sum,label, x1, x2)
button = Button(win, text='ADDITION', command=sum)
button.grid(row=3, column=0)
sub = partial(sub, label, x1, x2)
button2 = Button(win, text='SUBTRACT', command=sub)
button2.grid(row=3, column=1)
mul = partial(mul, label, x1, x2)
button3 = Button(win, text='MULTIPLY', command=mul)
button3.grid(row=3, column=2)
div = partial(div, label, x1, x2)
button4 = Button(win, text='DIVISION', command=div)
button4.grid(row=3, column=3)

win.mainloop()