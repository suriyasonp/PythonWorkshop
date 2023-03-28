usernameInput = input("Username : ")
passWordInput = input("Password : ")

if usernameInput == "admin" and passWordInput == "1234":
    print("Done !")
    print("-----Fern Shop------")
    print("1. Pen 10 THB")
    print("2. Eraser 5 THB")
    print("3. Ruler 15 THB")
    userSelected = int(input("Select item: "))
    amount = int(input("Amount to buy: "))
    if userSelected == 1:
        price = 10
        result = price * amount
        print("Total :",result,"THB")
    elif userSelected == 2:
        price = 5
        result = price * amount
        print("Total :", result, "THB")
    else:
        price = 15
        result = price * amount
        print("Total :", result, "THB")

else:
    print("Error!!!")
