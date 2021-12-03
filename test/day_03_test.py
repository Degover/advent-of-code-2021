import unittest
from challenges.day_03 import * 

class Day_03_Tests(unittest.TestCase):

    def testBitCounter_IncrementCount_ShouldIncrement(self):
        counter = BitCounter()
        counter.increment_count(1, 1)
        result = list(counter.count_list)[1][1]
        self.assertEqual(result, 1)

    def testBitCounter_ReadInput_ShouldBeCorrect(self):
        input = '''111111000000
111111000000
111111000000'''
        expected_result = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]

        counter = BitCounter()
        counter.read_input(input)
        result = counter.get_most_common_bits()

        self.assertListEqual(result, expected_result)

    def testBitFilter_GetOxygenGeneratorRating_ShouldBeCorrect(self):
        expected_result = [ 1, 0, 1, 1, 1 ]
        input = '''00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010'''

        filter = BitFilter()
        filter.read_input(input)
        result = filter.get_oxygen_generator_rating()

        self.assertListEqual(result, expected_result)

    def testBitFilter_GetCo2ScrubberRating_ShouldBeCorrect(self):
        expected_result = [ 0, 1, 0, 1, 0 ]
        input = '''00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010'''

        filter = BitFilter()
        filter.read_input(input)
        result = filter.get_co2_scrubber_rating()

        self.assertListEqual(result, expected_result)

    def test_RunSolution_WithPart1_ShouldBeCorrect(self):
        input = '''111111000000
111111000000
111111000000'''
        expected_result = 254016
        
        result = part1_solution(input)
        self.assertEqual(result, expected_result)