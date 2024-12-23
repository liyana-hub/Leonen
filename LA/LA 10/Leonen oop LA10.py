class Vehicle():
    def __init__(self, brand, model, fuel_type):
        self.brand = brand
        self.model = model
        self.fuel_type = fuel_type
       
    def describeVehicle(self):
        print(f" {self.brand} {self.model}, with {self.fuel_type} fuel")
       
class Car(Vehicle):
    pass
car = Car("honda", "civic", "regular unleaded" )
car.describeVehicle()

class Motorcycle(Vehicle):
    pass
motor = Motorcycle("yamaha", "aerox", "unleaded")
motor.describeVehicle()