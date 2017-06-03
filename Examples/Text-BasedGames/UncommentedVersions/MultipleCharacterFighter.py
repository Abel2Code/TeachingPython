import random

class Player():
    def __init__(self,number,character):
        self.number = number
        self.character = character

class Character():
    def __init__(self,name,maxHP,moves):
        self.name = name
        self.maxHP = maxHP
        self.currentHP = maxHP
        self.moves = moves

class Move():
    def __init__(self,damageMax,damageMin,healMax,healMin,itterates,description):
        self.damageMax = damageMax
        self.damageMin = damageMin
        self.healMax = healMax
        self.healMin = healMin
        self.itterates = itterates
        self.description = description

    def use(self,user,opponent):
        for counter in range(1,self.itterates+1):
            if self.healMax > 0:
                user.currentHP +=  random.randint(self.healMin, self.healMax)
                if user.currentHP > user.maxHP:
                    user.currentHP = user.maxHP
                print(user.name,"healed!")

            if self.damageMax > 0:
                attackValue = random.randint(self.damageMin,self.damageMax)
                opponent.currentHP -= attackValue
                print(user.name,"attacked",opponent.name,"and dealt",attackValue,"hp!")


def validMoveInput(input):
    if input == "1" or input == "2":
        return True
    else:
        return False

def executeTurn(char1,char2):
    question = "Would you like " + char1.name + " to " + char1.moves[0].description + " or " +\
               char1.moves[1].description + "?\nType 1 for " + char1.moves[0].description + " and 2 for " +\
               char1.moves[1].description + "\n"
    decision = input(question)
    validDecision = validMoveInput(decision)
    while not (validDecision):
        print("Try again")
        decision = input(question)
        validDecision = validMoveInput(decision)
    char1.moves[int(decision) - 1].use(char1,char2)

def initializeCharacters():
    mario = initMario()
    sonic = initSonic()

    return[mario,sonic]

def initMario():
    moves = [Move(8,6,0,0,1,"attack"),Move(0,0,9,9,1,"heal")]
    marioHealth = 64

    return Character("Mario",marioHealth,moves)

def initSonic():
    moves = [Move(10,7,0,0,1,"heavy attack"),Move(5,2,0,0,3,"fury attack")]
    sonicHealth = 44

    return Character("Sonic",sonicHealth,moves)


def listCharacters(characters):
    for counter in characters:
        print(counter.name)

def validCharacter(string, list):
    for interval in list:
        if interval.name == string:
            return list.index(interval)
    return -1

characters = initializeCharacters()
print("Welcome!\n")
print("These are the available characters:")
listCharacters(characters)

player1Character = (input("\nPlayer 1, choose a character!\n"))
player1CharacterPos = validCharacter(player1Character, characters)

while player1CharacterPos is -1:
    print("Please try again")
    player1Character = (input("Player 1, choose a character!"))
    player1CharacterPos = validCharacter(player1Character, characters)

player1Character = characters[player1CharacterPos]

player1 = Player(1,player1Character)

characters.remove(characters[player1CharacterPos])

print("\nThese are the available characters:")
listCharacters(characters)

player2Character = (input("\nPlayer 2, choose a character!\n"))
player2CharacterPos = validCharacter(player2Character, characters)

while validCharacter(player2Character, characters) is -1:
    print("Please try again")
    player2Character = (input("Player 2, choose a character!\n"))
    player2CharacterPos = validCharacter(player2Character, characters)

player2Character = characters[player2CharacterPos]

player2 = Player(2,player2Character)

isPlayer1Turn = True

while not (player1.character.currentHP <= 0 or player2.character.currentHP <= 0):
    print("\n" + player1.character.name + " has " + str(player1.character.currentHP) +" hp!")
    print(player2.character.name,"has",player2.character.currentHP,"hp!\n")
    if isPlayer1Turn:
        print(player1.character.name,"'s Turn!")

        executeTurn(player1.character,player2.character)
        isPlayer1Turn = False
    else:
        print(player2.character.name,"'s Turn")

        executeTurn(player2.character,player1.character)
        isPlayer1Turn = True

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
