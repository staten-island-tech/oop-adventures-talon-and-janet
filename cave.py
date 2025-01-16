class Cave:
    def __init__(self, player):
        self.player = player

    def display_cave(self):
        print("You are in the cave. Rocks are everywhere.")
        print("Press 'E' to mine a rock, or '0' to leave the cave.")

    def mine_rock(self):
        if "Wood pickaxe" in self.player.inventory.inventory or "Stone pickaxe" in self.player.inventory.inventory:
            print("You mined a rock and got stone!")
            self.player.inventory.add_to_inventory("Stone")
        else:
            print("You need a pickaxe to mine rocks.")