import pygame
from pygame.locals import *

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 1000

pygame.init()

FONT = pygame.font.SysFont('Arial', 36)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Untitled 2D Game")

# Load images
tree_img = pygame.image.load('tree.png')
cave_entrance_img = pygame.image.load('cave_entrance.png')
cave_img = pygame.image.load('cave.png')

class Game:
    def __init__(self, screen, font, screen_width, screen_height):
        self.screen = screen
        self.font = font
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.health = 100
        self.x = 500
        self.y = 500
        self.size = 50
        self.speed = 1
        self.selected_hotbar = 0
        self.hotbar_items = [None] * 9  # 9 item slots (hotbar)
        self.in_cave = False  # Track if the player is inside the cave

    def draw_health_bar(self):
        """Draw the health bar at the top of the screen but move it down slightly"""
        health_bar_width = self.screen_width - 20
        health_bar_height = 50
        health_bar_x = 10
        health_bar_y = 10 

        # Health bar
        pygame.draw.rect(self.screen, (255, 0, 0), (health_bar_x, health_bar_y, health_bar_width, health_bar_height))

        # Draw the health text (with slightly adjusted position to keep it in the same place)
        health_text = self.font.render(f"Health: {self.health}%", True, (255, 255, 255))
        self.screen.blit(health_text, (health_bar_x, health_bar_y))  # Keep text in place

    def draw_hotbar(self):
        """Draw the hotbar at the bottom of the screen"""
        hotbar_width = self.screen_width - 20
        hotbar_height = 50
        hotbar_x = 10
        hotbar_y = self.screen_height - hotbar_height - 10

        # Draw the red outline (border) around the hotbar
        pygame.draw.rect(self.screen, (255, 0, 0), (hotbar_x - 5, hotbar_y - 5, hotbar_width + 10, hotbar_height + 10), 5)

        # Draw the hotbar background (gray)
        pygame.draw.rect(self.screen, (50, 50, 50), (hotbar_x, hotbar_y, hotbar_width, hotbar_height))

        # Draw the hotbar items (with numbers in each box)
        box_width = (self.screen_width - 20) // 9
        for i in range(9):
            box_x = hotbar_x + i * box_width
            pygame.draw.rect(self.screen, (100, 100, 100), (box_x, hotbar_y, box_width, hotbar_height))

            # Draw the number on the top-left corner of each box
            number_text = self.font.render(str(i + 1), True, (255, 255, 255))
            self.screen.blit(number_text, (box_x + 5, hotbar_y + 5))  # Small number at the top-left

            # Highlight the selected box
            if i == self.selected_hotbar:
                pygame.draw.rect(self.screen, (255, 255, 255), (box_x, hotbar_y, box_width, hotbar_height), 5)

    def move_square(self):
        """Move the square on the screen with WASD, restricted by the border"""
        keys = pygame.key.get_pressed()

        # Calculate movement limits based on health bar (above) and hotbar (below)
        top_limit = 60  # Just below the health bar
        bottom_limit = self.screen_height - (110)  # Just above the hotbar

        if keys[K_w] and self.y > top_limit:  # Prevent going above health bar
            self.y -= self.speed
        if keys[K_s] and self.y < bottom_limit:  # Prevent going below hotbar
            self.y += self.speed
        if keys[K_a] and self.x > 0:
            self.x -= self.speed
        if keys[K_d] and self.x < self.screen_width - self.size:
            self.x += self.speed

    def select_hotbar_item(self):
        """Switch selected hotbar item with number keys"""
        keys = pygame.key.get_pressed()
        for i in range(9):
            if keys[K_1 + i]:  # Check for number key press (1-9)
                self.selected_hotbar = i

    def draw_interaction_boxes(self):
        """Draw interaction boxes for tree and cave"""
        # Draw a blue box in front of the cave entrance
        cave_box_x = 50
        cave_box_y = 50
        cave_box_width = 200
        cave_box_height = 100
        pygame.draw.rect(self.screen, (0, 0, 255), (cave_box_x, cave_box_y, cave_box_width, cave_box_height))

        # Draw a blue box in front of the tree
        tree_box_x = self.screen_width - 250
        tree_box_y = 50
        tree_box_width = 200
        tree_box_height = 100
        pygame.draw.rect(self.screen, (0, 0, 255), (tree_box_x, tree_box_y, tree_box_width, tree_box_height))

        # Show a tree image in the top right
        self.screen.blit(tree_img, (self.screen_width - 200, 50))

        # Show the cave entrance image in the top left
        self.screen.blit(cave_entrance_img, (50, 50))

    def handle_interactions(self):
        """Handle interactions for the tree and cave"""
        keys = pygame.key.get_pressed()

        # Check if the player is in front of the tree
        if self.x >= self.screen_width - 250 and self.y >= 50 and self.y <= 150:
            if keys[K_e]:
                choice = input("Do you want to grab sticks (1), cut the tree (requires an axe (2)), or leave (0): ")
                if choice == '1':
                    print("You grab some sticks.")
                elif choice == '2' and any(item == "Axe" for item in self.hotbar_items):
                    print("You cut the tree down.")
                elif choice == '0':
                    print("You leave the tree.")

        # Check if the player is in front of the cave entrance
        if self.x <= 250 and self.y >= 50 and self.y <= 150:
            if keys[K_e]:
                choice = input("Do you want to enter the cave? (1 to enter, 0 to leave): ")
                if choice == '1':
                    self.in_cave = True
                    print("Entering the cave...")
                elif choice == '0':
                    print("You leave the cave entrance.")

    def start_game(self):
        """Main game loop"""
        running = True
        while running:
            self.screen.fill((0, 0, 0))  # Black background

            if self.in_cave:
                self.screen.blit(cave_img, (0, 0))  # Set the background to cave.png

            # Handle events
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False

            # Move the square based on user input
            self.move_square()

            # Draw health bar
            self.draw_health_bar()

            # Draw hotbar
            self.draw_hotbar()

            # Draw the moving square
            pygame.draw.rect(self.screen, (0, 255, 0), (self.x, self.y, self.size, self.size))

            # Draw interaction areas
            self.draw_interaction_boxes()

            # Handle interactions
            self.handle_interactions()

            # Update the display
            pygame.display.flip()

            # Handle key events for hotbar item selection
            self.select_hotbar_item()


def draw_button(screen, text, x, y, width, height, color, text_color):
    """Draw a button with text"""
    pygame.draw.rect(screen, color, (x, y, width, height))
    text_surface = FONT.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text_surface, text_rect)


def start_game():
    """Function to start the game"""
    game = Game(screen, FONT, SCREEN_WIDTH, SCREEN_HEIGHT)  # Initialize game
    game.start_game()  # Start the main game loop


def show_controls():
    """Function to display the controls screen"""
    controls_running = True
    while controls_running:
        screen.fill((0, 0, 0))  # Black background
        draw_button(screen, "Controls", 0, 0, SCREEN_WIDTH, 100, (50, 50, 50), (255, 255, 255))
        control_text = [
            "1-9: Select items from Hotbar",
            "W: Move Up",
            "S: Move Down",
            "A: Move Left",
            "D: Move Right",
            "E: Interact with objects"
        ]

        y_offset = 120
        for text in control_text:
            control_surface = FONT.render(text, True, (255, 255, 255))
            screen.blit(control_surface, (50, y_offset))
            y_offset += 40

        for event in pygame.event.get():
            if event.type == QUIT:
                controls_running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    mouse_pos = pygame.mouse.get_pos()
                    if (0 <= mouse_pos[0] <= SCREEN_WIDTH and 0 <= mouse_pos[1] <= 100):
                        controls_running = False  # Close controls screen when clicked

        pygame.display.flip()


def main_menu():
    """Main menu screen"""
    menu_running = True
    while menu_running:
        screen.fill((0, 0, 0))  # Black background
        draw_button(screen, "Untitled 2D Game", 0, 0, SCREEN_WIDTH, 100, (50, 50, 50), (255, 255, 255))
        draw_button(screen, "Start Game", 100, 200, 300, 50, (0, 255, 0), (255, 255, 255))
        draw_button(screen, "Controls", 100, 300, 300, 50, (255, 165, 0), (255, 255, 255))

        for event in pygame.event.get():
            if event.type == QUIT:
                menu_running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    mouse_pos = pygame.mouse.get_pos()
                    if 100 <= mouse_pos[0] <= 400 and 200 <= mouse_pos[1] <= 250:
                        start_game()  # Start the game when "Start Game" is clicked
                        menu_running = False
                    elif 100 <= mouse_pos[0] <= 400 and 300 <= mouse_pos[1] <= 350:
                        show_controls()  # Show controls when "Controls" is clicked
                        menu_running = False

        pygame.display.flip()


def main():
    """Main function to run the game"""
    main_menu()


if __name__ == "__main__":
    main()
