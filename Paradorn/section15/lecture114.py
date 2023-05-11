from forex_python.converter import CurrencyRates
from forex_python.converter import CurrencyCodes

currency_rates = CurrencyRates()
currency_code = CurrencyCodes()
class ConvertCurrencyRates():
    currency_income =""
    currency_convert = ""
    value = ""

    def convertCurrency(self):
        result_value = ""
        result_code = ""
        if self.currency_income == "GBP":
            result_value = currency_rates.convert(self.currency_income, self.currency_convert , self.value)
        elif self.currency_income == "USD":
            result_value = currency_rates.convert(self.currency_income, self.currency_convert , self.value)
        elif self.currency_income == "EUR":
            result_value = currency_rates.convert(self.currency_income, self.currency_convert, self.value)
        elif self.currency_income == "INR":
            result_value = currency_rates.convert(self.currency_income, self.currency_convert, self.value)
        else:
            result_value ="ไม่เข้าเงื่อนไข"
        result_code = currency_code.get_currency_name(self.currency_convert)
        print(result_value,result_code)


convert_rates = ConvertCurrencyRates()
convert_rates.value = int(input("Please input value  :"))
convert_rates.currency_income = input("Please input currency income  :").upper()
convert_rates.currency_convert = input("Please input currency convert  :").upper()
convert_rates.convertCurrency()













