name = input("Firstname: ").capitalize()
lastname = input("Lastname: ").capitalize()

print("Hello %s %s!" % (name, lastname))

textFomatted = "Hello %s %s!" % (name, lastname)
print(textFomatted.center(30,"-"))
print("Length %s" %(len(name)+len(lastname)))

