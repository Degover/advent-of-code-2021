import unittest
from challenges.day_07 import *
from test.file_stub import FileStub

class Day_07_Tests(unittest.TestCase):

    def testCrabManager_GetFinalPosition_WithExampleInput_ShouldBeCorrect(self):
        manager = CrabManager()
        manager.crabs_positions = [16,1,2,0,4,2,7,1,2,14]

        output = manager.get_final_position()
        
        self.assertEqual(output, 2)
        
    def testCrabManager_GetTotalFuelConsumption_WithExampleInput_ShouldBeCorrect(self):
        manager = CrabManager()
        manager.crabs_positions = [16,1,2,0,4,2,7,1,2,14]

        output = manager.get_total_fuel_consumption()
        
        self.assertEqual(output, 37)
        
    def testCrabManager_ReadFileInput_WithExampleInput_ShouldReadCorrectly(self):
        file = FileStub()
        file.set_array([ '16,1,2,0,4,2,7,1,2,14' ])

        manager = CrabManager()
        manager.read_file_input(file)
        
        expected_output = [16,1,2,0,4,2,7,1,2,14]
        self.assertListEqual(manager.crabs_positions, expected_output)
        
    def testCompleteCrabManager_GetTotalFuelConsumption_WithExampleInput_ShouldBeCorrect(self):
        manager = CompleteCrabManager()
        manager.crabs_positions = [16,1,2,0,4,2,7,1,2,14]

        output = manager.get_total_fuel_consumption()
        
        self.assertEqual(output, 168)
        
    def testCompleteCrabManager_ReadFileInput_WithExampleInput_ShouldReadCorrectly(self):
        file = FileStub()
        file.set_array([ '16,1,2,0,4,2,7,1,2,14' ])

        manager = CompleteCrabManager()
        manager.read_file_input(file)
        
        expected_output = [16,1,2,0,4,2,7,1,2,14]
        self.assertListEqual(manager.crabs_positions, expected_output)
        
    def testCompleteCrabManager_CalculateTriangularSum_WithManyCases_ShouldCalculateCorrectly(self):
        test_cases = [
            (1, 1),
            (2, 3),
            (3, 6),
            (4, 10),
            (5, 15),
            (6, 21)
        ]

        manager = CompleteCrabManager()
        for input, expected_output in test_cases:
            output = manager.calculate_triangular_sum(input)
            self.assertEqual(output, expected_output)
        
    def testPart1_RunSolution_WithExampleInput_ShouldBeCorrect(self):
        file = FileStub()
        file.set_array([ '16,1,2,0,4,2,7,1,2,14' ])

        output = part1_solution(file)
        
        expected_output = 37
        self.assertEqual(output, expected_output)
      
    def testPart2_RunSolution_WithExampleInput_ShouldBeCorrect(self):
        file = FileStub()
        file.set_array([ '16,1,2,0,4,2,7,1,2,14' ])

        output = part2_solution(file)
        
        expected_output = 168
        self.assertEqual(output, expected_output)
          