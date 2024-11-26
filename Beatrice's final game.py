"""
Author: Beatrice Akinpelu
Date: 11/20/2024

Game description:

This is a text-based adventure game where the player embarks on a quest, navigating through different chapters filled with challenges and choices. Along the way, players can gather items, fight enemies, and make strategic decisions.

Options in the menu:
1. Check your inventory
2. Use an item from inventory
3. Proceed to the next chapter
4. Rest to regain health
5. Search for more supplies
6. Train to increase skills
7. Unlock a skill in the skill tree
8. Quit game

Each chapter presents unique scenarios and challenges. The player's choices determine their progress and success in the game.
"""

import random

# Character class to manage player details and inventory
class Character:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.skills = {"strength": 10, "agility": 10}
        self.skill_tree = {"magic": False, "stealth": False, "advanced combat": False}

    def add_to_inventory(self, item):
        self.inventory.append(item)
        print(f"{item} has been added to your inventory.")

    def remove_from_inventory(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            print(f"{item} has been removed from your inventory.")
        else:
            print(f"{item} not found in inventory.")

    def check_inventory(self):
        print(f"Inventory: {self.inventory}")

    def regain_health(self):
        self.health = min(100, self.health + 20)
        print(f"Your health is now {self.health}.")

    def train_skills(self):
        self.skills["strength"] += 1
        self.skills["agility"] += 1
        print(f"Your skills have improved: {self.skills}")

    def unlock_skill(self):
        print("Skill Tree: Magic, Stealth, Advanced Combat")
        print("Choose a skill to unlock:")
        skill_choice = input("Enter the skill name: ").lower()
        if skill_choice in self.skill_tree and not self.skill_tree[skill_choice]:
            self.skill_tree[skill_choice] = True
            print(f"You have unlocked the {skill_choice} skill!")
        elif skill_choice in self.skill_tree and self.skill_tree[skill_choice]:
            print(f"You have already unlocked {skill_choice}.")
        else:
            print("Invalid skill. Please try again.")

# Functions for randomized events
def randomized_events():
    events = [
        "A sudden ambush by a wild beast!",
        "Falling rocks block your path.",
        "A fierce storm makes visibility difficult.",
    ]
    print(f"Random Event: {random.choice(events)}")
    print("You must use your skills and wits to survive.")

# Fight enemies
def fight_bandits():
    bandits = ["Bandit1", "Bandit2", "Bandit3"]
    print("You encounter a band of bandits!")
    for bandit in bandits:
        if input(f"Do you want to fight {bandit}? (y/n): ").lower() == "y":
            print(f"You defeated {bandit}!")
        else:
            print(f"{bandit} escaped!")

def fight_enemies():
    enemies = ["Goblin", "Troll", "Dark Mage"]
    for enemy in enemies:
        if input(f"Do you want to fight {enemy}? (y/n): ").lower() == "y":
            print(f"You defeated the {enemy}!")
        else:
            print(f"{enemy} escaped!")

def navigate_forest():
    traps = ["spike trap", "hidden pit", "net trap"]
    print("The forest is filled with traps. Choose wisely!")
    choice = input("Do you want to go left, right, or straight? ")
    if choice.lower() in ["left", "right"]:
        print(f"You avoid a {random.choice(traps)}!")
    else:
        print("You fell into a trap! Game over.")

def fight_through_fortress():
    levels = 3
    for level in range(1, levels + 1):
        print(f"Level {level}: Facing enemies...")
        if input(f"Do you want to fight in level {level}? (y/n): ").lower() == "y":
            print("You defeated the enemies on this level!")
        else:
            print("You couldn't pass. Game over.")

def fight_warlord():
    phases = ["Phase 1", "Phase 2", "Phase 3"]
    for phase in phases:
        if input(f"Do you want to fight in {phase}? (y/n): ").lower() == "y":
            print(f"You survived {phase}!")
        else:
            print("The warlord defeated you. Game over.")
            return
    print("Congratulations! You have reclaimed the artifact and saved the kingdom!")
    print("The kingdom celebrates your heroic victory, and peace is restored.")
    print("Game Over - Thank you for playing!")

# Chapter functions
def chapter_1(player):
    print("Chapter 1: Preparing for the Quest")
    print('A local whispers: "Beware of what lies ahead. Take what you need, but tread carefully."')
    player.add_to_inventory("Sword")
    player.add_to_inventory("Shield")

def chapter_2(player):
    print("Chapter 2: The Forest of Shadows")
    print('A voice echoes: "You shouldn’t be here."')
    randomized_events()
    fight_bandits()
    navigate_forest()

def chapter_3(player):
    print("Chapter 3: Crossing the Canyon")
    print("The winds howl through the canyon, carrying the distant cries of unseen creatures.")
    randomized_events()
    fight_enemies()

def chapter_4(player):
    print("Chapter 4: Inside the Fortress")
    print('A guard sneers: "You’ll regret stepping into the warlord’s domain."')
    randomized_events()
    fight_through_fortress()

def chapter_5(player):
    print("Chapter 5: The Final Showdown")
    print('The warlord laughs: "Do you think you’re strong enough to take me down? Let’s see!"')
    fight_warlord()

# Main game function
def game():
    print("Welcome to the Dungeon Adventure Game!")
    name = input("Enter your character's name: ")
    player = Character(name)

    actions = [
        "Check your inventory",
        "Use an item from inventory",
        "Proceed to the next chapter",
        "Rest to regain health",
        "Search for more supplies",
        "Train to increase skills",
        "Unlock a skill in the skill tree",
        "Quit game",
    ]
    chapters = [chapter_1, chapter_2, chapter_3, chapter_4, chapter_5]
    current_chapter = 0
    game_over = False

    while not game_over:
        if current_chapter < len(chapters):
            chapters[current_chapter](player)
            current_chapter += 1
        else:
            print("You have completed all chapters. Congratulations!")
            break

        print("\nChoose an action:")
        for i, action in enumerate(actions):
            print(f"{i + 1}. {action}")

        choice = input("Enter the number of your action: ")

        if choice == "1":
            player.check_inventory()
        elif choice == "2":
            item_to_use = input("Enter an item to use from your inventory: ")
            if item_to_use in player.inventory:
                player.remove_from_inventory(item_to_use)
                print(f"You used the {item_to_use}!")
                if item_to_use == "Health Potion":
                    player.health = min(100, player.health + 20)
                    print("Your health increased by 20 points!")
        elif choice == "3":
            continue
        elif choice == "4":
            player.regain_health()
        elif choice == "5":
            print("You found a Health Potion!")
            player.add_to_inventory("Health Potion")
        elif choice == "6":
            player.train_skills()
        elif choice == "7":
            player.unlock_skill()
        elif choice == "8":
            game_over = True
            print("Thanks for playing the Dungeon Adventure Game!")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    game()
