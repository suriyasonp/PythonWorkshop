from tkinter import *

def sayHelloWorld():
    print("1345478")

mainWindows = Tk()
button = Button(mainWindows,text ="Click me",command= sayHelloWorld)
button.place(x=50,y=50)

mainWindows.mainloop()


MainWindows2 = Tk()
button2 = Button(MainWindows2,text ="Click me",command= sayHelloWorld)
button2.place(x=100,y=50)
MainWindows2.mainloop()