


usernameInput = input("Username :")
passwordInput = input("Password :")

userName = "admin"
password = "1111"


if usernameInput  == userName  and passwordInput == password:
        print("Done !")
        print("----- Sura Shop -----")
        print("1. Vat Calculator")
        print("2. Price Calculator")
        userSelected = int(input(">>"))
        if userSelected == 1:
                price = int(input("Price (THB): "))
                vat = 7
                result = price + (price *7/100)
                print(result)
        elif userSelected == 2:
                price1 = int(input("mango Product Price : "))
                price2 = int(input("pen Product Price : "))
                price3 = int(input("bicycle Product Price : "))
                price4 = int(input("drinking water Product Price : "))

                total = price1+price2+price3+price4
                print(total)
else:
        print("Error !!")