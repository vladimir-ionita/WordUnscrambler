import unittest
from utilities import *


class UtilitiesTests(unittest.TestCase):
    def test_is_number(self):
        self.assertTrue(is_number('4'))
        self.assertFalse(is_number('__r'))


if __name__ == '__main__':
    unittest.main()
