from forex_python.converter import CurrencyRates
from forex_python.bitcoin import BtcConverter
from forex_python.converter import CurrencyCodes
import datetime

b = BtcConverter()
c = CurrencyRates()
d = CurrencyCodes()

btc_converter = BtcConverter()
result1 = b.get_latest_price('EUR')
result = c.get_rates('USD')

print("result",result)

print("---------- Welcome to the Bitcoin buying system. ----------")
print("Currencies you can use:")
print("1.EUR")
print("2.THB")

currency_select = int(input("Please enter the currency you wish to use to purchase coins:"))
print("----------Please enter the date range of the price you wish to purchase.----------")

amount = int(input("Please enter an amount:"))
if currency_select == 1:
    # print(d.get_symbol('EUR'))
    convert_amout  = b.convert_to_btc(amount, 'EUR')
    print("Number of Bitcoin earned:",convert_amout,b.get_symbol())
else:
    convert_amout = b.convert_to_btc(amount, 'THB')
    print(b.get_latest_price('THB'))
    print("Number of Bitcoin earned:",convert_amout,b.get_symbol())

