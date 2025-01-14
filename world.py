import random

class World:
    def __init__(self, width=10, height=10):
        self.width = width
        self.height = height
        self.grid = [["." for _ in range(width)] for _ in range(height)]

    def randomize_features(self):
        self.place_random("T", 10)  # 10 trees
        self.place_random("C", 1)   # 1 cave
        self.place_random("B", 1)   # 1 blacksmith
        self.place_random("S", 5)   # 5 stick piles

    def place_random(self, feature, count):
        for _ in range(count):
            x, y = random.randint(0, self.width - 1), random.randint(0, self.height - 1)
            while self.grid[y][x] != ".":  # Ensure the spot is empty
                x, y = random.randint(0, self.width - 1), random.randint(0, self.height - 1)
            self.grid[y][x] = feature

    def display(self, player):
        for y in range(self.height):
            row = ""
            for x in range(self.width):
                if (x, y) == player.position:
                    row += "P"
                else:
                    row += self.grid[y][x]
            print(row)
