# Hangman
from random import *

# Gets the string to represent the hangman.  Based on wrong tries.
def get_hangman(wrong_guesses):
    if wrong_guesses == 6:
        return " O\n/|\\\n/ \\"
    if wrong_guesses == 5:
        return " O\n/|\\\n  \\"
    if wrong_guesses == 4:
        return " O\n/|\\"
    if wrong_guesses == 3:
        return " O\n |\\"
    if wrong_guesses == 2:
        return " O\n |"
    if wrong_guesses == 1:
        return " O"
    if wrong_guesses == 0:
        return ""



# Gets the phrase showing the correct letters when guessed and "_" when unknown.
def get_masked_phrase(chosen, phrase):

    mask = ""

    for letter in phrase:
        if letter in chosen or letter == " ":
            mask += letter
        else:
            mask += "_"
        mask += " "

    return mask


# The main game and loop
def game():

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # If numbers are acceptable, add them here.
    phrases = ["PYTHON ROCKS", "LATE NIGHT SNACK", "MONTY PYTHON"]
    phrase = phrases[randint(0, 2)] # Choose a phrase at random.
    letters_chosen = ""
    wrong_guesses = 0

    while True:

        # Print the hangman.
        print(get_hangman(wrong_guesses))
        print()
        print("Phrase : ", end="")
        print(get_masked_phrase(letters_chosen, phrase))
        print()

        # Calculate the available count.
        available_count = 26 - len(letters_chosen)

        # Show letters available with count.
        print("Letters available [{}] : ".format(available_count), end="")
        for letter in alphabet:
            if letter not in letters_chosen:
                print(letter, end=" ")
        print()

        # Show letters chosen with count.
        print("Letters chosen [{}]: ".format(len(letters_chosen)), end="")

        for letter in letters_chosen:
            print(letter, end=" ")
        print()
        print()

        # Choose a LETTER or "SOLVE".  Case insensitive.
        user_choice = input("Please choose a letter or write \"solve\" to solve the puzzle. :").upper()

        # Here it's make-it or break-it.  Wrong guess = loss.  Correct = win.
        if user_choice == "SOLVE":
            guess = input("What is the puzzle? :").upper()
            if guess == phrase:
                print("Correct!  You win")
            else:
                print("Sorry, wrong guess.  You lose!")
                print("The correct phrase was : {}".format(phrase))
            exit(0)

        if user_choice not in alphabet:
            print("Sorry you must choose a valid letter from A to Z.  Try again.")
            continue

        if user_choice not in phrase:
            print("Your choice is not a letter in the puzzle.")
            wrong_guesses += 1
            if wrong_guesses > 5:
                print("You've guessed too many times, you lose.")
                print("The correct phrase was : {}".format(phrase))
                exit()

        if user_choice not in letters_chosen:
            letters_chosen += user_choice
        else:
            print("You have already chosen this.")
            print()

        print("\n" + "-" * 80 + "\n")


if __name__ == '__main__':
    game()
