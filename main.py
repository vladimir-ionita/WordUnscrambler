from nltk.corpus import words
from filters import *


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
