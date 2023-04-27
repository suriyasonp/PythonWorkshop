class Customer:
    name = ""
    lastName = ""
    age = 0

    def addCart (self):
        print("Added to ",self.name,self.lastName,"'s cart")

customer1 = Customer()
customer1.name = "AA"
customer1.lastName = "BB"
customer1.addCart()

customer2 = Customer()
customer2.name = "CC"
customer2.lastName = "DD"
customer2.addCart()

customer3 = Customer()
customer3.name = "FF"
customer3.lastName = "GG"
customer3.addCart()

customer4 = Customer()
customer4.name = "HH"
customer4.lastName = "LL"
customer4.addCart()
