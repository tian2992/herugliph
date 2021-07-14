import math

class HeruLang:
    ALPHABET = list("sxocqnmwpfyheljrdgui")
    FOO_LETTERS = ["u", "d", "x", "s", "m", "p", "f"]
    BAR_LETTERS = list(set(ALPHABET) - set(FOO_LETTERS))  # List instead of set just for consistency.

    @staticmethod
    def is_preposition(self, word):
        return ((len(word) == 6) and
                (word[-1] in HeruLang.FOO_LETTERS) and
                ('u' not in word))

    @staticmethod
    def is_verb(self, word):
        return (len(word) >= 6) and (word[-1] in HeruLang.BAR_LETTERS)

    @staticmethod
    def is_subjunctive_verb(self, word):
        return self.is_verb(word) and word[0] in HeruLang.BAR_LETTERS

    @staticmethod
    def _herulang_sort(self, word):
        """Generates sorting key for words on herulang alphabet."""
        return [HeruLang.ALPHABET.index(l) for l in word]

    @staticmethod
    def as_number(self, word):
        """Parses numbers as vigesimal based on their position read from left to right."""
        index = 0
        digit_sum: int = 0
        for letter in word:
            digit_sum += HeruLang.ALPHABET.index(letter) * int(math.pow(20, index))
            index += 1
        return digit_sum

    @staticmethod
    def is_pretty(self, number):
        """Checks if number is classified as 'pretty'."""
        return number >= 81827 and number % 3 == 0

    def analyze(self, full_text):
        wordlist = full_text.split(" ")
        ## TODO: remove dupes
        sort_words = sorted(wordlist, key=self._herulang_sort)
        return
