import unittest

from string_operations import *

class TestStringMethods(unittest.TestCase):

    ##Create a simple String calculator with a method signature like this:
    def test_string_caluclator(self):
        self.assertEqual(string_addition("10,9"), 19)
