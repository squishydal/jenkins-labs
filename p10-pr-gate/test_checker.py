import unittest

from checker import initials, slugify


class SlugifyTests(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(slugify("Hello Jenkins World"), "hello-jenkins-world")

    def test_trims_and_pads(self):
        self.assertEqual(slugify("  padded  text "), "padded-text")

    def test_empty(self):
        self.assertEqual(slugify(""), "")


class InitialsTests(unittest.TestCase):
    def test_two_words(self):
        self.assertEqual(initials("Ada Byron"), "A.B.")

    def test_three_words(self):
        self.assertEqual(initials("Grace Brewster Hopper"), "G.B.H.")

    def test_empty(self):
        self.assertEqual(initials(""), "")


if __name__ == "__main__":
    unittest.main()
