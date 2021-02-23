import random
from words import word_list
from display import display_hangman


def get_word():
    word = random.choice(word_list)

    return word.upper()


def play(word):
    word_completion = "_" * len(word)

    guessed = False

    guessed_letters = []

    guessed_words = []

    tries = 6

    print("Lets play Hangman. ")

    print(display_hangman(tries))

    print(word_completion)

    print("\n")

    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("you already guessed the letter ", guess)

            elif guess not in word:
                print("is not in the word. ")

                tries -= 1

                guessed_letters.append(guess)

            else:
                print("good job. ")

                guessed_letters.append(guess)

                word_as_list = list(word_completion)

                indices = [i for i, letter in enumerate(word) if letter == guess]

                for index in indices:
                    word_as_list[index] = guess

                word_completion = "".join(word_as_list)

                if "_" not in word_completion:
                    guessed = True

        elif len(guess) == len(word_completion) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word. ", guess)

            elif guess != word:
                print(guess, "Word guess is incorrect! ")

                tries -= 1

                guessed_words.append(guess)

            else:
                guessed = True

                word_completion = word
        else:
            print("Not a valid guess. ")

        print(display_hangman(tries))
        print(word_completion)
        print("\n")

    if guessed:
        print("Congrate, you have guessed the word, You win!")

    else:
        print("you ran out of tries. The word was  " + word + ". Maybe next time!")
