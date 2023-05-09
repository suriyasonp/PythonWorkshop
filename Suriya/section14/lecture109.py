class Animal:
    def eat(self):
        print("Eating Eating")

class Cat(Animal):
    __name = ""

    def setName(self, text):
        self.__name = text
        print("Setting New Cat Name = ", self.__name)

    def eat(self):
        print("Meow eating! ", self.__name)

cat1 = Cat()
cat1.setName("Kitty")
cat1.eat()