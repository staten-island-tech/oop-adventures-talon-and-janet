from item import WoodenAxe, StoneAxe, WoodenPickaxe, StonePickaxe

class NPC:
    def __init__(self, name, position, dialogue):
        self.name = name
        self.position = position  
        self.dialogue = dialogue  

    def talk(self):
        print(f"{self.name} says: {self.dialogue}")

    def interact(self, player):
        self.talk()

class Blacksmith(NPC):
    def __init__(self, name, position, dialogue):
        super().__init__(name, position, dialogue)

    def craft(self, player, tool_name):
        if tool_name == "Wooden Axe" and player.inventory["Wood"] >= 3:
            player.inventory["Wood"] -= 3
            player.hotbar.append(WoodenAxe())
            print("Crafted a Wooden Axe!")
        elif tool_name == "Stone Axe" and player.inventory["Wood"] >= 3 and player.inventory["Stone"] >= 2:
            player.inventory["Wood"] -= 3
            player.inventory["Stone"] -= 2
            player.hotbar.append(StoneAxe())
            print("Crafted a Stone Axe!")
        elif tool_name == "Wooden Pickaxe" and player.inventory["Wood"] >= 3 and player.inventory["Stone"] >= 2:
            player.inventory["Wood"] -= 3
            player.inventory["Stone"] -= 2
            player.hotbar.append(WoodenPickaxe())
            print("Crafted a Wooden Pickaxe!")
        elif tool_name == "Stone Pickaxe" and player.inventory["Wood"] >= 3 and player.inventory["Stone"] >= 3:
            player.inventory["Wood"] -= 3
            player.inventory["Stone"] -= 3
            player.hotbar.append(StonePickaxe())
            print("Crafted a Stone Pickaxe!")
        else:
            print("You do not have the required resources to craft this tool.")
    
    def interact(self, player):
        self.talk()
        tool_choice = input("Which tool would you like to craft? (Wooden Axe, Stone Axe, Wooden Pickaxe, Stone Pickaxe): ")
        self.craft(player, tool_choice)
