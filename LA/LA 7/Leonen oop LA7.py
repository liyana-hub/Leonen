class car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

civic1 = car("civic", "white")
print(civic1.brand, civic1.color)
civic1.color = "black"
print(civic1.brand, civic1.color)

civic2 = car("lambo", "green")
print(civic2.brand, civic2.color)