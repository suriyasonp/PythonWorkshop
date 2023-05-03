from tkinter import *

displayText = ""


def sayHelloWorld():
    return "Hello World"


def ClickSomething():
    result = sayHelloWorld()
    displayText = result


mainWindow = Tk()
Button(mainWindow, text="Click me", command=sayHelloWorld).grid(row=0)
Button(mainWindow, text="Click me2", command=sayHelloWorld).grid(row=1)
Button(mainWindow, text="Click me3", command=sayHelloWorld).grid(row=2, column=1)
Label(mainWindow, text=sayHelloWorld()).grid(row=3, column=2)
mainWindow.mainloop()
