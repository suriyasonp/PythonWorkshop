# refactor from lecture71
def showBill():
    totalPrice = 0
    print("Smile Cooker".center(20, "-"))
    for i in range(len(menuList)):
        totalPrice += float(menuList[i][1])
        print(str(i + 1), " Item:" + menuList[i][0] + "   Price: " + str(menuList[i][1]))
    print("Total Price: ", totalPrice)


menuList = []
while True:
    menuName = input("Please enter menu: ").lower()
    if (menuName.lower() == "exit"):
        break
    else:
        menuPrice = float(input("Price: "))
        menuList.append([menuName, menuPrice])

print("DEBUG".center(20, "-"))
print(menuList)
print()
showBill()
