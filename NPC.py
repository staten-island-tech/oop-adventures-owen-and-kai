class npc():
    def __init__(self, name):
        self.name = name

class enemy(npc):
    def __init__(self, name, health, attacks, stamina):
        super().__init__(name)

class seller(npc):
    def __init__(self, name, trading, products):
        super().__init__(name)
        self.trading = trading
        self.products = products
    def __str__(self):
        return f"{self.name}"

Glove_seller = seller('David Gloveman','')