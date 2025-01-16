class Blacksmith:
    def __init__(self, player):
        self.player = player

    def menu(self):
        print("\nWelcome to the Blacksmith! What would you like to craft?")
        print("1. Wooden Pickaxe (Requires 1 Wood, 2 Sticks)")
        print("2. Wooden Axe (Requires 1 Wood, 3 Sticks)")
        print("3. Stone Pickaxe (Requires 2 Stone, 2 Sticks)")
        print("4. Stone Axe (Requires 2 Stone, 3 Sticks)")
        print("5. Stone Sword (Requires 2 Stone, 2 Wood)")
        print("6. Exit")
        choice = input("> ")

        recipes = {
            "1": ("Wood pickaxe", {"Wood": 1, "Stick": 2}),
            "2": ("Wood axe", {"Wood": 1, "Stick": 3}),
            "3": ("Stone pickaxe", {"Stone": 2, "Stick": 2}),
            "4": ("Stone axe", {"Stone": 2, "Stick": 3}),
            "5": ("Stone sword", {"Stone": 2, "Wood": 2}),
        }

        if choice in recipes:
            item, materials = recipes[choice]
            if self.player.inventory.check_materials(materials):
                for mat, qty in materials.items():
                    self.player.inventory.remove_from_inventory(mat, qty)
                self.player.inventory.add_to_inventory(item)
                print(f"You crafted a {item}!")
            else:
                print("You don't have enough materials.")
        elif choice == "6":
            return
        else:
            print("Invalid choice.")