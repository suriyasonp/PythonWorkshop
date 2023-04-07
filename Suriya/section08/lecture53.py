def vatCalculate(totalPrice):
    result = totalPrice * 1.07
    return result

inputTotalPrice = float(input("Total price:"))
print(vatCalculate(inputTotalPrice))