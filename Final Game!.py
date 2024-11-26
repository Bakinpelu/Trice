"""
Author: Beatrice Akinpelu
Date: 11/20/2024

Game description:
This is a text-based adventure game where the player embarks on a quest,
navigating through different chapters filled with challenges and choices.
Players gather items, fight enemies, and make strategic decisions to progress.
"""

import random

# ==========================
# CLASS DEFINITIONS
# ==========================

class Character:
    # Represents the player character in the game
    def __init__(self, name):
        # Initialize character attributes
        self.name = name  # Player's name
        self.health = 100  # Starting health
        self.inventory = []  # Inventory list
        self.skills = {"strength": 10, "agility": 10}  # Starting skills
        self.skill_tree = {"magic": False, "stealth": False, "advanced combat": False}  # Unlockable skills

    # Add an item to the player's inventory
    def add_to_inventory(self, item):
        self.inventory.append(item)
        print(f"{item} has been added to your inventory.")

    # Remove an item from the player's inventory
    def remove_from_inventory(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            print(f"{item} has been removed from your inventory.")
        else:
            print(f"{item} not found in inventory.")

    # Display the player's inventory
    def check_inventory(self):
        print(f"Inventory: {self.inventory}")

    # Regain health by 20 points (up to a maximum of 100)
    def regain_health(self):
        self.health = min(100, self.health + 20)
        print(f"Your health is now {self.health}.")

    # Improve the player's strength and agility
    def train_skills(self):
        self.skills["strength"] += 1
        self.skills["agility"] += 1
        print(f"Your skills have improved: {self.skills}")

    # Unlock a skill in the skill tree
    def unlock_skill(self):
        print("Skill Tree: Magic, Stealth, Advanced Combat")
        print("Choose a skill to unlock:")
        skill_choice = input("Enter the skill name: ").lower()
        if skill_choice in self.skill_tree and not self.skill_tree[skill_choice]:
            self.skill_tree[skill_choice] = True
            print(f"You have unlocked the {skill_choice} skill!")
        elif skill_choice in self.skill_tree and self.skill_tree[skill_choice]:
            print(f"{skill_choice} is already unlocked.")
        else:
            print("Invalid skill. Please try again.")

# ==========================
# RANDOMIZED EVENTS
# ==========================

# Generate a random event to add variety to the game
def randomized_events():
    events = [
        "A sudden ambush by a wild beast!",
        "Falling rocks block your path.",
        "A fierce storm makes visibility difficult.",
    ]
    print(f"Random Event: {random.choice(events)}")
    print("You must use your skills and wits to survive.")

# ==========================
# ENEMY ENCOUNTERS
# ==========================

# Encounter a group of bandits and decide whether to fight
def fight_bandits():
    bandits = ["Bandit1", "Bandit2", "Bandit3"]
    print("You encounter a band of bandits!")
    for bandit in bandits:
        if input(f"Do you want to fight {bandit}? (y/n): ").lower() == "y":
            print(f"You defeated {bandit}!")
        else:
            print(f"{bandit} escaped!")

# Encounter various enemies and decide whether to fight
def fight_enemies():
    enemies = ["Goblin", "Troll", "Dark Mage"]
    for enemy in enemies:
        if input(f"Do you want to fight the {enemy}? (y/n): ").lower() == "y":
            print(f"You defeated the {enemy}!")
        else:
            print(f"The {enemy} escaped!")

# ==========================
# GAME CHAPTERS
# ==========================

# Chapter 1: Introduce the quest and prepare the player
def chapter_1(player):
    print("Chapter 1: Preparing for the Quest")
    print('A local whispers: "Beware of what lies ahead. Take what you need, but tread carefully."')
    player.add_to_inventory("Sword")  # Add a sword to inventory
    player.add_to_inventory("Shield")  # Add a shield to inventory

# Chapter 2: Navigate through a dangerous forest
def chapter_2(player):
    print("Chapter 2: The Forest of Shadows")
    print('A voice echoes: "You shouldn’t be here."')
    randomized_events()  # Generate a random event
    fight_bandits()  # Encounter bandits in the forest

# Chapter 3: Cross a canyon while facing challenges
def chapter_3(player):
    print("Chapter 3: Crossing the Canyon")
    print("The winds howl through the canyon, carrying the distant cries of unseen creatures.")
    randomized_events()
    fight_enemies()

# Chapter 4: Battle through a fortress filled with enemies
def chapter_4(player):
    print("Chapter 4: Inside the Fortress")
    print('A guard sneers: "You’ll regret stepping into the warlord’s domain."')
    randomized_events()
    fight_enemies()

# Chapter 5: Final boss battle with the warlord
def chapter_5(player):
    print("Chapter 5: The Final Showdown")
    print('The warlord laughs: "Do you think you’re strong enough to take me down? Let’s see!"')
    fight_enemies()  # Multiple phases of battle

# ==========================
# MAIN GAME FUNCTION
# ==========================

def game():
    # Greet the player and create a character
    print("Welcome to the Dungeon Adventure Game!")
    name = input("Enter your character's name: ")
    player = Character(name)  # Create a new Character instance

    # Define the sequence of chapters
    chapters = [chapter_1, chapter_2, chapter_3, chapter_4, chapter_5]
    current_chapter = 0  # Start at Chapter 1
    game_over = False  # Track whether the game is over

    while not game_over:
        if current_chapter < len(chapters):
            # Play the current chapter
            chapters[current_chapter](player)
            current_chapter += 1
        else:
            print("You have completed all chapters. Congratulations!")
            break

        # Allow the player to take actions
        print("\nWhat would you like to do?")
        print("1. Check inventory\n2. Proceed to next chapter\n3. Rest\n4. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            player.check_inventory()  # Display inventory
        elif choice == "2":
            continue  # Proceed to the next chapter
        elif choice == "3":
            player.regain_health()  # Restore health
        elif choice == "4":
            game_over = True  # End the game
            print("Thanks for playing!")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    game()
