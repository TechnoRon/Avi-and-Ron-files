from tkinter import *
from tkinter import ttk
root = Tk()

entry1 = ttk.Entry(root , text = "test")
entry1.grid(row = 1, column = 1)
entry2 = ttk.Entry(root, text = 'type your second number here')
entry2.grid(row = 1, column = 2)
entry3 = ttk.Entry(root , text = "Result")
entry3.grid(row = 6, column = 2)


def add():
    a = entry1.get()
    b = entry2.get()
    entry3.insert(0,str(int(a)+int(b)))

def multiply():
    a = entry1.get()
    b = entry2.get()
    entry3.insert(0,str(int(a)*int(b)))
 

def subtract():
    a = entry1.get()
    b = entry2.get()
    entry3.insert(0,str(int(a)-int(b)))

def divide():
    a = entry1.get()
    b = entry2.get()
    entry3.insert(0,str(int(a)/int(b)))

def clear():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)

def percent():
    a = entry1.get()
    b = entry2.get()
    entry3.insert(0,str(int(a)%int(b)))





button1 = ttk.Button(root, text = 'add', command = add).grid(row = 3, column = 1)
button2 = ttk.Button(root, text = 'multiply', command = multiply).grid(row = 4, column = 1)
button3 = ttk.Button(root, text = 'subtract', command = subtract).grid(row = 5, column = 1)
button4 = ttk.Button(root, text = 'divide', command = divide).grid(row = 6, column = 1)
button5 = ttk.Button(root, text = 'clear', command = clear).grid(row = 4, column = 2)
button6 = ttk.Button(root, text = 'percent', command = percent).grid(row = 7, column = 1)












    
