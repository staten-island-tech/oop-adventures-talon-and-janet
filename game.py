from world import World
from player import Player

class Game:
    def __init__(self):
        self.world = World()
        self.player = Player(self.world)  # Pass world to player
        self.in_cave = False

    def start(self):
        self.show_start_screen()

    def show_start_screen(self):
        print("=" * 30)
        print(" " * 10 + "Title: Too Early")
        print("=" * 30)
        print("1. Start Game")
        print("2. Controls")
        choice = input("> ")

        if choice == "1":
            self.world.randomize_features()
            self.game_loop()
        elif choice == "2":
            self.show_controls()
        else:
            print("Invalid choice. Please try again.")
            self.show_start_screen()

    def show_controls(self):
        print("\nControls:")
        print("WASD - Move")
        print("1-9  - Use item from hotbar")
        print("E    - Interact")
        print("Q    - Drop an item")
        print("0    - Leave the cave (if inside)")
        print("P    - Quit the game")
        print("\nPress Enter to return to the menu.")
        input()
        self.show_start_screen()

    def game_loop(self):
        print("Welcome to the 2D Sandbox Game!")

        # Ensure wood spawns near the player
        x, y = self.player.position
        self.world.grid[y][x] = "W"  # Place a wood item on the starting tile
        print("As you begin your adventure, you spot a piece of wood nearby!")

        while True:
            if not self.in_cave:
                self.world.display(self.player)
            else:
                self.display_cave()

            print("Hotbar:", self.player.inventory.inventory)
            command = input("Enter command: ").lower()

            if command in ["w", "a", "s", "d"]:
                self.player.move(command, self.world)
            elif command.isdigit() and 1 <= int(command) <= 9:
                self.player.use_hotbar(int(command) - 1)
            elif command == "e":
                if not self.in_cave:
                    self.interact()
                else:
                    self.mine_rock()
            elif command == "q":
                self.drop_item()
            elif command == "0" and self.in_cave:
                self.in_cave = False
                print("You leave the cave.")
            elif command == "p":
                print("Goodbye!")
                break
            else:
                print("Invalid command.")

    def interact(self):
        x, y = self.player.position
        current_tile = self.world.grid[y][x]

        if current_tile == "T":
            if "Wood axe" in self.player.inventory.inventory or "Stone axe" in self.player.inventory.inventory:
                print("You chop the tree. Do you want to proceed? (y/n)")
                if input("> ").lower() == "y":
                    self.world.grid[y][x] = "."
                    self.player.inventory.add_to_inventory("Wood", preferred_slot=2)
                    print("You got wood!")
            else:
                print("You need an axe to chop the tree.")
        elif current_tile == "W":
            print("You found a piece of wood! Pick it up? (y/n)")
            if input("> ").lower() == "y":
                self.world.grid[y][x] = "."
                self.player.inventory.add_to_inventory("Wood", preferred_slot=None)
                print("You picked up wood!")
        elif current_tile == "S":
            print("You found a pile of sticks! Do you want to grab sticks? (y/n)")
            if input("> ").lower() == "y":
                self.world.grid[y][x] = "."
                for _ in range(2):  # Add 2 sticks
                    self.player.inventory.add_to_inventory("Stick", preferred_slot=None)
                print("You grabbed some sticks!")
        elif current_tile == "C":
            print("You found a cave! Do you want to go in? (y/n)")
            if input("> ").lower() == "y":
                self.in_cave = True
        elif current_tile == "B":
            self.blacksmith_menu()
        elif current_tile.islower():
            item_name = self.world.dropped_items.get((x, y))
            if item_name:
                print(f"You found {item_name}! Pick it up? (y/n)")
                if input("> ").lower() == "y":
                    self.player.inventory.add_to_inventory(item_name, preferred_slot=None)
                    self.world.grid[y][x] = "."
                    del self.world.dropped_items[(x, y)]
        else:
            print("Nothing to interact with here.")

    def drop_item(self):
        print("Inventory:", self.player.inventory.inventory)
        slot = input("Enter the slot number (1-9) of the item to drop: ")
        if slot.isdigit() and 1 <= int(slot) <= 9:
            index = int(slot) - 1
            item = self.player.inventory.inventory[index]
            if item:
                x, y = self.player.position
                if self.world.grid[y][x] == ".":
                    self.world.grid[y][x] = item[0].lower()
                    self.world.dropped_items[(x, y)] = item
                    self.player.inventory.inventory[index] = ""
                    print(f"You dropped {item}.")
                else:
                    print("You can't drop an item here.")
            else:
                print("No item in that slot.")
        else:
            print("Invalid slot number.")

    def blacksmith_menu(self):
        print("\nWelcome to the Blacksmith! What would you like to craft?")
        print("1. Wooden Pickaxe (Requires 1 Wood, 2 Sticks)")
        print("2. Wooden Axe (Requires 1 Wood, 3 Sticks)")
        print("3. Stone Pickaxe (Requires 2 Stone, 2 Sticks)")
        print("4. Stone Axe (Requires 2 Stone, 3 Sticks)")
        print("5. Stone Sword (Requires 2 Stone, 2 Wood)")
        print("6. Exit")
        choice = input("> ")

        recipes = {
            "1": ("Wood pickaxe", {"Wood": 1, "Stick": 2}, 1),
            "2": ("Wood axe", {"Wood": 1, "Stick": 3}, 2),
            "3": ("Stone pickaxe", {"Stone": 2, "Stick": 2}, 1),
            "4": ("Stone axe", {"Stone": 2, "Stick": 3}, 2),
            "5": ("Stone sword", {"Stone": 2, "Wood": 2}, 3),
        }

        if choice in recipes:
            item, materials, slot = recipes[choice]
            if self.player.inventory.check_materials(materials):
                for mat, qty in materials.items():
                    self.player.inventory.remove_from_inventory(mat, qty)
                if "Stone" in item and "Pickaxe" in item:
                    self.player.inventory.replace_or_add(item, slot, replace="Wood pickaxe")
                elif "Stone" in item and "Axe" in item:
                    self.player.inventory.replace_or_add(item, slot, replace="Wood axe")
                else:
                    self.player.inventory.add_to_inventory(item, preferred_slot=slot)
                print(f"You crafted a {item}!")
            else:
                print("You don't have enough materials.")
        elif choice == "6":
            return
        else:
            print("Invalid choice.")

    def display_cave(self):
        print("You are in the cave. Rocks are everywhere.")
        print("Press 'E' to mine a rock, or '0' to leave the cave.")

    def mine_rock(self):
        if "Wood pickaxe" in self.player.inventory.inventory or "Stone pickaxe" in self.player.inventory.inventory:
            print("You mined a rock and got stone!")
            self.player.inventory.add_to_inventory("Stone")
        else:
            print("You need a pickaxe to mine rocks.")


if __name__ == "__main__":
    game = Game()
    game.start()
