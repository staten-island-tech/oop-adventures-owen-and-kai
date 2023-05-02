class Attack:
    def __init__(self, name, damage, stamina_drained):
        self.name = name
        self.damage = damage
        self.stamina_drained = stamina_drained

Jab = Attack('Jab', '5', '10')

Straight = Attack('Straight', '20', '30')

