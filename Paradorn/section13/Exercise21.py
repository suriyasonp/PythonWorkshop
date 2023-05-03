from tkinter import *
import  math
def leftClickButton(event):
    print(float(textBoxWeigth.get()) / math.pow(float(textBoxHeight.get())/100,2))
    labelResult.configure(text=float(textBoxWeigth.get()) / math.pow(float(textBoxHeight.get())/100,2))
    calcuRateCheck()

def calcuRateCheck():
    resultCheck = float(textBoxWeigth.get()) / math.pow(float(textBoxHeight.get())/100,2)
    if resultCheck >= 30.0:
        print("อ้วนมาก")
        totalResutl.configure(text="อ้วนมาก")
    elif 25.0 <= resultCheck <= 29.9:
        print("อ้วน")
        totalResutl.configure(text="อ้วน")
    elif 23.0 <= resultCheck <= 24.9:
        print("น้ำหนักเกิน")
        totalResutl.configure(text="น้ำหนักเกิน")
    elif 18.6 <= resultCheck <= 22.9:
        print("น้ำหนักปกติ")
        totalResutl.configure(text="น้ำหนักปกติ")
    else:
        print("ผอมเกินไป")
        totalResutl.configure(text="ผอมเกินไป")



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

totalResutl = Label(mainWindow,text="สถานะ")
totalResutl.grid(row=3,column=1)


mainWindow.mainloop()

