from forex_python.converter import CurrencyRates
c = CurrencyRates()
currentResult = c.get_rates('THB')
print(currentResult)