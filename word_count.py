from collections import Counter
from string import punctuation


def filter_unwanted(wordlist):
    return [word for word in wordlist if word != ""]


def word_count(text):
    lines = [
        "".join([c for c in word if c not in punctuation]).lower()
        for word in text.split()
    ]
    return Counter(filter_unwanted(lines))
