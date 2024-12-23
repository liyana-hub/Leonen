class character:
    def __init__(self, name, role):
        self.name = name
        self.role = role
hero = character("kagura", "mage")
hero2 = character("argus", "fighter")
print(hero.name, hero.role, hero2.name, hero2.role)
