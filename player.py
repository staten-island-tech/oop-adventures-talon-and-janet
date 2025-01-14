class Player:
    def __init__(self, start_x=0, start_y=0):
        self.position = (start_x, start_y)
        self.inventory = [""] * 9  # 9 hotbar slots, initially empty

    def move(self, direction, world):
        x, y = self.position
        if direction == "w" and y > 0:
            y -= 1
        elif direction == "s" and y < world.height - 1:
            y += 1
        elif direction == "a" and x > 0:
            x -= 1
        elif direction == "d" and x < world.width - 1:
            x += 1
        self.position = (x, y)

    def use_hotbar(self, index):
        item = self.inventory[index]
        if item:
            print(f"You used {item}!")
        else:
            print("That slot is empty!")
