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

    def testPolymerator_DoSteps_WithSingleStep_ShouldReturnCorrectly(self):
        polymerator = Polymerator()
        polymerator.rules = { ('N', 'N'): 'B' }
        polymerator.template = ['N', 'N']

        output = polymerator.do_steps(1)

        expected_output = ['N', 'B', 'N']
        self.assertListEqual(output, expected_output)

    def testPolymerator_DoSteps_WithThreeSteps_ShouldReturnCorrectly(self):
        polymerator = Polymerator()
        polymerator.rules = {
            ('N', 'N'): 'B',
            ('N', 'B'): 'B',
            ('B', 'N'): 'B',
            ('B', 'B'): 'N'
        }
        polymerator.template = ['N', 'N']

        output = polymerator.do_steps(3)

        expected_output = ['N', 'B', 'B', 'N', 'B', 'N', 'B', 'B', 'N']
        self.assertListEqual(output, expected_output)

    def testPolymerator_DoSteps_WithExampleInput_ShouldReturnCorrectly(self):
        polymerator = Polymerator()
        polymerator.rules = {
            ('C', 'H'): 'B',
            ('H', 'H'): 'N',
            ('C', 'B'): 'H',
            ('N', 'H'): 'C',
            ('H', 'B'): 'C',
            ('H', 'C'): 'B',
            ('H', 'N'): 'C',
            ('N', 'N'): 'C',
            ('B', 'H'): 'H',
            ('N', 'C'): 'B',
            ('N', 'B'): 'B',
            ('B', 'N'): 'B',
            ('B', 'B'): 'N',
            ('B', 'C'): 'B',
            ('C', 'C'): 'N',
            ('C', 'N'): 'C',
        }
        polymerator.template = ['N', 'N', 'C', 'B']

        output = polymerator.do_steps(4)

        expected_output = ['N', 'B', 'B', 'N', 'B', 'N', 'B', 'B', 'C', 'C', 'N', 'B', 'C', 'N', 'C', 'C', 'N', 'B',
            'B', 'N', 'B', 'B', 'N', 'B', 'B', 'B', 'N', 'B', 'B', 'N', 'B', 'B', 'C', 'B', 'H', 'C', 'B', 'H', 'H',
            'N', 'H', 'C', 'B', 'B', 'C', 'B', 'H', 'C', 'B']
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

        expected_output = 2188189693529
        self.assertEqual(output, expected_output)
