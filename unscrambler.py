from filters import *


def unscramble_word(dictionary, scrambled_word):
    """ Return a list of words from the dictionary that are composed from the scrambled word's letters only.

    Parameters
    :param dictionary: list of words to unscramble against
    :type dictionary: list of str
    :param str scrambled_word: allowed letters

    Returns
    :return list of str: list of unscrambled words
    """
    return filter_words_that_match_allowed_letters(dictionary, scrambled_word)


def unscramble_word_that_match_length(dictionary, scrambled_word, length):
    """ Return list of words from the dictionary that are composed from the scrambled word's letters only and satisfy the length.

    Parameters
    :param dictionary: list of words to unscramble against
    :type dictionary: list of str
    :param str scrambled_word: allowed letters
    :param int length: length criteria for words

    Returns
    :return list of str: list of unscrambled words
    """
    filtered_words = filter_words_by_length(dictionary, length)
    return filter_words_that_match_allowed_letters(filtered_words, scrambled_word)


def unscramble_word_that_match_pattern(dictionary, scrambled_word, pattern):
    """ Return a list of words from the dictionary that are composed from the scrambled word's letters only and satisfy a pattern.
    Pattern format examples:
    __e - words that are 3 characters long and end with an 'e', for example 'bye';
    __u_ - words that are 4 characters long and the 3rd character should be 'u, for example 'true';

    Parameters
    :param dictionary: list of words to unscramble against
    :type dictionary: list of str
    :param str scrambled_word: allowed letters
    :param str pattern: pattern criteria for words

    Returns
    :return list of str: list of unscrambled words
    """
    filtered_words = filter_words_that_match_pattern(dictionary, pattern)
    return filter_words_that_match_allowed_letters(filtered_words, scrambled_word)
