class World:
    def __init__(self, width=10, height=10):
        self.width = width
        self.height = height
        self.grid = [["." for _ in range(width)] for _ in range(height)]
        self.place_trees()

    def place_trees(self):
        # Place some trees on the grid ('T')
        for i in range(3, self.height, 3):
            for j in range(3, self.width, 3):
                self.grid[i][j] = "T"

    def display(self, player):
        for y in range(self.height):
            row = ""
            for x in range(self.width):
                if (x, y) == player.position:
                    row += "P"  # Player position
                else:
                    row += self.grid[y][x]
            print(row)
