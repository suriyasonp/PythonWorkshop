from tkinter import *

def leftClickButton(event):
    print("Left Click!!")
def rightClickButton(event):
    print("Double right Click!!")


main = Tk()
button = Button(main,text = "My Button!!" ,width=50,height=5,fg="red")
button.pack()
button.bind('<Button-1>',leftClickButton)
button.bind('<Double-3>',rightClickButton)
main.mainloop()

