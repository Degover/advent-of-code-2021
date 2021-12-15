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

    def _createFalseGrid(self, max_x, max_y):
        return [ [ False for _ in range(max_x+1) ] for _ in range(max_y+1) ]

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

        expected_points = self._createFalseGrid(3, 3)
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

        expected_points = self._createFalseGrid(3, 3)
        expected_points[3][3] = True
        self.assertListEqual(paper.points_array, expected_points)
        self.assertEqual(paper.max_x, 3)
        self.assertEqual(paper.max_y, 3)

    def testTransparentPaper_ExpandPaper_WithVerticalExpansion_ShouldExpandCorrectly(self):
        paper = TransparentPaper()
        paper.max_x = 1
        paper.max_y = 1
        paper.points_array = self._createFalseGrid(1, 1)

        paper.expand_paper(1, 3)

        expected_points = self._createFalseGrid(1, 3)
        self.assertListEqual(paper.points_array, expected_points)
        self.assertEqual(paper.max_x, 1)
        self.assertEqual(paper.max_y, 3)

    def testTransparentPaper_ExpandPaper_WithHorizontalExpansion_ShouldExpandCorrectly(self):
        paper = TransparentPaper()
        paper.max_x = 1
        paper.max_y = 1
        paper.points_array = self._createFalseGrid(1, 1)

        paper.expand_paper(3, 1)

        expected_points = self._createFalseGrid(3, 1)
        self.assertListEqual(paper.points_array, expected_points)
        self.assertEqual(paper.max_x, 3)
        self.assertEqual(paper.max_y, 1)

    def testTransparentPaper_ExpandPaper_WithDiagonalExpansion_ShouldExpandCorrectly(self):
        paper = TransparentPaper()
        paper.max_x = 1
        paper.max_y = 1
        paper.points_array = self._createFalseGrid(1, 1)

        paper.expand_paper(3, 3)

        expected_points = self._createFalseGrid(3, 3)
        self.assertListEqual(paper.points_array, expected_points)
        self.assertEqual(paper.max_x, 3)
        self.assertEqual(paper.max_y, 3)

    def testTransparentPaper_ExpandPaper_WithoutExpansion_ShouldDoNothing(self):
        paper = TransparentPaper()
        paper.max_x = 3
        paper.max_y = 3
        paper.points_array = self._createFalseGrid(3, 3)

        paper.expand_paper(1, 1)

        expected_points = self._createFalseGrid(3, 3)
        self.assertListEqual(paper.points_array, expected_points)
        self.assertEqual(paper.max_x, 3)
        self.assertEqual(paper.max_y, 3)

    def testTransparentPaper_Fold_WithXAxisAndEven_ShouldFoldCorrectly(self):
        paper = TransparentPaper()
        paper.max_y = 4
        paper.points_array = self._createFalseGrid(4, 4)
        paper.points_array[0][0] = True
        paper.points_array[1][3] = True
        paper.points_array[4][0] = True
        paper.points_array[4][4] = True

        paper.fold('x', 2)

        expected_points = self._createFalseGrid(1, 4)
        expected_points[0][0] = True
        expected_points[1][1] = True
        expected_points[4][0] = True
        self.assertListEqual(paper.points_array, expected_points)

    def testTransparentPaper_Fold_WithXAxisAndUnevenToLeft_ShouldFoldCorrectly(self):
        paper = TransparentPaper()
        paper.max_y = 6
        paper.points_array = self._createFalseGrid(6, 6)
        paper.points_array[0][0] = True
        paper.points_array[1][2] = True
        paper.points_array[1][6] = True
        paper.points_array[3][5] = True

        paper.fold('x', 4)

        expected_points = self._createFalseGrid(3, 6)
        expected_points[0][0] = True
        expected_points[1][2] = True
        expected_points[3][3] = True
        self.assertListEqual(paper.points_array, expected_points)

    def testTransparentPaper_Fold_WithXAxisAndUnevenToRight_ShouldFoldCorrectly(self):
        paper = TransparentPaper()
        paper.max_y = 6
        paper.points_array = self._createFalseGrid(6, 6)
        paper.points_array[0][0] = True
        paper.points_array[1][5] = True
        paper.points_array[4][1] = True
        paper.points_array[4][3] = True

        paper.fold('x', 2)

        expected_points = self._createFalseGrid(3, 6)
        expected_points[0][2] = True
        expected_points[1][1] = True
        expected_points[4][3] = True
        self.assertListEqual(paper.points_array, expected_points)

    def testTransparentPaper_Fold_WithYAxisAndEven_ShouldFoldCorrectly(self):
        paper = TransparentPaper()
        paper.max_x = 4
        paper.points_array = self._createFalseGrid(4, 4)
        paper.points_array[0][0] = True
        paper.points_array[3][1] = True
        paper.points_array[0][4] = True
        paper.points_array[4][4] = True

        paper.fold('y', 2)

        expected_points = self._createFalseGrid(4, 1)
        expected_points[0][0] = True
        expected_points[1][1] = True
        expected_points[0][4] = True
        self.assertListEqual(paper.points_array, expected_points)

    def testTransparentPaper_Fold_WithYAxisAndUnevenToTop_ShouldFoldCorrectly(self):
        paper = TransparentPaper()
        paper.max_x = 6
        paper.points_array = self._createFalseGrid(6, 6)
        paper.points_array[0][0] = True
        paper.points_array[2][1] = True
        paper.points_array[6][1] = True
        paper.points_array[5][3] = True

        paper.fold('y', 4)

        expected_points = self._createFalseGrid(6, 3)
        expected_points[0][0] = True
        expected_points[2][1] = True
        expected_points[3][3] = True
        self.assertListEqual(paper.points_array, expected_points)

    def testTransparentPaper_Fold_WithYAxisAndUnevenToBottom_ShouldFoldCorrectly(self):
        paper = TransparentPaper()
        paper.max_x = 6
        paper.points_array = self._createFalseGrid(6, 6)
        paper.points_array[0][0] = True
        paper.points_array[5][1] = True
        paper.points_array[1][4] = True
        paper.points_array[3][4] = True

        paper.fold('y', 2)

        expected_points = self._createFalseGrid(6, 3)
        expected_points[2][0] = True
        expected_points[1][1] = True
        expected_points[3][4] = True
        self.assertListEqual(paper.points_array, expected_points)

    def testPart1_RunSolution_WithExampleInput_ShouldBeCorrect(self):
        file_stub = FileStub()
        file_stub.set_array(test_input)

        output = part1_solution(file_stub)

        expected_output = 17
        self.assertEqual(output, expected_output)
