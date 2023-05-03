from tkinter import *
import math
def leftClickButton(event):
    print(float(textboxWeight.get())/math.pow(float(textboxHeight.get())/100,2))
    labelResult.configure(text=float(textboxWeight.get())/math.pow(float(textboxHeight.get())/100,2))
    '''/100 เพราะต้องการเปลี่ยนหน่วยจาก cm. เป็น เมตร'''
    '''configure() ใช้ในการ config ข้อความต่างๆ สามารถเปลี่ยนได้'''
    '''textbox = Entry() คือ การสร้าง Box '''
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

MainWindow.mainloop()

