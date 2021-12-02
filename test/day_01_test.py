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

class Day_01_Tests(unittest.TestCase):

    def test_ParseRawInput_WithNormalParser_ShouldParseCorrectly(self): 
        test_output = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
        index = 0
        parser = InputParser(raw_test_input)
        for parsedInput in parser.parse():
            self.assertEqual(parsedInput, test_output[index])
            index += 1

    def test_ParseRawInput_WithCumulativeParser_ShouldBeCorrect(self):
        test_output = [607, 618, 618, 617, 647, 716, 769, 792]
        index = 0
        parser = InputParser(raw_test_input)
        for parsedInput in parser.accumulate_parse():
            self.assertEqual(parsedInput, test_output[index])
            index += 1

    def test_RunSolution_WithPart1_ShouldResolve(self):
        result = part1_solution(raw_test_input)
        self.assertEqual(result, 7)

    def test_RunSolution_WithPart2_ShouldResolve(self):
        result = part2_solution(raw_test_input)
        self.assertEqual(result, 5)


