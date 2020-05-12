def filter_words_by_length(words, length):
    """ Filter a list of strings by a specified length.

    Parameters
    :param words: the list of strings to be filtered
    :type words: list of str
    :param int length: the string length to filter by

    Returns
    :return list of str: the filtered list
    """
    return list(filter(lambda x: len(x) == length, words))


def filter_words_that_match_pattern(words, pattern):
    """ Filter a list of words to match a specified pattern.
    Pattern format examples:
    __e - words that are 3 characters long and end with an 'e', for example 'bye';
    __u_ - words that are 4 characters long and the 3rd character should be 'u, for example 'true';

    Parameters
    :param words: the list of strings to be filtered
    :type words: list of str
    :param str pattern: pattern string to filter by

    Returns
    :return list of str: the filtered list
    """
    res = filter_words_by_length(words, len(pattern))
    for index, letter in enumerate(pattern):
        if letter != "_":
            res = [w for w in res if w[index] == letter]
    return res


def filter_words_that_match_allowed_letters(words, allowed_letters):
    """ Filter a list of words that match allowed characters.

    Parameters
    :param words: the list of strings to be filtered
    :type words: list of str
    :param str allowed_letters: a string composed of the allowed letters

    Returns
    :return list of str: the filtered list
    """
    filtered_words = []
    for w in words:
        remaining_allowed_letters = '%s' % allowed_letters      # copy allowed_letters
        word_match = True
        for letter in w:
            if letter not in remaining_allowed_letters:
                word_match = False
                break
            remaining_allowed_letters = remaining_allowed_letters.replace(letter, '', 1)
        if word_match:
            filtered_words.append(w)
    return filtered_words
