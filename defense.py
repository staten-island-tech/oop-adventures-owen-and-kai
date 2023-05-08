class Move:
    def __init__(self, name):
        self.name = name

class Defend(Move):
    def __init__(self, name):
        super().__init__(name)
    def __str__(self):
        return f"{self.name}" 

Block_Jab = Defend('Block Jab',)

Block_Straight = Defend('Block Jab')

Block_Left_Hook = Defend('Block Left Hook')

Block_Right_Hook = Defend('Block Right Hook')

Block_Right_Uppercut = Defend('Block Right Uppercut')