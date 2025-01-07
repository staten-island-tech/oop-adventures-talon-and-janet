import pygame
from player import Player
from npc import NPC, Blacksmith
from item import Item, Wood, Stone, WoodenAxe, StoneAxe, WoodenPickaxe, StonePickaxe

class Game:
    def __init__(self, screen, font, screen_width, screen_height):
        self.screen = screen
        self.font = font
        self.screen_width = screen_width  
        self.screen_height = screen_height  
        self.player = Player()  
        self.npcs = [
            NPC("Guide", [5, 5], "Welcome to the sandbox world!"),
            Blacksmith("Blacksmith", [10, 10], "I can craft tools for you if you have the right materials.")
        ]
        self.blue_block = [7, 7]  
        self.quest_given = False  
        self.items = [
            Wood(),
            Stone()
        ]
        self.game_running = True  # Game loop flag

    def start_game(self):
        while self.game_running:
            self.screen.fill((255, 255, 255))  # Fill the screen with a white background

            # Display the game world
            self.display_game()

            # Handle user input and events
            self.player_input()

            # Update the screen
            pygame.display.flip()

    def display_game(self):
        # Display the player (as a block)
        pygame.draw.rect(self.screen, (0, 0, 255), (self.player.position[0] * 40, self.player.position[1] * 40, 40, 40))  # Blue square (player)
        
        # Display NPCs
        for npc in self.npcs:
            pygame.draw.rect(self.screen, (255, 0, 0), (npc.position[0] * 40, npc.position[1] * 40, 40, 40))  # Red square (NPC)

        # Display Blue Block for interaction
        self.display_blue_block()

        # Display the hotbar at the bottom
        self.display_hotbar()

        # Display the health bar with text (adjusted)
        self.display_health_bar()

        # Display the score at the top-left corner
        self.display_score()

        # Display text and player position above the black bar
        self.display_text()

        # Display guide quest text if the quest has been given
        if self.quest_given:
            self.display_quest_text()

    def display_blue_block(self):
        # Draw the blue block on the screen
        pygame.draw.rect(self.screen, (0, 0, 255), (self.blue_block[0] * 40, self.blue_block[1] * 40, 40, 40))  # Blue block for interaction
        
        # Check if the player is standing on the blue block
        if self.player.position == self.blue_block:
            self.display_question_prompt()

    def display_question_prompt(self):
        # Display a question prompt when the player stands on the blue block
        question_text = self.font.render("Do you want to interact with the blue block? (Y/N)", True, (255, 255, 255))
        self.screen.blit(question_text, (self.screen_width // 4, self.screen_height // 2))  # Center the text

    def display_hotbar(self):
        # Draw the black hotbar background
        pygame.draw.rect(self.screen, (0, 0, 0), (0, self.screen_height - 100, self.screen_width, 50))  # Black bar for hotbar

        # Draw item slots in the hotbar
        slot_width = self.screen_width // 9
        for i in range(9):
            pygame.draw.rect(self.screen, (255, 255, 255), (i * slot_width, self.screen_height - 100, slot_width, 50), 2)  # White box for items

            # Display item number (1-9) on the hotbar
            item_number = self.font.render(str(i + 1), True, (255, 255, 255))
            self.screen.blit(item_number, (i * slot_width + 10, self.screen_height - 90))  # Position item numbers

    def display_health_bar(self):
        # Adjust the health bar to be higher (around 100 pixels from the bottom)
        health_bar_y_position = self.screen_height - 150  # Move the health bar 100 pixels up from the bottom
        health_width = (self.player.health / 100) * self.screen_width  # Adjust width based on health percentage
        pygame.draw.rect(self.screen, (255, 0, 0), (0, health_bar_y_position, health_width, 20))  # Red bar

        # Display health text on top of the health bar
        health_text = self.font.render(f"Health: {self.player.health}", True, (255, 255, 255))
        self.screen.blit(health_text, (10, health_bar_y_position + 2))  # Display health text

    def display_score(self):
        # Display the score at the top-left corner
        score_text = f"Score: {self.player.score}"
        score_surface = self.font.render(score_text, True, (255, 255, 255))  # White text
        self.screen.blit(score_surface, (10, 10))  # Position score in the top-left corner

    def display_quest_text(self):
        # Display the guide's quest in orange color
        quest_text = "Quest: Find the mysterious blue block!"
        quest_surface = self.font.render(quest_text, True, (255, 165, 0))  # Orange text
        self.screen.blit(quest_surface, (self.screen_width // 2 - 100, self.screen_height - 200))  # Position the quest text

    def display_text(self):
        # Display position info above the black bar
        position_text = f"Position: {self.player.position}"
        position_surface = self.font.render(position_text, True, (255, 255, 255))  # White text

        # Draw the black bar at the bottom
        pygame.draw.rect(self.screen, (0, 0, 0), (0, self.screen_height - 50, self.screen_width, 50))  # Black bar
        
        # Position the position text on top of the black bar
        self.screen.blit(position_surface, (10, self.screen_height - 40))  # Position text

    def player_input(self):
        # Check for events (keyboard inputs, quit, etc.)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_running = False  # Close the game
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.player.move('w')  # Move up
                elif event.key == pygame.K_s:
                    self.player.move('s')  # Move down
                elif event.key == pygame.K_a:
                    self.player.move('a')  # Move left
                elif event.key == pygame.K_d:
                    self.player.move('d')  # Move right
                elif event.key == pygame.K_q:
                    self.game_running = False  # Quit the game
                elif event.key == pygame.K_y:
                    if self.player.position == self.blue_block:
                        print("You chose to interact with the blue block.")
                elif event.key == pygame.K_n:
                    if self.player.position == self.blue_block:
                        print("You chose not to interact with the blue block.")
                # Handle interactions with NPCs
                elif event.key == pygame.K_e:
                    for npc in self.npcs:
                        if self.player.position == npc.position:
                            npc.interact(self.player)
