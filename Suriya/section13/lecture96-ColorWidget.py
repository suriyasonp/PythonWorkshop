from tkinter import *

displayText = ""


def sayHelloWorld():
    return "Hello World"


def ClickSomething():
    result = sayHelloWorld()
    displayText = result


mainWindow = Tk()
Button(mainWindow, text="Click me", width=20, bg="yellow", fg="blue", command=sayHelloWorld).grid(row=0)
Button(mainWindow, text="Click me2", command=sayHelloWorld).grid(row=1)
Button(mainWindow, text="Click me3", command=sayHelloWorld).grid(row=2, column=1)
Label(mainWindow, text=sayHelloWorld(), width=30, foreground="red", background="#CCCCCC").grid(row=3, column=2)

phone = StringVar()
home = Radiobutton(mainWindow, text='Home', variable=phone, value='home').grid(row=4)
office = Radiobutton(mainWindow, text='Office', variable=phone, value='office').grid(row=5)
cell = Radiobutton(mainWindow, text='Mobile', variable=phone, value='cell').grid(row=6)

mainWindow.mainloop()
