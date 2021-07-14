import math
from collections import Counter


class HeruLang:
    ALPHABET = list("sxocqnmwpfyheljrdgui")  # The order of the alphabet letters is important.
    FOO_LETTERS = ["u", "d", "x", "s", "m", "p", "f"]
    BAR_LETTERS = list(set(ALPHABET) - set(FOO_LETTERS))  # List instead of set for consistency.

    def __init__(self):
        pass

    @staticmethod
    def is_preposition(word):
        return ((len(word) == 6) and
                (word[-1] in HeruLang.FOO_LETTERS) and
                ('u' not in word))

    @staticmethod
    def is_verb(word):
        return len(word) >= 6 and word[-1] in HeruLang.BAR_LETTERS

    @staticmethod
    def is_subjunctive_verb(word):
        return HeruLang.is_verb(word) and word[0] in HeruLang.BAR_LETTERS

    @staticmethod
    def _herulang_sort(word):
        """Generates sorting key for words on herulang alphabet."""
        return [HeruLang.ALPHABET.index(l) for l in word]

    @staticmethod
    def as_number(word):
        """Parses numbers as vigesimal based on their position read from left to right."""
        index = 0
        digit_sum: int = 0
        for letter in word:
            digit_sum += HeruLang.ALPHABET.index(letter) * int(math.pow(20, index))
            index += 1
        return digit_sum

    @staticmethod
    def is_pretty(number):
        """Checks if number is classified as 'pretty'."""
        return number >= 81827 and number % 3 == 0

    def analyze(self, full_text):
        full_wordlist = full_text.split()
        if len(full_wordlist) < 1:
            # Empty wordlist
            return {}
        recounted = Counter(full_wordlist)
        wordlist = list(recounted.keys())
        sort_words = sorted(wordlist, key=self._herulang_sort)
        count_verbs, count_prep, count_subj, count_pretty = 0, 0, 0, 0
        for word in sort_words:
            if self.is_preposition(word):
                count_prep += 1
            if self.is_verb(word):
                count_verbs += 1
            if self.is_subjunctive_verb(word):
                count_subj += 1
            if self.is_pretty(self.as_number(word)):
                count_pretty += 1

        return {
            "sorted_words": sort_words,
            "verbs": count_verbs,
            "pretty_numbers": count_pretty,
            "subjunctive_verbs": count_subj,
            "prepositions": count_prep
        }
