Title: Trice Dungeon Adventure Game
Author: Beatrice Akinpelu
Date: November 20, 2024

Purpose of the Code
This code is a text-based adventure game designed to offer players an immersive experience in a fictional fantasy world. Players navigate through different chapters, make strategic choices, and interact with challenges such as combat, exploration, and skill progression. The game combines role-playing (RPG), resource management, and decision-making elements to create an engaging journey.

The game was created to demonstrate creativity in game development, practice programming skills and entertain users with a fun and dynamic experience.

How the Code Works
1. Player Setup and Initialization
The game begins by prompting the player to enter their character's name.
A Character class manages all player-specific details:
Attributes:
health (default 100)
inventory (an empty list to hold items)
skills (tracks strength and agility)
skill_tree (unlockable abilities like "magic" or "stealth")
Methods:
Add, remove, and check items in inventory.
Regain health by resting.
Train skills to increase strength and agility.
Unlock skills from the skill_tree.

2. Game Structure and Chapters
The game is divided into five chapters, each representing a stage in the player’s journey:

Chapter 1: Players gather supplies and prepare for the quest.
Chapter 2: They enter the Forest of Shadows, facing traps and bandits.
Chapter 3: They cross a dangerous canyon, dealing with enemies and environmental challenges.
Chapter 4: They infiltrate a fortress and confront its guards.
Chapter 5: The final showdown with the warlord to reclaim an artifact.
Each chapter introduces new story elements, randomized events, and challenges that test the player’s decision-making and resource-management skills.

3. Gameplay Actions
During gameplay, players can choose from the following options:

Check Inventory: View the items collected.
Use an Item: Use items like health potions to regain health.
Proceed to the Next Chapter: Advance the story and face new challenges.
Rest: Regain some health.
Search for Supplies: Find useful items like weapons or potions.
Train Skills: Improve strength and agility, making future battles easier.
Unlock Skills: Access new abilities (e.g., stealth or advanced combat) from the skill tree.
Quit Game: Exit the adventure.

4. Combat and Randomized Events
Combat: Players face enemies like bandits, goblins, or fortress guards. They decide whether to fight or retreat, influencing the story's outcome.
Randomized Events: Surprise elements, such as ambushes, falling rocks, or storms, add unpredictability to the gameplay. These events challenge the player’s ability to adapt.
5. Winning or Losing
The game progresses through all chapters unless the player fails a critical decision (e.g., falling into a trap).
The final victory involves defeating the warlord and reclaiming the artifact, restoring peace to the kingdom.
If the player’s health reaches zero or they fail critical objectives, the game ends with a loss.
Why the Code Was Made
Skill Development: The game demonstrates:
Object-oriented programming concepts like classes, methods, and attributes.
We are handling user input and controlling game flow with loops and conditionals.
Randomization for dynamic gameplay.
Creative Expression: The story and game mechanics allow for creativity in designing a fantasy world, interactive dialogue, and challenges.
Problem-Solving Practice: Writing a complex, structured game involves breaking problems into smaller functions and debugging issues.
Engagement: The game was built as an enjoyable project to engage players in a simple yet compelling format, showcasing the versatility of Python for interactive storytelling.
Key Features
Dynamic Storytelling: Each chapter has unique challenges and story elements.
Skill Tree: Players can customize their character’s abilities, adding depth to the gameplay.
Randomized Events: Keeps the game fresh and unpredictable.
Inventory Management: Encourages players to strategize how they use resources.
Replayability: Decisions influence outcomes, encouraging players to replay and explore different choices.
