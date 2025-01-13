from world import World
from player import Player
from items import Items

class Game:
    def __init__(self):
        self.world = World()
        self.player = Player()

    def start(self):
        print("Welcome to the 2D Sandbox Game!")
        while True:
            self.world.display(self.player)
            print("Hotbar:", self.player.inventory)
            command = input("Enter command (WASD to move, 1-9 to use item, E to interact): ").lower()

            if command in ["w", "a", "s", "d"]:
                self.player.move(command, self.world)
            elif command.isdigit() and 1 <= int(command) <= 9:
                self.player.use_hotbar(int(command) - 1)
            elif command == "e":
                self.interact()
            elif command == "q":
                print("Goodbye!")
                break
            else:
                print("Invalid command.")

    def interact(self):
        x, y = self.player.position
        if self.world.grid[y][x] == "T":
            print("You're in front of a tree. Use the axe to chop it down (y/n)?")
            if input("> ").lower() == "y":
                self.world.grid[y][x] = "."
                self.add_to_inventory("Wood")
                print("You chopped the tree and got wood!")
        else:
            print("Nothing to interact with here.")

    def add_to_inventory(self, item):
        for i in range(len(self.player.inventory)):
            if not self.player.inventory[i]:
                self.player.inventory[i] = item
                break
        else:
            print("Inventory is full!")
