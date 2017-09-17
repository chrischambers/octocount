from collections import Counter
from string import digits, punctuation

import nltk

nltk.download("stopwords")
unwanted = set(nltk.corpus.stopwords.words()) | {""}


def desirable_word(word):
    """
    True if the word does not contain numbers, is a non-empty string, and is
    not a stop-word.
    """
    return (word not in unwanted) and not [c for c in word if c in digits]


def word_count(iterable):
    if isinstance(iterable, str):
        iterable = iterable.split()
    lines = (word.strip(punctuation).lower() for word in iterable)
    lines = (word for word in lines if desirable_word(word))
    return Counter(lines)
