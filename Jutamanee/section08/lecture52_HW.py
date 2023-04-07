
def checkPrice(number):
    if number == "1":
        price = 20
    else:
        price = 40
    return price

price1 = checkPrice("1")
print("Price: ", price1)

price1 = checkPrice("20")
print("Price: ", price1)
