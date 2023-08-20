import unittest
from unittest.mock import patch
from challenge_1 import convert_time_system


class TestConvertTimeSystem(unittest.TestCase):
    def test_am_times(self):
        am_times = [
            (1, 0, "am", "0100 hours"),
            (9, 15, "am", "0915 hours"),
            (11, 30, "am", "1130 hours"),
        ]

        with patch("builtins.print") as mock_print:
            for hour, minute, period, expected_output in am_times:
                convert_time_system(hour, minute, period)
                mock_print.assert_called_with(expected_output)

    def test_pm_times(self):
        pm_times = [
            (1, 0, "pm", "1300 hours"),
            (9, 15, "pm", "2115 hours"),
            (11, 30, "pm", "2330 hours"),
            (12, 00, "pm", "1200 hours")
        ]

        with patch("builtins.print") as mock_print:
            for hour, minute, period, expected_output in pm_times:
                convert_time_system(hour, minute, period)
                mock_print.assert_called_with(expected_output)

    def test_invalid_hour(self):
        hours = [
            (15, 30, "am", "Invalid Hour or Minute"),
            (90, 20, "pm", "Invalid Hour or Minute"),
            (0, 15, "am", "Invalid Hour or Minute"),
            (-1, 45, "pm", "Invalid Hour or Minute")

        ]
        with patch("builtins.print") as mock_print:
            for hour, minute, period, expected_output in hours:
                convert_time_system(hour, minute, period)
                mock_print.assert_called_with(expected_output)

    def test_invalid_minute(self):
        with patch("builtins.print") as mock_print:
            convert_time_system(9, 61, "pm")
            mock_print.assert_called_with("Invalid Hour or Minute")

    def test_invalid_period(self):
        with patch("builtins.print") as mock_print:
            convert_time_system(6, 30, "abc")
            mock_print.assert_called_with("Invalid period")

    def test_invalid_input_type(self):
        with patch("builtins.print") as mock_print:
            convert_time_system("10", 30, "am")
            mock_print.assert_called_with("Hour or Minute should be numbers")

    def test_invalid_period_type(self):
        with patch("builtins.print") as mock_print:
            convert_time_system(6, 30, 123)
            mock_print.assert_called_with(
                "Period should be a string of either am or pm")


if __name__ == '__main__':
    unittest.main()
