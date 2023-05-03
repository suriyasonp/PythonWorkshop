from tkinter import *

displayText = ""


def sayHelloWorld():
    return "Hello World"


def ClickSomething():
    result = sayHelloWorld()
    displayText = result


mainWindow = Tk()
button = Button(mainWindow, text="Click me", command=sayHelloWorld)
button.place(x=50, y=20)
label = Label(mainWindow, text=sayHelloWorld())
label.place(x=50, y=50)
mainWindow.mainloop()
