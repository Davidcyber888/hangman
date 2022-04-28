"""Hangman game with ASCII-art"""

import random, sys

# Set up the constants.
# 7 trys and images.
HANGMAN_IMG = [r"""
 +--+
 |  |
    |
    |
    |
    |
=====""",
               r"""
 +--+
 |  |
 O  |
    |
    |
    |
=====
    """,
               r"""
 +--+
 |  |
 O  |
 |  |
    |
    |
=====
    """,
               r"""
 +--+
 |  |
 O  |
/|  |
    |
    |
=====
    """,
               r"""
 +--+
 |  |
 O  |
/|\ |
    |
    |
=====
    """,
               r"""
 +--+
 |  |
 O  |
/|\ |
/   |
    |
=====
    """,
               r"""
 +--+
 |  |
 O  |
/|\ |
/ \ |
    |
=====
    """,

               ]
# Bank of words.
WORDS = 'ANT BABOON BADGER BAT BEAR BEAVER CAMEL CAT CLAM COBRA COUGAR ' \
        'COYOTE CROW DEER DOG DONKEY DUCK EAGLE FERRET FOX FROG GOAT GOOSE HAWK' \
        'LION LIZARD LLAMA MOLE MONKEY MOOSE MOUSE MULE NEWT OTTER OWL PANDA PARROT' \
        'PIGEON PYTHON RABBIT RAM RAT RAVEN RHINO SALMON SEAL SHARK SHEEP SKUNK ' \
        'SLOTH SNAKE SPIDER STORK SWAN TIGER TOAD TROUT TURKEY TURTLE WEASEL WHALE ' \
        'WOLF WOMBAT ZEBRA'.split()


CATEGORY = 'Animals'


def main():
    print("The Hangman Game")
    # Setup variables for a new game.
    # List of incorrect letter guesses.
    missedLetters = []
    # List of correct letter guesses.
    correctLetters = []
    # The word the player must guess.
    secretWord = random.choice(WORDS)

    # Main loop.
    while True:
        # Draw the hangman.
        drawHangman(missedLetters, correctLetters, secretWord)

        # Let the player enter their letter guess.
        guess = getPlayerGuess(missedLetters + correctLetters)

        if guess in secretWord:
            # Add the correct guess to correct letters.
            correctLetters.append(guess)
            # Check if the player has won.
            foundAllLetters = True
            for word_letter in secretWord:
                if word_letter not in correctLetters:
                    # There's a letter in the secret word that isn't
                    # yet in correctLetters, so the player hasn't won.
                    foundAllLetters = False
                    break
            # The player guess all letters.
            if foundAllLetters:
                print(f"You won , The secret word is {secretWord}")
                break
        else:
            # The player guess incorrectly.
            missedLetters.append(guess)
            # Check if player lost.
            if len(missedLetters) == len(HANGMAN_IMG) - 1:
                drawHangman(missedLetters, correctLetters, secretWord)
                print("You try too much times!")
                print(f"The right word is {secretWord.format}")
                break


def drawHangman(missedLetters, correctLetters, secretWord):
    """Draw the current state of the hangman, along with the missed and correctly-guessed letters of the secret word."""
    print(HANGMAN_IMG[len(missedLetters)])
    print(f"The category is: {CATEGORY}\n")

    # Show the incorrectly guessed letters.
    print('Missed letters: ', end='')
    for letter in missedLetters:
        print(letter, end=' ')
    if len(missedLetters) == 0:
        print('No missed letters!')
    print()

    # Display the blanks for the secret word (one blank per letter):
    blanks = ['_'] * len(secretWord)

    # Replace blanks with correctly guessed letters.
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks[i] = secretWord[i]

    # Show the secret word with spaces in between each letter.
    print(' '.join(blanks))


def getPlayerGuess(alreadyGuessed):
    """Returns the letter the player entered. This function makes sure
    the player entered a single letter they haven't guessed before."""
    # Keep asking until the player enters a valid letter.
    while True:
        print("Pls guess a letter.")
        guess = input('> ').upper()
        # Check player input.
        if len(guess) != 1:
            print("Pls enter a single letter!!!")
        elif not guess.isalpha():
            print("Pls enter only letter, not other chars!!!")
        elif guess in alreadyGuessed:
            print(f"You have already guessed the {guess} letter!!! Pls choose an other one")
        else:
            return guess


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        # Press Ctrl+C to end the program.
        sys.exit()
