"""
CodeAlpha Internship - Task 1
Hangman Game (text-based, beginner level)

Concepts used: random, while loops, if-else, strings, lists, functions.
No external libraries are used.
"""

import random

# ---------------------------------------------------------------
# 1. GAME DATA (constants)
# ---------------------------------------------------------------

# Exactly 5 predefined words, as required by the task.
WORDS = ["python", "laptop", "coffee", "rocket", "guitar"]

# Maximum number of incorrect guesses allowed.
MAX_WRONG = 6

# Drawing for each number of wrong guesses (index 0 = no mistakes yet).
HANGMAN_STAGES = [
    """
     +---+
         |
         |
         |
    =======""",
    """
     +---+
     O   |
         |
         |
    =======""",
    """
     +---+
     O   |
     |   |
         |
    =======""",
    """
     +---+
     O   |
    /|   |
         |
    =======""",
    """
     +---+
     O   |
    /|\\  |
         |
    =======""",
    """
     +---+
     O   |
    /|\\  |
    /    |
    =======""",
    """
     +---+
     O   |
    /|\\  |
    / \\  |
    ======="""
]


# ---------------------------------------------------------------
# 2. HELPER FUNCTIONS
# ---------------------------------------------------------------

def choose_word():
    """Pick one random word from the WORDS list."""
    return random.choice(WORDS)


def build_display(secret_word, guessed_letters):
    """
    Build the '_ _ t _ _ n' style string.
    Revealed letters are shown, unknown letters are shown as '_'.
    """
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display = display + letter + " "
        else:
            display = display + "_ "
    return display.strip()


def is_word_complete(secret_word, guessed_letters):
    """Return True only if every letter of the word has been guessed."""
    for letter in secret_word:
        if letter not in guessed_letters:
            return False
    return True


def get_valid_guess(guessed_letters):
    """
    Keep asking until the player types a valid, NEW single letter.
    Invalid input does NOT cost a life.
    """
    while True:
        guess = input("Guess a letter: ").strip().lower()

        if len(guess) == 0:
            print("You typed nothing. Please enter one letter.\n")
        elif len(guess) > 1:
            print("Please enter only ONE letter at a time.\n")
        elif not guess.isalpha():
            print("Only alphabet letters (a-z) are allowed.\n")
        elif guess in guessed_letters:
            print("You already guessed '" + guess + "'. Try a different letter.\n")
        else:
            return guess


def show_status(wrong_guesses, secret_word, guessed_letters):
    """Print the gallows, the word, guessed letters and lives left."""
    print(HANGMAN_STAGES[wrong_guesses])
    print("\nWord: " + build_display(secret_word, guessed_letters))

    if len(guessed_letters) == 0:
        print("Guessed letters: (none)")
    else:
        # sorted() keeps the list tidy and alphabetical
        print("Guessed letters: " + ", ".join(sorted(guessed_letters)))

    print("Wrong guesses left: " + str(MAX_WRONG - wrong_guesses))
    print("-" * 40)


# ---------------------------------------------------------------
# 3. MAIN GAME LOOP
# ---------------------------------------------------------------

def play_game():
    """Play one full round of Hangman."""
    secret_word = choose_word()
    guessed_letters = []   # every letter the player has tried
    wrong_guesses = 0      # counter for incorrect guesses

    print("=" * 40)
    print("        WELCOME TO HANGMAN!")
    print("=" * 40)
    print("Guess the hidden word, one letter at a time.")
    print("You are allowed " + str(MAX_WRONG) + " incorrect guesses.")
    print("-" * 40)

    # The loop runs while the player still has lives AND has not won.
    while wrong_guesses < MAX_WRONG and not is_word_complete(secret_word, guessed_letters):

        show_status(wrong_guesses, secret_word, guessed_letters)

        guess = get_valid_guess(guessed_letters)
        guessed_letters.append(guess)

        if guess in secret_word:
            print("Correct! '" + guess + "' is in the word.\n")
        else:
            wrong_guesses = wrong_guesses + 1
            print("Wrong! '" + guess + "' is not in the word.\n")

    # ----- The loop has ended, so decide win or lose -----
    print("=" * 40)
    if is_word_complete(secret_word, guessed_letters):
        print("YOU WIN! The word was: " + secret_word.upper())
        print("You finished with " + str(MAX_WRONG - wrong_guesses) + " guesses to spare.")
    else:
        print(HANGMAN_STAGES[MAX_WRONG])
        print("\nGAME OVER! You ran out of guesses.")
        print("The word was: " + secret_word.upper())
    print("=" * 40)


def main():
    """Run the game, and let the player play again if they want."""
    play_again = "y"
    while play_again == "y":
        play_game()

        # Simple validation for the replay question
        answer = ""
        while answer not in ["y", "n"]:
            answer = input("\nPlay again? (y/n): ").strip().lower()
            if answer not in ["y", "n"]:
                print("Please type 'y' for yes or 'n' for no.")
        play_again = answer

    print("Thanks for playing Hangman. Goodbye!")


# This makes the game start only when the file is run directly.
if __name__ == "__main__":
    main()