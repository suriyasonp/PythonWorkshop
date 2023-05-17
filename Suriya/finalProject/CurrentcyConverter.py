from forex_python.converter import CurrencyRates
import json


def print_menu():
    print("*" * 50)
    print("*" + " " * 48 + "*")
    print("*" + " " * 48 + "*")

    print("*" + "Welcome to Currency Exchange Rate Program".center(48) + "*")
    # Menu 1
    print("*" + "1. Get currency rate".center(48) + "*")
    print("*" + "2. Convert currency rate".center(48) + "*")
    print("*" + "Press Q or q to exit".center(48) + "*")

    print("*" + " " * 48 + "*")
    print("*" * 50)

    input_menu = input("Select menu:")
    return input_menu


def get_currency_rate(source_currency):
    c = CurrencyRates()
    rate_result = c.get_rates(source_currency)
    return rate_result


def convert_currency_rate(source_currency, to_currency):
    pass


def access_menu(selected_menu):
    if selected_menu == '1':
        print("<" * 10 + "Currency Rate".center(30) + ">" * 10)
        currency_unit = input(">" * 5 + " Please enter currency unit: >> ")
        currency_list = get_currency_rate(currency_unit)

        for key, value in currency_list.items():
            print(">>>  " + (key + " " + str(value).center(30)))

        return question_continue()
    elif selected_menu == '2':
        print("Menu 2")
    elif selected_menu == 'q' or selected_menu == 'Q':
        pass


def question_continue():
    answer = input("\n\nWould you like to continue? Y=Yes, N=No: >> ")
    return answer == 'Y' or answer == 'y'


def goodbye():
    print("\n")
    print("Thank you. See you again.".center(50))
    print("\n")


# Core Program

running = True

while running:
    selected_menu = print_menu()

    if selected_menu == 'q' or selected_menu == 'Q':
        running = False

    running = access_menu(selected_menu)

goodbye()
