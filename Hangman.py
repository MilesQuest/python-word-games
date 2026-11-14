import random

wongame = False

lives = 6
guessed = ""
guessedtally = 0

with open("dictionary.txt", "r") as file:
    allText = file.read()
    words = list(map(str, allText.split()))
    
    word = random.choice(words).upper()

print()
print("WELCOME TO HANGMAN. THE WORD HAS BEEN SELECTED.")
print()
while lives > 0:
    guessedtally = 0
    for letter in word:
        if letter.upper() in guessed:
            print(end=letter)
            guessedtally = guessedtally + 1
        else: 
                print(end=" _ ")
        if guessedtally == len(word):
            print()
            print("Correct!")
            wongame = True
            lives = 0
    print()
    if wongame == False:
        print()
        print("Lives:", lives)
        print("Guessed Letters:", guessed)
        guess = input("Guess a letter: ")
        if guess.upper() in word:
            print("Correct!")
            guessed = (guess.upper() + guessed)
            print()
            
        else:
            print()
            print("Incorrect.")
            print()
            lives = lives - 1
            guessed = (guess.upper() + guessed)
print("The word was", word)
print()