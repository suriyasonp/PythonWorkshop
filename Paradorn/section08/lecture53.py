def vatCalculate(totalPrice):
    result = totalPrice+(totalPrice*7/100)
    return result
addNumber = int(input("Please enter number"))
print(vatCalculate(addNumber))