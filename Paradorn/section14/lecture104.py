class Customer:
    name = ""
    lastName = ""
    nickName = ""
    age = ""
    phone = ""

    def addCart(self):
        print("Added product to",self.name,self.lastName,"s cart")

customer1 = Customer()
customer1.name = "Paradorn"
customer1.lastName ="Sonjai"
customer1.addCart()

customer2 = Customer()
customer2.name = "Peter"
customer2.lastName ="Dominic"
customer2.addCart()
