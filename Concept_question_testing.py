import unittest
from Concept_questions import is_isogram

class IsIsogramTestCase(unittest.TestCase):
##Tester Comment
    def test_case_insensitive(self):
        # The function should be case-insensitive, so the result should be the same regardless of letter casing
        self.assertTrue(is_isogram('IsOgRaM'))
        self.assertFalse(is_isogram('HeLLo'))

    def test_numbers_and_symbols(self):
        # The function should treat numbers and symbols as separate characters and consider them for determining isogram status
        self.assertTrue(is_isogram('12345'))
        self.assertFalse(is_isogram('12 34 5'))

if __name__ == '__main__':
    unittest.main()
