
myFriends = ['prame','guide','veen']
print(myFriends)

'''Ex1.การเพิ่มข้อมูลใน List '''
myFriends.append('bank')
'''append()  ฟังก์ชั่นในการเพิ่มสมาชิกตัวใหม่เข้าไปใน List ข้อมูล '''
print(myFriends)

'''Ex2.การลบข้อมูลใน List '''
myFriends.remove('guide')
'''.remove() ฟังก์ชั่นในการลบข้อมูล โดยเราต้องระบุข้อมูลที่ต้องการลบด้วย'''
print(myFriends)

'''Ex3.การแก้ไขข้อมูลใน List '''
myFriends[1]='deee'
print(myFriends)

del myFriends[0]
'''del คือ การลบข้อมูล โดยระบุลำดับข้อมูลที่ต้องการลบ'''
print(myFriends)
