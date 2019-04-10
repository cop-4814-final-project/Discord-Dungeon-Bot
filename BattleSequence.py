import random
import time
import json

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
        print("\nMy name is " + self.name + "!")
        print(self.name + " is level " + str(self.level) + "!")
        print(self.name + " is of class: " + str(self.battleclass) + "!")
        print(self.stats)

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
characterName = input("\nEnter character name:\n")


tempLevel = int(input("\nEnter character level:\n"))
if tempLevel != 1:
    boolLevelFlag = False
else:
    characterLevel = tempLevel
    boolLevelFlag = True

# Validate whether user has access to override character default level
while not boolLevelFlag:
    print("Input Alert: You are trying to create a character level higher than 1.")
    passwordToken = input("\nEnter your admin password:\n")

    if passwordToken == "admin":
        print("Access Granted!")
        characterLevel = tempLevel
        boolLevelFlag = True

    else:
        print("Access Denied!")
        tempLevel = 1
        characterLevel = tempLevel
        boolLevelFlag = True


print("\nValid battle classes:"
      "\nWarrior: Specializes in defense."
      "\nRanger: Specializes in speed."
      "\nCastor: Specializes in attack.")

tempBattleClass = input("\nEnter your battle class:\n")

# Validate user input for battle class
while not (tempBattleClass.lower() == "warrior" or tempBattleClass.lower() == "ranger"
           or tempBattleClass.lower() == "castor"):
    print("You must select a valid battle class.")
    tempBattleClass = input("\nEnter your battle class:\n")

characterClass = tempBattleClass.lower()


# Function to create one of 3 random enemies using RNG
def randomEnemy():
    rng = random.randint(1, 3)
    if rng == 1:
        characterName = "Goblin"
        characterLevel = char1.level
        characterClass = "warrior"

    elif rng == 2:
        characterName = "Skeleton"
        characterLevel = char1.level
        characterClass = "ranger"

    else:
        characterName = "Witch"
        characterLevel = char1.level
        characterClass = "castor"

    return character(characterName, characterLevel, characterClass)

# ------------------ #
# UNDER CONSTRUCTION #
# ------------------ #

# Begin user battle sequence
def battleSequence(entity1, entity2):
    print("\n" + entity2.name + " appears and challenges " + entity1.name + " to battle!")
    entity2.printDetails()

    while entity1.health > 0 and entity2.health > 0:
        if entity1.health > 100:
            entity1.health = 100

        if entity2.health > 100:
            entity2.health = 100

        print("\n" + entity1.name + "'s Health: " + str(entity1.health))
        print(entity2.name + "'s Health: " + str(entity2.health))

        print("\nNext move:\n1. Attack\n2. Defend\n3. Flee\n")
        choice = int(input("\nEnter the number of your choice:\n"))

        # Validate user choice
        while not (choice == 1 or choice == 2 or choice == 3):
            print("\nPlease enter a valid choice!\n")
            choice = int(input("\nEnter the number of your choice:\n"))

        # Determine enemy turn
        rng = random.randint(1, 2)

        # Situation 1: Entity1 -> ATTACK and Entity2 -> ATTACK
        if choice == 1 and rng == 1:

            # Situation 1a: Entity1 attacks first
            if entity1.speed > entity2.speed:
                print(entity1.name + " attacks first with Speed: " + str(entity1.speed) + "!")
                entity2DmgTaken = entity1.attack
                critRoll = random.randint(1, 100)

                if critRoll <= entity1.critical:
                    print("It's super effective!")
                    entity2DmgTaken += (entity1.attack / 2)

                print(entity1.name + " strikes " + entity2.name + " for " + str(entity2DmgTaken) + " points of damage!")
                entity2.health -= entity2DmgTaken
                print(entity2.name + "'s Health: " + str(entity2.health) + "\n")

                # Entity2 attacks second
                print(entity2.name + " attacks second with Speed: " + str(entity2.speed) + "!")
                entity1DmgTaken = entity2.attack
                critRoll = random.randint(1, 100)

                if critRoll <= entity2.critical:
                    print("It's super effective!")
                    entity1DmgTaken += (entity2.attack / 2)

                print(entity2.name + " strikes " + entity1.name + " for " + str(entity1DmgTaken) + " points of damage!")
                entity1.health -= entity1DmgTaken
                print(entity1.name + "'s Health: " + str(entity1.health) + "\n")

            # Situation 1b: Entity2 attacks first
            else:
                print(entity2.name + " attacks first with Speed: " + str(entity2.speed) + "!")
                entity1DmgTaken = entity2.attack
                critRoll = random.randint(1, 100)

                if critRoll <= entity2.critical:
                    print("It's super effective!")
                    entity1DmgTaken += (entity2.attack / 2)

                print(entity2.name + " strikes " + entity1.name + " for " + str(entity1DmgTaken) + " points of damage!")
                entity1.health -= entity1DmgTaken
                print(entity1.name + "'s Health: " + str(entity1.health) + "\n")

                # Entity1 attacks second
                print(entity1.name + " attacks second with Speed: " + str(entity1.speed) + "!")
                entity2DmgTaken = entity1.attack
                critRoll = random.randint(1, 100)

                if critRoll <= entity1.critical:
                    print("It's super effective!")
                    entity2DmgTaken += (entity1.attack / 2)

                print(entity1.name + " strikes " + entity2.name + " for " + str(entity2DmgTaken) + " points of damage!")
                entity2.health -= entity2DmgTaken
                print(entity2.name + "'s Health: " + str(entity2.health) + "\n")

        # Situation 2: Entity1 -> ATTACK and Entity2 -> DEFEND
        if choice == 1 and rng == 2:

            # Entity1 damages Entity2 after factoring in Entity2's defense
            print(entity1.name + " attacks " + entity2.name + "!")
            entity2DmgTaken = entity1.attack
            critRoll = random.randint(1, 100)
            if critRoll <= entity1.critical:
                print("It's super effective!")
                entity2DmgTaken += (entity1.attack / 2)

            print(entity2.name + " defends against " + entity1.name + "'s attack!")
            entity2DmgTaken -= entity2.defense
            critRoll = random.randint(1, 100)
            if critRoll <= entity2.critical:
                print("It's super effective!")
                entity2DmgTaken -= (entity2.defense / 2)

            if entity2DmgTaken > 0:
                print(entity1.name + " strikes " + entity2.name + " for " + str(entity2DmgTaken) + " points of damage!")
                entity2.health -= entity2DmgTaken

            elif entity2DmgTaken < 0:
                print(entity2.name + " blocks all damage from " + entity1.name + "!")
                print("+5 Health to " + entity2.name)
                entity2.health += 5

            else:
                print(entity2.name + " blocks all damage from " + entity1.name + "!")

        # Situation 3: Entity1 -> DEFEND and Entity2 -> ATTACK
        if choice == 2 and rng == 1:

            # Entity2 damages Entity1 after factoring in Entity1's defense
            print(entity2.name + " attacks " + entity1.name + "!")
            entity1DmgTaken = entity2.attack
            critRoll = random.randint(1, 100)
            if critRoll <= entity2.critical:
                print("It's super effective!")
                entity1DmgTaken += (entity2.attack / 2)

            print(entity1.name + " defends against " + entity2.name + "'s attack!")
            entity1DmgTaken -= entity1.defense
            critRoll = random.randint(1, 100)
            if critRoll <= entity1.critical:
                print("It's super effective!")
                entity1DmgTaken -= (entity1.defense / 2)

            if entity1DmgTaken > 0:
                print(entity2.name + " strikes " + entity1.name + " for " + str(entity1DmgTaken) + " points of damage!")
                entity1.health -= entity1DmgTaken

            elif entity1DmgTaken < 0:
                print(entity1.name + " blocks all damage from " + entity2.name + "!")
                print("+5 Health to " + entity1.name)
                entity1.health += 5

            else:
                print(entity1.name + " blocks all damage from " + entity2.name + "!")

            print(entity1.name + "'s Health: " + str(entity1.health))

        # Situation 4: Entity1 -> DEFEND and Entity1 -> DEFEND
        if choice == 2 and rng == 2:

            print(entity1.name + " and " + entity2.name +" both defend against nothing?!\n")
            print("Both adversaries begin to taunt each other from a distance!")
            print("The adrenaline from taunting causes both entities to heal a small amount of health!")
            print("\n+5 Health to both " + entity1.name + " and " + entity2.name + "!")
            entity1.health += 5
            entity2.health += 5

        # Situation 5: Entity1 -> FLEE and Entity2 -> ATTACK
        if choice == 3 and rng == 1:

            print(entity1.name + " attempts to flee from the battle!\n")
            time.sleep(2)

            # Roll to determine outcome of attempted FLEE
            fleeRoll = random.randint(1, 100)
            if fleeRoll <= entity1.speed:
                print("Success!\n")
                print(entity1.name + " flees from the battle to live another day!")
                entity2.health = 0

            else:
                print("Fail!\n")
                print(entity1.name + " tries to flee but trips and lands on their face...")
                print("-5 Health to " + entity1.name + "\n")
                entity1.health -= 5

                # Entity2 attacks Entity1
                print(entity2.name + " attacks " + entity1.name + "!")
                entity1DmgTaken = entity2.attack
                critRoll = random.randint(1, 100)

                if critRoll <= entity2.critical:
                    print("It's super effective!")
                    entity1DmgTaken += (entity2.attack / 2)

                print(entity2.name + " strikes " + entity1.name + " for " + str(entity1DmgTaken) + " points of damage!")
                entity1.health -= entity1DmgTaken
                print(entity1.name + "'s Health: " + str(entity1.health) + "\n")

        # Situation 6: Entity1 -> FLEE and Entity2 -> DEFEND
        if choice == 3 and rng == 2:

            print(entity1.name + " attempts to flee from the battle!\n")
            time.sleep(2)

            # Roll to determine outcome of attempted FLEE
            fleeRoll = random.randint(1, 100)
            if fleeRoll <= entity1.speed:
                print("Success!\n")
                print(entity1.name + " flees from the battle to live another day!")
                entity2.health = 0

            else:
                print("Fail!\n")
                print(entity1.name + " tries to flee but trips and lands on their face...")
                print(entity2.name + " laughs at " + entity1.name + "'s failure!\n")
                print("The shame causes " + entity1.name + " to lose additional health...")
                print("-10 Health to " + entity1.name)
                entity1.health -= 10
                print(entity1.name + "'s Health: " + str(entity1.health) + "\n")


    print("\nEND OF BATTLE!\n")


    if entity1.health > 0:
        print(entity1.name + " wins the battle against " + entity2.name + "!\n")

    else:
        print(entity1.name + " loses the battle against " + entity2.name + "!\n")


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


char1 = character(characterName, characterLevel, characterClass)
char1.printDetails()

time.sleep(2) # Pause between displaying character details

enemy1 = randomEnemy()

time.sleep(2) # Pause before first battle sequence

battleSequence(char1, enemy1)
