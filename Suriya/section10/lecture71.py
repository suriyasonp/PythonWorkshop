def showBill():
    totalPrice = 0
    print("Smile Cooker".center(20, "-"))
    for i in range(len(menuList)):
        totalPrice += float(priceList[i])
        print(str(i+1), " Item:" + menuList[i] + "   Price: " + str(priceList[i]))
    print("Total Price: ", totalPrice)

menuList = []
priceList = []
itemCollection = {}
while True:
    menuName = input("Please enter menu: ").lower()
    if (menuName.lower() == "exit"):
        break
    else:
        menuPrice = float(input("Price: "))
        menuList.append((menuName))
        priceList.append(menuPrice)
showBill()
