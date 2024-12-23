class Toy():
    def __init__(self, name, price):
        self.name = name
        self.price = price
       
    def describeToy(self):
        print(f" The toy {self.name} is {self.price} million dollars dollars.")
   
       
class Car(Toy):
    def __init__(self, name, price):
        super().__init__(name, price)

l1 = Car("Barbie doll", "twenty four")
l1.describeToy()
