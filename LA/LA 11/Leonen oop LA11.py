class Phone():
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
       
    def describePhone(self):
        print(f" {self.brand} {self.model}")
   
       
class Android(Phone):
    def __init__(self, brand, model):
        Phone.__init__(self, brand, model)

l1 = Android("Iphone", "16 pro max")
l1.describePhone()