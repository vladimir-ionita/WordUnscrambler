from nltk.corpus import words
from unscrambler import *
from utilities import *


dictionary = words.words()
dictionary = list(set(dictionary))      # make it unique

scrambled_word = input("Enter the scrambled word: ")
while True:
    criteria = input("Enter pattern or length of word: ")
    if is_number(criteria):
        words = unscramble_word_that_match_length(dictionary, scrambled_word, int(criteria))
    else:
        words = unscramble_word_that_match_pattern(dictionary, scrambled_word, criteria)

    print("Found {} result(s):".format(len(words)))
    for w in words:
        print("\t{}".format(w))
    print()
