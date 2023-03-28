userNameInput = input("Enter username:")
passwordInput = input("Enter password:")

userNameValid = "abc"
passwordValid = "1234"

if userNameInput == userNameValid and passwordInput == passwordValid:
    print("Authenticated success")
    print("----------Smile Shop-----------")
    print("1. Vat Calculator")
    print("2. Price Calculator")

    userSelected = int(input(">>"))
    if userSelected == 1:
        price = float(input("Enter Price (THB):"))
        vat = 7
        netPrice = price + (price * vat / 100)
        print("Net price:", netPrice)
    elif userSelected == 2:
        price1 = float(input("Enter Price-1: >>"))
        price2 = float(input("Enter Price-2: >>"))
        price3 = float(input("Enter Price-3: >>"))
        sumPrice = price1 + price2 + price3
        print("Summary:", sumPrice)
else:
    print("Error!")
