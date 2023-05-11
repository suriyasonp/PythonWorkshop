class Animal:
    def eat(self):
        print("Eating Eating!")

class Cat(Animal):
    name = ""
    def setName(self,text):
        self.name = text
        print("Setting Naw Cat Name")
    def eat(self):
        print("Meoww 123456!!",self.name,self.name)

cat1 = Cat()
cat1.setName("ET")
cat1.name="dfdfsfsf"
cat1.eat()
