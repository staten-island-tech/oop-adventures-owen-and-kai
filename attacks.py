class Attack:
    def __init__(self, name, damage, stamina_drained):
        self.name = name
        self.damage = damage
        self.stamina_drained = stamina_drained
    def __str__(self):
        return f"{self.name}, {self.damage}, {self.stamina_drained}"
    
Jab = Attack('Jab', '10', '5')

Straight = Attack('Straight', '45', '30')

Left_Hook = Attack('Left Hook', '25', '15')

Right_Hook = Attack('Right Hook', '65', '45')

Right_Uppercut = Attack('Right Uppercut', '80', '60')