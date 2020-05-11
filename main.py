from nltk.corpus import words


def filter_words_by_length(words, length):
    return list(filter(lambda x: len(x) == length, words))


def filter_words_that_match_pattern(words, pattern):
    res = filter_words_by_length(words, len(pattern))
    for i, l in enumerate(pattern):
        if l != "_":
            res = [w for w in res if w[i] == l]
    return res


def filter_words_that_match_allowed_letters(words, allowed_letters):
    filtered_words = []
    for w in words:
        remaining_allowed_letters = '%s' % allowed_letters
        word_match = True
        for letter in w:
            if letter not in remaining_allowed_letters:
                word_match = False
                break
            remaining_allowed_letters = remaining_allowed_letters.replace(letter, '', 1)
        if word_match:
            filtered_words.append(w)
    return filtered_words


if __name__ == '__main__':
    dictionary = words.words()
    dictionary = list(set(dictionary))

    scrambled_word = input("Enter the scrambled word: ")
    while True:
        pattern = input("Enter pattern: ")
        filtered_words = filter_words_that_match_pattern(dictionary, pattern)
        filtered_words = filter_words_that_match_allowed_letters(filtered_words, scrambled_word)

        print("Found {} result(s):".format(len(filtered_words)))
        for w in filtered_words:
            print("\t{}".format(w))
        print()
