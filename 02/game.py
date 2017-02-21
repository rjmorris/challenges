#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

import random
import itertools


from data import DICTIONARY, LETTER_SCORES, POUCH

NUM_LETTERS = 7


# re-use from challenge 01
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


# re-use from challenge 01
def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)


def is_response_from_draw(response, draw):
    remaining = list(draw)
    for letter in response:
        if letter not in remaining:
            return False
        remaining.remove(letter)
    return True
    
def main():
    draw = random.sample(POUCH, NUM_LETTERS)
    draw = [d.upper() for d in draw]

    print('You have drawn the letters: {}'.format(' '.join(draw)))

    score = None
    while True:
        response = input('Enter a Scrabble word using your letters: ')

        if is_response_from_draw(response.upper(), draw):
            if response.lower() in DICTIONARY:
                score = calc_word_value(response)
                print('You scored {} points for the word {}.'.format(score, response.upper()))
                break
            else:
                print('Sorry, {} isn\'t in the Scrabble dictionary.'.format(response.upper()))
        else:
            print('Sorry, {} can\'t be formed from {}.'.format(response.upper(), ' '.join(draw)))

    letters = ''.join([d.lower() for d in draw])
    valid_words = []
    for word_len in range(2, NUM_LETTERS + 1):
        valid_words += [''.join(w) for w in itertools.permutations(letters, word_len)
                        if ''.join(w) in DICTIONARY]

    max_word = max_word_value(valid_words)
    max_value = calc_word_value(max_word)

    if max_value == score:
        print('Congratulations, you have scored the most possible points!')
    else:
        print('You could have scored {} points with the word {}.'.format(max_value, max_word.upper()))


if __name__ == "__main__":
    main()
