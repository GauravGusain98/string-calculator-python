import unittest
from string_calculator.calculator import add

class TestStringCalculator(unittest.TestCase):

    def test_empty_string_returns_zero(self):
        self.assertEqual(add(""), 0)

    def test_single_number(self):
        self.assertEqual(add("1"), 1)

    def test_two_numbers(self):
        self.assertEqual(add("1,2"), 3)
 
    def test_multiple_numbers_with_whitespaces(self):
        self.assertEqual(add(" 1,2, 6, 7 "), 16)

    def test_newline_between_numbers(self):
        self.assertEqual(add("1\n2,3"), 6)
        
if __name__ == "__main__":
    unittest.main()