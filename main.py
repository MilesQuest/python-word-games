while True:
    print()
    print("Welcome to the word game launcher. Please select a game from the following list:")
    print()
    print("- Hangman")
    print("- Word Ladder")
    print("- Kaladont")
    print()
    print("* Side note, all words are from the dictionary.txt file. Rude terms may rarely appear.")
    print()
    chosengame = input(">>> ")
    print()

    if chosengame.upper() == "HANGMAN":
        with open('games/hangman.py', 'r') as Hangman:
            code = Hangman.read()
            exec(code)
    elif chosengame.upper() == "WORD LADDER":
        with open('games/word-ladder.py', 'r') as WordLadder:
            code = WordLadder.read()
            exec(code)
    elif chosengame.upper() == "KALADONT":
        with open('games/kaladont.py', 'r') as Kaladont:
            code = Kaladont.read()
            exec(code)
