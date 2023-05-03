from tkinter import *
'''tkinter คือ library'''
def sayHelloWorld():
    print("HelloWorld")
MainWindow = Tk()
button = Button(MainWindow,text="ClickMe",command=sayHelloWorld)
button.place(x=50,y=20)
MainWindow.mainloop()

'''Notes: Event-Driven Programming => การทำงานของโปรแกรมที่ทำให้เกิดเหตุการณ์ต่างๆเกิดขึ้น เช่น เมื่อเราคลิกปุุ่ม  ClickMe ในหน้า Widget จะทำให้ข้อความ HelloWorld แสดงใน console ตามจำนวนครั้งที่เราคลิก '''