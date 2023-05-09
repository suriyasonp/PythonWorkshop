from forex_python.converter import CurrencyRates

c = CurrencyRates()
currentResult = c.get_rates('THB')
print(currentResult)

# Convert THB to USD
thb_to_usd = c.convert('THB', 'USD', 100)
print('THB to USD : ' + str(thb_to_usd) + "USD")
