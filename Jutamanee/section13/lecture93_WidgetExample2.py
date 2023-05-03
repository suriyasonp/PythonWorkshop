from tkinter import *
'''tkinter คือ library'''
def sayHelloWorld():
    print("HelloWorld")

MainWindow = Tk()
'''MainWindow คือตัวแปร 1 ตัวที่เอาไว้เก็บ TK โดยที่สามารถสร่้างเป็นชื่ออื่นได้ (คือ ตัวหลักในการจัดการ GUI => Graphical User Interface) '''
button = Button(MainWindow,text="ClickMe",command=sayHelloWorld)

'''สำหรับส่วนต่างที่เราต้องการสร้าง ไม่ว่าจะเป็นปุ่ม จะต้องสร้างหลังจากมีการสร้าง Tk() เรียบร้อยแล้ว 
ส่วนประกอบต่างๆใน button ที่เรากำหนดเรียกว่า 
Attribute คือ  รูปแบบคุณลักษณะบางอย่าง หรือ คุณสมบัติของตัววัตถุหรือสื่งของต่างๆ  
ิBehavior คือ พฤติกรรม เช่น กล้องมี Behavior สามารถถ่ายรูปได้
command คือ เมื่อเรามีการคลิกปุ่ม ClickMe ให้เราเรียกใช้งานฟังก์ชั่น หรือ ทำงานอะไรต่ิ '''

button.place(x=50,y=20)
MainWindow.mainloop()

'''Notes: Event-Driven Programming => การทำงานของโปรแกรมที่ทำให้เกิดเหตุการณ์ต่างๆเกิดขึ้น 
เช่น เมื่อเราคลิกปุุ่ม  ClickMe ในหน้า Widget จะทำให้ข้อความ HelloWorld แสดงใน console ตามจำนวนครั้งที่เราคลิก '''