class Inventory:
    def __init__(self, player):
        self.player = player
        self.inventory = [""] * 20  # 20 hotbar slots

    def add_to_inventory(self, item, preferred_slot=None):
        if preferred_slot is not None and self.inventory[preferred_slot] == "":
            self.inventory[preferred_slot] = item
        else:
            for i in range(len(self.inventory)):
                if self.inventory[i] == "":
                    self.inventory[i] = item
                    return
        print("No space to add item!")

    def remove_from_inventory(self, item, quantity=1):
        count = quantity
        for i in range(len(self.inventory)):
            if self.inventory[i] == item:
                self.inventory[i] = ""
                count -= 1
                if count == 0:
                    return

    def check_materials(self, materials):
        inventory_count = {item: self.inventory.count(item) for item in set(self.inventory)}
        for material, qty in materials.items():
            if inventory_count.get(material, 0) < qty:
                return False
        return True

    def replace_or_add(self, item, slot, replace=None):
        if replace in self.inventory:
            index = self.inventory.index(replace)
            self.inventory[index] = item
        else:
            self.add_to_inventory(item, slot)
