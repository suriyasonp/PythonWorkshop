def logIn():
    userNameInput = input("Enter username:")
    passwordInput = input("Enter password:")

    userNameValid = "abc"
    passwordValid = "1234"
    if userNameInput == userNameValid and passwordInput == passwordValid:
        return True
    else:
        return False


def showMenu():
    print("Authenticated success")
    print("----------Smile Shop-----------")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    userSelected = int(input(">>"))
    return userSelected


def vatCalculate(totalPrice):
    vat = 7
    netPrice = totalPrice * 1.07
    return netPrice


def priceCalculate():
    price1 = float(input("Enter Price-1: >>"))
    price2 = float(input("Enter Price-2: >>"))
    price3 = float(input("Enter Price-3: >>"))
    sumPrice = price1 + price2 + price3
    return vatCalculate(sumPrice)


if (logIn()):
    userSelected = showMenu()
    if (userSelected == 1):
        totalPrice = float(input("Enter total price:"))
        print("Net price: ", vatCalculate((totalPrice)))
    elif (userSelected == 2):
        print("Net price: ", priceCalculate())
else:
    print("Authentication error!")
