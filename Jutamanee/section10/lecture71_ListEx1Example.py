menuList = []
priceList = []

def showBill():
    totalprice = 0
    print("----My food----")
    for number in range(len(menuList)):
        print(str(number + 1)+"."+menuList[number]," Price :"+priceList[number])
        totalprice += int(priceList[number])
    print("Total :", totalprice)
while True:
   menuName = input("Plese Enter Menu :")
   if (menuName.lower() == "exit"):
      break
   else:
    menuPrice = input("Price :")
    menuList.append(menuName)
    priceList.append(menuPrice)
showBill()




