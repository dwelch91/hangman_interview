import unittest

import hangman
from hangman import Hangman

class HangmanTests(unittest.TestCase):
    def test_initially_9_failures_are_allowed(self):
        game = Hangman('foo')
        self.assertEqual(hangman.STATUS_ONGOING, game.get_status())
        self.assertEqual(9, game.remaining_guesses)

    def test_initially_no_letters_are_guessed(self):
        game = Hangman('foo')

        self.assertEqual('___', game.get_masked_word())

    def test_after_10_failures_the_game_is_over(self):
        game = Hangman('foo')

        for i in range(10):
            game.guess('x')

        self.assertEqual(-1, game.remaining_guesses)
        self.assertEqual(hangman.STATUS_LOSE, game.get_status())

    def test_after_game_is_over_more_guesses_are_exceptions(self):
        game = Hangman('foo')

        for i in range(10):
            game.guess('x')

        with self.assertRaises(ValueError) as err:
            game.guess('x')

        self.assertEqual(ValueError, type(err.exception))
        self.assertEqual("The game has already ended.", err.exception.args[0])

    def test_feeding_a_correct_letter_removes_underscores(self):
        game = Hangman('foobar')

        game.guess('b')
        self.assertEqual(hangman.STATUS_ONGOING, game.get_status())
        self.assertEqual(9, game.remaining_guesses)
        self.assertEqual('___b__', game.get_masked_word())

        game.guess('o')
        self.assertEqual(hangman.STATUS_ONGOING, game.get_status())
        self.assertEqual(9, game.remaining_guesses)
        self.assertEqual('_oob__', game.get_masked_word())


    def test_feeding_a_correct_letter_twice_counts_as_a_failure(self):
        game = Hangman('foobar')

        game.guess('b')
        self.assertEqual(hangman.STATUS_ONGOING, game.get_status())
        self.assertEqual(9, game.remaining_guesses)
        self.assertEqual('___b__', game.get_masked_word())

        game.guess('b')
        self.assertEqual(hangman.STATUS_ONGOING, game.get_status())
        self.assertEqual(8, game.remaining_guesses)
        self.assertEqual('___b__', game.get_masked_word())


    def test_getting_all_the_letters_right_makes_for_a_win(self):
        game = Hangman('hello')

        game.guess('b')
        self.assertEqual(hangman.STATUS_ONGOING, game.get_status())
        self.assertEqual(8, game.remaining_guesses)
        self.assertEqual('_____', game.get_masked_word())

        game.guess('e')
        self.assertEqual(hangman.STATUS_ONGOING, game.get_status())
        self.assertEqual(8, game.remaining_guesses)
        self.assertEqual('_e___', game.get_masked_word())

        game.guess('l')
        self.assertEqual(hangman.STATUS_ONGOING, game.get_status())
        self.assertEqual(8, game.remaining_guesses)
        self.assertEqual('_ell_', game.get_masked_word())

        game.guess('o')
        self.assertEqual(hangman.STATUS_ONGOING, game.get_status())
        self.assertEqual(8, game.remaining_guesses)
        self.assertEqual('_ello', game.get_masked_word())

        game.guess('h')
        self.assertEqual(hangman.STATUS_WIN, game.get_status())
        self.assertEqual('hello', game.get_masked_word())

    def test_assert_if_game_won(self):
        game = Hangman('hello')

        game.guess('b')
        game.guess('e')
        game.guess('l')
        game.guess('o')
        game.guess('h')

        with self.assertRaises(ValueError) as err:
            game.guess('x')
        self.assertEqual(ValueError, type(err.exception))
        self.assertEqual("The game has already ended.", err.exception.args[0])

    def test_winning_on_last_guess_still_counts_as_a_win(self):
        guesses = 10

        game = Hangman('aaa', guesses)
        bad_guesses = 'b' * guesses
        for ch in bad_guesses:
            game.guess(ch)
        game.guess('a')
        self.assertEqual(0, game.remaining_guesses)
        self.assertEqual(hangman.STATUS_WIN, game.get_status())
        self.assertEqual( 'aaa', game.get_masked_word())
