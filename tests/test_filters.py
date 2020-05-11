import unittest
from filters import *


class FiltersTests(unittest.TestCase):
    def setUp(self):
        self.dictionary = ['bye', 'but', 'rue', 'critic', 'tea', 'need', 'busted', 'surge']

    def test_filter_words_by_length_some_results(self):
        # Given
        length = 3

        # When
        filtered_words = filter_words_by_length(self.dictionary, length)

        # Then
        self.assertEqual(len(filtered_words), 4)
        self.assertEqual(set(filtered_words), {'bye', 'but', 'rue', 'tea'})

    def test_filter_words_by_length_no_results(self):
        # Given
        length = 2

        # When
        filtered_words = filter_words_by_length(self.dictionary, length)

        # Then
        self.assertEqual(len(filtered_words), 0)

    def test_filter_words_that_match_pattern_p1(self):
        # Given
        pattern = '__e'

        # When
        filtered_words = filter_words_that_match_pattern(self.dictionary, pattern)

        # Then
        self.assertEqual(len(filtered_words), 2)
        self.assertEqual(set(filtered_words), {'bye', 'rue'})

    def test_filter_words_that_match_pattern_p2(self):
        # Given
        pattern = 'b__'

        # When
        filtered_words = filter_words_that_match_pattern(self.dictionary, pattern)

        # Then
        self.assertEqual(len(filtered_words), 2)
        self.assertEqual(set(filtered_words), {'bye', 'but'})

    def test_filter_words_that_match_pattern_p3(self):
        # Given
        pattern = '___'

        # When
        filtered_words = filter_words_that_match_pattern(self.dictionary, pattern)

        # Then
        self.assertEqual(len(filtered_words), 4)
        self.assertEqual(set(filtered_words), {'bye', 'but', 'rue', 'tea'})

    def test_filter_words_that_match_allowed_letters(self):
        # Given
        allowed_letters = 'uegsr'

        # When
        filtered_words = filter_words_that_match_allowed_letters(self.dictionary, allowed_letters)

        # Then
        self.assertEqual(len(filtered_words), 2)
        self.assertEqual(set(filtered_words), {'surge', 'rue'})


if __name__ == '__main__':
    unittest.main()
