from enum import Enum


# Notes:
# 1. You may alter everything in this file.
# 2. The initial code for the Hangman class is incomplete and is just a starting point.
# 3. This initial code uses type annotations, you do not need to (but it is recommended).
# 4. This class represents just the "engine" of a hangman game, it does not include any user interfaces, etc.


class HangmanStatus(Enum):
    WIN = 'WIN'
    LOSE = 'LOSE'
    ONGOING = 'ONGOING'


MAX_GUESSES = 9


class Hangman:
    """
    A minimum implementation for the logic necessary to play the game Hangman.
    """
    def __init__(self, word: str, remaining_guesses: int = MAX_GUESSES):
        pass


    def guess(self, char: str):
        """
        The player can guess at a character that is in the words.
        A correct guess should reveal the letter in the masked word.
        A wrong guess counts against the number of guesses the player has.

        :param char: The character guessed by a player
        :return: None
        """
        pass
