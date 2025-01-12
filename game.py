import pygame
from pygame.locals import *

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 1000

pygame.init()

FONT = pygame.font.SysFont('Arial', 36)

def draw_button(screen, text, x, y, width, height, bg_color, text_color):
    """Draws a button with text on the screen."""
    pygame.draw.rect(screen, bg_color, (x, y, width, height))
    pygame.draw.rect(screen, (255, 255, 255), (x, y, width, height), 2)  # Add a border
    button_text = FONT.render(text, True, text_color)
    text_rect = button_text.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(button_text, text_rect)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Untitled 2D Game")

tree_img = pygame.image.load('tree.png')
cave_entrance_img = pygame.image.load('cave_entrance.png')
cave_img = pygame.image.load('cave.png')
rock_img = pygame.image.load('rock.png')

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
        self.hotbar_items = [None] * 9
        self.in_cave = False
        self.has_pickaxe = False

    def draw_health_bar(self):
        """Draw the health bar at the top of the screen."""
        health_bar_width = self.screen_width - 20
        health_bar_height = 50
        health_bar_x = 10
        health_bar_y = 10 

        pygame.draw.rect(self.screen, (255, 0, 0), (health_bar_x, health_bar_y, health_bar_width, health_bar_height))
        health_text = self.font.render(f"Health: {self.health}%", True, (255, 255, 255))
        self.screen.blit(health_text, (health_bar_x, health_bar_y))

    def draw_hotbar(self):
        """Draw the hotbar at the bottom of the screen."""
        hotbar_width = self.screen_width - 20
        hotbar_height = 50
        hotbar_x = 10
        hotbar_y = self.screen_height - hotbar_height - 10

        pygame.draw.rect(self.screen, (255, 0, 0), (hotbar_x - 5, hotbar_y - 5, hotbar_width + 10, hotbar_height + 10), 5)
        pygame.draw.rect(self.screen, (50, 50, 50), (hotbar_x, hotbar_y, hotbar_width, hotbar_height))

        box_width = (self.screen_width - 20) // 9
        for i in range(9):
            box_x = hotbar_x + i * box_width
            pygame.draw.rect(self.screen, (100, 100, 100), (box_x, hotbar_y, box_width, hotbar_height))

            number_text = self.font.render(str(i + 1), True, (255, 255, 255))
            self.screen.blit(number_text, (box_x + 5, hotbar_y + 5)) 
            
            if i == self.selected_hotbar:
                pygame.draw.rect(self.screen, (255, 255, 255), (box_x, hotbar_y, box_width, hotbar_height), 5)

    def move_square(self):
        keys = pygame.key.get_pressed()
        top_limit = 60  
        bottom_limit = self.screen_height - 110
        if keys[K_w] and self.y > top_limit:
            self.y -= self.speed
        if keys[K_s] and self.y < bottom_limit:
            self.y += self.speed
        if keys[K_a] and self.x > 0:
            self.x -= self.speed
        if keys[K_d] and self.x < self.screen_width - self.size:
            self.x += self.speed

    def select_hotbar_item(self):
        keys = pygame.key.get_pressed()
        for i in range(9):
            if keys[K_1 + i]: 
                self.selected_hotbar = i

    def draw_interaction_boxes(self):
        """Draw interaction boxes depending on the game state."""
        if self.in_cave:
            # Rock (inside the cave)
            rock_box_x = self.screen_width - 250
            rock_box_y = 250
            rock_box_width = 200
            rock_box_height = 100
            pygame.draw.rect(self.screen, (0, 0, 255), (rock_box_x, rock_box_y, rock_box_width, rock_box_height))
            self.screen.blit(rock_img, (self.screen_width - 200, 250))

            # Exit cave box
            exit_cave_box_x = 50
            exit_cave_box_y = 150
            exit_cave_box_width = 300
            exit_cave_box_height = 100
            pygame.draw.rect(self.screen, (0, 0, 255), (exit_cave_box_x, exit_cave_box_y, exit_cave_box_width, exit_cave_box_height))
        else:
            # Cave entrance and tree (outside the cave)
            cave_box_x = 50
            cave_box_y = 150
            cave_box_width = 300
            cave_box_height = 100
            pygame.draw.rect(self.screen, (0, 0, 255), (cave_box_x, cave_box_y, cave_box_width, cave_box_height))
            self.screen.blit(cave_entrance_img, (50, 150))

            # Tree box
            tree_box_x = self.screen_width - 250
            tree_box_y = 750
            tree_box_width = 200
            tree_box_height = 100
            pygame.draw.rect(self.screen, (0, 0, 255), (tree_box_x, tree_box_y, tree_box_width, tree_box_height))
            self.screen.blit(tree_img, (self.screen_width - 200, 700))

    def handle_interactions(self):
        keys = pygame.key.get_pressed()

        # Tree interaction (outside the cave)
        if not self.in_cave and self.screen_width - 250 <= self.x <= self.screen_width - 50 and 750 <= self.y <= 850:
            if keys[K_e]:
                print("The tree whispers: 'Welcome to the forest...'")

        # Cave entrance interaction (outside the cave)
        if not self.in_cave and 50 <= self.x <= 350 and 150 <= self.y <= 250:
            if keys[K_e]:
                print("You enter the cave...")
                self.in_cave = True

        # Rock interaction (inside the cave)
        if self.in_cave and self.screen_width - 250 <= self.x <= self.screen_width - 50 and 250 <= self.y <= 350:
            if keys[K_e]:
                if self.has_pickaxe:
                    print("You acquire some rocks!")
                else:
                    print("You need a pickaxe to acquire rocks.")

        # Exit cave interaction
        if self.in_cave and 50 <= self.x <= 350 and 150 <= self.y <= 250:
            if keys[K_e]:
                print("You exit the cave...")
                self.in_cave = False

    def start_game(self):
        """Main game loop."""
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


def start_game():
    """Function to start the game."""
    game = Game(screen, FONT, SCREEN_WIDTH, SCREEN_HEIGHT)
    game.start_game()


def main_menu():
    """Main menu screen."""
    menu_running = True
    while menu_running:
        screen.fill((0, 0, 0))  # Black background
        draw_button(screen, "Untitled 2D Game", 0, 0, SCREEN_WIDTH, 100, (50, 50, 50), (255, 255, 255))
        draw_button(screen, "Start Game", 100, 200, 300, 50, (0, 255, 0), (255, 255, 255))

        for event in pygame.event.get():
            if event.type == QUIT:
                menu_running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    mouse_pos = pygame.mouse.get_pos()
                    if 100 <= mouse_pos[0] <= 400 and 200 <= mouse_pos[1] <= 250:
                        start_game()
                        menu_running = False

        pygame.display.flip()


def main():
    """Main function to run the game."""
    main_menu()


if __name__ == "__main__":
    main()
