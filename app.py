import random
import json
import os

class Player:
    def __init__(self):
        self.name = input("What is your name? ")
        print("Choose a race:")
        print("1. Human")
        print("2. Elf")
        print("3. Dwarf")
        print("4. Orc")
        self.race = input("Enter the number of your chosen race: ")
        if self.race == "1":
            print("Humans are known for their versatility and adaptability.")
            print("Perks: +10% to all stats")
            confirm_race = input("Are you sure you want to choose Human? (yes/no) ")
            if confirm_race.lower() == "yes":
                self.race = "Human"
            else:
                self.race = input("Enter the number of your chosen race: ")
        elif self.race == "2":
            print("Elves are known for their agility and quick reflexes.")
            print("Perks: +20% to agility, +10% to intelligence")
            confirm_race = input("Are you sure you want to choose Elf? (yes/no) ")
            if confirm_race.lower() == "yes":
                self.race = "Elf"
            else:
                self.race = input("Enter the number of your chosen race: ")
        elif self.race == "3":
            print("Dwarves are known for their strength and resilience.")
            print("Perks: +20% to strength, +10% to vitality")
            confirm_race = input("Are you sure you want to choose Dwarf? (yes/no) ")
            if confirm_race.lower() == "yes":
                self.race = "Dwarf"
            else:
                self.race = input("Enter the number of your chosen race: ")
        elif self.race == "4":
            print("Orcs are known for their ferocity and brute strength.")
            print("Perks: +20% to strength, +10% to agility")
            confirm_race = input("Are you sure you want to choose Orc? (yes/no) ")
            if confirm_race.lower() == "yes":
                self.race = "Orc"
            else:
                self.race = input("Enter the number of your chosen race: ")

        print("Choose a class:")
        print("1. Warrior")
        print("2. Mage")
        print("3. Rogue")
        print("4. Paladin")
        print("5. Assassin")
        print("6. Archer")
        print("7. Monk")
        print("8. Alchemist")
        print("9. Spiritualist")
        print("10. Martial Artist")
        self.class_type = input("Enter the number of your chosen class: ")
        if self.class_type == "1":
            print("Warriors are known for their strength and combat prowess.")
            print("Abilities: Slash, Shield Block, Charge, Battle Cry")
            confirm_class = input("Are you sure you want to choose Warrior? w(yes/no) ")
            if confirm_class.lower() == "yes":
                self.class_type = "Warrior"
            else:
                self.class_type = input("Enter the number of your chosen class: ")
        elif self.class_type == "2":
            print("Mages are known for their magical abilities and intelligence.")
            print("Abilities: Fireball, Healing Spell, Lightning Bolt, Mana Shield")
            confirm_class = input("Are you sure you want to choose Mage? (yes/no) ")
            if confirm_class.lower() == "yes":
                self.class_type = "Mage"
            else:
                self.class_type = input("Enter the number of your chosen class: ")
        elif self.class_type == "3":
            print("Rogues are known for their agility and stealth.")
            print("Abilities: Stealth, Poison Strike, Backstab, Smoke Bomb")
            confirm_class = input("Are you sure you want to choose Rogue? (yes/no) ")
            if confirm_class.lower() == "yes":
                self.class_type = "Rogue"
            else:
                self.class_type = input("Enter the number of your chosen class: ")
        elif self.class_type == "4":
            print("Paladins are known for their strength and holy magic.")
            print("Abilities: Holy Strike, Shield of Faith, Healing Aura, Divine Intervention")
            confirm_class = input("Are you sure you want to choose Paladin? (yes/no) ")
            if confirm_class.lower() == "yes":
                self.class_type = "Paladin"
            else:
                self.class_type = input("Enter the number of your chosen class: ")
        elif self.class_type == "5":
            print("Assassins are known for their agility and deadly precision.")
            print("Abilities: Backstab, Smoke Bomb, Shadow Step, Deadly Strike")
            confirm_class = input("Are you sure you want to choose Assassin? (yes/no) ")
            if confirm_class.lower() == "yes":
                self.class_type = "Assassin"
            else:
                self.class_type = input("Enter the number of your chosen class: ")
        elif self.class_type == "6":
            print("Archers are known for their agility and ranged combat.")
            print("Abilities: Shoot Arrow, Rapid Fire, Precision Shot, Camouflage")
            confirm_class = input("Are you sure you want to choose Archer? (yes/no) ")
            if confirm_class.lower() == "yes":
                self.class_type = "Archer"
            else:
                self.class_type = input("Enter the number of your chosen class: ")
        elif self.class_type == "7":
            print("Monks are known for their agility and martial arts skills.")
            print("Abilities: Meditate, Kung Fu, Healing Hands, Inner Peace")
            confirm_class = input("Are you sure you want to choose Monk? (yes/no) ")
            if confirm_class.lower() == "yes":
                self.class_type = "Monk"
            else:
                self.class_type = input("Enter the number of your chosen class: ")
        elif self.class_type == "8":
            print("Alchemists are known for their intelligence and potion-making skills.")
            print("Abilities: Mix Potion, Create Bomb, Healing Potion, Poisonous Gas")
            confirm_class = input("Are you sure you want to choose Alchemist? (yes/no) ")
            if confirm_class.lower() == "yes":
                self.class_type = "Alchemist"
            else:
                self.class_type = input("Enter the number of your chosen class: ")
        elif self.class_type == "9":
            print("Spiritualists are known for their intelligence and magical abilities.")
            print("Abilities: Summon Spirit, Healing Prayer, Protective Barrier, Divine Judgment")
            confirm_class = input("Are you sure you want to choose Spiritualist? (yes/no) ")
            if confirm_class.lower() == "yes":
                self.class_type = "Spiritualist"
            else:
                self.class_type = input("Enter the number of your chosen class: ")
        elif self.class_type == "10":
            print("Martial Artists are known for their agility and martial arts skills.")
            print("Abilities: Martial Arts, Kicking Technique, Punching Technique, Defensive Stance")
            confirm_class = input("Are you sure you want to choose Martial Artist? (yes/no) ")
            if confirm_class.lower() == "yes":
                self.class_type = "Martial Artist"
            else:
                self.class_type = input("Enter the number of your chosen class: ")

        self.level = 1
        self.experience = 0
        self.health = 100
        self.hunger = 100
        self.tiredness = 100
        self.inventory = []
        self.abilities = []
        self.skill_points = 0
        self.skills = {
            "Strength": 10,
            "Agility": 10,
            "Intelligence": 10,
            "Vitality": 10
        }

        if self.class_type == "Warrior":
            self.abilities.append("Slash")
            self.abilities.append("Shield Block")
            self.abilities.append("Charge")
            self.abilities.append("Battle Cry")
            self.skills["Strength"] += 5
        elif self.class_type == "Mage":
            self.abilities.append("Fireball")
            self.abilities.append("Healing Spell")
            self.abilities.append("Lightning Bolt")
            self.abilities.append("Mana Shield")
            self.skills["Intelligence"] += 5
        elif self.class_type == "Rogue":
            self.abilities.append("Stealth")
            self.abilities.append("Poison Strike")
            self.abilities.append("Backstab")
            self.abilities.append("Smoke Bomb")
            self.skills["Agility"] += 5
        elif self.class_type == "Paladin":
            self.abilities.append("Holy Strike")
            self.abilities.append("Shield of Faith")
            self.abilities.append("Healing Aura")
            self.abilities.append("Divine Intervention")
            self.skills["Vitality"] += 5
        elif self.class_type == "Assassin":
            self.abilities.append("Backstab")
            self.abilities.append("Smoke Bomb")
            self.abilities.append("Shadow Step")
            self.abilities.append("Deadly Strike")
            self.skills["Agility"] += 5
        elif self.class_type == "Archer":
            self.abilities.append("Shoot Arrow")
            self.abilities.append("Rapid Fire")
            self.abilities.append("Precision Shot")
            self.abilities.append("Camouflage")
            self.skills["Agility"] += 5
        elif self.class_type == "Monk":
            self.abilities.append("Meditate")
            self.abilities.append("Kung Fu")
            self.abilities.append("Healing Hands")
            self.abilities.append("Inner Peace")
            self.skills["Vitality"] += 5
        elif self.class_type == "Alchemist":
            self.abilities.append("Mix Potion")
            self.abilities.append("Create Bomb")
            self.abilities.append("Healing Potion")
            self.abilities.append("Poisonous Gas")
            self.skills["Intelligence"] += 5
        elif self.class_type == "Spiritualist":
            self.abilities.append("Summon Spirit")
            self.abilities.append("Healing Prayer")
            self.abilities.append("Protective Barrier")
            self.abilities.append("Divine Judgment")
            self.skills["Intelligence"] += 5
        elif self.class_type == "Martial Artist":
            self.abilities.append("Martial Arts")
            self.abilities.append("Kicking Technique")
            self.abilities.append("Punching Technique")
            self.abilities.append("Defensive Stance")
            self.skills["Agility"] += 5

    def access_inventory(self):
        print("You have the following items in your inventory:")
        for item in self.inventory:
            print(item)

    def use_abilities(self):
        print("You have the following abilities:")
        for ability in self.abilities:
            print(ability)

        ability_to_use = input("Which ability would you like to use? ")

        if ability_to_use in self.abilities:
            roll = random.randint(1, 20)
            if roll <= 5:
                print("You failed to use the ability.")
            elif roll <= 10:
                print("You used the ability, but it was not very effective.")
            elif roll <= 15:
                print("You used the ability successfully.")
            elif roll <= 18:
                print("You used the ability with great success.")
            elif roll == 19:
                print("You used the ability with exceptional success.")
            elif roll == 20:
                print("You used the ability with perfect success.")
        else:
            print("You do not have that ability.")

    def rest(self):
        self.health += 10
        self.hunger += 10
        self.tiredness += 10
        print("You rested and regained some health, hunger, and tiredness.")

    def is_dead(self):
        if self.health <= 0:
            return True
        return False

    def level_up(self):
        self.level += 1
        self.experience = 0
        self.skill_points += 1
        print("You have leveled up! You are now level", self.level)

    def upgrade_class(self):
        if self.level >= 10:
            print("You can upgrade your class to:")
            print("1. Knight (Warrior)")
            print("2. Wizard (Mage)")
            print("3. Thief (Rogue)")
            print("4. Holy Knight (Paladin)")
            print("5. Shadow Assassin (Assassin)")
            print("6. Huntsman (Archer)")
            print("7. Martial Artist (Monk)")
            print("8. Chemist (Alchemist)")
            print("9. Shaman (Spiritualist)")
            print("10. Kung Fu Master (Martial Artist)")

            class_to_upgrade_to = input("Which class would you like to upgrade to? ")

            if class_to_upgrade_to == "1" and self.class_type == "Warrior":
                self.class_type = "Knight"
                self.abilities.append("Charge")
                self.skills["Strength"] += 5
            elif class_to_upgrade_to == "2" and self.class_type == "Mage":
                self.class_type = "Wizard"
                self.abilities.append("Lightning Bolt")
                self.skills["Intelligence"] += 5
            elif class_to_upgrade_to == "3" and self.class_type == "Rogue":
                self.class_type = "Thief"
                self.abilities.append("Backstab")
                self.skills["Agility"] += 5
            elif class_to_upgrade_to == "4" and self.class_type == "Paladin":
                self.class_type = "Holy Knight"
                self.abilities.append("Healing Aura")
                self.skills["Vitality"] += 5
            elif class_to_upgrade_to == "5" and self.class_type == "Assassin":
                self.class_type = "Shadow Assassin"
                self.abilities.append("Shadow Step")
                self.skills["Agility"] += 5
            elif class_to_upgrade_to == "6" and self.class_type == "Archer":
                self.class_type = "Huntsman"
                self.abilities.append("Precision Shot")
                self.skills["Agility"] += 5
            elif class_to_upgrade_to == "7" and self.class_type == "Monk":
                self.class_type = "Martial Artist"
                self.abilities.append("Kung Fu")
                self.skills["Vitality"] += 5
            elif class_to_upgrade_to == "8" and self.class_type == "Alchemist":
                self.class_type = "Chemist"
                self.abilities.append("Mix Potion")
                self.skills["Intelligence"] += 5
            elif class_to_upgrade_to == "9" and self.class_type == "Spiritualist":
                self.class_type = "Shaman"
                self.abilities.append("Summon Spirit")
                self.skills["Intelligence"] += 5
            elif class_to_upgrade_to == "10" and self.class_type == "Martial Artist":
                self.class_type = "Kung Fu Master"
                self.abilities.append("Martial Arts")
                self.skills["Agility"] += 5
            else:
                print("You cannot upgrade to that class.")
        else:
            print("You are not high enough level to upgrade your class.")

    def spend_skill_points(self):
        print("You have", self.skill_points, "skill points to spend.")
        print("You can spend them on:")
        print("1. Strength")
        print("2. Agility")
        print("3. Intelligence")
        print("4. Vitality")

        skill_to_spend_on = input("Which skill would you like to spend your points on? ")

        if skill_to_spend_on == "1":
            self.skills["Strength"] += 1
            self.skill_points -= 1
        elif skill_to_spend_on == "2":
            self.skills["Agility"] += 1
            self.skill_points -= 1
        elif skill_to_spend_on == "3":
            self.skills["Intelligence"] += 1
            self.skill_points -= 1
        elif skill_to_spend_on == "4":
            self.skills["Vitality"] += 1
            self.skill_points -= 1
        else:
            print("You cannot spend points on that skill.")

    def fight_monster(self, monster, number):
        health = 0
        if monster == "Goblin":
            health = 20 * number
        elif monster == "Troll":
            health = 50 * number
        elif monster == "Sea Serpent":
            health = 100 * number
        elif monster == "Giant Spider":
            health = 30 * number

        while health > 0:
            print("The", monster, "has", health, "health.")
            action = input("What would you like to do? (1. Attack, 2. Run) ")

            if action == "1":
                roll = random.randint(1, 20)
                if roll <= 5:
                    print("You missed the", monster)
                    print("The", monster, "laughs at you and says 'You're no match for me!'")
                elif roll <= 10:
                    print("You hit the", monster, "for 5 damage.")
                    health -= 5
                    print("The", monster, "grunts in pain and says 'Ow, that hurts!'")
                elif roll <= 15:
                    print("You hit the", monster, "for 10 damage.")
                    health -= 10
                    print("The", monster, "yells out in pain and says 'Ahh, my body!'")
                elif roll <= 18:
                    print("You hit the", monster, "for 15 damage.")
                    health -= 15
                    print("The", monster, "cries out in agony and says 'No, it can't be!'")
                elif roll == 19:
                    print("You hit the", monster, "for 20 damage.")
                    health -= 20
                    print("The", monster, "screams in terror and says 'I'm going to die!'")
                elif roll == 20:
                    print("You hit the", monster, "for 25 damage.")
                    health -= 25
                    print("The", monster, "lets out a blood-curdling scream and says 'AHHHHHH!'")
            elif action == "2":
                print("You ran away from the", monster)
                break
            else:
                print("Invalid action.")

        if health <= 0:
            print("You killed the", monster)
            if monster == "Goblin":
                self.experience += 20 * number
            elif monster == "Troll":
                self.experience += 50 * number
            elif monster == "Sea Serpent":
                self.experience += 100 * number
            elif monster == "Giant Spider":
                self.experience += 30 * number
            if self.experience >= 1000:
                self.level_up()

class Town:
    def __init__(self):
        self.current_location = "Willowdale"
        self.npcs = [
            {"name": "Blacksmith", "location": "Willowdale", "quest": "Mine for iron ore"},
            {"name": "Merchant", "location": "Willowdale", "quest": "Buy goods from me"},
            {"name": "Civilian", "location": "Willowdale", "quest": "Find my lost cat"},
            {"name": "King", "location": "Willowdale", "quest": "Kill the demon king"},
            {"name": "Sailor", "location": "Willowdale", "quest": "Sail to the nearby island"},
            {"name": "Kid", "location": "Willowdale", "quest": "Play with me"},
            {"name": "Guard", "location": "Willowdale", "quest": "Protect the town"},
            {"name": "Healer", "location": "Willowdale", "quest": "Heal the wounded"},
            {"name": "Innkeeper", "location": "Willowdale", "quest": "Stay at my inn"},
            {"name": "Farmer", "location": "Willowdale", "quest": "Help me with my farm"},
            {"name": "Enchanter", "location": "Willowdale", "quest": "Enchant your gear"},
            {"name": "Food Vendor", "location": "Willowdale", "quest": "Buy food from me"},
            {"name": "Potion Vendor", "location": "Willowdale", "quest": "Buy potions from me"}
        ]

    def talk_to_npcs(self, player):
        print("You can talk to the following NPCs:")
        for npc in self.npcs:
            if npc["location"] == self.current_location:
                print(npc["name"])

        npc_to_talk_to = input("Which NPC would you like to talk to? ")

        for npc in self.npcs:
            if npc["name"] == npc_to_talk_to and npc["location"] == self.current_location:
                print("You talked to", npc["name"])
                if npc["name"] == "Blacksmith":
                    print("The blacksmith says, 'Ah, you must be here for a quest. I need someone to mine for iron ore.'")
                elif npc["name"] == "Merchant":
                    print("The merchant says, 'Welcome to my shop! I have a quest for you. I need someone to buy goods from me.'")
                elif npc["name"] == "Civilian":
                    print("The civilian says, 'Oh, thank goodness you're here! I need someone to find my lost cat.'")
                elif npc["name"] == "King":
                    print("The king says, 'Ah, brave adventurer, I have a quest for you. I need someone to kill the demon king.'")
                elif npc["name"] == "Sailor":
                    print("The sailor says, 'Ah, you must be here for a quest. I need someone to sail to the nearby island.'")
                elif npc["name"] == "Kid":
                    print("The kid says, 'Yay! You're here to play with me!'")
                elif npc["name"] == "Guard":
                    print("The guard says, 'Ah, you must be here for a quest. I need someone to protect the town.'")
                elif npc["name"] == "Healer":
                    print("The healer says, 'Welcome to my clinic! I have a quest for you. I need someone to heal the wounded.'")
                elif npc["name"] == "Innkeeper":
                    print("The innkeeper says, 'Welcome to my inn! I have a quest for you. I need someone to stay at my inn.'")
                elif npc["name"] == "Farmer":
                    print("The farmer says, 'Ah, you must be here for a quest. I need someone to help me with my farm.'")
                elif npc["name"] == "Enchanter":
                    print("The enchanter says, 'Welcome to my shop! I have a quest for you. I need someone to enchant their gear.'")
                elif npc["name"] == "Food Vendor":
                    print("The food vendor says, 'Welcome to my shop! I have a quest for you. I need someone to buy food from me.'")
                elif npc["name"] == "Potion Vendor":
                    print("The potion vendor says, 'Welcome to my shop! I have a quest for you. I need someone to buy potions from me.'")

                print("Do you want to accept the quest? (1. Yes, 2. No)")
                accept_quest = input()
                if accept_quest == "1":
                    if npc["quest"] == "Mine for iron ore":
                        if player.level >= 5:
                            print("You have mined for iron ore and received 100 gold.")
                            player.inventory.append("Iron Ore")
                            player.experience += 100
                            if player.experience >= 1000:
                                player.level_up()
                        else:
                            print("You are not high enough level to mine for iron ore.")
                    elif npc["quest"] == "Buy goods from me":
                        if player.level >= 3:
                            print("You have bought goods from the merchant and received 50 gold.")
                            player.inventory.append("Goods")
                            player.experience += 50
                            if player.experience >= 1000:
                                player.level_up()
                        else:
                            print("You are not high enough level to buy goods from the merchant.")
                    elif npc["quest"] == "Find my lost cat":
                        if player.level >= 2:
                            print("You have found the lost cat and received 20 gold.")
                            player.inventory.append("Cat")
                            player.experience += 20
                            if player.experience >= 1000:
                                player.level_up()
                        else:
                            print("You are not high enough level to find the lost cat.")
                    elif npc["quest"] == "Kill the demon king":
                        if player.level >= 20:
                            print("You have killed the demon king and received 1000 gold.")
                            player.inventory.append("Demon King's Sword")
                            player.experience += 1000
                            if player.experience >= 1000:
                                player.level_up()
                        else:
                            print("You are not high enough level to kill the demon king.")
                    elif npc["quest"] == "Sail to the nearby island":
                        if player.level >= 6:
                            print("You have sailed to the nearby island and received 150 gold.")
                            player.inventory.append("Island Map")
                            player.experience += 150
                            if player.experience >= 1000:
                                player.level_up()
                        else:
                            print("You are not high enough level to sail to the nearby island.")
                    elif npc["quest"] == "Play with me":
                        if player.level >= 1:
                            print("You have played with the kid and received 10 gold.")
                            player.inventory.append("Toy")
                            player.experience += 10
                            if player.experience >= 1000:
                                player.level_up()
                        else:
                            print("You are not high enough level to play with the kid.")
                    elif npc["quest"] == "Protect the town":
                        if player.level >= 8:
                            print("You have protected the town and received 200 gold.")
                            player.inventory.append("Town Shield")
                            player.experience += 200
                            if player.experience >= 1000:
                                player.level_up()
                        else:
                            print("You are not high enough level to protect the town.")
                    elif npc["quest"] == "Heal the wounded":
                        if player.level >= 4:
                            print("You have healed the wounded and received 30 gold.")
                            player.inventory.append("Healing Potion")
                            player.experience += 30
                            if player.experience >= 1000:
                                player.level_up()
                        else:
                            print("You are not high enough level to heal the wounded.")
                    elif npc["quest"] == "Stay at my inn":
                        if player.level >= 1:
                            print("You have stayed at the inn and received 5 gold.")
                            player.inventory.append("Inn Key")
                            player.experience += 5
                            if player.experience >= 1000:
                                player.level_up()
                        else:
                            print("You are not high enough level to stay at the inn.")
                    elif npc["quest"] == "Help me with my farm":
                        if player.level >= 7:
                            print("You have helped the farmer and received 120 gold.")
                            player.inventory.append("Farm Tools")
                            player.experience += 120
                            if player.experience >= 1000:
                                player.level_up()
                        else:
                            print("You are not high enough level to help the farmer.")
                    elif npc["quest"] == "Enchant your gear":
                        if player.level >= 5:
                            print("You have enchanted your gear and received 100 gold.")
                            player.inventory.append("Enchanted Gear")
                            player.experience += 100
                            if player.experience >= 1000:
                                player.level_up()
                        else:
                            print("You are not high enough level to enchant your gear.")
                    elif npc["quest"] == "Buy food from me":
                        if player.level >= 1:
                            print("You have bought food from the vendor and received 10 gold.")
                            player.inventory.append("Food")
                            player.experience += 10
                            if player.experience >= 1000:
                                player.level_up()
                        else:
                            print("You are not high enough level to buy food from the vendor.")
                    elif npc["quest"] == "Buy potions from me":
                        if player.level >= 1:
                            print("You have bought potions from the vendor and received 10 gold.")
                            player.inventory.append("Potions")
                            player.experience += 10
                            if player.experience >= 1000:
                                player.level_up()
                        else:
                            print("You are not high enough level to buy potions from the vendor.")
                else:
                    print("You declined the quest.")
                return

        print("You cannot talk to that NPC here.")

    def go_to_different_locations(self, player):
        print("You can go to the following locations:")
        print("1. Forest")
        print("2. Mountain")
        print("3. Island")
        print("4. Cave")
        print("5. Town")
        print("6. Demon's Land")
        print("7. Dark Forest")
        print("8. Snowy Mountain")
        print("9. Desert")
        print("10. Volcano")

        location_to_go_to = input("Where would you like to go? ")

        if location_to_go_to == "1":
            self.current_location = "Forest"
            if random.randint(1, 10) <= 5:
                print("You have been ambushed by a group of goblins!")
                player.fight_monster("Goblin", 3)
        elif location_to_go_to == "2":
            self.current_location = "Mountain"
            if random.randint(1, 10) <= 5:
                print("You have been ambushed by a group of trolls!")
                player.fight_monster("Troll", 2)
        elif location_to_go_to == "3":
            self.current_location = "Island"
            if random.randint(1, 10) <= 5:
                print("You have been ambushed by a group of sea serpents!")
                player.fight_monster("Sea Serpent", 2)
        elif location_to_go_to == "4":
            self.current_location = "Cave"
            if random.randint(1, 10) <= 5:
                print("You have been ambushed by a group of giant spiders!")
                player.fight_monster("Giant Spider", 3)
        elif location_to_go_to == "5":
            self.current_location = "Willowdale"
        elif location_to_go_to == "6":
            self.current_location = "Demon's Land"
            if player.level >= 20:
                print("You have entered the demon king's castle.")
                print("The demon king says, 'Ah, you must be the brave adventurer who has come to kill me.'")
                print("Do you want to fight the demon king? (1. Yes, 2. No)")
                fight_demon_king = input()
                if fight_demon_king == "1":
                    player.fight_monster("Demon King", 1)
                else:
                    print("You declined the fight.")
            else:
                print("You are not high enough level to enter the demon king's castle.")
        elif location_to_go_to == "7":
            self.current_location = "Dark Forest"
            if random.randint(1, 10) <= 5:
                print("You have been ambushed by a group of dark elves!")
                player.fight_monster("Dark Elf", 3)
        elif location_to_go_to == "8":
            self.current_location = "Snowy Mountain"
            if random.randint(1, 10) <= 5:
                print("You have been ambushed by a group of yetis!")
                player.fight_monster("Yeti", 2)
        elif location_to_go_to == "9":
            self.current_location = "Desert"
            if random.randint(1, 10) <= 5:
                print("You have been ambushed by a group of sand worms!")
                player.fight_monster("Sand Worm", 3)
        elif location_to_go_to == "10":
            self.current_location = "Volcano"
            if random.randint(1, 10) <= 5:
                print("You have been ambushed by a group of lava giants!")
                player.fight_monster("Lava Giant", 2)
        else:
            print("You cannot go to that location.")

def save_game(player, filename):
    data = {
        "name": player.name,
        "race": player.race,
        "class_type": player.class_type,
        "level": player.level,
        "experience": player.experience,
        "health": player.health,
        "hunger": player.hunger,
        "tiredness": player.tiredness,
        "inventory": player.inventory,
        "abilities": player.abilities,
        "skill_points": player.skill_points,
        "skills": player.skills
    }
    with open(filename, "w") as file:
        json.dump(data, file)

def load_game(filename):
    with open(filename, "r") as file:
        data = json.load(file)
    player = Player()
    player.name = data["name"]
    player.race = data["race"]
    player.class_type = data["class_type"]
    player.level = data["level"]
    player.experience = data["experience"]
    player.health = data["health"]
    player.hunger = data["hunger"]
    player.tiredness = data["tiredness"]
    player.inventory = data["inventory"]
    player.abilities = data["abilities"]
    player.skill_points = data["skill_points"]
    player.skills = data["skills"]
    return player

def main():
    print("Welcome to the land of Eldoria, a mystical realm of wonder and danger.")
    print("You are a brave adventurer seeking fortune and glory in these untamed lands.")
    print("Your journey begins in the small town of Willowdale, where rumors of a demon king's return have drawn you and many other adventurers.")

    print("Do you want to start a new game or load a saved game? (1. New Game, 2. Load Game)")
    choice = input()
    if choice == "1":
        player = Player()
    elif choice == "2":
        print("Enter the filename of your saved game:")
        filename = input()
        player = load_game(filename)
    else:
        print("Invalid choice. Please try again.")
        return

    town = Town()

    while True:
        print("\nYou are currently in:", town.current_location)
        print("You can:")
        print("1. Talk to NPCs")
        print("2. Access inventory")
        print("3. Use abilities")
        print("4. Go to different locations")
        print("5. Rest")
        print("6. Upgrade class")
        print("7. Spend skill points")
        print("8. Save game")

        action = input("What would you like to do? ")

        if action == "1":
            town.talk_to_npcs(player)
        elif action == "2":
            player.access_inventory()
        elif action == "3":
            player.use_abilities()
        elif action == "4":
            town.go_to_different_locations(player)
        elif action == "5":
            player.rest()
        elif action == "6":
            player.upgrade_class()
        elif action == "7":
            player.spend_skill_points()
        elif action == "8":
            print("Enter the filename to save your game:")
            filename = input()
            save_game(player, filename)
        else:
            print("Invalid action. Please try again.")

        if player.is_dead():
            print("You have died. Game over.")
            break

        if player.level >= 20 and "Demon King's Sword" in player.inventory:
            print("Congratulations, you have defeated the demon king and saved the land of Eldoria!")
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    main()