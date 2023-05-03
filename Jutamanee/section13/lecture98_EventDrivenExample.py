from tkinter import *
def leftClickButton(event):
    print("Left Click!!")
def doubleClickButton(event):
    print("Double Click!!")

main = Tk()
button = Button(main,text="My Button !!")
button.pack()
# button.bind('<Button-1>',leftClickButton)
button.bind('<Button-1>',leftClickButton)
button.bind('<Double-1>',doubleClickButton)
main.mainloop()

'''bind() คือ ฟังก์ชั่นสำหรับผูกเหตุการณ์และฟังก์ชั่นไว้ด้วยกัน'''
'''Button-1 คือ ปุ่มของเม้าส์ซ้ายสุด '''
'''Button-2 คือ ปุ่มของเม้าส์ตรงกลาง '''
'''Button-3 คือ ปุ่มของเม้าส์ขวามือ หรือ คลิกขวาถูกคลิก '''

