import random
class Battle:
    def __init__(self, player):
        self.player = player

    def battle_scene(self):
        print("\nA battle starts! You encounter two slimes!")
        slime_healths = [5, 5]  
        player_health = 20  

        while any(hp > 0 for hp in slime_healths):  
            print("\nYour Health:", player_health)
            print("Slime 1 Health:", slime_healths[0], "Slime 2 Health:", slime_healths[1])
            print("1. Throw Pickaxe (2 damage, lose pickaxe)")
            print("2. Throw Axe (3 damage, lose axe)")
            print("3. Slap with Sword (4 damage, 40% crit for 10 damage)")
            print("4. Run away")

            action = input("> ")

            if action == "1":  
                if "Wood pickaxe" in self.player.inventory.inventory or "Stone pickaxe" in self.player.inventory.inventory:
                    print("You throw your pickaxe and deal 2 damage!")
                    target = 0 if slime_healths[0] > 0 else 1
                    slime_healths[target] = max(0, slime_healths[target] - 2)
                    self.player.inventory.remove_from_inventory("Wood pickaxe", 1)
                    self.player.inventory.remove_from_inventory("Stone pickaxe", 1)
                else:
                    print("You don't have a pickaxe!")

            elif action == "2":  
                if "Wood axe" in self.player.inventory.inventory or "Stone axe" in self.player.inventory.inventory:
                    print("You throw your axe and deal 3 damage!")
                    target = 0 if slime_healths[0] > 0 else 1
                    slime_healths[target] = max(0, slime_healths[target] - 3)
                    self.player.inventory.remove_from_inventory("Wood axe", 1)
                    self.player.inventory.remove_from_inventory("Stone axe", 1)
                else:
                    print("You don't have an axe!")

            elif action == "3":  
                if "Stone sword" in self.player.inventory.inventory or "Wood sword" in self.player.inventory.inventory:
                    damage = 4
                    if random.random() <= 0.4:  
                        damage = 10
                        print("Critical hit!")
                    else:
                        print("You deal 4 damage!")
                    target = 0 if slime_healths[0] > 0 else 1
                    slime_healths[target] = max(0, slime_healths[target] - damage)
                else:
                    print("You don't have a sword!")

            elif action == "4":  
                print("You attempt to run away, but the slimes trap you with sticky slime!")
                player_health -= 5
                print("You lose 5 health.")
                if player_health <= 0:
                    print("You succumbed to the slimes' attack!")
                    return

            else:
                print("Invalid action.")
                continue

            
            for i, hp in enumerate(slime_healths):
                if hp > 0:
                    print(f"Slime {i + 1} attacks you! You lose 2 health.")
                    player_health -= 2

            if player_health <= 0:
                print("You were defeated by the slimes!")
                return

        print("\nYou defeated the slimes!")
        print("The final slime boss appears!")
        self.final_boss_battle(player_health)

    def final_boss_battle(self, player_health):
        boss_health = 200
        print("\nThe final slime boss has 200 health! Fight or perish!")
        while player_health > 0 and boss_health > 0:
            print("\nYour Health:", player_health)
            print("Boss Health:", boss_health)
            print("1. Throw Pickaxe (2 damage, lose pickaxe)")
            print("2. Throw Axe (3 damage, lose axe)")
            print("3. Slap with Sword (4 damage, 40% crit for 10 damage)")
            print("4. Run away")

            action = input("> ")

            if action == "1":  
                if "Wood pickaxe" in self.player.inventory.inventory or "Stone pickaxe" in self.player.inventory.inventory:
                    print("You throw your pickaxe and deal 2 damage!")
                    boss_health = max(0, boss_health - 2)
                    self.player.inventory.remove_from_inventory("Wood pickaxe", 1)
                    self.player.inventory.remove_from_inventory("Stone pickaxe", 1)
                else:
                    print("You don't have a pickaxe!")

            elif action == "2":  
                if "Wood axe" in self.player.inventory.inventory or "Stone axe" in self.player.inventory.inventory:
                    print("You throw your axe and deal 3 damage!")
                    boss_health = max(0, boss_health - 3)
                    self.player.inventory.remove_from_inventory("Wood axe", 1)
                    self.player.inventory.remove_from_inventory("Stone axe", 1)
                else:
                    print("You don't have an axe!")

            elif action == "3":  
                if "Stone sword" in self.player.inventory.inventory or "Wood sword" in self.player.inventory.inventory:
                    damage = 4
                    if random.random() <= 0.4:  
                        damage = 10
                        print("Critical hit!")
                    else:
                        print("You deal 4 damage!")
                    boss_health = max(0, boss_health - damage)
                else:
                    print("You don't have a sword!")

            elif action == "4":  
                print("The slime boss blocks your path! You cannot escape.")
                continue

            else:
                print("Invalid action.")
                continue

            print("The boss attacks you! You lose 10 health.")
            player_health -= 10

        if player_health <= 0:
            print("\nYou were defeated by the final slime boss!")
        else:
            print("\nYou defeated the final slime boss! Victory is yours!")