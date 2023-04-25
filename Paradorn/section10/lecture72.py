def showInvoice():
    total = 0
    print("--------- My shop------")
    for number in range(len(menuList)):
        total += float(menuList[number][1])
        print(menuList[number])

    print(total)


menuList = []
temp = [[10, 10], [20, 20]]

while True:
    menuName = input("Please Enter Menu :")
    if menuName.lower() == "exit":
        break
    else:
        menuPrice = input("Price :")
        menuList.append([menuName, menuPrice])
print(menuList)
print("------")
showInvoice()
