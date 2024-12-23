class Dog:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("Bark!")
   
class Cat:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("Meow!")

class Bird:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("Chirp")

class Fish:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("blop blop:)")
       
aso = Dog ("choki")
pusa = Cat ("chaw")
ibon = Bird ("Choc")
pish = Fish ("Nemo")

def animal_sounds(animal):
    animal.speak()

for animal in [aso, pusa, ibon, pish]:
    animal_sounds(animal) 