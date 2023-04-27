class Customer:
    name = ""
    lastName = ""
    age = 0

    def addCart(self):
        print("Added to " + self.name + " " + self.lastName + "'s cart")


customer1 = Customer()
customer1.name = "Bob"
customer1.lastName = "Baby"
customer1.age = 8
customer1.addCart()
