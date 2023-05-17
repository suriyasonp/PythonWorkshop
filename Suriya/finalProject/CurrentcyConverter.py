from forex_python.converter import CurrencyRates


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


selected_menu = print_menu()

