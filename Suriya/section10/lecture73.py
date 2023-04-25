# refactor from lecture72

systemMenu = {"Menu1": 45, "Menu2": 40, "Menu3": 50, "Menu4": 45}
menuList = []

print(systemMenu)
def showBill():
    totalPrice = 0
    print("Smile Cooker".center(20, "-"))
    for i in range(len(menuList)):
        totalPrice += float(menuList[i][1])
        print(str(i + 1), " Item:" + menuList[i][0] + "   Price: " + str(menuList[i][1]))
    print("Total Price: ", totalPrice)


menuList = []
while True:
    menuName = input("Please enter menu: ").capitalize()
    if (menuName.lower() == "exit"):
        break
    else:
        menuList.append([menuName, systemMenu[menuName]])

print("DEBUG".center(20, "-"))
print(menuList)
print()
showBill()
