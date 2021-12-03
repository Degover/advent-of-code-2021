import unittest
from challenges.day_03 import * 

class Day_03_Tests(unittest.TestCase):

    def testBitCounter_IncrementCount_ShouldIncrement(self):
        counter = BitCounter()
        counter.increment_count(1, 1)
        result = list(counter.count_list)[1][1]
        self.assertEqual(result, 1)

    def testBitCounter_ReadInput_ShouldBeCorrect(self):
        input = '''11110000
11110000
11110000'''
        expected_result = [1, 1, 1, 1, 0, 0, 0, 0]

        counter = BitCounter()
        counter.read_input(input)
        result = counter.get_most_common_bits()

        self.assertListEqual(result, expected_result)