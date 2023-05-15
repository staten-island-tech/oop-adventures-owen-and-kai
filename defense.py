class Move:
    def __init__(self, name):
        self.name = name

class Defend(Move):
    def __init__(self, name):
        super().__init__(name)
    def __str__(self):
        return f"{self.name}" 

Block_Forward = Defend('Block Forward')

Block_Side = Defend('Block Side')

Block_Down = Defend('Block Down')