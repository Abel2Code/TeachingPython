import random


def executeMarioTurn(marioHealth, sonicHealth):
    validInput = False

    while not validInput:
        decision = input("Type attack for Mario to attack! \nType heal for Mario to heal!\n")
        if decision == "attack" or decision == "heal":
            validInput = True

    if decision == "attack":
        attackValue = random.randint(marioAttackRange[0], marioAttackRange[1])
        sonicHealth -= attackValue
        print("Mario attacked Sonic and dealt", attackValue, "hp!")
    else:
        marioHealth += marioHeal
        if marioHealth > 64:
            marioHealth = 64
        print("Mario healed!")
    return [marioHealth, sonicHealth]


def executeSonicTurn(marioHealth, sonicHealth):
    validInput = False

    while not validInput:
        decision = input(
            "Type heavy for Sonic to use his heavy attack! \nType fury for Sonic to use his fury attack!\n")
        if decision == "heavy" or decision == "fury":
            validInput = True

    if decision == "heavy":
        attackValue = random.randint(sonicMainAttackRange[0], sonicMainAttackRange[1])
        marioHealth -= attackValue
        print("Sonic attacked Mario and dealt", attackValue, "hp!")
    else:
        for counter in range(1, 4):
            attackValue = random.randint(sonicQuickAttackRange[0], sonicQuickAttackRange[1])
            marioHealth -= attackValue
            print("On punch #" + str(counter) + ", sonic dealt " + str(attackValue) + " damage!")
    return [marioHealth, sonicHealth]

marioHealth = 64

marioAttackRange = [6, 8]
marioHeal = 9


sonicHealth = 44

sonicMainAttackRange = [7, 10]
sonicQuickAttackRange = [2, 5]

isMarioTurn = True

while not (marioHealth <= 0 or sonicHealth <= 0):
    print("\nMario has", marioHealth, "hp!")
    print("Sonic has", sonicHealth, "hp!\n")
    if isMarioTurn:
        print("Mario's Turn!")

        tempHealth = executeMarioTurn(marioHealth, sonicHealth)
        marioHealth = tempHealth[0]
        sonicHealth = tempHealth[1]
        isMarioTurn = False
    else:
        print("Sonic's Turn")

        tempHealth = executeSonicTurn(marioHealth, sonicHealth)
        marioHealth = tempHealth[0]
        sonicHealth = tempHealth[1]
        isMarioTurn = True

if (marioHealth <= 0):
    print("Mario has fainted. Sonic Wins at " + str(sonicHealth) + " hp!")
else:
    print("Sonic has fainted. Mario Wins at " + str(marioHealth) + " hp!")
