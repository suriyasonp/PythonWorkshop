price = float(input("Enter price (THB):"))
vat = 7
netVat = price + (price * vat / 100)
print("Net vat", netVat)

