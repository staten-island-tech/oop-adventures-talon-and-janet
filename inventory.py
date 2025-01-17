class Inventory:
    def __init__(self, player):
        self.player = player  # Link back to Player instance
        self.inventory = [""] * 9  # 9 hotbar slots, initially empty

    def add_to_inventory(self, item, preferred_slot=None):
        if preferred_slot is not None and not self.player.inventory.inventory[preferred_slot - 1]:
            self.player.inventory.inventory[preferred_slot - 1] = item
        else:
            for i in range(len(self.player.inventory.inventory)):
                if not self.player.inventory.inventory[i]:
                    self.player.inventory.inventory[i] = item
                    return
            # If inventory is full
            x, y = self.player.position
            self.player.world.grid[y][x] = item[0].lower()
            self.player.world.dropped_items[(x, y)] = item
            print(f"Inventory full! {item} dropped on the ground.")

    def replace_or_add(self, item, slot, replace=None):
        if replace in self.player.inventory.inventory:
            index = self.player.inventory.inventory.index(replace)
            self.player.inventory.inventory[index] = item
        else:
            self.add_to_inventory(item, preferred_slot=slot)

    def remove_from_inventory(self, item, qty):
        for _ in range(qty):
            if item in self.player.inventory.inventory:
                self.player.inventory.inventory.remove(item)
            else:
                print(f"Not enough {item} in inventory!")

    def check_materials(self, materials):
        inventory_counts = {item: self.player.inventory.inventory.count(item) for item in set(self.player.inventory.inventory)}
        return all(inventory_counts.get(mat, 0) >= qty for mat, qty in materials.items())
