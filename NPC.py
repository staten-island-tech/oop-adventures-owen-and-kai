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
Round_3_Boss = enemy('Albert Hilton', '2000', '40','350', '13')
Quarter_Finals_Boss = enemy('Scorpio Lancer','2500', '50', '500', '15')
semi_finals_boss = enemy('Phuk Sheet Jr.', '3500','75','750', '20')
class final_boss(enemy):
    def __init__(self, name, health, attacks, stamina, technique, special_move):
        super().__init__(name, health, attacks, stamina, technique)
        self.special_move = special_move
        return f"{self.name},{self.health},{self.attacks},{self.samina},{self.technique},{self.special_move}"
final_round_boss = final_boss("Jaquavious Dontavious Requise III", "5000",'150','1000','25', '0.05')
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
black_market_dealer = seller('Miguel Ángel Félix Gallardo', 'money', 'sepecial_candy','N/A','talking')
class friendly_npc(npc):
    def __init__(self, name, action, dialogue):
        super().__init__(name)
        self.action = action
        self.dialogue = dialogue
def __str__(self):
    return f"{self.name},{self.action},{self.dialogue}"
Coach = friendly_npc('Shawn Wilson','training','talking/asking for advice')
The_miracle_builder = friendly_npc('William Smith','building','talking')