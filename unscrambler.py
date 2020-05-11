from filters import *


def unscramble_word(dictionary, scrambled_word):
    return filter_words_that_match_allowed_letters(dictionary, scrambled_word)


def unscramble_word_that_match_length(dictionary, scrambled_word, length):
    filtered_words = filter_words_by_length(dictionary, length)
    return filter_words_that_match_allowed_letters(filtered_words, scrambled_word)


def unscramble_word_that_match_pattern(dictionary, scrambled_word, pattern):
    filtered_words = filter_words_that_match_pattern(dictionary, pattern)
    return filter_words_that_match_allowed_letters(filtered_words, scrambled_word)
