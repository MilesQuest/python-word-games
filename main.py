while True:
    print()
    print("Welcome to the word game launcher. Please select a game from the following list:")
    print()
    print("- Hangman")
    print("- Word Ladder")
    print("- Kaladont")
    print()
    print("* Side note, all words are from the ENABLE1 dictionary file. Rude terms may rarely appear.")
    print()
    chosengame = input(">>> ")
    print()

    if chosengame.upper() == "HANGMAN":
        import Hangman
    elif chosengame.upper() == "WORD LADDER":
        import WordLadder
    elif chosengame.upper() == "KALADONT":
        import Kaladont
