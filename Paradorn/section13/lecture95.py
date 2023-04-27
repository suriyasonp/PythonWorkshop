from tkinter import *

def sayHelloWorld():
   print("Hello World")

MainWindow = Tk()
button = Button(MainWindow,text = "Click me",command = sayHelloWorld,width=30,height=5).grid(row=0,column=1)
button2 = Button(MainWindow,text = "Click me",command = sayHelloWorld).grid(row=0,column=2)
button2 = Button(MainWindow,text = "Click me",command = sayHelloWorld).grid(row=1,column=0)
label = Label(MainWindow,text ="Hello",width=20).grid(row=2)
MainWindow.mainloop()



