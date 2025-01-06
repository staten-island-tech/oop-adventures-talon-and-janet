import pygame
from game import Game

# Constants for screen size and font
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# Initialize Pygame
pygame.init()

# Use the system default font with size 36
FONT = pygame.font.SysFont('Arial', 36)

# Create the Pygame screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Text-Based 2D Sandbox Game")

def main():
    game = Game(screen, FONT, SCREEN_WIDTH, SCREEN_HEIGHT)  # Pass the dimensions here
    game.start_game()

if __name__ == "__main__":
    main()
