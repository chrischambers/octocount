from word_count import word_count


def describe_word_count():
    def returns_count_of_word_occurrences_in_string():
        outcome = word_count("one two two three three three")
        expected = {'one': 1, 'two': 2, 'three': 3}
        assert outcome == expected

    def ignores_symbols():
        outcome = word_count("one, two. two? - (three) three three!!!")
        expected = {'one': 1, 'two': 2, 'three': 3}
        assert outcome == expected

    def is_case_insensitive():
        outcome = word_count("one TWO Two FoUr foUR fOur FouR")
        expected = {'one': 1, 'two': 2, 'four': 4}
        assert outcome == expected

    def does_not_count_stop_words():
        outcome = word_count("To be or not to be.")
        expected = {}
        assert outcome == expected
