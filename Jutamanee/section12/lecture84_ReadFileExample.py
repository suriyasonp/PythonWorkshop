file = open("demo.txt","r")
# print(file.read())
'''อ่านทั้งหมด'''
# print(file.read(5))
'''อ่าน 5 ตัวแรก'''
print(file.readline())
'''อ่านบรรทัดเดียว บรรทัดแรก'''
print(file.readline())
'''หากมีการเรียกใช้งาน readline() ซ้ำๆ โปรแกรมจะเลื่อนบรรทัดในการอ่านไปเรื่อยๆทีละครั้ง '''