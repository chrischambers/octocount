from word_count import word_count


def describe_word_count():
    def returns_count_of_word_occurrences_in_string():
        outcome = word_count("one two two three three three")
        expected = {'one': 1, 'two': 2, 'three': 3}
        assert outcome == expected

    def ignores_symbols():
        pass

    def is_case_insensitive():
        pass

    def does_not_count_stop_words():
        pass
