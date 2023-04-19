name = input("Firstname :").capitalize()
lastName = input("Lastname :").capitalize()
print("Hello !! %s  %s !" % (name,lastName))

textFormatted = "Welcome %s" %(name)
print(textFormatted.center(50,"*"))

print(len(name))