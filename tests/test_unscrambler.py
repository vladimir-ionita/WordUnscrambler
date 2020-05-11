import unittest
from unscrambler import *


class UnscramblerTests(unittest.TestCase):
    def setUp(self):
        self.dictionary = ['bye', 'but', 'rue', 'critic', 'tea', 'need', 'true', 'busted', 'surge']

    def test_unscramble_word(self):
        # Given
        scrambled_word = "ertbu"

        # When
        filtered_words = unscramble_word(self.dictionary, scrambled_word)

        # Then
        self.assertEqual(len(filtered_words), 3)
        self.assertEqual(set(filtered_words), {'true', 'rue', 'but'})

    def test_unscramble_word_that_match_length(self):
        # Given
        scrambled_word = "ertbu"
        length = 3

        # When
        filtered_words = unscramble_word_that_match_length(self.dictionary, scrambled_word, length)

        # Then
        self.assertEqual(len(filtered_words), 2)
        self.assertEqual(set(filtered_words), {'but', 'rue'})

    def test_unscramble_word_that_match_pattern(self):
        # Given
        scrambled_word = "ertbu"

        # When
        filtered_words = unscramble_word_that_match_pattern(self.dictionary, scrambled_word, 'b__')

        # Then
        self.assertEqual(len(filtered_words), 1)
        self.assertEqual(set(filtered_words), {'but'})


if __name__ == '__main__':
    unittest.main()
