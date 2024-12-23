class character:
    def __init__(self, name, role):
        self.name = name
        self.role = role
    
    def __str__ (self):
        return f" {self.name} is an {self.role} hero."


hero = character("Benedetta","assassin" )
print(hero)