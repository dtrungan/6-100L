# Problem Set 2, hangman.py
# Name: An Dang Trung
# Collaborators: No
# Time spent: 1:00

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, "r")
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    return random.choice(wordlist)


# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()


def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
    for letter in secret_word:
        if letter not in letters_guessed:
            return False

    return True


def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    progress = ""

    for letter in secret_word:
        if letter in letters_guessed:
            progress += letter

        else:
            progress += "*"

    return progress


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    available_letters = string.ascii_lowercase

    for letter in letters_guessed:
        if letter in available_letters:
            available_letters = available_letters.replace(letter, "")

    return available_letters


def choose_letter(secret_word, available_letters):
    choose_from = ""

    for letter in secret_word:
        if letter in available_letters:
            choose_from += letter

    new = random.randint(0, len(choose_from) - 1)
    revealed_letter = choose_from[new]

    return revealed_letter


def unique_letters(secret_word):
    seen = ""
    count = 0

    for letter in secret_word:
        if letter not in seen:
            seen += letter
            count += 1

    return count


def hangman(secret_word, with_help):
    """
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter (or help character '!'
      for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------
    * If the guess is the symbol !, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    """
    print("Welcome to Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")

    letters_guessed = []
    guesses_remaining = 10
    vowels = "aeiou"
    while not has_player_won(secret_word, letters_guessed):
        print("--------------")

        if guesses_remaining <= 0:
            print(f"Sorry, you ran out of guesses. The word was {secret_word}.")
            break

        print(f"You have {guesses_remaining} guesses left.")
        print(f"Available letters: {get_available_letters(letters_guessed)}")
        letter = input("Please guess a letter: ").lower()

        if letter in letters_guessed:
            print(
                f"Oops! You've already guessed that letter: {get_word_progress(secret_word, letters_guessed)}"
            )
            continue

        if with_help and letter == "!":
            if guesses_remaining >= 3:
                guesses_remaining -= 3
                letter = choose_letter(
                    secret_word, get_available_letters(letters_guessed)
                )
                letters_guessed.append(letter)

                print(f"Letter revealed: {letter}")
                print(get_word_progress(secret_word, letters_guessed))

            else:
                print(
                    f"Oops! Not enough guesses left: {get_word_progress(secret_word, letters_guessed)}"
                )

            continue

        letters_guessed.append(letter)

        if len(letter) != 1 or not letter.isalpha():
            print(
                f"Oops! That is not a valid letter. Please input a letter from the alphabet: {get_word_progress(secret_word, letters_guessed)}"
            )
            continue

        if letter in secret_word:
            print(f"Good guess: {get_word_progress(secret_word, letters_guessed)}")

        else:
            if letter in vowels:
                guesses_remaining -= 2

            else:
                guesses_remaining -= 1

            print(
                f"Oops! That letter is not in my word: {get_word_progress(secret_word, letters_guessed)}"
            )

    if has_player_won(secret_word, letters_guessed):
        print("--------------")
        print("Congratulations, you won!")
        total_score = (
            guesses_remaining + 4 * unique_letters(secret_word) + 3 * len(secret_word)
        )
        print(f"Your total score for this game is: {total_score}")


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

if __name__ == "__main__":
    # To test your game, uncomment the following three lines.

    secret_word = choose_word(wordlist)
    with_help = False
    hangman(secret_word, with_help)

    # After you complete with_help functionality, change with_help to True
    # and try entering "!" as a guess!

    ###############

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your pset. However, please run ps2_student_tester.py
    # one more time before submitting to make sure all the tests pass.
    pass
