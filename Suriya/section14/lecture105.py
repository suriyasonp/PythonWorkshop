class Vehicle:
    licenseCode = ""
    serialCode = ""

    def turnOnAirConditioner(self):
        print("Turn On : Air")

    def showLicenseCode(self):
        print("License Code is " + self.licenseCode)


class Car(Vehicle):
   pass

car1 = Car()
car1.licenseCode = "ABC1234"
car1.showLicenseCode()
car1.turnOnAirConditioner()

