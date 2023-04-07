def askPrice(itemCode):
    price = 0
    if (itemCode == "001"):
        price = 100
    elif(itemCode == "002"):
        price = 50
    else:
        price = 0
    return price

goodsPrice = askPrice("001")
print("Price: ", goodsPrice)

goodsPrice = askPrice("002")
print("Price: ", goodsPrice)

goodsPrice = askPrice("003")
print("Price: ", goodsPrice)
