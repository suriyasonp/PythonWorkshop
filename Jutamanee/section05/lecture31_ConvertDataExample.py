print(type(10+5.0))
'''print(type("10"+5.0)) **Error:ข้อมูลคนละประเภทกัน ไม่สามารถนำมาบวกกันได้'''
print(type("10"+"5.0"))
print(type("String"))

a="Jutamanee"
b="thongbor"
print(a+b)

c="10"
d=5
e=int(c)+d
'''**ใส่ประเภทข้อมูลที่ต้องการแปลงไว้ข้างหน้า ตามด้วย (ตัวแปรที่ต้องการแปลง)'''
print(e)
f=float(c)+d
print(f)


