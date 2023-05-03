from tkinter import *
import math
def leftClickButton(event):
    print(float(textboxWeight.get())/math.pow(float(textboxHeight.get())/100,2))
    bmiResult = float(textboxWeight.get())/math.pow(float(textboxHeight.get())/100,2)
    labelResult.configure(text=float(textboxWeight.get())/math.pow(float(textboxHeight.get())/100,2))

    if  bmiResult >= 25.0 and  bmiResult<=29.9 :
        criteriaResult.configure(text="อ้วน!")
        print("อ้วน!")
    elif  bmiResult >= 23.0 and  bmiResult<=24.9:
        criteriaResult.configure(text="น้ำหนักเกิน")
        print("น้ำหนักเกิน")
    elif  bmiResult >= 18.6 and  bmiResult<=22.9:
        criteriaResult.configure(text="น้ำหนักปกติ เหมาะสม")
        print("น้ำหนักปกติ เหมาะสม")
    elif  bmiResult < 18.9:
        criteriaResult.configure(text="อ้วนมาก")
    else:
        criteriaResult.configure(text="อ้วนมาก!!!!")
        print("อ้วนมาก!!!!")
def doubleClickButton(event):
    print("Double Click!!")

MainWindow = Tk()
labelHeight = Label(MainWindow,text="ส่วนสูง(cm.)")
labelHeight.grid(row=0,column=0)
textboxHeight = Entry(MainWindow)
textboxHeight.grid(row=0,column=1)

labelWeight = Label(MainWindow,text="น้ำหนัก(Kg.)")
labelWeight.grid(row=1,column=0)
textboxWeight = Entry(MainWindow)
textboxWeight.grid(row=1,column=1)

calculateButton = Button(MainWindow,text="คำนวณ")
calculateButton.bind('<Button-1>',leftClickButton)
calculateButton.grid(row=2,column=0)

labelResult = Label(MainWindow,text="ผลลัพธ์")
labelResult.grid(row=2,column=1)

criteriaResult = Label(MainWindow, text = " ")
criteriaResult.grid(row=4,column=1)

MainWindow.mainloop()

