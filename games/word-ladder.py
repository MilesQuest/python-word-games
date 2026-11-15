import random

with open("dictionary.txt", "r") as file:
    allText = file.read()
    wordlist = list(map(str, allText.split()))

wordlength = int(input("Set length of your starting and ending word: "))
print()

worda = random.choice(wordlist)
wordb = random.choice(wordlist)

while wordlength != len(worda) or wordlength != len(wordb):
    worda = random.choice(wordlist)
    wordb = random.choice(wordlist)

worda = worda.upper()
wordb = wordb.upper()

while worda == wordb:
    worda = random.choice(wordlist)
    wordb = random.choice(wordlist)
    
print("Your starting word is", worda, "Your ending word is", wordb)
print()
print("TRADITIONAL RULES: You may add, remove, or change one letter from your word at a time until you reach your ending word.")
print("ADVANCED RULES: Same as traditional rules, however you may also scramble the word in any pattern OR repeat letters without it counting towards your turn. Removing letters also does not count towards your turn.")
print("Play your way!")
print()
while worda != wordb:
    changedletters = 0
    valid = True
    print()
    nextword = input("WORD: ")
    print()
    if nextword in open('dictionary.txt').read():
        print("Valid!")
        print()
        validword = True
    else:
        print("Invalid.")
        print()
        validword = False
    if validword == True:
        for letter in nextword:
            if letter.upper() in worda.upper():
                print("Checking Your Word...")
            else:
                changedletters = changedletters + 1
                if changedletters > 1:
                    print("INVALID WORD.")
                    valid = False
    else:
        valid = False
    if valid == True:
        print()
        print("Valid!")
        worda = nextword.upper()
        print()
    else:
        worda = worda
        
print("Congratulations! You have beat word ladder!")
print() 
