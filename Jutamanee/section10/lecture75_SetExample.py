setTest  = {"apple","banana","orange"}
# print(setTest[0])
'''*** เนื่องจาก set มีลำดับไม่แน่นอน จึงไม่สามารถรองรับการเรียกใช้งาน index'''

for x in setTest:
    print(x)
'''ใช้งานกับ Loop ได้'''

print("apple" in setTest)
'''คำตอบที่ได้คือ True เพราะ ใน setTest มี apple ข้างใน '''

'''ไม่สามารถเปลี่ยนของใน set ได้ แต่สามารถลบของก่อน แลัวใส่ของใหม่เข้าไปแทนได้'''