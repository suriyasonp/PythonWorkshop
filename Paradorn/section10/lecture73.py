def showInvoice():
    total = 0
    print("--------- My shop------")
    for number in range(len(menuList)):
        total += float(menuList[number][1])
        print(menuList[number])
    print(total)


systemMenu = {"ข้าวมันไก่": 50, "ข้าวหมูกรอบ": 55, "ข้าวกระเพราหมูสับ": 56}
menuList = []

while True:
    menuName = input("Please Enter Menu :")
    if menuName.lower() == "exit":
        break
    else:
        menuList.append([menuName, systemMenu[menuName]])
print(menuList)
print("------")
showInvoice()
