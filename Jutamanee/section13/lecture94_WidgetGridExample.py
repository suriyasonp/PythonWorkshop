from tkinter import *

def sayHelloWorld():
   print("Hello World")

MainWindow = Tk()

# button = Button(MainWindow,text = "Click me",command = sayHelloWorld)
# button.place(x = 50, y = 20)
# button2 = Button(MainWindow,text = "Click me",command = sayHelloWorld)
# button2.place(x = 150, y = 120)

#ใช้คำสั่งgrid()
button3 = Button(MainWindow,text = "Click me1",command = sayHelloWorld).grid(row=0,column=1)
button4 = Button(MainWindow,text = "Click me2",command = sayHelloWorld).grid(row=2,column=1)
button4 = Button(MainWindow,text = "Click me3",command = sayHelloWorld).grid(row=0,column=2)

'''Notes: หากสังเกตการกำหนด layout button2 แกน y มีการเพิ่มค่า 120 
แต่ตำแหน่งปุ่ม ใน widget จะสวนทางวามเป็นจริงของกราฟ ค่าจะถูกแสดงมีค่าลดลง โดยใช้คำสั่ง .place ในการจัดการ'''
MainWindow.mainloop()

