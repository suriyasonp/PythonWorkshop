from tkinter import *
import  math
def leftClickButton(event):
    print(float(textBoxWeigth.get()) / math.pow(float(textBoxHeight.get())/100,2))
    labelResult.configure(text=float(textBoxWeigth.get()) / math.pow(float(textBoxHeight.get())/100,2))

mainWindow = Tk()
labelHeight = Label(mainWindow, text="ส่วนสูง (cm.)")
labelHeight.grid(row=0, column=0)
textBoxHeight = Entry(mainWindow)
textBoxHeight.grid(row=0,column=1)
labelWeigth = Label(mainWindow,text="น้ำหนัก (Kg.)")
labelWeigth.grid(row=1,column=0)
textBoxWeigth = Entry(mainWindow)
textBoxWeigth.grid(row=1,column=1)

calculateButton = Button(mainWindow,text = "คำนวณ ",fg="black")
calculateButton.bind('<Button-1>',leftClickButton)
calculateButton.grid(row=2,column=0)

labelResult = Label(mainWindow,text="ผลลัพท์")
labelResult.grid(row=2,column=1)


mainWindow.mainloop()

