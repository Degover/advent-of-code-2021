import unittest
from challenges.day_01 import increment

class AnotherTEsts(unittest.TestCase):
    def test_increment(self):
        self.assertEqual(4, 4)

    def test_decrement(self):
        self.assertEqual(increment(3), 4)