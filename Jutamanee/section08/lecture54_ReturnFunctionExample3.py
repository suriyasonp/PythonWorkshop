def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        print("Welcome to System!")
        return True
    else:
        return False

def showMenu():
    print("----- FernShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
def menuSelect():
    userSelected = int(input(">>"))
    return userSelected

def vatCalculator(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result

def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculator(price1 + price2)

if login() == True:
    showMenu()
    menuSelect = menuSelect()
    if menuSelect == 1:
        print("-------------------------")
        totalPrice = int(input("Price :"))
        print("-------------------------")
        print("Total Price = %s THB" % vatCalculator(totalPrice))
        print("-------------------------")

    elif menuSelect == 2:
        print("Total Price = %s THB" % priceCalculator())
        print("-------------------------")

    else:
        print("Please select menu 1 or 2 only.")

else:
    print("Username or password is incorrect.")