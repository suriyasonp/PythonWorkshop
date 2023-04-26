from tkinter import *
def sayHelloWorld():
    print("HelloWorld")
main = Tk()
label = Label(main, text = "Hello World", width=20, fg = "red", bg = "blue",font=("Helvetica",76),anchor=E).grid(row=0,column=1)
main.mainloop()