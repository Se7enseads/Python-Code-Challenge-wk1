import unittest
from unittest.mock import patch
from challenge_2 import check_positive_integers


class TestCheckPositiveIntegers(unittest.TestCase):
    def test_positive_numbers(self):
        with patch("builtins.print") as mock_print:
            check_positive_integers(2, 3, 4)
            mock_print.assert_called_with(True)

    def test_one_positive_number(self):
        with patch("builtins.print") as mock_print:
            check_positive_integers(-2, 3, 0)
            mock_print.assert_called_with(False)

    def test_no_positive_numbers(self):
        with patch("builtins.print") as mock_print:
            check_positive_integers(-2, -3, -4)
            mock_print.assert_called_with(False)

    def test_invalid_input(self):
        with patch("builtins.print") as mock_print:
            check_positive_integers(2.5, 3, 4)
            mock_print.assert_called_with("a, b, or c should be integers")

    def test_mixed_input(self):
        with patch("builtins.print") as mock_print:
            check_positive_integers(2, -3, "4")
            mock_print.assert_called_with("a, b, or c should be integers")


if __name__ == '__main__':
    unittest.main()
