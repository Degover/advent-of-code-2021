import unittest
from challenges.day_09 import *
from test.file_stub import FileStub

test_input = [
    '2199943210',
    '3987894921',
    '9856789892',
    '8767896789',
    '9899965678'
]

class Day_09_Test(unittest.TestCase):

    def testInputParser_ParseLine_WithDefaultLine_ShouldBeCorrect(self):
        parser = InputParser(None)

        output = parser.parse_line('2199943210')

        expected_output = [2, 1, 9, 9, 9, 4, 3, 2, 1, 0 ]
        self.assertListEqual(output, expected_output)

    def testInputParser_ParseFile_WithExampleInput_ShouldBeCorrect(self):
        file_stub = FileStub()
        file_stub.set_array(test_input)

        parser = InputParser(file_stub)
        output = list(parser.parse_file())

        expected_output = [
            [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
            [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
            [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
            [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
            [9, 8, 9, 9, 9, 6, 5, 6, 7, 8]
        ]
        self.assertListEqual(output, expected_output)

    def testHeightmapAnalyser_CalculateTotalRiskLevels_WithExampleInput_ShouldBeCorrect(self):
        file_stub = FileStub()
        file_stub.set_array(test_input)

        analyser = HeightmapAnalyser(file_stub)
        output = analyser.calculate_total_risk_levels()

        expected_output = 15
        self.assertEqual(output, expected_output)
        
    def testHeightmapAnalyser_GetLowerPoints_WithExampleInput_ShouldBeCorrect(self):
        file_stub = FileStub()
        file_stub.set_array(test_input)

        analyser = HeightmapAnalyser(file_stub)
        output = list(analyser.get_lower_points())

        expected_output = [(1, 1, 0), (0, 9, 0), (5, 2, 2), (5, 6, 4)]
        self.assertEqual(output, expected_output)
     
    def testHeightmapAnalyser_GetUpValues_WithDefaultInput_ShouldBeCorrect(self):
        input = [
            [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
            [3, 9, 8, 7, 8, 9, 4, 9, 2, 1]
        ]
        expected_output = input[0]

        analyser = HeightmapAnalyser(FileStub())
        analyser.height_grid = input

        output = [ analyser.get_up_value(i, 1) for i in range(len(expected_output)) ]

        self.assertEqual(output, expected_output)
         
    def testHeightmapAnalyser_GetUpValues_WithFirstRowInput_ShouldBeCorrect(self):
        input = [ [2, 1, 9, 9, 9, 4, 3, 2, 1, 0] ]
        expected_output = [9] * len(input[0])

        analyser = HeightmapAnalyser(FileStub())
        analyser.height_grid = input

        output = [ analyser.get_up_value(i, 0) for i in range(len(expected_output)) ]

        self.assertEqual(output, expected_output)
        
    def testHeightmapAnalyser_GetDownValues_WithDefaultInput_ShouldBeCorrect(self):
        input = [
            [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
            [3, 9, 8, 7, 8, 9, 4, 9, 2, 1]
        ]
        expected_output = input[1]

        analyser = HeightmapAnalyser(FileStub())
        analyser.height_grid = input

        output = [ analyser.get_down_value(i, 0) for i in range(len(expected_output)) ]

        self.assertEqual(output, expected_output)
           
    def testHeightmapAnalyser_GetDownValues_WithLastRowInput_ShouldBeCorrect(self):
        input = [
            [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
            [3, 9, 8, 7, 8, 9, 4, 9, 2, 1]
        ]
        expected_output = [9] * len(input[0])

        analyser = HeightmapAnalyser(FileStub())
        analyser.height_grid = input

        output = [ analyser.get_down_value(i, 1) for i in range(len(expected_output)) ]

        self.assertEqual(output, expected_output)
          
    def testHeightmapAnalyser_GetRightValues_WithDefaultInput_ShouldBeCorrect(self):
        input = [ [2, 1, 9, 9, 9, 4, 3, 2, 1, 0] ]
        expected_output = input[0] + [9]
        expected_output.pop(0)

        analyser = HeightmapAnalyser(FileStub())
        analyser.height_grid = input

        output = [ analyser.get_right_value(i, 0) for i in range(len(expected_output)) ]

        self.assertEqual(output, expected_output)

    def testHeightmapAnalyser_GetLeftValues_WithDefaultInput_ShouldBeCorrect(self):
        input = [ [2, 1, 9, 9, 9, 4, 3, 2, 1, 0] ]
        expected_output = [9] + input[0]
        expected_output.pop()

        analyser = HeightmapAnalyser(FileStub())
        analyser.height_grid = input

        output = [ analyser.get_left_value(i, 0) for i in range(len(expected_output)) ]

        self.assertEqual(output, expected_output)

    def testHeightmapAnalyser_CalculateBasinSize_WithExampleInput_ShouldBeCorrect(self):
        test_cases = [
            ((1,0), 3),
            ((9,0), 9),
            ((2,2), 14),
            ((6,4), 9)
        ]
        file_stub = FileStub()
        file_stub.set_array(test_input)
        analyser = HeightmapAnalyser(file_stub)

        for input, expected_output in test_cases:
            output = analyser.calculate_basin_size(input,[])
            self.assertEqual(output, expected_output)
        
    def testHeightmapAnalyser_GetAllBasinsSize_WithExampleInput_ShouldBeCorrect(self):
        file_stub = FileStub()
        file_stub.set_array(test_input)
        analyser = HeightmapAnalyser(file_stub)

        output = list(analyser.get_all_basins_sizes())

        expected_output = [3, 9, 14, 9]
        self.assertEqual(output, expected_output)
        
    def testPart1_RunSolution_WithExampleInput_ShouldBeCorrect(self):
        file_stub = FileStub()
        file_stub.set_array(test_input)

        output = part1_solution(file_stub)

        expected_output = 15
        self.assertEqual(output, expected_output)
        
    def testPart2_RunSolution_WithExampleInput_ShouldBeCorrect(self):
        file_stub = FileStub()
        file_stub.set_array(test_input)

        output = part2_solution(file_stub)

        expected_output = 1134
        self.assertEqual(output, expected_output)
        