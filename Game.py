import random
import time
import json
import discord

class character():
    # Parameterized constructor for character class object
    def __init__(self, name, level, battleclass):
        self.name = name
        self.level = level
        self.battleclass = battleclass
        self.stats = [] # Possible dict conversion with format: {"Health" : "" , "Attack" : "" , "Defense" : "" , "Speed" : "" , "Critical" : ""}
        self.health = 100

        #  Assigns character object stats variable based on characterClass
        if battleclass == "warrior":
            self.attack = random.randint(1, 20)
            self.defense = random.randint(20, 20)
            self.speed = random.randint(1, 20)
            self.critical = random.randint(1, 20)
            self.stats.insert(0, self.health)
            self.stats.insert(1, self.attack)
            self.stats.insert(2, self.defense)
            self.stats.insert(3, self.speed)
            self.stats.insert(4, self.critical)

        elif battleclass == "ranger":
            self.attack = random.randint(1, 20)
            self.defense = random.randint(1, 20)
            self.speed = random.randint(20, 20)
            self.critical = random.randint(1, 20)
            self.stats.insert(0, self.health)
            self.stats.insert(1, self.attack)
            self.stats.insert(2, self.defense)
            self.stats.insert(3, self.speed)
            self.stats.insert(4, self.critical)

        elif battleclass == "castor":
            self.attack = random.randint(20, 20)
            self.defense = random.randint(1, 20)
            self.speed = random.randint(1, 20)
            self.critical = random.randint(1, 20)
            self.stats.insert(0, self.health)
            self.stats.insert(1, self.attack)
            self.stats.insert(2, self.defense)
            self.stats.insert(3, self.speed)
            self.stats.insert(4, self.critical)

    # Prints the details of the character object
    def printDetails(self):
        embed = discord.Embed(title="Character Stats:", color=0x00ff00)
        embed.set_thumbnail(url="https://orig00.deviantart.net/f025/f/2017/277/f/2/ffbe___cloud_strife_gif_2_by_zerolympiustrife-dbpjw5t.gif")
        embed.add_field(name="Attack", value=str(self.attack), inline=True)
        embed.add_field(name="Defense", value=str(self.defense), inline=True)
        embed.add_field(name="Speed", value=str(self.speed), inline=True)
        embed.add_field(name="Luck", value=str(self.critical), inline=True)
        embed.add_field(name="Level", value=str(self.level), inline=True)
        return embed

    # Series of accessors and mutators for character objects
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setLevel(self, level):
        self.level = level

    def getLevel(self):
        return self.level

    def setBattleclass(self, battleclass):
        self.battleclass = battleclass

    def getBattleclass(self):
        return self.battleclass

    # Returns a specific stat based on index ({0 - 4} / {Health - Critical})
    def getStats(self, value):
        return self.stats[value:value + 1]


# Begin user adventure with character object creation
# characterName = input("\nEnter character name:\n")
#
#
# tempLevel = int(input("\nEnter character level:\n"))
# if tempLevel != 1:
#     boolLevelFlag = False
# else:
#     characterLevel = tempLevel
#     boolLevelFlag = True
#
# # Validate whether user has access to override character default level
# while not boolLevelFlag:
#     print("Input Alert: You are trying to create a character level higher than 1.")
#     passwordToken = input("\nEnter your admin password:\n")
#
#     if passwordToken == "admin":
#         print("Access Granted!")
#         characterLevel = tempLevel
#         boolLevelFlag = True
#
#     else:
#         print("Access Denied!")
#         tempLevel = 1
#         characterLevel = tempLevel
#         boolLevelFlag = True
#
#
# print("\nValid battle classes:"
#       "\nWarrior: Specializes in defense."
#       "\nRanger: Specializes in speed."
#       "\nCastor: Specializes in attack.")
#
# tempBattleClass = input("\nEnter your battle class:\n")
#
# # Validate user input for battle class
# while not (tempBattleClass.lower() == "warrior" or tempBattleClass.lower() == "ranger"
#            or tempBattleClass.lower() == "castor"):
#     print("You must select a valid battle class.")
#     tempBattleClass = input("\nEnter your battle class:\n")
#
# characterClass = tempBattleClass.lower()


# Function to create one of 3 random enemies using RNG
def randomEnemy(level):
    rng = random.randint(1, 3)
    if rng == 1:
        characterName = "Goblin"
        characterLevel = level
        characterClass = "warrior"

    elif rng == 2:
        characterName = "Skeleton"
        characterLevel = level
        characterClass = "ranger"

    else:
        characterName = "Witch"
        characterLevel = level
        characterClass = "castor"

    return character(characterName, characterLevel, characterClass)

# ------------------ #
# UNDER CONSTRUCTION #
# ------------------ #

# Begin user battle sequence
# def battleSequence(character, enemy):
#     print("\n" + enemy.name + " appears and challenges " + character.name + " to battle!")
#     enemy.printDetails()
#
#     while character.health > 0 and enemy.health > 0:
#         if character.health > 100:
#             character.health = 100
#
#         if enemy.health > 100:
#             enemy.health = 100
#
#         print("\n" + character.name + "'s Health: " + str(character.health))
#         print(enemy.name + "'s Health: " + str(enemy.health))
#
#         print("\nNext move:\n1. Attack\n2. Defend\n3. Flee\n")
#         choice = int(input("\nEnter the number of your choice:\n"))
#
#         # Validate user choice
#         while not (choice == 1 or choice == 2 or choice == 3):
#             print("\nPlease enter a valid choice!\n")
#             choice = int(input("\nEnter the number of your choice:\n"))
#
#         # Determine enemy turn
#         rng = random.randint(1, 2)
#
#         # Situation 1: character -> ATTACK and enemy -> ATTACK
#         if choice == 1 and rng == 1:
#
#             # Situation 1a: character attacks first
#             if character.speed > enemy.speed:
#                 print(character.name + " attacks first with Speed: " + str(character.speed) + "!")
#                 enemyDmgTaken = character.attack
#                 critRoll = random.randint(1, 100)
#
#                 if critRoll <= character.critical:
#                     print("It's super effective!")
#                     enemyDmgTaken += (character.attack / 2)
#
#                 print(character.name + " strikes " + enemy.name + " for " + str(enemyDmgTaken) + " points of damage!")
#                 enemy.health -= enemyDmgTaken
#                 print(enemy.name + "'s Health: " + str(enemy.health) + "\n")
#
#                 # enemy attacks second
#                 print(enemy.name + " attacks second with Speed: " + str(enemy.speed) + "!")
#                 characterDmgTaken = enemy.attack
#                 critRoll = random.randint(1, 100)
#
#                 if critRoll <= enemy.critical:
#                     print("It's super effective!")
#                     characterDmgTaken += (enemy.attack / 2)
#
#                 print(enemy.name + " strikes " + character.name + " for " + str(characterDmgTaken) + " points of damage!")
#                 character.health -= characterDmgTaken
#                 print(character.name + "'s Health: " + str(character.health) + "\n")
#
#             # Situation 1b: enemy attacks first
#             else:
#                 print(enemy.name + " attacks first with Speed: " + str(enemy.speed) + "!")
#                 characterDmgTaken = enemy.attack
#                 critRoll = random.randint(1, 100)
#
#                 if critRoll <= enemy.critical:
#                     print("It's super effective!")
#                     characterDmgTaken += (enemy.attack / 2)
#
#                 print(enemy.name + " strikes " + character.name + " for " + str(characterDmgTaken) + " points of damage!")
#                 character.health -= characterDmgTaken
#                 print(character.name + "'s Health: " + str(character.health) + "\n")
#
#                 # character attacks second
#                 print(character.name + " attacks second with Speed: " + str(character.speed) + "!")
#                 enemyDmgTaken = character.attack
#                 critRoll = random.randint(1, 100)
#
#                 if critRoll <= character.critical:
#                     print("It's super effective!")
#                     enemyDmgTaken += (character.attack / 2)
#
#                 print(character.name + " strikes " + enemy.name + " for " + str(enemyDmgTaken) + " points of damage!")
#                 enemy.health -= enemyDmgTaken
#                 print(enemy.name + "'s Health: " + str(enemy.health) + "\n")
#
#         # Situation 2: character -> ATTACK and enemy -> DEFEND
#         if choice == 1 and rng == 2:
#
#             # character damages enemy after factoring in enemy's defense
#             print(character.name + " attacks " + enemy.name + "!")
#             enemyDmgTaken = character.attack
#             critRoll = random.randint(1, 100)
#             if critRoll <= character.critical:
#                 print("It's super effective!")
#                 enemyDmgTaken += (character.attack / 2)
#
#             print(enemy.name + " defends against " + character.name + "'s attack!")
#             enemyDmgTaken -= enemy.defense
#             critRoll = random.randint(1, 100)
#             if critRoll <= enemy.critical:
#                 print("It's super effective!")
#                 enemyDmgTaken -= (enemy.defense / 2)
#
#             if enemyDmgTaken > 0:
#                 print(character.name + " strikes " + enemy.name + " for " + str(enemyDmgTaken) + " points of damage!")
#                 enemy.health -= enemyDmgTaken
#
#             elif enemyDmgTaken < 0:
#                 print(enemy.name + " blocks all damage from " + character.name + "!")
#                 print("+5 Health to " + enemy.name)
#                 enemy.health += 5
#
#             else:
#                 print(enemy.name + " blocks all damage from " + character.name + "!")
#
#         # Situation 3: character -> DEFEND and enemy -> ATTACK
#         if choice == 2 and rng == 1:
#
#             # enemy damages character after factoring in character's defense
#             print(enemy.name + " attacks " + character.name + "!")
#             characterDmgTaken = enemy.attack
#             critRoll = random.randint(1, 100)
#             if critRoll <= enemy.critical:
#                 print("It's super effective!")
#                 characterDmgTaken += (enemy.attack / 2)
#
#             print(character.name + " defends against " + enemy.name + "'s attack!")
#             characterDmgTaken -= character.defense
#             critRoll = random.randint(1, 100)
#             if critRoll <= character.critical:
#                 print("It's super effective!")
#                 characterDmgTaken -= (character.defense / 2)
#
#             if characterDmgTaken > 0:
#                 print(enemy.name + " strikes " + character.name + " for " + str(characterDmgTaken) + " points of damage!")
#                 character.health -= characterDmgTaken
#
#             elif characterDmgTaken < 0:
#                 print(character.name + " blocks all damage from " + enemy.name + "!")
#                 print("+5 Health to " + character.name)
#                 character.health += 5
#
#             else:
#                 print(character.name + " blocks all damage from " + enemy.name + "!")
#
#             print(character.name + "'s Health: " + str(character.health))
#
#         # Situation 4: character -> DEFEND and character -> DEFEND
#         if choice == 2 and rng == 2:
#
#             print(character.name + " and " + enemy.name +" both defend against nothing?!\n")
#             print("Both adversaries begin to taunt each other from a distance!")
#             print("The adrenaline from taunting causes both entities to heal a small amount of health!")
#             print("\n+5 Health to both " + character.name + " and " + enemy.name + "!")
#             character.health += 5
#             enemy.health += 5
#
#         # Situation 5: character -> FLEE and enemy -> ATTACK
#         if choice == 3 and rng == 1:
#
#             print(character.name + " attempts to flee from the battle!\n")
#             time.sleep(2)
#
#             # Roll to determine outcome of attempted FLEE
#             fleeRoll = random.randint(1, 100)
#             if fleeRoll <= character.speed:
#                 print("Success!\n")
#                 print(character.name + " flees from the battle to live another day!")
#                 enemy.health = 0
#
#             else:
#                 print("Fail!\n")
#                 print(character.name + " tries to flee but trips and lands on their face...")
#                 print("-5 Health to " + character.name + "\n")
#                 character.health -= 5
#
#                 # enemy attacks character
#                 print(enemy.name + " attacks " + character.name + "!")
#                 characterDmgTaken = enemy.attack
#                 critRoll = random.randint(1, 100)
#
#                 if critRoll <= enemy.critical:
#                     print("It's super effective!")
#                     characterDmgTaken += (enemy.attack / 2)
#
#                 print(enemy.name + " strikes " + character.name + " for " + str(characterDmgTaken) + " points of damage!")
#                 character.health -= characterDmgTaken
#                 print(character.name + "'s Health: " + str(character.health) + "\n")
#
#         # Situation 6: character -> FLEE and enemy -> DEFEND
#         if choice == 3 and rng == 2:
#
#             print(character.name + " attempts to flee from the battle!\n")
#             time.sleep(2)
#
#             # Roll to determine outcome of attempted FLEE
#             fleeRoll = random.randint(1, 100)
#             if fleeRoll <= character.speed:
#                 print("Success!\n")
#                 print(character.name + " flees from the battle to live another day!")
#                 enemy.health = 0
#
#             else:
#                 print("Fail!\n")
#                 print(character.name + " tries to flee but trips and lands on their face...")
#                 print(enemy.name + " laughs at " + character.name + "'s failure!\n")
#                 print("The shame causes " + character.name + " to lose additional health...")
#                 print("-10 Health to " + character.name)
#                 character.health -= 10
#                 print(character.name + "'s Health: " + str(character.health) + "\n")
#
#
#     print("\nEND OF BATTLE!\n")
#
#
#     if character.health > 0:
#         print(character.name + " wins the battle against " + enemy.name + "!\n")
#
#     else:
#         print(character.name + " loses the battle against " + enemy.name + "!\n")


# Reading from JSON file
#  with open("data.txt") as json_file:
#      data = json.load(json_file)
#      for x in data['character']:
#          print("Character Name: " + x["name"])
#          print("Character Level: " + x["level"])
#          print("Character Class: ") + x["battleclass"]
#          print("Character Stats: " + x["stats"] + "\n")

# Saving to JSON file
#  data = {}
#  data['character'] = []
#  data['character'].append({
#      'name': characterName,
#      'level': characterLevel,
#      'battleclass': characterClass,
#      'stats': character.stats
#  })
#
#  with open("data.txt", "w") as outfile:
#      json.dump(data, outfile)


# char1 = character(characterName, characterLevel, characterClass)
# char1.printDetails()
#
# time.sleep(2) # Pause between displaying character details
#
# enemy1 = randomEnemy()
#
# time.sleep(2) # Pause before first battle sequence
#
# battleSequence(char1, enemy1)

