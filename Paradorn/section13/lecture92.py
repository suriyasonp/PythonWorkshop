from tkinter import *

def sayHelloWorld():
    print("abbb")

mainWindows = Tk()
button = Button(mainWindows,text ="Click me",command= sayHelloWorld)
button.place(x=50,y=50)


mainWindows.mainloop()
