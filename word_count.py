from collections import Counter
from string import punctuation

import nltk

nltk.download("stopwords")
unwanted = set(nltk.corpus.stopwords.words()) | {""}


def word_count(text):
    lines = [
        "".join([c for c in word if c not in punctuation]).lower()
        for word in text.split()
    ]
    lines = [word for word in lines if word not in unwanted]
    return Counter(lines)
