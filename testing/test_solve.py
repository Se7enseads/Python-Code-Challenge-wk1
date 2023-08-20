import unittest
from challenge_3 import solve


class TestSolve(unittest.TestCase):
    def test_max_consonant_value(self):
        string = [
            ("vwxyz", 120),
            ("zoxvyp", 87)
        ]
        for string, expected_output in string:
            result = solve(string)
            self.assertEqual(result, expected_output)

    def test_empty_string(self):
        result = solve("")
        self.assertEqual(result, 0)

    def test_no_consonants(self):
        result = solve("aeiou")
        self.assertEqual(result, 0)

    def test_single_consonant(self):
        string = [
            ("a", 0),
            ("b", 2),
            ("c", 3),
            ("d", 4)
        ]
        for string, expected_output in string:
            result = solve(string)
            self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()
