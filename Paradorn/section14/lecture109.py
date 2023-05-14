class Animal:
    def eat(self):
        print("Eating Eating!")

class Cat(Animal):
    __name = ""
    def setName(self,text):
        self.name = text
        print("Setting Naw Cat Name")
    def eat(self):
        print("Meoww 123456!!",self.name,self.name)

cat1 = Cat()
cat1.setName("ET")
print(cat1.__name)
cat1.eat()
