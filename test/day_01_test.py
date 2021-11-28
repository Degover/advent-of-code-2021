import unittest
from challenges.day_01 import increment

class Test_TestIncrementDecrement(unittest.TestCase):
    def test_increment(self):
        self.assertEqual(4, 4)

    def test_decrement(self):
        self.assertEqual(increment(3), 4)