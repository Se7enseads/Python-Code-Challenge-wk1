import unittest
from challenge_3 import solve


class TestSolve(unittest.TestCase):
    def test_max_consonant_value(self):
        result = solve("zoxvyp")
        # The maximum consonant value for "zoxvyp" is 226.
        self.assertEqual(result, 87)

    def test_empty_string(self):
        result = solve("")
        self.assertEqual(result, 0)  # An empty string should return 0.

    def test_no_consonants(self):
        result = solve("aeiou")
        # A string containing only vowels should return 0.
        self.assertEqual(result, 0)

    def test_single_consonant(self):
        result = solve("b")
        self.assertEqual(result, 2)  # The consonant value of 'b' is 2.

    # Add more test cases as needed


if __name__ == '__main__':
    unittest.main()
