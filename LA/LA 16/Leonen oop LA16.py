class Appliance:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
   
    def operate(self):
        print("operating!")
       
class WashingMachine(Appliance):
    def operate(self):
        print("washing clothes!")

class Refrigerator(Appliance):
   def operate(self):
        print("keeping food cold!")

class Microwave(Appliance):
    def operate(self):
        print("heating food!")

washeng = WashingMachine("Lg", "front load")
ref = Refrigerator("Haier", "t-door magic")
mw = Microwave("Breville", "joule")

def tawaginSila(pangalan):
    pangalan.operate()

for appliance in [washeng, ref, mw]:
    tawaginSila(appliance)