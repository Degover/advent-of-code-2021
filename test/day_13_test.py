import unittest
from challenges.day_13 import *
from test.file_stub import FileStub

test_input = [
    '6,10',
    '0,14',
    '9,10',
    '0,3',
    '10,4',
    '4,11',
    '6,0',
    '6,12',
    '4,1',
    '0,13',
    '10,12',
    '3,4',
    '3,0',
    '8,4',
    '1,10',
    '2,14',
    '8,10',
    '9,0',
    '',
    'fold along y=7',
    'fold along x=5'
]

class Day_13_Tests(unittest.TestCase):

    def testTransparentPaper_ReadFileInput_WithSimpleInput_ShouldReadCorrectly(self):
        input = [
            '0,0',
            '0,2',
            '2,0',
            '3,3',
            '',
            'fold along y=1',
            'fold along x=14'
        ]
        paper = TransparentPaper()

        paper.read_file_input(input)

        expected_points = [ [ False for _ in range(4) ] for _ in range(4) ]
        expected_points[0][0] = True
        expected_points[0][2] = True
        expected_points[2][0] = True
        expected_points[3][3] = True
        self.assertListEqual(paper.points_array, expected_points)

        expected_instructions = [
            ('y', 1),
            ('x', 14)
        ]
        self.assertListEqual(paper.instructions, expected_instructions)

        self.assertEqual(paper.max_x, 3)
        self.assertEqual(paper.max_y, 3)
    
    def testTransparentPaper_MarkPoint_WithSimpleInput_ShouldMarkAndExpandCorrectly(self):
        paper = TransparentPaper()

        paper.mark_point(3, 3)

        expected_points = [ [ False for _ in range(4) ] for _ in range(4) ]
        expected_points[3][3] = True
        self.assertListEqual(paper.points_array, expected_points)
        self.assertEqual(paper.max_x, 3)
        self.assertEqual(paper.max_y, 3)

    def testTransparentPaper_ExpandPaper_WithVerticalExpansion_ShouldExpandCorrectly(self):
        paper = TransparentPaper()
        paper.max_x = 1
        paper.max_y = 1
        paper.points_array = [ [ False for _ in range(2) ] for _ in range(2) ]

        paper.expand_paper(1, 3)

        expected_points = [ [ False for _ in range(2) ] for _ in range(4) ]
        self.assertListEqual(paper.points_array, expected_points)
        self.assertEqual(paper.max_x, 1)
        self.assertEqual(paper.max_y, 3)

    def testTransparentPaper_ExpandPaper_WithHorizontalExpansion_ShouldExpandCorrectly(self):
        paper = TransparentPaper()
        paper.max_x = 1
        paper.max_y = 1
        paper.points_array = [ [ False for _ in range(2) ] for _ in range(2) ]

        paper.expand_paper(3, 1)

        expected_points = [ [ False for _ in range(4) ] for _ in range(2) ]
        self.assertListEqual(paper.points_array, expected_points)
        self.assertEqual(paper.max_x, 3)
        self.assertEqual(paper.max_y, 1)

    def testTransparentPaper_ExpandPaper_WithDiagonalExpansion_ShouldExpandCorrectly(self):
        paper = TransparentPaper()
        paper.max_x = 1
        paper.max_y = 1
        paper.points_array = [ [ False for _ in range(2) ] for _ in range(2) ]

        paper.expand_paper(3, 3)

        expected_points = [ [ False for _ in range(4) ] for _ in range(4) ]
        self.assertListEqual(paper.points_array, expected_points)
        self.assertEqual(paper.max_x, 3)
        self.assertEqual(paper.max_y, 3)

    def testTransparentPaper_ExpandPaper_WithoutExpansion_ShouldDoNothing(self):
        paper = TransparentPaper()
        paper.max_x = 3
        paper.max_y = 3
        paper.points_array = [ [ False for _ in range(4) ] for _ in range(4) ]

        paper.expand_paper(1, 1)

        expected_points = [ [ False for _ in range(4) ] for _ in range(4) ]
        self.assertListEqual(paper.points_array, expected_points)
        self.assertEqual(paper.max_x, 3)
        self.assertEqual(paper.max_y, 3)

    def testPart1_RunSolution_WithExampleInput_ShouldBeCorrect(self):
        file_stub = FileStub()
        file_stub.set_array(test_input)

        output = part1_solution(file_stub)

        expected_output = 0
        self.assertEqual(output, expected_output)

    def testPart2_RunSolution_WithExampleInput_ShouldBeCorrect(self):
        file_stub = FileStub()
        file_stub.set_array(test_input)

        output = part2_solution(file_stub)

        expected_output = 0
        self.assertEqual(output, expected_output)
