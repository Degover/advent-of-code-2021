import unittest
from challenges.day_05 import *
from test.file_stub import FileStub

test_input = [
    '0,9 -> 5,9',
    '8,0 -> 0,8',
    '9,4 -> 3,4',
    '2,2 -> 2,1',
    '7,0 -> 7,4',
    '6,4 -> 2,0',
    '0,9 -> 2,9',
    '3,4 -> 1,4',
    '0,0 -> 8,8',
    '5,5 -> 8,2'
]

class Day_05_Tests(unittest.TestCase):

    def testHotTubesFormation_ReadFileInput_WithExampleInput_ShouldMapCorrectly(self):
        file_stub = FileStub()
        file_stub.set_array(test_input)

        formation = HotTubesFormation()
        formation.read_file_input(file_stub)

        expected_output = [
            [0,0,0,0,0,0,0,1,0,0],
            [0,0,1,0,0,0,0,1,0,0],
            [0,0,1,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,0,0],
            [0,1,1,2,1,1,1,2,1,1],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [2,2,2,1,1,1,0,0,0,0]
        ]
        output = [ row[:10] for row in formation.tubes_grid[:10] ]
        self.assertListEqual(output, expected_output)

    def testHotTubesFormation_MapLine_WithSinglePoint_ShouldMapCorrectly(self):
        formation = HotTubesFormation()
        
        formation.map_line((0, 0), (0, 0))

        output = [ row[:5] for row in formation.tubes_grid[:5] ]
        expected_output = [ [ 0 for _ in range(5) ] for _ in range(5) ]
        expected_output[0][0] = 1
        self.assertListEqual(output, expected_output)

    def testHotTubesFormation_MapLine_WithMultipleHorizontalPoints_ShouldMapCorrectly(self):
        formation = HotTubesFormation()
        
        formation.map_line((0, 0), (3, 0))

        output = [ row[:5] for row in formation.tubes_grid[:5] ]
        expected_output = [ [ 0 for _ in range(5) ] for _ in range(5) ]
        for i in range(4):
            expected_output[0][i] = 1
        self.assertListEqual(output, expected_output)

    def testHotTubesFormation_MapLine_WithMultipleVerticalPoints_ShouldMapCorrectly(self):
        formation = HotTubesFormation()
        
        formation.map_line((0, 0), (0, 3))

        output = [ row[:5] for row in formation.tubes_grid[:5] ]
        expected_output = [ [ 0 for _ in range(5) ] for _ in range(5) ]
        for i in range(4):
            expected_output[i][0] = 1
        self.assertListEqual(output, expected_output)

    def testHotTubesFormation_MapLine_WithDescendingRightDiagonalPoints_ShouldMapCorrectly(self):
        formation = HotTubesFormation(False)
        
        formation.map_line((0, 0), (3, 3))

        output = [ row[:5] for row in formation.tubes_grid[:5] ]
        expected_output = [ [ 0 for _ in range(5) ] for _ in range(5) ]
        for i in range(4):
            expected_output[i][i] = 1
        self.assertListEqual(output, expected_output)

    def testHotTubesFormation_MapLine_WithDescendingLeftDiagonalPoints_ShouldMapCorrectly(self):
        formation = HotTubesFormation(False)
        
        formation.map_line((3, 0), (0, 3))

        output = [ row[:5] for row in formation.tubes_grid[:5] ]
        expected_output = [ [ 0 for _ in range(5) ] for _ in range(5) ]
        for i in range(4):
            expected_output[i][3-i] = 1
        self.assertListEqual(output, expected_output)

    def testHotTubesFormation_MapLine_WithAscendingLeftDiagonalPoints_ShouldMapCorrectly(self):
        formation = HotTubesFormation(False)
        
        formation.map_line((3, 3), (0, 0))

        output = [ row[:5] for row in formation.tubes_grid[:5] ]
        expected_output = [ [ 0 for _ in range(5) ] for _ in range(5) ]
        for i in range(4):
            expected_output[3-i][3-i] = 1
        self.assertListEqual(output, expected_output)

    def testHotTubesFormation_MapLine_WithAscendingRightDiagonalPoints_ShouldMapCorrectly(self):
        formation = HotTubesFormation(False)
        
        formation.map_line((0, 3), (3, 0))

        output = [ row[:5] for row in formation.tubes_grid[:5] ]
        expected_output = [ [ 0 for _ in range(5) ] for _ in range(5) ]
        for i in range(4):
            expected_output[3-i][i] = 1
        self.assertListEqual(output, expected_output)

    def testHotTubesFormation_MapHorizontalLine_WithSinglePoint_ShouldMapCorrectly(self):
        formation = HotTubesFormation()
        
        formation.map_horizontal_line((0, 0), (0, 0))

        output = [ row[:5] for row in formation.tubes_grid[:5] ]
        expected_output = [ [ 0 for _ in range(5) ] for _ in range(5) ]
        expected_output[0][0] = 1
        self.assertListEqual(output, expected_output)

    def testHotTubesFormation_MapHorizontalLine_WithMultiplePoints_ShouldMapCorrectly(self):
        formation = HotTubesFormation()
        
        formation.map_horizontal_line((0, 0), (3, 0))

        output = [ row[:5] for row in formation.tubes_grid[:5] ]
        expected_output = [ [ 0 for _ in range(5) ] for _ in range(5) ]
        for i in range(4):
            expected_output[0][i] = 1
        self.assertListEqual(output, expected_output)

    def testHotTubesFormation_MapVerticalLine_WithSinglePoint_ShouldMapCorrectly(self):
        formation = HotTubesFormation()
        
        formation.map_vertical_line((0, 0), (0, 0))

        output = [ row[:5] for row in formation.tubes_grid[:5] ]
        expected_output = [ [ 0 for _ in range(5) ] for _ in range(5) ]
        expected_output[0][0] = 1
        self.assertListEqual(output, expected_output)

    def testHotTubesFormation_MapVerticalLine_WithMultiplePoints_ShouldMapCorrectly(self):
        formation = HotTubesFormation()
        
        formation.map_vertical_line((0, 0), (0, 3))

        output = [ row[:5] for row in formation.tubes_grid[:5] ]
        expected_output = [ [ 0 for _ in range(5) ] for _ in range(5) ]
        for i in range(4):
            expected_output[i][0] = 1
        self.assertListEqual(output, expected_output)

    def testHotTubesFormation_MapDiagonalLine_WithSinglePoint_ShouldMapCorrectly(self):
        formation = HotTubesFormation()
        
        formation.map_diagonal_line((0, 0), (0, 0))

        output = [ row[:5] for row in formation.tubes_grid[:5] ]
        expected_output = [ [ 0 for _ in range(5) ] for _ in range(5) ]
        expected_output[0][0] = 1
        self.assertListEqual(output, expected_output)

    def testHotTubesFormation_MapDiagonalLine_WithMultiplePoints_ShouldMapCorrectly(self):
        formation = HotTubesFormation()
        
        formation.map_diagonal_line((0, 0), (3, 3))

        output = [ row[:5] for row in formation.tubes_grid[:5] ]
        expected_output = [ [ 0 for _ in range(5) ] for _ in range(5) ]
        for i in range(4):
            expected_output[i][i] = 1
        self.assertListEqual(output, expected_output)

    def testPart1_RunSolution_WithExampleInput_ShouldBeCorrect(self):
        file_stub = FileStub()
        file_stub.set_array(test_input)

        output = part1_solution(file_stub)

        expected_output = 5
        self.assertEqual(output, expected_output)

    def testPart2_RunSolution_WithExampleInput_ShouldBeCorrect(self):
        file_stub = FileStub()
        file_stub.set_array(test_input)

        output = part2_solution(file_stub)

        expected_output = 12
        self.assertEqual(output, expected_output)
