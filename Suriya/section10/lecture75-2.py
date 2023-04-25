userInput = int(input("Enter number of your favorite fruits:"))
myFruits = set()

while (len(myFruits) < userInput):
   myFruits.add(input("Fruits:").capitalize())

print(myFruits)