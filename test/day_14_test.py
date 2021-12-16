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

    def testPolymerator_CountLetter_WithUnexistingLetter_ShouldInsertIt(self):
        polymerator = Polymerator()

        polymerator.count_letter('A')

        expected_count = { 'A': 1 }
        self.assertDictEqual(polymerator.letter_counts, expected_count)

    def testPolymerator_CountLetter_WithExistingLetter_ShouldIncrementIt(self):
        polymerator = Polymerator()
        polymerator.letter_counts = { 'A': 3 }

        polymerator.count_letter('A')

        expected_count = { 'A': 4 }
        self.assertDictEqual(polymerator.letter_counts, expected_count)

    def testPolymerator_StepInto_WithSingleStep_ShouldCountCorrectly(self):
        polymerator = Polymerator()
        polymerator.rules = { ('N', 'N'): 'B' }

        polymerator.step_into('N', 'N', 1)

        expected_count = { 'B': 1 }
        self.assertDictEqual(polymerator.letter_counts, expected_count)

    def testPolymerator_StepInto_WithThreeSteps_ShouldCountCorrectly(self):
        polymerator = Polymerator()
        polymerator.rules = {
            ('N', 'N'): 'B',
            ('N', 'B'): 'B',
            ('B', 'N'): 'B',
            ('B', 'B'): 'N'
        }

        polymerator.step_into('N', 'N', 3)

        expected_count = { 'N': 2, 'B': 5 }
        self.assertDictEqual(polymerator.letter_counts, expected_count)

    def testPolymerator_StepInto_WithExampleInput_ShouldCountCorrectly(self):
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
        
        polymerator.step_into('N', 'N', 4)

        expected_count = { 'N': 4, 'B': 6, 'C': 5 }
        self.assertDictEqual(polymerator.letter_counts, expected_count)

    def testPolymerator_StepInto_WithMemorizedIter_ShouldCountCorrectly(self):
        polymerator = Polymerator()
        polymerator.memorized_iters = { ('A', 'A', 3): { 'B': 2, 'A': 1 } }
        polymerator.rules = { ('A', 'A'): 'B' }

        polymerator.step_into('A', 'A', 3)

        expected_counter = { 'B': 3, 'A': 1 }
        self.assertDictEqual(polymerator.letter_counts, expected_counter)

    def testPolymerator_StepInto_WithIterToMemorize_ShouldCountCorrectly(self):
        polymerator = Polymerator()
        polymerator.rules = {
            ('A', 'A'): 'B',
            ('B', 'A'): 'B',
            ('A', 'B'): 'B',
            ('B', 'B'): 'B'
        }

        polymerator.step_into('A', 'A', 4)

        expected_counter = { 'B': 15 }
        self.assertDictEqual(polymerator.letter_counts, expected_counter)

    def testPolymerator_CountBySteps_WithSingleStep_ShouldCountCorrectly(self):
        polymerator = Polymerator()
        polymerator.rules = { ('N', 'N'): 'B' }
        polymerator.template = ['N', 'N']

        output = polymerator.count_by_steps(1)

        expected_output = { 'N': 2, 'B': 1 }
        self.assertDictEqual(output, expected_output)

    def testPolymerator_CountBySteps_WithThreeSteps_ShouldCountCorrectly(self):
        polymerator = Polymerator()
        polymerator.rules = {
            ('N', 'N'): 'B',
            ('N', 'B'): 'B',
            ('B', 'N'): 'B',
            ('B', 'B'): 'N'
        }
        polymerator.template = ['N', 'N']

        output = polymerator.count_by_steps(3)

        expected_output = { 'N': 4, 'B': 5 }
        self.assertDictEqual(output, expected_output)

    def testPolymerator_CountBySteps_WithExampleInput_ShouldCountCorrectly(self):
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

        output = polymerator.count_by_steps(4)

        expected_output = {'N': 11, 'B': 23, 'C': 10, 'H': 5}
        self.assertDictEqual(output, expected_output)

    def testPolymerator_MemorizeIter_WithEmptyOldCount_ShouldMemorizeCorrectly(self):
        new_counts = { 'A': 2, 'B': 3 }

        polymerator = Polymerator()
        polymerator.memorize_iter('A', 'A', 5, {}, new_counts)

        expected_memorized = { ('A', 'A', 5): new_counts }
        self.assertDictEqual(polymerator.memorized_iters, expected_memorized)

    def testPolymerator_MemorizeIter_WithFilledOldCount_ShouldMemorizeCorrectly(self):
        new_counts = { 'A': 2, 'B': 3 }

        polymerator = Polymerator()
        polymerator.memorize_iter('A', 'A', 5, { 'A': 1 }, new_counts)

        expected_memorized = { ('A', 'A', 5): { 'A': 1, 'B': 3 } }
        self.assertDictEqual(polymerator.memorized_iters, expected_memorized)

    def testPolymerator_SumCounter_WithEmptyOldCount_ShouldSumCorrectly(self):
        new_counts = { 'A': 2, 'B': 3 }

        polymerator = Polymerator()
        polymerator.sum_counter(new_counts)

        self.assertDictEqual(polymerator.letter_counts, new_counts)

    def testPolymerator_SumCounter_WithFilledOldCount_ShouldSumCorrectly(self):
        polymerator = Polymerator()
        polymerator.letter_counts = { 'A': 1 }

        polymerator.sum_counter({ 'A': 2, 'B': 3 })

        expected_count = { 'A': 3, 'B': 3 }
        self.assertDictEqual(polymerator.letter_counts, expected_count)

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
