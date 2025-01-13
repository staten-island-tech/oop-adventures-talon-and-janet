class Player:
    def __init__(self):
        self.position = [5, 5]  # Player's position on the grid
        self.health = 100
        self.hotbar = [None] * 9  # 9 item slots (hotbar)
        self.inventory = {"Wood": 0, "Stone": 0}  # Resources the player has collected
        self.score = 0

    def move(self, direction):
        """Move the player in the specified direction."""
        if direction == 'w':  # Move up
            self.position[1] -= 1
        elif direction == 's':  # Move down
            self.position[1] += 1
        elif direction == 'a':  # Move left
            self.position[0] -= 1
        elif direction == 'd':  # Move right
            self.position[0] += 1

    def collect_resource(self, resource, amount=1):
        """Collect resources like Wood or Stone."""
        if resource in self.inventory:
            self.inventory[resource] += amount
            print(f"Collected {amount} {resource}.")
        else:
            print(f"{resource} not available to collect.")