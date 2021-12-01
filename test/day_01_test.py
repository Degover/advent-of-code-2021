import unittest
from challenges.day_01 import *

raw_test_input = '''199
200
208
210
200
207
240
269
260
263'''

class Day_01_Common_Tests(unittest.TestCase):

    def test_ParseRawInput_ShouldParseCorrectly(self): 
        test_output = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
        index = 0
        for parsedInput in parse_raw_input(raw_test_input):
            self.assertEqual(parsedInput, test_output[index])
            index += 1

class Day_01_Part1_Tests(unittest.TestCase):

    def test_RunSolution_ShouldResolve(self):
        result = day_01_part_1_solution(raw_test_input)
        self.assertEqual(result, 7)

class Day_01_Part2_Tests(unittest.TestCase):

    def test_AccumulateDepths_ShouldBeCorrect(self):
        test_output = [607, 618, 618, 617, 647, 716, 769, 792]
        index = 0
        for parsedInput in accumulate_depth(raw_test_input):
            self.assertEqual(parsedInput, test_output[index])
            index += 1

    def test_RunSolution_ShouldResolve(self):
        result = day_01_part_2_solution(raw_test_input)
        self.assertEqual(result, 5)


