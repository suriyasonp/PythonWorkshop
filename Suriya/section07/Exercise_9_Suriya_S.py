usernameInput = ""
passwordInput = ""
retry = 0
while usernameInput != "admin" or passwordInput != "1234" and retry < 3:
    usernameInput = input("Username:")
    passwordInput = input("Password:")
    retry += 1
    if usernameInput == "admin" and passwordInput == "1234":
        print("Done!")
    else:
        print("Failed!")