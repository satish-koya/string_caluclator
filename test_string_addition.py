import unittest

from string_operations import *

class TestStringMethods(unittest.TestCase):

    ##Create a simple String calculator with a method signature like this:
    def test_string_caluclator(self):
        self.assertEqual(string_addition("10,9"), 19)


    ##Allow the add method to handle any amount of numbers.:
    def test_string_caluclator_multi(self):
        self.assertEqual(string_addition("10,9,20,30,40,50"), 159)


    #Allow the add method to handle new lines between numbers (instead of commas). ("1\n2,3" should return 6)
    def test_string_caluclator_witn_newline(self):
        self.assertEqual(string_addition("10,20,30,40\n50"), 150)

    #Support different delimiters
    def test_string_caluclator_witn_diff_delimiter(self):
       " //[delimiter]\n[numbers…]"
       self.assertEqual(string_addition("//;\n10;20;30;40;50"), 150)
       self.assertEqual(string_addition("//.\n10.20.30.40.50"), 150)

    # Calling add with a negative number will throw an exception
    def test_negative_number(self):
        with self.assertRaises(NegativeNumberException) as context:
            string_addition("10,-9")
        self.assertEqual(str(context.exception), "negative numbers not allowed: -9")