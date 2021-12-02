import unittest
from challenges.day_02 import *

raw_test_input = '''forward 5
down 5
forward 8
up 3
down 8
forward 2'''

class Day_02_Tests(unittest.TestCase):

    def test_ReadCommand_WithNormalSubmarine_ShouldBeCorrect(self):
        commands = [
            ('f', 5),
            ('d', 5),
            ('f', 8),
            ('u', 3),
            ('d', 8),
            ('f', 2)
        ]
        submarine = Submarine()
        for [char_command, quantity] in commands:
            submarine.read_command(char_command, quantity)
        
        self.assertEqual(submarine.horizontal_pos, 15)
        self.assertEqual(submarine.depth, 10)

    def test_ParseRawInput_WithNormalSubmarine_ShouldBeCorrect(self):
        
        submarine = Submarine()
        submarine.parse_raw_input(raw_test_input)

        self.assertEqual(submarine.horizontal_pos, 15)
        self.assertEqual(submarine.depth, 10)

    def test_ReadCommand_WithAimedSubmarine_ShouldBeCorrect(self):
        commands = [
            ('f', 5),
            ('d', 5),
            ('f', 8),
            ('u', 3),
            ('d', 8),
            ('f', 2)
        ]
        submarine = AimedSubmarine()
        for [char_command, quantity] in commands:
            submarine.read_command(char_command, quantity)
        
        self.assertEqual(submarine.horizontal_pos, 15)
        self.assertEqual(submarine.depth, 60)

    def test_ParseRawInput_WithAimedSubmarine_ShouldBeCorrect(self):
        
        submarine = AimedSubmarine()
        submarine.parse_raw_input(raw_test_input)

        self.assertEqual(submarine.horizontal_pos, 15)
        self.assertEqual(submarine.depth, 60)

    def test_RunSolution_WithPart1_ShouldSolve(self):
        result = part1_solution(raw_test_input)
        self.assertEqual(result, 150)

    def test_RunSolution_WithPart2_ShouldSolve(self):
        result = part2_solution(raw_test_input)
        self.assertEqual(result, 900)
