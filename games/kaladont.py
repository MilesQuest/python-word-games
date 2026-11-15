import random

nokaladont = True

with open("dictionary.txt", "r") as file:
    allText = file.read()
    dictionary = list(map(str, allText.split()))

computerword = random.choice(dictionary)

print("Welcome to Kaladont, a South Slavic word game!")
print("To play, you must add a word to the last person's word beginning with the last two letters. If anyone calls Kaladont, they win!")
print("Example: Create >> Terrible >> Lesser >> Error etc...")
print()

def getplayerword():
    
    global computerword
    global playerword
    global nokaladont
    
    print("Computer's word is", computerword)
    print()

    playerword = input(">>> ")
    print()

    valid = False

    while valid == False:
        if computerword[-2:] == playerword[:2]:
            if playerword.upper() == ("KALADONT"):
                valid = True
                nokaladont = False
                print("Player called Kaladont! Player wins!")
            if playerword in open('dictionary.txt').read():
                valid = True
            else:
                print()
                print("Invalid word, computer wins!")
                nokaladont = False
                valid = True
        else:
            print()
            print("Invalid word, computer wins!")
            nokaladont = False
            valid = True
def getcomputerword():
    
    global nokaladont
    global computerword
    global playerword
    
    if playerword[-2:] == ("ka"):
        computerword = "Kaladont"
        computerwordvalid = True
        nokaladont = False
        print("Computer called Kaladont! Computer wins!")
    computerword = random.choice(dictionary)
    computerwordvalid = False
    variations = 0
    while computerwordvalid == False:
        if variations < 1000000:
            if computerword[:2] == playerword[-2:]:
                computerwordvalid = True
            else:
                computerwordvalid = False
                computerword = random.choice(dictionary)
                variations = variations + 1
        else:
            nokaladont = False
            print("Computer unable to think of a word! Player wins!")
            computerwordvalid = True
            
while nokaladont == True:
    getplayerword()
    if nokaladont == True:
        getcomputerword()
            
            
            
