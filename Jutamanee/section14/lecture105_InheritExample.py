class Vehicle:
    licenceCode = ""
    serialCode = ""
    def tureOnAirConditioner(self):
        print("True On : Air")
class Car(Vehicle):
    def sayHello(self):
        print("Hello World")
class PickUp(Vehicle):
    pass
class Van(Vehicle):
    pass
class Estatecar(Vehicle):
    pass

car1 = Car()
car1.tureOnAirConditioner()
car1.sayHello()

pickUp1 = PickUp()
pickUp1.tureOnAirConditioner()

van1 = Van()
van1.tureOnAirConditioner()

estatecar1 = Estatecar()
estatecar1.tureOnAirConditioner()
