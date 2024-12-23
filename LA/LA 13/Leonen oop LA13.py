class Animal():
    def __init__ (self, name, type):
        self.name = name
        self.type = type
       

    def describeAnimal(self):
        print(f" {self.name} is {self.type}.")

class Fish(Animal):
    def __init__(self, name, type, can_swim):
        super().__init__(name, type)
        self.can_swim = True

l1 = Fish("Nemo", "blo", "true")
print(l1.can_swim)