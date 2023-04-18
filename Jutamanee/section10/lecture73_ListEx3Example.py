systemMenu = {"ข้าวหมกไก่":"45","ข้าวมันไก่":"40","ข้าวมันไก่ผสม":"50","ข้าวมันไก่พิเศษ":"45"}
menuList = []
def showBill():
    totalprice = 0
    print("----My food----")
    for number in range(len(menuList)):
        print(menuList[number][0],menuList[number][1])
        totalprice += int(menuList[number][1])
    print("Total :", totalprice)
while True:
   menuName = input("Plese Enter Menu :")
   if (menuName.lower() == "exit"):
      break
   else:
    menuList.append([menuName,systemMenu[menuName]])

showBill()


