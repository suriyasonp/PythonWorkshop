
def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    userName = "admin"
    password = "1234"
    if usernameInput == userName and passwordInput == password:
        return True
    else:
        return False
def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
def menuSelect():
    userSelected = int(input(">>"))
    return userSelected
def vatCalculate(totalPrice):
     vat = 7
     return totalPrice + (totalPrice * vat / 100)
def priceCalculate():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculate(price1 + price2)

if (login()):
    showMenu()
    userSelected = menuSelect()
    if (userSelected == 1):
        totalPrice = float(input("Enter total price:"))
        print("Net price: ", vatCalculate((totalPrice)))
    elif (userSelected == 2):
        print("Net price: ", priceCalculate())
else:
    print("Login error!")