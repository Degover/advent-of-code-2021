import unittest
from challenges.day_02 import *

raw_test_input = '''forward 5
down 5
forward 8
up 3
down 8
forward 2'''

class Day02_Common_Tests(unittest.TestCase):

    def test_ReadCommand_WithoutAim_ShouldBeCorrect(self):
        commands = [
            ('f', 5),
            ('d', 5),
            ('f', 8),
            ('u', 3),
            ('d', 8),
            ('f', 2)
        ]
        submarine = SubmarineCommandReader()
        for [char_command, quantity] in commands:
            submarine.read_command(char_command, quantity)
        
        self.assertEqual(submarine.horizontal_pos, 15)
        self.assertEqual(submarine.depth, 10)

    def test_ParseRawInput_WithoutAim_ShouldBeCorrect(self):
        
        submarine = SubmarineCommandReader()
        submarine.parse_raw_input(raw_test_input)

        self.assertEqual(submarine.horizontal_pos, 15)
        self.assertEqual(submarine.depth, 10)

    def test_ReadCommand_WithAim_ShouldBeCorrect(self):
        commands = [
            ('f', 5),
            ('d', 5),
            ('f', 8),
            ('u', 3),
            ('d', 8),
            ('f', 2)
        ]
        submarine = SubmarineCommandReaderWithAim()
        for [char_command, quantity] in commands:
            submarine.read_command(char_command, quantity)
        
        self.assertEqual(submarine.horizontal_pos, 15)
        self.assertEqual(submarine.depth, 60)

    def test_ParseRawInput_WithAim_ShouldBeCorrect(self):
        
        submarine = SubmarineCommandReaderWithAim()
        submarine.parse_raw_input(raw_test_input)

        self.assertEqual(submarine.horizontal_pos, 15)
        self.assertEqual(submarine.depth, 60)

class Day02_Part1_Tests(unittest.TestCase):

    def test_RunSolution_ShouldSolve(self):
        result = part1_solution(raw_test_input)
        self.assertEqual(result, 150)

class Day02_Part2_Tests(unittest.TestCase):

    def test_RunSolution_ShouldSolve(self):
        result = part2_solution(raw_test_input)
        self.assertEqual(result, 900)
