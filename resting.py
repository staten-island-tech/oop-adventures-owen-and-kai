class Move:
    def __init__(self, name):
        self.name = name

class Rest(Move):
    def __init__(self, name, stamina_regained):
        super().__init__(name)
        self.stamina_regained = stamina_regained
    def __str__(self):
        return f"{self.name}, {self.stamina_regained}"

Relax_Muscles = Rest('Relax Muscles', '20')

Put_Guard_Down = Rest('Put Guard Down', '50')

Full_Body_Relaxation = Rest('Full Body Relaxation', '100')