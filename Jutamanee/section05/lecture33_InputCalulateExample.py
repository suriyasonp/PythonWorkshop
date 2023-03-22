'''Ex.1'''
price1 = int(input("price(THB):"))
''' ข้อมูลถูกแปลงค่าเป็น int ตั้งแต่ตรงนี้เลย '''
vat = 7
result = price1+(price1*vat/100)
print(result)

'''Ex.2'''
price2 = input("price(THB):")
''' Input ยังคงเป็น String)'''
result = int(price2)+(int(price2)*vat/100)
''' Input ถูกแปลงค่าเป็น int'''
print(result)


