import pygame
from game import Game
from pygame.locals import *

# Constants for screen size and font
SCREEN_WIDTH = 1200  # Width
SCREEN_HEIGHT = 1000  # Height

# Initialize Pygame
pygame.init()

# Use the system default font with size 36
FONT = pygame.font.SysFont('Arial', 36)

# Create the Pygame screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Untitled 2D Game")

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
    main_menu()

def main_menu():
    """Main menu screen"""
    menu_running = True
    while menu_running:
        screen.fill((0, 0, 0))  #Background

        # Draw the title centered at the top
        title_surface = FONT.render("Untitled 2D Game", True, (255, 255, 255))
        title_rect = title_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
        screen.blit(title_surface, title_rect)

        # Draw the "Start Game" and "Controls" buttons centered below the title
        draw_button(screen, "Start Game", SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 50, 300, 50, (0, 255, 0), (255, 255, 255))
        draw_button(screen, "Controls", SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 50, 300, 50, (255, 165, 0), (255, 255, 255))

        for event in pygame.event.get():
            if event.type == QUIT:
                menu_running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    mouse_pos = pygame.mouse.get_pos()
                    if SCREEN_WIDTH // 2 - 150 <= mouse_pos[0] <= SCREEN_WIDTH // 2 + 150 and SCREEN_HEIGHT // 2 - 50 <= mouse_pos[1] <= SCREEN_HEIGHT // 2:
                        start_game()  # Start the game when "Start Game" is clicked
                        menu_running = False
                    elif SCREEN_WIDTH // 2 - 150 <= mouse_pos[0] <= SCREEN_WIDTH // 2 + 150 and SCREEN_HEIGHT // 2 + 50 <= mouse_pos[1] <= SCREEN_HEIGHT // 2 + 100:
                        show_controls()  # Show controls when "Controls" is clicked
                        menu_running = False

        pygame.display.flip()

def main():
    """Main function to run the game"""
    main_menu()

if __name__ == "__main__":
    main()
