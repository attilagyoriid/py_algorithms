from unittest import TestCase

from algorithms.anagram import Anagram


class TestAnagram(TestCase):
    def test_anagram(self):
        self.assertTrue(Anagram.anagram("asd ASDA dsg", "dsgasd ASDA "))

    def test_anagram_fail(self):
        self.assertFalse(Anagram.anagram("asd ASDA dsg", "dsga"))
