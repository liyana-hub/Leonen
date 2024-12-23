class car:
    def __init__(self, brand):
        self.brand = brand
    
    def __str__ (self):
        return f"{self.brand} is a car"
    
cvc = car("civic")
del cvc
print(cvc)