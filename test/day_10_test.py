import unittest
from challenges.day_10 import *
from test.file_stub import FileStub

test_input = [
    '[({(<(())[]>[[{[]{<()<>>',
    '[(()[<>])]({[<{<<[]>>(',
    '{([(<{}[<>[]}>{[]{[(<()>',
    '(((({<>}<{<{<>}{[]{[]{}',
    '[[<[([]))<([[{}[[()]]]',
    '[{[{({}]{}}([{[{{{}}([]',
    '{<[[]]>}<{[{[{[]{()[[[]',
    '[<(<(<(<{}))><([]([]()',
    '<{([([[(<>()){}]>(<<{{',
    '<{([{{}}[<[[[<>{}]]]>[]]'
]

class Day_10_Tests(unittest.TestCase):

    def testChunkChecker_CheckLine_WithCorruptedLines_ShouldReturnCorrectCorruptedChars(self):
        test_cases = [
            ('(]', ']'),
            ('{()()()>', '>'),
            ('(((()))}', '}'),
            ('<([]){()}[{}])', ')'),
            ('{([(<{}[<>[]}>{[]{[(<()>', '}'),
            ('[[<[([]))<([[{}[[()]]]', ')'),
            ('[{[{({}]{}}([{[{{{}}([]', ']'),
            ('[<(<(<(<{}))><([]([]()', ')'),
            ('<{([([[(<>()){}]>(<<{{', '>')
        ]

        checker = ChunkChecker()
        for input, expected_output in test_cases:
            output = checker.check_line(input)
            self.assertEqual(output['corrupted'], expected_output)

    def testChunkChecker_CheckLine_WithNonCorruptedLines_ShouldNotReturnCorruptedChars(self):
        test_cases = [
            '([])',
            '{()()()}',
            '<([{}])>',
            '[<>({}){}[([])<>]]',
            '(((((((((())))))))))',
            '[({(<(())[]>[[{[]{<()<>>',
            '<{([{{}}[<[[[<>{}]]]>[]]'
        ]

        checker = ChunkChecker()
        for input in test_cases:
            output = checker.check_line(input)
            self.assertEqual(output['corrupted'], '')

    def testChunkChecker_CheckLine_WithIncompleteLines_ShouldReturnCorrectCompletionStrings(self):
        test_cases = [
            ('[({(<(())[]>[[{[]{<()<>>', '}}]])})]'),
            ('[(()[<>])]({[<{<<[]>>(', ')}>]})'),
            ('(((({<>}<{<{<>}{[]{[]{}', '}}>}>))))'),
            ('{<[[]]>}<{[{[{[]{()[[[]', ']]}}]}]}>'),
            ('<{([{{}}[<[[[<>{}]]]>[]]', '])}>')
        ]

        checker = ChunkChecker()
        for input, expected_output in test_cases:
            output = checker.check_line(input)
            self.assertEqual(output['completion'], expected_output)

    def testChunkChecker_ReadFileInput_WithExampleinput_ShouldCountCorruptedCorrectly(self):
        file_stub = FileStub()
        file_stub.set_array(test_input)

        checker = ChunkChecker()
        checker.read_file_input(file_stub)

        expected_output = { ')': 2, ']': 1, '}': 1, '>': 1 }
        self.assertDictEqual(checker.corrupted_count, expected_output)

    def testChunkChecker_ReadFileInput_WithExampleinput_ShouldCalculateCompletionScoresCorrectly(self):
        file_stub = FileStub()
        file_stub.set_array(test_input)

        checker = ChunkChecker()
        checker.read_file_input(file_stub)

        expected_output = [288957, 5566, 1480781, 995444, 294]
        self.assertListEqual(checker.completion_scores, expected_output)

    def testChunkChecker_GetTotalCorruptedPoints_WithExampleinput_ShouldReturnCorrectTotal(self):
        checker = ChunkChecker()
        checker.corrupted_count = { ')': 2, ']': 1, '}': 1, '>': 1 }

        output = checker.get_total_corrupted_points()

        expected_output = 26397
        self.assertEqual(output, expected_output)

    def testChunkChecker_CalculateCompletionStrPoints_WithExamplInput_ShouldBeCorrect(self):
        test_cases = [
            ('}}]])})]', 288957),
            (')}>]})', 5566),
            ('}}>}>))))', 1480781),
            (']]}}]}]}>', 995444),
            ('])}>', 294)
        ]
        checker = ChunkChecker()
        for input, expected_output in test_cases:
            output = checker.calculate_completion_str_points(input)
            self.assertEqual(output, expected_output)

    def testPart1_RunSolution_WithExampleInput_ShouldBeCorrect(self):
        file_stub = FileStub()
        file_stub.set_array(test_input)

        output = part1_solution(file_stub)

        expected_output = 26397
        self.assertEqual(output, expected_output)

    def testPart2_RunSolution_WithExampleInput_ShouldBeCorrect(self):
        file_stub = FileStub()
        file_stub.set_array(test_input)

        output = part2_solution(file_stub)

        expected_output = 288957
        self.assertEqual(output, expected_output)
