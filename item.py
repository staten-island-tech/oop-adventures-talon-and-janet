class Item:
    def __init__(self, name):
        self.name = name

    def apply(self, player):
        """Apply the effect of using the item."""
        pass

class Wood(Item):
    def __init__(self):
        super().__init__("Wood")

class Stone(Item):
    def __init__(self):
        super().__init__("Stone")

class WoodenAxe(Item):
    def __init__(self):
        super().__init__("Wooden Axe")

class StoneAxe(Item):
    def __init__(self):
        super().__init__("Stone Axe")

class WoodenPickaxe(Item):
    def __init__(self):
        super().__init__("Wooden Pickaxe")

class StonePickaxe(Item):
    def __init__(self):
        super().__init__("Stone Pickaxe")
