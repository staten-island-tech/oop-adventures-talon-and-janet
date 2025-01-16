import random
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
class GemCave(Cave):
    def __init__(self, player):
        super().__init__(player)

    def display_cave(self):
        print("You are in the Gem Cave. Sparkling gems glisten on the walls!")
        print("Press 'E' to mine a gem, or '0' to leave the cave.")

    def mine_rock(self):
        if "Wood pickaxe" in self.player.inventory.inventory or "Stone pickaxe" in self.player.inventory.inventory:
            gem = self.mine_gem()  
            if gem:
                self.player.inventory.add_to_inventory(gem)
            else:
                print("You mined a rock and got stone!")
                self.player.inventory.add_to_inventory("Stone")
        else:
            print("You need a pickaxe to mine.")

    def mine_gem(self):
        gems = ["Ruby", "Sapphire", "Emerald", "Amethyst", "Shiny other thing"]
        chance = random.choice([True, False])  

        if chance:
            gem = random.choice(gems)
            print(f"You mined a {gem}!")
            return gem
        return None  