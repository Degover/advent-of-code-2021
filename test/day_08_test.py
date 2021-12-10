import unittest
from challenges.day_08 import *
from test.file_stub import FileStub

test_input = [
    'be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe',
    'edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc',
    'fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg',
    'fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb',
    'aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea',
    'fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb',
    'dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe',
    'bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef',
    'egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb',
    'gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce',
]

class Day_08_Tests(unittest.TestCase):

    def testDigitChecker_GetOutput_WithExampleInput_ShouldBeCorrect(self):
        checker = DigitChecker()
        checker.digit_map = {
            (1, 1, 1, 1, 1, 0, 1): '0',
            (1, 1, 0, 0, 0, 0, 0): '1',
            (1, 0, 1, 1, 0, 1, 1): '2',
            (1, 1, 1, 1, 0, 1, 0): '3',
            (1, 1, 0, 0, 1, 1, 0): '4',
            (0, 1, 1, 1, 1, 1, 0): '5',
            (0, 1, 1, 1, 1, 1, 1): '6',
            (1, 1, 0, 1, 0, 0, 0): '7',
            (1, 1, 1, 1, 1, 1, 1): '8',
            (1, 1, 1, 1, 1, 1, 0): '9'
        }

        output = checker.get_output(['cdfeb', 'fcadb', 'cdfeb', 'cdbaf'])

        expected_output = 5353
        self.assertEqual(output, expected_output)

    def testDigitChecker_MapDigits_WithExampleInput_ShouldMapCorrectly(self):
        input = ['acedgfb', 'cdfbe', 'gcdfa', 'fbcad', 'dab', 'cefabd', 'cdfgeb', 'eafb', 'cagedb', 'ab']
        checker = DigitChecker()
        checker.map_digits(input)

        expected_output = {
            (1, 1, 1, 1, 1, 0, 1): '0',
            (1, 1, 0, 0, 0, 0, 0): '1',
            (1, 0, 1, 1, 0, 1, 1): '2',
            (1, 1, 1, 1, 0, 1, 0): '3',
            (1, 1, 0, 0, 1, 1, 0): '4',
            (0, 1, 1, 1, 1, 1, 0): '5',
            (0, 1, 1, 1, 1, 1, 1): '6',
            (1, 1, 0, 1, 0, 0, 0): '7',
            (1, 1, 1, 1, 1, 1, 1): '8',
            (1, 1, 1, 1, 1, 1, 0): '9'
        }
        self.assertDictEqual(checker.digit_map, expected_output)

    def testDigitChecker_MapToIntTuple_WithSingleCharInput_ShouldBeCorrect(self):
        test_cases = [
            ('a', (1, 0, 0, 0, 0, 0, 0)),
            ('b', (0, 1, 0, 0, 0, 0, 0)),
            ('c', (0, 0, 1, 0, 0, 0, 0)),
            ('d', (0, 0, 0, 1, 0, 0, 0)),
            ('e', (0, 0, 0, 0, 1, 0, 0)),
            ('f', (0, 0, 0, 0, 0, 1, 0)),
            ('g', (0, 0, 0, 0, 0, 0, 1))
        ]

        checker = DigitChecker()
        for input, expected_output in test_cases:
            output = checker.map_to_int_tuple(input)
            self.assertEqual(output, expected_output)

    def testDigitChecker_MapToIntTuple_WithComplexCharInput_ShouldBeCorrect(self):
        test_cases = [
            ('acedgfb', (1, 1, 1, 1, 1, 1, 1)),
            ('ab', (1, 1, 0, 0, 0, 0, 0)),
            ('dab', (1, 1, 0, 1, 0, 0, 0)),
            ('fcadb', (1, 1, 1, 1, 0, 1, 0)),
            ('cdbaf', (1, 1, 1, 1, 0, 1, 0))
        ]

        checker = DigitChecker()
        for input, expected_output in test_cases:
            output = checker.map_to_int_tuple(input)
            self.assertEqual(output, expected_output)

    def testDigitChecker_ReadLine_WithExampleInputs_ShouldBeCorrect(self):
        test_cases = [
            ('be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe', 8394),
            ('edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc', 9781),
            ('fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg', 1197),
            ('fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb', 9361),
            ('aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea', 4873),
            ('fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb', 8418),
            ('dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe', 4548),
            ('bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef', 1625),
            ('egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb', 8717),
            ('gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce', 4315)
        ]
        checker = DigitChecker()
        for input, expected_output in test_cases:
            output = checker.read_line(input)
            self.assertEqual(output, expected_output)

    def testPart1_RunSolution_WithExampleInput_ShouldBeCorrect(self):
        file_stub = FileStub()
        file_stub.set_array(test_input)

        output = part1_solution(file_stub)

        expected_output = 26
        self.assertEqual(output, expected_output)

    def testPart2_RunSolution_WithExampleInput_ShouldBeCorrect(self):
        file_stub = FileStub()
        file_stub.set_array(test_input)

        output = part2_solution(file_stub)

        expected_output = 61229
        self.assertEqual(output, expected_output)


