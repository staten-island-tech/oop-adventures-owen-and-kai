class Move:
    def __init__(self, name):
        self.name = name

class Attack(Move):
    def __init__(self, name, damage, stamina_drained):
        super().__init__(name)
        self.damage = int(damage)
        self.stamina_drained = int(stamina_drained)
    def __str__(self):
        return f"{self.name}, {self.damage}, {self.stamina_drained}"

Jab = Attack('Jab', '5', '10')

Straight = Attack('Straight', '20', '30')

Left_Hook = Attack('Left Hook', '25', '15')

Right_Hook = Attack('Right Hook', '65', '45')

Right_Uppercut = Attack('Right Uppercut', '80', '60')