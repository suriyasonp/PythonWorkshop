def vatCalculate(totalPrice):
    result = totalPrice+(totalPrice*7/100)
    return result

inputTotalPrice = float(input("Total price:"))
print(vatCalculate(inputTotalPrice))