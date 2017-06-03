import random  # Will be used to generate random numbers for attack


class Player():  # Tracks players and information about them
    def __init__(self, number, character):  # Class tracks there number and character - One could track usernames here
        self.number = number
        self.character = character  # stores object of type Character created below


class Character():  # Stores attributes specific to each character Ex: Mario and Sonic
    def __init__(self, name, maxHP, moves):
        self.name = name
        self.maxHP = maxHP  # Since a character cannot heal over their max health, we keep track of this value here
        self.currentHP = maxHP
        self.moves = moves  # For the sake of this example, we will assume Characters have two moves


class Move():  # Stores information about Character's moevs
    def __init__(self, damageMax, damageMin, healMax, healMin, itterates, description):
        self.damageMax = damageMax
        self.damageMin = damageMin
        self.healMax = healMax
        self.healMin = healMin
        self.itterates = itterates
        self.description = description

    def use(self, user, opponent):  # Based on damage and heal values, this executes the move
        for counter in range(1, self.itterates + 1):  # If a move itterates multiple times, this loop keeps track
            if self.healMax > 0:  # Checks if move heals
                user.currentHP += random.randint(self.healMin, self.healMax)  # Adds health to Character
                if user.currentHP > user.maxHP:  # Checks if Character is over max health
                    user.currentHP = user.maxHP
                print(user.name, "healed!")

            if self.damageMax > 0:  # Checks if the move deals damage
                attackValue = random.randint(self.damageMin, self.damageMax)
                opponent.currentHP -= attackValue
                print(user.name, "attacked", opponent.name, "and dealt", attackValue, "hp!")


def validMoveInput(input):
    if input == "1" or input == "2":  # Since user input is always a string, we use "1" instead of 1
        return True
    else:
        return False


def executeTurn(char1, char2):  # Logic for Character turn
    question = "Would you like " + char1.name + " to " + char1.moves[0].description + " or " + \
               char1.moves[1].description + "?\nType 1 for " + char1.moves[0].description + " and 2 for " + \
               char1.moves[1].description + "\n"

    decision = input(question)
    validDecision = validMoveInput(decision)
    while not (validDecision):  # Checks if user inputted 1 or 2
        print("Try again")
        decision = input(question)
        validDecision = validMoveInput(decision)
    char1.moves[int(decision) - 1].use(char1, char2)  # executes move


def initializeCharacters():  # Creates the characters. If we wanted to add a new Character, we would add it here
    # Mario and Sonic are initialized in different methods so that our code is cleaner and easier to read
    mario = initMario()
    sonic = initSonic()

    return [mario, sonic]  # Returns list of all characters


def initMario():  # Creates Mario Character
    moves = [Move(8, 6, 0, 0, 1, "attack"), Move(0, 0, 9, 9, 1, "heal")]  # Creates Mario move list
    marioHealth = 64  # Is Mario's starting health

    return Character("Mario", marioHealth, moves)


def initSonic():  # Creates Sonic Character
    moves = [Move(10, 7, 0, 0, 1, "heavy attack"), Move(5, 2, 0, 0, 3, "fury attack")]  # Creates Sonic move list
    sonicHealth = 44  # Is Sonic's starting health

    return Character("Sonic", sonicHealth, moves)


def listCharacters(characters):  # lists all initialized Characters
    for counter in characters:
        print(counter.name)


def validCharacter(string, list):  # Checks if inputted is in the list passed into the method
    for interval in list:
        if interval.name == string:
            return list.index(interval)
    return -1  # If we cannot find the string, we return -1


characters = initializeCharacters()  # Creates the character list
print("Welcome!\n")
print("These are the available characters:")
listCharacters(characters)

player1Character = (input("\nPlayer 1, choose a character!\n"))
player1CharacterPos = validCharacter(player1Character, characters)

while player1CharacterPos is -1:  # Checks if Player 1 inputted a valid Character name - Case Sensitive
    print("Please try again")
    player1Character = (input("Player 1, choose a character!"))
    player1CharacterPos = validCharacter(player1Character, characters)

player1Character = characters[player1CharacterPos]

player1 = Player(1, player1Character)  # Creates Player 1

characters.remove(characters[player1CharacterPos])

print("\nThese are the available characters:")
listCharacters(characters)

player2Character = (input("\nPlayer 2, choose a character!\n"))
player2CharacterPos = validCharacter(player2Character, characters)

while player1CharacterPos is -1:  # Checks if Player 2 inputted a valid Character name - Case Sensitive
    print("Please try again")
    player2Character = (input("Player 2, choose a character!\n"))
    player2CharacterPos = validCharacter(player2Character, characters)

player2Character = characters[player2CharacterPos]

player2 = Player(2, player2Character)

isPlayer1Turn = True  # Will keep track of which player's turn it is
# Since there are only 2 players, we can use a boolean

# While loop checks to see that no character is dead
while not (player1.character.currentHP <= 0 or player2.character.currentHP <= 0):
    print("\n" + player1.character.name + " has " + str(player1.character.currentHP) + " hp!")
    print(player2.character.name, "has", player2.character.currentHP, "hp!\n")
    if isPlayer1Turn:  # This conditional statement check's whos turn it is
        print(player1.character.name, "'s Turn!")
        executeTurn(player1.character, player2.character)  # Executes Player's turn
        isPlayer1Turn = False  # Makes it Player2's turn
    else:
        print(player2.character.name, "'s Turn")
        executeTurn(player2.character, player1.character)  # Executes Player's turn
        isPlayer1Turn = True  # Makes it Player1's Turn

# Get here once one player has dropped below 1 health
if (player1.character.currentHP <= 0):
    print(player1.character.name +
          " has fainted. " +
          player2.character.name +
          " wins at " + str(player2.character.currentHP) +
          " hp!")
else:
    print(player2.character.name +
          " has fainted. " +
          player1.character.name +
          " wins at " +
          str(player1.character.currentHP) +
          " hp!")
