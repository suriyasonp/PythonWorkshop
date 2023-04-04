correctNumber = 17
userGuess = 0
while userGuess != correctNumber:
    userGuess = int(input("Please guess a number:"))
    if userGuess > correctNumber:
        print("Too Large")
    elif userGuess < correctNumber:
        print("Too Small")
    elif userGuess == 17:
        print("Correct!")
        print("End game.")
