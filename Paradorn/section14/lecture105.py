class Vehicle:
    licenseCode = ""
    serialCode = ""
    face =""
    def turnOnAirConditioner(self):
        print("Turn On : Air")

class Car(Vehicle):
    def turnOnAirConditioner(self):
        print("Turn On : Air",self.licenseCode,self.serialCode)

class Pickup(Vehicle):
    def turnOnAirConditioner(self):
        print("Turn On : Air",self.licenseCode,self.serialCode)

class Van(Vehicle):
    def turnOnAirConditioner(self):
        print("Turn On : Air",self.licenseCode,self.serialCode)
class EstateCar(Vehicle) :
    def turnOnAirConditioner(self):
        print("Turn On : Air",self.licenseCode,self.serialCode)


car1 = Car()
car1.licenseCode = "Car 1234"
car1.serialCode = "1234567890"
car1.turnOnAirConditioner()

pickup = Pickup()
pickup.licenseCode = "Pickup 1234"
pickup.serialCode = "1234567890"
pickup.turnOnAirConditioner()

van = Van()
van.licenseCode = "Van 1234"
van.serialCode ="1234567890"
van.turnOnAirConditioner()

estateCar = EstateCar()
estateCar.licenseCode ="1234"
estateCar.serialCode = "123457890"
estateCar.turnOnAirConditioner()