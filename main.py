import hangman

if __name__ == '__main__':
    word = hangman.get_word()

    hangman.play(word)

    while input("Play Again (Y/N) ").upper() == "Y":
        word = hangman.get_word()

        hangman.play(word)