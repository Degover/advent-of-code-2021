import unittest
from challenges.day_10 import *

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
