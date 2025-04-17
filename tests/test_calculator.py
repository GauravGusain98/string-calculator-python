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

    def test_custom_delimiter(self):
        self.assertEqual(add("//;\n1;2"), 3)

    def test_custom_delimiter_with_different_symbol(self):
        self.assertEqual(add("//|\n4|5|6"), 15)
        
    def test_negative_number_raises_exception(self):            
        with self.assertRaises(Exception) as context:
            add("1,-2,3")
        self.assertEqual(str(context.exception), "negative numbers not allowed -2")
    
    def test_multiple_negative_number_raises_exception(self):            
        with self.assertRaises(Exception) as context:
            add("1,-2,-4,3,-8")
        self.assertEqual(str(context.exception), "negative numbers not allowed -2,-4,-8")
    
    def test_invalid_input(self):             
        self.assertEqual(add("1,nan, ,3,-8"), -1)
        
    def test_start_delimiter(self):
        self.assertEqual(add("//*\n1*2*4"), 7)

if __name__ == "__main__":
    unittest.main()