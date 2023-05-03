from tkinter import *

def sayHelloWorld():
   print("Hello World")

MainWindow = Tk()
button = Button(MainWindow,text = "Click me",command = sayHelloWorld).grid(row=0,column=1)
button2 = Button(MainWindow,text = "Click me",command = sayHelloWorld).grid(row=0,column=2)
button2 = Button(MainWindow,text = "Click me",command = sayHelloWorld).grid(row=1,column=0)
MainWindow.mainloop()



