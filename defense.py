class Move:
    def __init__(self, name):
        self.name = name

class Defend(Move):
    def __init__(self, name, damage_reduced):
        super().__init__(name)
        self.damage_reduced = int(damage_reduced)
    def __str__(self):
        return f"{self.name, self.damage_reduced}" 

Block_Jab = Defend('Block Jab', '5')

Block_Straight = Defend('Block Straight', '20')

Block_Left_Hook = Defend('Block Left Hook', '25')

Block_Right_Hook = Defend('Block Right Hook', '65')

Block_Right_Uppercut = Defend('Block Right Uppercut', '80')