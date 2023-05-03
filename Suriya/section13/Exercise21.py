from tkinter import *
import math


def leftClickButton(event):
    bmi = calculateBmi()
    bmiResult = checkBmi(bmi)
    labelResult.configure(text="{:.2f}".format(bmi))
    labelResult2.configure(text=bmiResult)


def calculateBmi():
    bmi = float(textBoxWeight.get()) / math.pow(float(textBoxHeight.get()) / 100, 2)
    return bmi


def checkBmi(bmi):
    result = ""
    if bmi >= 30.0:
        result = "Too fat"
    elif 25.0 <= bmi <= 29.9:
        result = "Fat"
    elif 23.0 <= bmi <= 24.9:
        result = "Over normal"
    elif 18.6 <= bmi <= 22.9:
        result = "Normal"
    else:
        result = "Too thin"

    return result


MainWindow = Tk()
labelHeight = Label(MainWindow, text="ส่วนสูง (cm.)")
labelHeight.grid(row=0, column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0, column=1)
labelWeigth = Label(MainWindow, text="น้ำหนัก (Kg.)")
labelWeigth.grid(row=1, column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1, column=1)
calculateButton = Button(MainWindow, text="คำนวน")
calculateButton.bind('<Button-1>', leftClickButton)
calculateButton.grid(row=2, column=0)
labelResult = Label(MainWindow, text="ผลลัพธ์")
labelResult.grid(row=2, column=1)
labelResult2 = Label(MainWindow, text="ผลประเมิน")
labelResult2.grid(row=3, column=1)

MainWindow.mainloop()
