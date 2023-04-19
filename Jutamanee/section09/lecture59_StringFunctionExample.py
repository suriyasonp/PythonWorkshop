name = input("Firstname :").capitalize()
lastName = input("Lastname :").capitalize()

print("Hello %s" % (name))
print("Hello !! %s %s !" % (name,lastName))

'''print("Hello !! %s %s !" % (name.capitalize(),lastName))'''
'''ฟังก์ชั่น capitalize() จะช่วยทำให้อักษรตัวแรกเป็นตัวใหญ่เสมอ '''

text = "Pop"
'''print("-----------Welcome-----------")'''
textFormatted = "Welcome %s"%(text)
print(textFormatted.center(21,"-"))
'''ฟังก์ชั่น center() จะช่วยทำให้ String อยู่ตรงกลาง โดยรวมสัญลักษณ์ - จะต้องมีจำนวนทั้งหมดรวม 21 ตัว'''

print(len(text))
'''ฟังก์ชั่น len() จะช่วยทำให้นับจำนวนของสตริง '''
