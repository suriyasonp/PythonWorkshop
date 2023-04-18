fruits = {"apple","banana","pineapple","orange"}
print(fruits)

fruits.add("Grape")
print(fruits)

fruits.remove("apple")
print(fruits)

'''fruits.clear()
print(fruits)'''
'''การใช้งาน clear มันจะเคลียร์ค่าข้อมูลทั้งหมดใน fruits เหลือเป็น set() เปล่าๆ'''

'''del fruits
print(fruits)'''
'''การใช้งานฟังก์ชั่น del คือ การลบข้อมูลทั้งก้อนของ fruits'''

userInput= int(input("Enter Number of Your Favorite Fruits: "))
myFruits=set()
while (len(myFruits)<userInput):
    myFruits.add(input("Fruits: "))
print(myFruits)
'''***Note:
หากเปรียบเทียบการใช้งาน Set กับ list จะคล้ายกัน แต่ Set จะไม่สามารถมีข้อมูลซ้ำได้ กรณีที่เป็นสิ่งเดียวกันแต่ใช้งานตัวพิมพ์เล็ก พิมพ์ใหญ่ ก็ถือว่าต่างกัน'''