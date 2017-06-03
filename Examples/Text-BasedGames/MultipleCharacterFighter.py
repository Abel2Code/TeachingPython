import random  # Will be used to generate random numbers for attack


def executeMarioTurn(marioHealth, sonicHealth):
    validInput = False  # We will use this variable to decide whether to keep trying to get the user input

    while not validInput:  # This will run until the user enter a valid move
        decision = input("Type attack for Mario to attack! \nType heal for Mario to heal!\n")
        if decision == "attack" or decision == "heal":
            validInput = True  # Stops loop if valid move

    if decision == "attack":
        attackValue = random.randint(marioAttackRange[0], marioAttackRange[1])  # Generates random value in attk range
        sonicHealth -= attackValue  # Subtracts attackValue from current SonicHealth
        print("Mario attacked Sonic and dealt", attackValue, "hp!")
    else:
        marioHealth += marioHeal  # Adds marioHeal to current marioHealth
        if marioHealth > 64:  # Makes sure Mario does not heal over max hp
            marioHealth = 64
        print("Mario healed!")
    return [marioHealth, sonicHealth]  # Returns new hp values


def executeSonicTurn(marioHealth, sonicHealth):
    validInput = False  # We will use this variable to decide whether to keep trying to get the user input

    while not validInput:  # This will run until the user enter a valid move
        decision = input(
            "Type heavy for Sonic to use his heavy attack! \nType fury for Sonic to use his fury attack!\n")
        if decision == "heavy" or decision == "fury":
            validInput = True  # Stops loop if valid move

    if decision == "heavy":

        # Generates random value in attk range
        attackValue = random.randint(sonicMainAttackRange[0], sonicMainAttackRange[1])
        marioHealth -= attackValue
        print("Sonic attacked Mario and dealt", attackValue, "hp!")
    else:
        for counter in range(1, 4):  # Sonic fury attacks 3 times

            # Generates random value in attk range
            attackValue = random.randint(sonicQuickAttackRange[0], sonicQuickAttackRange[1])
            marioHealth -= attackValue
            print("On punch #" + str(counter) + ", sonic dealt " + str(attackValue) + " damage!")
    return [marioHealth, sonicHealth]  # Returns new hp values


# Mario Stats
marioHealth = 64  # Is the starting health that Mario starts with

marioAttackRange = [6, 8]  # Since this attack value is based on chance, we opt to use a list to hold both values
marioHeal = 9  # Since the heal is not based on chance, we use an integer instead of a list

# Sonic Stats
sonicHealth = 44  # Is the starting health that Sonic starts with

sonicMainAttackRange = [7, 10]  # Since this attack value is based on chance, we opt to use a list to hold both values
sonicQuickAttackRange = [2, 5]  # Since this attack value is based on chance, we opt to use a list to hold both values

# If we wish to change any of these values later, we just need to tweak the value!

isMarioTurn = True  # Will keep track of which player's turn it is
# Since there are only 2 players, we can use a boolean

while not (marioHealth <= 0 or sonicHealth <= 0):  # Checks to see that no character is dead
    print("\nMario has", marioHealth, "hp!")
    print("Sonic has", sonicHealth, "hp!\n")
    if isMarioTurn:  # This conditional statement check's whos turn it is
        print("Mario's Turn!")

        # See Mario turn logic on line 3
        tempHealth = executeMarioTurn(marioHealth, sonicHealth)  # We assign the list this method returns to a variable
        marioHealth = tempHealth[0]  # executeMarioTurn returns a list with Mario and Sonic's health
        sonicHealth = tempHealth[1]
        isMarioTurn = False  # Makes it Sonic's turn
    else:
        print("Sonic's Turn")

        # See Sonic turn logic on line
        tempHealth = executeSonicTurn(marioHealth, sonicHealth)  # We assign the list this method returns to a variable
        marioHealth = tempHealth[0]  # executeSonicTurn returns a list with Mario and Sonic's health
        sonicHealth = tempHealth[1]
        isMarioTurn = True  # Makes it Mario's Turn

# Get here once one player has dropped below 1 health
if (marioHealth <= 0):
    print("Mario has fainted. Sonic Wins at " + str(sonicHealth) + " hp!")
else:
    print("Sonic has fainted. Mario Wins at " + str(marioHealth) + " hp!")
