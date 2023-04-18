menuList = []
def showBill():
    print("----My food----")
    for number in range(len(menuList)):
        print(menuList[number][0], "Price: " + menuList[number][1])

while True:
   menuName = input("Plese Enter Menu :")
   if (menuName.lower() == "exit"):
      break
   else:
    menuPrice = input("Price :")
    menuList.append([menuName,menuPrice])
    '''คำสั่งใน append คือการเพิ่มสมาชิกเข้าไปใน List'''
'''Ex.[['A', '20'], ['B', '30']] => ในList ใหญ่่ จะมี list ย่อยๆ '''
showBill()


