usernameInput = input("Username : ")
passWordInput = input("Password : ")

if usernameInput == "admin" and passWordInput == "1234":
    print("Done !")
    print("-----iShop------")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    userSelected = int(input(">>"))
    if userSelected == 1:
        price = int(input("Price (THB): "))
        vat = 7
        result = price + (price*vat / 100)
        print(result)
    elif userSelected == 2:
        price1 = int(input("First Product Price : "))
        price2 = int(input("Second Product Price : "))

