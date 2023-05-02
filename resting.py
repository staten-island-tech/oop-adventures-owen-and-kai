class Rest:
    def __init__(self, name, stamina_regained):
        self.name = name
        self.stamina_regained = stamina_regained
    def __str__(self):
        return f"{self.name}, {self.stamina_regained}"
    
Relax_Muscles = Rest('Relax Muscles', '10%')

Put_Guard_Down = Rest('Put Guard Down', '25%')

Full_Body_Relaxation = Rest('Full Body Relaxation', '50%')