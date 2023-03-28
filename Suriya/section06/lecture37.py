userNameInput = input("Enter username:")
passwordInput = input("Enter password:")

userNameValid = "abc"
passwordValid = "1234"

if userNameInput == userNameValid and passwordInput == passwordValid:
    print("Authenticated success")
else:
    print("Error!")
