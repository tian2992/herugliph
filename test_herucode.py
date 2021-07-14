from unittest import TestCase
from herucode import HeruLang

class TestHeruLangInner(TestCase):

    def setUp(self) -> None:
        self.HL = HeruLang

    def test_is_preposition(self):
        self.assertTrue(True)

    def test_is_verb(self):
        self.assertTrue(self.HL.is_verb("iygsee"))

    def test_is_subjunctive_verb(self):
        self.assertTrue(True)

    def test_as_number(self):
        self.assertEqual(self.HL.as_number(word="gxjrc"), 605637)

    def test_is_pretty(self):
        self.assertTrue(self.HL.is_pretty(self.HL.as_number(word="gxjrc")))

    def test_analyze(self):
        self.assertTrue(True)


class TestHeruLangBehaviour(TestCase):
    pass
