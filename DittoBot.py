# Work with Python 3.6
import discord
import Game
import random
import time

TOKEN = 'NTQ1MDAzODM3MTAzMjc2MDMy.D0TWWQ.e-6BetIff7PgXybJMzvOmTwv2rs'

client = discord.Client()

@client.event
async def on_message(message, self=None):
    character = Game.character("Cloud", 1, 'warrior')
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('help'):
        msg = 'Hello {0.author.mention}! Welcome to [GAME NAME], a text based adventure game on Discord.\n' \
              'To begin, send me a private message with the word \'start\''.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('start'):
        battleclass = 'none'

        await client.send_message(message.channel, 'What is your chatacters name?')
        msg = await client.wait_for_message(author=message.author)
        name = msg.content

        while battleclass not in ['warrior', 'castor', 'ranger']:
            await client.send_message(message.channel, 'Do you consider yourself a warrior, castor, or a ranger?')
            msg = await client.wait_for_message(author=message.author)
            battleclass = msg.content

        character = Game.character(name, 1, battleclass)
        embed = character.printDetails()
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('encounter'):
        enemy = Game.randomEnemy(character.getLevel())

        msg = ("\n" + enemy.name + " appears and challenges " + character.name + " to battle!")
        await client.send_message(message.channel, msg)
        embed = enemy.printDetails()
        await client.send_message(message.channel, embed=embed)

        while character.health > 0 and enemy.health > 0 :
            if character.health > 100 :
                character.health = 100

            if enemy.health > 100 :
                enemy.health = 100

            msg = ("\n" + character.name + "'s Health: " + str(character.health))
            await client.send_message(message.channel, msg)
            msg = (enemy.name + "'s Health: " + str(enemy.health))
            await client.send_message(message.channel, msg)

            msg = ("\nNext move:\n1. Attack\n2. Defend\n3. Flee\n")
            await client.send_message(message.channel, msg)
            choice = "0"


            # Validate user choice
            while choice not in ["1", "2", "3"]:
                await client.send_message(message.channel, 'Emter the number of your choice')
                msg = await client.wait_for_message(author=message.author)
                choice = msg.content


            # Determine enemy turn
            rng = random.randint(1, 2)

            # Situation 1: character -> ATTACK and enemy -> ATTACK
            if choice == "1" and rng == 1 :

                # Situation 1a: character attacks first
                if character.speed > enemy.speed :
                    msg = (character.name + " attacks first with Speed: " + str(character.speed) + "!")
                    await client.send_message(message.channel, msg)
                    enemyDmgTaken = character.attack
                    critRoll = random.randint(1, 100)

                    if critRoll <= character.critical :
                        msg = ("It's super effective!")
                        await client.send_message(message.channel, msg)
                        enemyDmgTaken += (character.attack / 2)

                    msg = (character.name + " strikes " + enemy.name + " for " + str(
                        enemyDmgTaken) + " points of damage!")
                    await client.send_message(message.channel, msg)
                    enemy.health -= enemyDmgTaken
                    msg = (enemy.name + "'s Health: " + str(enemy.health) + "\n")
                    await client.send_message(message.channel, msg)

                    # enemy attacks second
                    msg = (enemy.name + " attacks second with Speed: " + str(enemy.speed) + "!")
                    await client.send_message(message.channel, msg)
                    characterDmgTaken = enemy.attack
                    critRoll = random.randint(1, 100)

                    if critRoll <= enemy.critical :
                        msg = ("It's super effective!")
                        await client.send_message(message.channel, msg)
                        characterDmgTaken += (enemy.attack / 2)

                    msg = (enemy.name + " strikes " + character.name + " for " + str(
                        characterDmgTaken) + " points of damage!")
                    await client.send_message(message.channel, msg)
                    character.health -= characterDmgTaken
                    msg = (character.name + "'s Health: " + str(character.health) + "\n")
                    await client.send_message(message.channel, msg)

                # Situation 1b: enemy attacks first
                else :
                    msg = (enemy.name + " attacks first with Speed: " + str(enemy.speed) + "!")
                    await client.send_message(message.channel, msg)
                    characterDmgTaken = enemy.attack
                    critRoll = random.randint(1, 100)

                    if critRoll <= enemy.critical :
                        msg = ("It's super effective!")
                        await client.send_message(message.channel, msg)
                        characterDmgTaken += (enemy.attack / 2)

                    msg = (enemy.name + " strikes " + character.name + " for " + str(
                        characterDmgTaken) + " points of damage!")
                    await client.send_message(message.channel, msg)
                    character.health -= characterDmgTaken
                    msg = (character.name + "'s Health: " + str(character.health) + "\n")
                    await client.send_message(message.channel, msg)

                    # character attacks second
                    msg = (character.name + " attacks second with Speed: " + str(character.speed) + "!")
                    await client.send_message(message.channel, msg)
                    enemyDmgTaken = character.attack
                    critRoll = random.randint(1, 100)

                    if critRoll <= character.critical :
                        msg = ("It's super effective!")
                        await client.send_message(message.channel, msg)
                        enemyDmgTaken += (character.attack / 2)

                    msg = (character.name + " strikes " + enemy.name + " for " + str(
                        enemyDmgTaken) + " points of damage!")
                    await client.send_message(message.channel, msg)
                    enemy.health -= enemyDmgTaken
                    msg = (enemy.name + "'s Health: " + str(enemy.health) + "\n")
                    await client.send_message(message.channel, msg)

            # Situation 2: character -> ATTACK and enemy -> DEFEND
            if choice == "1" and rng == 2 :

                # character damages enemy after factoring in enemy's defense
                msg = (character.name + " attacks " + enemy.name + "!")
                await client.send_message(message.channel, msg)
                enemyDmgTaken = character.attack
                critRoll = random.randint(1, 100)
                if critRoll <= character.critical :
                    msg = ("It's super effective!")
                    await client.send_message(message.channel, msg)
                    enemyDmgTaken += (character.attack / 2)

                msg = (enemy.name + " defends against " + character.name + "'s attack!")
                await client.send_message(message.channel, msg)
                enemyDmgTaken -= enemy.defense
                critRoll = random.randint(1, 100)
                if critRoll <= enemy.critical :
                    msg = ("It's super effective!")
                    await client.send_message(message.channel, msg)
                    enemyDmgTaken -= (enemy.defense / 2)

                if enemyDmgTaken > 0 :
                    msg = (character.name + " strikes " + enemy.name + " for " + str(
                        enemyDmgTaken) + " points of damage!")
                    await client.send_message(message.channel, msg)
                    enemy.health -= enemyDmgTaken

                elif enemyDmgTaken < 0 :
                    msg = (enemy.name + " blocks all damage from " + character.name + "!")
                    await client.send_message(message.channel, msg)
                    msg = ("+5 Health to " + enemy.name)
                    await client.send_message(message.channel, msg)
                    enemy.health += 5

                else :
                    msg = (enemy.name + " blocks all damage from " + character.name + "!")
                    await client.send_message(message.channel, msg)

            # Situation 3: character -> DEFEND and enemy -> ATTACK
            if choice == "2" and rng == 1 :

                # enemy damages character after factoring in character's defense
                msg = (enemy.name + " attacks " + character.name + "!")
                await client.send_message(message.channel, msg)
                characterDmgTaken = enemy.attack
                critRoll = random.randint(1, 100)
                if critRoll <= enemy.critical :
                    msg = ("It's super effective!")
                    await client.send_message(message.channel, msg)
                    characterDmgTaken += (enemy.attack / 2)

                msg = (character.name + " defends against " + enemy.name + "'s attack!")
                await client.send_message(message.channel, msg)
                characterDmgTaken -= character.defense
                critRoll = random.randint(1, 100)
                if critRoll <= character.critical :
                    msg = ("It's super effective!")
                    await client.send_message(message.channel, msg)
                    characterDmgTaken -= (character.defense / 2)

                if characterDmgTaken > 0 :
                    msg = (enemy.name + " strikes " + character.name + " for " + str(
                        characterDmgTaken) + " points of damage!")
                    await client.send_message(message.channel, msg)
                    character.health -= characterDmgTaken

                elif characterDmgTaken < 0 :
                    msg = (character.name + " blocks all damage from " + enemy.name + "!")
                    await client.send_message(message.channel, msg)
                    msg = ("+5 Health to " + character.name)
                    await client.send_message(message.channel, msg)
                    character.health += 5

                else :
                    msg = (character.name + " blocks all damage from " + enemy.name + "!")
                    await client.send_message(message.channel, msg)
                msg = (character.name + "'s Health: " + str(character.health))
                await client.send_message(message.channel, msg)

            # Situation 4: character -> DEFEND and character -> DEFEND
            if choice == "2" and rng == 2 :
                msg = (character.name + " and " + enemy.name + " both defend against nothing?!\n")
                await client.send_message(message.channel, msg)
                msg =("Both adversaries begin to taunt each other from a distance!")
                await client.send_message(message.channel, msg)
                msg =("The adrenaline from taunting causes both entities to heal a small amount of health!")
                await client.send_message(message.channel, msg)
                msg =("\n+5 Health to both " + character.name + " and " + enemy.name + "!")
                await client.send_message(message.channel, msg)
                character.health += 5
                enemy.health += 5

            # Situation 5: character -> FLEE and enemy -> ATTACK
            if choice == "3" and rng == 1 :

                msg =(character.name + " attempts to flee from the battle!\n")
                await client.send_message(message.channel, msg)
                time.sleep(2)

                # Roll to determine outcome of attempted FLEE
                fleeRoll = random.randint(1, 100)
                if fleeRoll <= character.speed :
                    msg =("Success!\n")
                    await client.send_message(message.channel, msg)
                    msg =(character.name + " flees from the battle to live another day!")
                    await client.send_message(message.channel, msg)
                    enemy.health = 0

                else :
                    msg =("Fail!\n")
                    await client.send_message(message.channel, msg)
                    msg =(character.name + " tries to flee but trips and lands on their face...")
                    await client.send_message(message.channel, msg)
                    msg =("-5 Health to " + character.name + "\n")
                    await client.send_message(message.channel, msg)
                    character.health -= 5

                    # enemy attacks character
                    msg =(enemy.name + " attacks " + character.name + "!")
                    await client.send_message(message.channel, msg)
                    characterDmgTaken = enemy.attack
                    critRoll = random.randint(1, 100)

                    if critRoll <= enemy.critical :
                        msg =("It's super effective!")
                        await client.send_message(message.channel, msg)
                        characterDmgTaken += (enemy.attack / 2)

                    msg =(enemy.name + " strikes " + character.name + " for " + str(
                        characterDmgTaken) + " points of damage!")
                    await client.send_message(message.channel, msg)
                    character.health -= characterDmgTaken
                    msg =(character.name + "'s Health: " + str(character.health) + "\n")
                    await client.send_message(message.channel, msg)

            # Situation 6: character -> FLEE and enemy -> DEFEND
            if choice == "3" and rng == 2 :

                msg =(character.name + " attempts to flee from the battle!\n")
                await client.send_message(message.channel, msg)
                time.sleep(2)

                # Roll to determine outcome of attempted FLEE
                fleeRoll = random.randint(1, 100)
                if fleeRoll <= character.speed :
                    msg =("Success!\n")
                    await client.send_message(message.channel, msg)
                    msg =(character.name + " flees from the battle to live another day!")
                    await client.send_message(message.channel, msg)
                    enemy.health = 0

                else :
                    msg =("Fail!\n")
                    await client.send_message(message.channel, msg)
                    msg =(character.name + " tries to flee but trips and lands on their face...")
                    await client.send_message(message.channel, msg)
                    msg =(enemy.name + " laughs at " + character.name + "'s failure!\n")
                    await client.send_message(message.channel, msg)
                    msg =("The shame causes " + character.name + " to lose additional health...")
                    await client.send_message(message.channel, msg)
                    msg =("-10 Health to " + character.name)
                    await client.send_message(message.channel, msg)
                    character.health -= 10
                    msg =(character.name + "'s Health: " + str(character.health) + "\n")
                    await client.send_message(message.channel, msg)

        msg =("\nEND OF BATTLE!\n")
        await client.send_message(message.channel, msg)

        if character.health > 0 :
            msg =(character.name + " wins the battle against " + enemy.name + "!\n")
            await client.send_message(message.channel, msg)

        else :
            msg =(character.name + " loses the battle against " + enemy.name + "!\n")
            await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)