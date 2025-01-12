class TextGame:
    def __init__(self):
        self.health = 100
        self.x = 0
        self.y = 0
        self.size = 1
        self.speed = 1
        self.selected_hotbar = 0
        self.hotbar_items = [None] * 9
        self.in_cave = False
        self.has_pickaxe = False
        self.has_axe = False

    def display_status(self):
        """Displays the current game status."""
        print("\n========== STATUS ==========")
        print(f"Health: {self.health}%")
        print(f"Location: {'Cave' if self.in_cave else 'Forest'}")
        print(f"Hotbar: {self.hotbar_items}")
        print(f"Selected Hotbar Slot: {self.selected_hotbar + 1}")
        print("============================\n")

    def move(self, direction):
        """Handles movement commands."""
        directions = {
            "north": (0, -1),
            "south": (0, 1),
            "east": (1, 0),
            "west": (-1, 0),
        }
        if direction in directions:
            dx, dy = directions[direction]
            self.x += dx * self.speed
            self.y += dy * self.speed
            print(f"You move {direction}.")
        else:
            print("Invalid direction! Use 'north', 'south', 'east', or 'west'.")

    def tree_interaction(self):
        """Handles tree interactions."""
        print("\nYou approach a tree. What would you like to do?")
        print("1. Cut down the tree (requires axe)")
        print("2. Grab some sticks")
        print("3. Leave")
        choice = input("> ").strip()
        if choice == "1":
            if self.has_axe:
                print("You cut down the tree and collected wood!")
            else:
                print("You need an axe to cut down the tree.")
        elif choice == "2":
            print("You grab some sticks from the tree and put them in your hotbar.")
            self.hotbar_items[8] = "stick.png"  # Put the stick item in the 9th hotbar slot
        elif choice == "3":
            print("You walk away from the tree.")
        else:
            print("Invalid choice!")

    def cave_entrance_interaction(self):
        """Handles cave entrance interactions."""
        print("\nYou are at the cave entrance. What would you like to do?")
        print("1. Enter the cave")
        print("2. Leave")
        choice = input("> ").strip()
        if choice == "1":
            print("You enter the cave.")
            self.in_cave = True
        elif choice == "2":
            print("You decide to stay outside.")
        else:
            print("Invalid choice!")

    def inside_cave_interaction(self):
        """Handles interactions inside the cave."""
        print("\nYou are inside the cave. What would you like to do?")
        print("1. Leave the cave")
        print("2. Stay")
        choice = input("> ").strip()
        if choice == "1":
            print("You leave the cave.")
            self.in_cave = False
        elif choice == "2":
            print("You remain inside the cave.")
        else:
            print("Invalid choice!")

    def handle_interaction(self):
        """Handles player interactions."""
        if self.in_cave:
            self.inside_cave_interaction()
        else:
            print("\nYou see a tree and a cave entrance nearby. What would you like to interact with?")
            print("1. Tree")
            print("2. Cave Entrance")
            print("3. Nothing")
            choice = input("> ").strip()
            if choice == "1":
                self.tree_interaction()
            elif choice == "2":
                self.cave_entrance_interaction()
            elif choice == "3":
                print("You decide to do nothing for now.")
            else:
                print("Invalid choice!")

    def start_game(self):
        """Starts the text-based game."""
        print("Welcome to the Text-Based 2D Game!")
        while True:
            self.display_status()
            print("What would you like to do?")
            print("1. Move")
            print("2. Interact")
            print("3. Exit Game")
            choice = input("> ").strip()
            if choice == "1":
                print("Which direction? (north, south, east, west)")
                direction = input("> ").strip().lower()
                self.move(direction)
            elif choice == "2":
                self.handle_interaction()
            elif choice == "3":
                print("Thank you for playing!")
                break
            else:
                print("Invalid choice! Please select a valid action.")

if __name__ == "__main__":
    game = TextGame()
    game.start_game()
