import unittest
from challenges.day_14 import *
from test.file_stub import FileStub

test_input = [
    'NNCB',
    '',
    'CH -> B',
    'HH -> N',
    'CB -> H',
    'NH -> C',
    'HB -> C',
    'HC -> B',
    'HN -> C',
    'NN -> C',
    'BH -> H',
    'NC -> B',
    'NB -> B',
    'BN -> B',
    'BB -> N',
    'BC -> B',
    'CC -> N',
    'CN -> C'
]

class Day_14_Tests(unittest.TestCase):
    
    def testPolymerator_ReadFileInput_WithSimpleInput_ShouldBeCorrect(self):
        file_stub = FileStub()
        file_stub.set_array(['NNCB',
            '',
            'CH -> B',
            'HH -> N',
            'CB -> H'
        ])
        polymerator = Polymerator()

        polymerator.read_file_input(file_stub)

        expected_template = ['N', 'N', 'C', 'B']
        self.assertListEqual(polymerator.template, expected_template)

        expected_rules = {
            ('C', 'H'): 'B',
            ('H', 'H'): 'N',
            ('C', 'B'): 'H'
        }
        self.assertDictEqual(polymerator.rules, expected_rules)

    def testPolymerator_StepPair_WithSingleStep_ShouldReturnCorrectly(self):
        polymerator = Polymerator()
        polymerator.rules = { ('N', 'N'): 'B' }

        output = polymerator.step_pair('N', 'N', 1)

        expected_output = ['B']
        self.assertListEqual(output, expected_output)

    def testPolymerator_StepPair_WithThreeSteps_ShouldReturnCorrectly(self):
        polymerator = Polymerator()
        polymerator.rules = {
            ('N', 'N'): 'B',
            ('N', 'B'): 'B',
            ('B', 'N'): 'B',
            ('B', 'B'): 'N'
        }

        output = polymerator.test('N', 'N', 3)

        expected_output = ['N', 'B', 'B', 'N', 'B', 'N', 'B', 'B', 'N']
        self.assertListEqual(output, expected_output)

    def testPart1_RunSolution_WithExampleInput_ShouldBeCorrect(self):
        file_stub = FileStub()
        file_stub.set_array(test_input)

        output = part1_solution(file_stub)

        expected_output = 1588
        self.assertEqual(output, expected_output)

    def testPart2_RunSolution_WithExampleInput_ShouldBeCorrect(self):
        file_stub = FileStub()
        file_stub.set_array(test_input)

        output = part2_solution(file_stub)

        expected_output = -1
        self.assertEqual(output, expected_output)


