from utils import normalize


def word_cloud(word_count, minimum_font_size=1, maximum_font_size=8):
    """
    A presenter for a word count object: extracts the 100 most frequent word
    counts, sorted by frequency, and normalizes their scores between the
    minimum and maximum font sizes.
    """
    items = sorted(word_count.items(), key=lambda p: p[1], reverse=True)[:100]
    keys, values = zip(*items)
    return zip(keys, normalize(minimum_font_size, maximum_font_size, values))
