class npc():
    def __init__(self, name):
        self.name = name

class enemy(npc):
    def __init__(self, name, health, attacks, stamina, technique):
        super().__init__(name)
        self.health = health
        self.attacks = attacks 
        self.samina = stamina 
        self.technique = technique
    def __str__(self):
        return f"{self.name},{self.health},{ self.attacks},{self.stamina},{self.technique}"

Tutorial_Boss = enemy('John Parkinson','500','10','100','5') 
round_1_boss = enemy('Alexander Angela Alexandrios II', '750', '25', '200', '7')
round_2_boss = enemy('Bob Smith Jr.', '1500', '30', '250', '10')

class seller(npc):
    def __init__(self, name, trading, products):
        super().__init__(name)
        self.trading = trading
        self.products = products
    def __str__(self):
        return f"{self.name},{self.trading},{self.products}"

Glove_seller = seller('David Gloveman','')