class Player:
    def __init__(self, name, health, atk_power):
        self.name = name
        self.health = health
        self.atk_power = atk_power
    def basic_atk(self, target):
        target.health -= self.atk_power
   
olegna = Player("Mahito",8000,5000)
liyan = Player("Nanami Kento",9000, 7000)

while olegna.health < 0:
    print("tay na <3")