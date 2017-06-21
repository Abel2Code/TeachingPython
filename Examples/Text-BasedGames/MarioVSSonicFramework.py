import     # Figure out what to import to generate random numbers

# Mario Stats
marioHealth = 64

marioAttackRange = [6, 8]  # When mario attacks, make his attack between 6 and 8 (inclusive)
# By learning how to generate random numbers. you should be able to figure out how to generate a number between 6 and 8
marioHeal = 9  # This will increase Mario's health if he is damaged. Try to figure out how to make him not heal past 64

# Sonic Stats
sonicHealth = 44

sonicMainAttackRange = [7, 10]  # When Sonic uses this attack, make his attack between 7 and 10 (inclusive)
sonicQuickAttackRange = [2, 5]  # When Sonic uses his quick attack, make his attack between 2 and 5 (inclusiv)

# If we wish to change any of these values later, we just need to tweak the value!

isMarioTurn = True  # Will keep track of which player's turn it is
# Since there are only 2 players, we can use a boolean

while not (marioHealth <= 0 or sonicHealth <= 0):  # Checks to see that no character is dead
    print("\nMario has", marioHealth, "hp!")
    print("Sonic has", sonicHealth, "hp!\n")
    if isMarioTurn:  # This conditional statement check's whos turn it is
        print("Mario's Turn!")

        # Write Mario's Turn logic here, be sure to ask player which attack they would like to use
        # TO make things simple, have them input '1' for attack and '2' for heal
        # If you would like a challenge, try writing this logic in a method.
        # NOTE The method should be at the top of this file, but under the import statements.
        # HINT If using a method, you should have the method return an array with Mario and Sonic's new health
        # You will not be able access the MarioHealth variable from the method



        isMarioTurn = False  # Makes it Sonic's turn
    else:
        print("Sonic's Turn")

        # Write Mario's Turn logic here, be sure to ask player which attack they would like to use
        # TO make things simple, have them input '1' for attack and '2' for heal



# Get here once one player has dropped below 1 health
if (marioHealth <= 0):
    print("Mario has fainted. Sonic Wins at " + str(sonicHealth) + " hp!")
else:
    print("Sonic has fainted. Mario Wins at " + str(marioHealth) + " hp!")
