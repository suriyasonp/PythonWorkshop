'''List of string methods available in Python 3.'''
'''https://www.qhmit.com/python/reference/python_3_string_methods.cfm '''

a = "Mushroooom soup"
print(a.count("O"))
print(a.count("o"))
print(a.count("oo"))
print(a.count("ooo"))
print(a.count("Homer"))
print(a.count("o", 4, 7))
print(a.count("o", 7))

'''ฟังก์ชั่น count() นับจำนวนของ ของใน () ว่าในชุด String มีกี่ตัว'''

b = "Fitness"
print(b.find("F"))
print(b.find("f"))
print(b.find("n"))
print(b.find("ness"))
print(b.find("ess"))
print(b.find("z"))
print(b.find("Homer"))

'''ฟังก์ชั่น find()หากหาข้อไม่เจอจะ Return ค่า -1 '''

c = "123"
print(c.isdecimal())
'''ฟังก์ชั่น isdecimal() หากของเป็นเลขฐาน 10 จะ Return ค่าเป็น True หากไม่ใช่จะ Return เป็น False '''