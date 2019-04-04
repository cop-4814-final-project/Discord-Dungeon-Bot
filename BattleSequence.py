import random
import time
import json

class character():
    #Parameterized constructor for character class object
    def __init__(self, name, level, battleclass):
        self.name = name
        self.level = level
        self.battleclass = battleclass
        self.stats = [] #Possible dict conversion with format: {"Health" : "" , "Attack" : "" , "Defense" : "" , "Speed" : "" , "Critical" : ""}
        self.health = 100

        # Assigns character object stats variable based on characterClass
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

        # self.stats.insert(0, self.health)
        # self.stats.insert(1, self.attack)
        # self.stats.insert(2, self.defense)
        # self.stats.insert(3, self.speed)
        # self.stats.insert(4, self.critical)

    #Prints the details of the character object
    def printDetails(self):
        print("\nMy name is " + self.name + "!")
        print(self.name + " is level " + str(self.level) + "!")
        print(self.name + " is of class: " + str(self.battleclass) + "!")
        print(self.stats)

    #Series of accessors and mutators for character objects
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

    #Returns a specific stat based on index ({0 - 4} / {Health - Critical})
    def getStats(self, value):
        return self.stats[value:value + 1]


#Begin user adventure with character object creation
characterName = input("\nEnter character name:\n")


tempLevel = int(input("\nEnter character level:\n"))
if tempLevel != 1:
    boolLevelFlag = False
else:
    characterLevel = tempLevel
    boolLevelFlag = True

#Validate whether user has access to override character default level
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

#Validate user input for battle class
while not (tempBattleClass.lower() == "warrior" or tempBattleClass.lower() == "ranger"
           or tempBattleClass.lower() == "castor"):
    print("You must select a valid battle class.")
    tempBattleClass = input("\nEnter your battle class:\n")

characterClass = tempBattleClass.lower()


#Function to create one of 3 random enemies using RNG
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

#------------------#
#UNDER CONSTRUCTION#
#------------------#

#Begin user battle sequence
def battleSequence(entity1, entity2):
    print(entity2.name + " appears and challenges " + entity1.name + " to battle!")
    print("\nNext move:\n1. Attack\n2. Defend\n3. Flee\n")
    choice = int(input("\nEnter the number of your choice:\n"))

    #Validate user choice
    while not (choice == 1 or choice == 2 or choice == 3):
        print("\nplease enter a valid choice!\n")
        choice = int(input("\nEnter the number of your choice:\n"))

    #Determine enemy turn
    rng = random.randint(1, 2)

    if choice == 1 and rng == 1:
        if entity1.speed > entity2.speed:
            print(entity1.name + " moves first from Speed: " + entity1.speed + "!")
            damage = entity1.attack
            critChance = random.randint(1, 100)
            if critChance <= entity1.critical:
                print("It's super effective!")
                damage += (entity1.attack/2) - entity2.defense

            print(damage)

        else:
            print(entity2.name + " moves first from Speed: " + entity2.speed + "!")
            damage = entity2.attack
            critChance = random.randint(1, 100)
            if critChance <= entity2.critical:
                print("It's super effective!")
                damage += (entity2.attack / 2)

            print(damage)
    if choice == 1 and rng == 2:
        if entity1.speed > entity2.speed:
            print(entity1.name + " moves first from Speed: " + entity1.speed + "!")
            damage = entity1.attack
            critChance = random.randint(1, 100)
            if critChance <= entity1.critical:
                print("It's super effective!")
                damage += (entity1.attack/2) - entity2.defense

            print(damage)

        else:
            print(entity2.name + " moves first from Speed: " + entity2.speed + "!")
            damage = entity2.attack
            critChance = random.randint(1, 100)
            if critChance <= entity2.critical:
                print("It's super effective!")
                damage += (entity2.attack / 2)

            print(damage)
    print("END SEQUENCE!")


#Reading from JSON file
# with open("data.txt") as json_file:
#     data = json.load(json_file)
#     for x in data['character']:
#         print("Character Name: " + x["name"])
#         print("Character Level: " + x["level"])
#         print("Character Class: ") + x["battleclass"]
#         print("Character Stats: " + x["stats"] + "\n")

#Saving to JSON file
# data = {}
# data['character'] = []
# data['character'].append({
#     'name': characterName,
#     'level': characterLevel,
#     'battleclass': characterClass,
#     'stats': character.stats
# })
#
# with open("data.txt", "w") as outfile:
#     json.dump(data, outfile)


char1 = character(characterName, characterLevel, characterClass)
char1.printDetails()

time.sleep(2) #Pause between displaying character details

enemy1 = randomEnemy()
enemy1.printDetails()

time.sleep(2) #Pause before first battle sequence

battleSequence(char1, enemy1)