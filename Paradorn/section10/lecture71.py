

def showInvoice():
    total = 0
    print("--------- My shop------")
    for number in range(len(menuList)):
        print(menuList[number],priceList[number])
        total += float(priceList[number])
    print(total)

menuList = []
priceList = []

while True:
    menuName = input("Please Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price :")
        menuList.append(menuName)
        priceList.append(menuPrice)
print(menuList,priceList)
print("------")
showInvoice()
