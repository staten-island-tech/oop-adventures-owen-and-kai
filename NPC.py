class npc():
    def __init__(self, name):
        self.name = name

class enemy(npc):
    def __init__(self, name, health, attacks, stamina, technique):
        super().__init__(name)
        self.health = int(health)
        self.attacks = int(attacks) 
        self.samina = int(stamina) 
        self.technique = int(technique)
    def __str__(self):
        return f"{self.name},{self.health},{ self.attacks},{self.stamina},{self.technique}"

Tutorial_Boss = enemy('John Parkinson','500','10','100','5') 
Round_1_Boss = enemy('Alexander Angela Alexandrios II', '750', '25', '200', '7')
Round_2_Boss = enemy('Bob Smith Jr.', '1500', '30', '250', '10')
Round_3_Boss = enemy('Albert Hilton', '2000', '40','350', '13')
Quarter_Finals_Boss = enemy('Scorpio Lancer','2500', '50', '500', '15')
Semi_Finals_Boss = enemy('Phuk Sheet Jr.', '3500','75','750', '20')
class final_boss(enemy):
    def __init__(self, name, health, attacks, stamina, technique, special_move):
        super().__init__(name, health, attacks, stamina, technique)
        self.special_move = special_move
        def __str__(self):
            return f"{self.name},{self.health},{self.attacks},{self.stamina},{self.technique},{self.special_move}"
Final_Round_Boss = final_boss("Jaquavious Dontavious Requise III", "5000",'150','1000','25', '0.05')
class seller(npc):
    def __init__(self, name, trading, product1, product2, dialogue):
        super().__init__(name)
        self.trading = trading
        self.product1 = product1
        self.product2 = product2
        self.dialogue = dialogue
    def __str__(self):
        return f"{self.name},{self.trading},{self.products}"

Glove_seller = seller('David Gloveman','money','gloves','steroids','talking')
Black_Market_Dealer = seller('Miguel Ángel Félix Gallardo', 'money', 'sepecial_candy','N/A','talking')
class friendly_npc(npc):
    def __init__(self, name, action, dialogue):
        super().__init__(name)
        self.action = action
        self.dialogue = dialogue
def __str__(self):
    return f"{self.name},{self.action},{self.dialogue}"
Coach = friendly_npc('Shawn Wilson','training','talking/asking for advice')
The_Miracle_Builder = friendly_npc('William Smith','building','talking')