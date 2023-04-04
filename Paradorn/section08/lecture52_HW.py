def checkPrice(number):
    price = 0
    if (number == "1111"):
        price = 300
    elif(number == "2222"):
        price = 200
    else:
        price = 10000
    return price

price1 = checkPrice("1111")
print("Price: ", price1)

price2 = checkPrice("2222")
print("Price: ", price2)

price3 = checkPrice("3333")
print("Price: ", price3)
