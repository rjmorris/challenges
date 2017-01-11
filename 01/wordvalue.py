from operator import itemgetter
from data import DICTIONARY, LETTER_SCORES

all_words = []
word_values = {}

def load_words():
    """Load dictionary into a list and return list"""
    global all_words
    with open(DICTIONARY, mode = 'rt') as f:
        all_words = f.read().splitlines()
    return all_words

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""

    word = word.upper()

    try:
        return word_values[word]
    except KeyError:
        value = 0
        for letter in word:
            value += LETTER_SCORES.get(letter, 0)
        word_values[word] = value

        return value

def max_word_value(words = None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""

    if words is None:
        words = all_words

    values = [calc_word_value(w) for w in words]
    index, _ = max(enumerate(values), key=itemgetter(1))
    return words[index]

if __name__ == "__main__":
    pass # run unittests to validate
