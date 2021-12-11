import unittest
from challenges.day_11 import *
from test.file_stub import FileStub

test_input = [
    '5483143223',
    '2745854711',
    '5264556173',
    '6141336146',
    '6357385478',
    '4167524645',
    '2176841721',
    '6882881134',
    '4846848554',
    '5283751526'
]

class Day_11_Tests(unittest.TestCase):

    def testOctopusFlashSimulator_ReadFileInput_WithDefaultFile_ShouldReadCorrectly(self):
        file_stub = FileStub()
        file_stub.set_array(test_input)

        simulator = OctopusFlashSimulator()
        simulator.read_file_input(file_stub)

        expected_output = [ [ int(char) for char in row ] for row in test_input ]
        self.assertEqual(simulator.octopus_grid, expected_output)
        self.assertEqual(simulator.MAX_X, 10)
        self.assertEqual(simulator.MAX_Y, 10)

    def testOctopusFlashSimulator_FlashAdjacents_WithSingleFlash_ShouldIncrementAdjacents(self):
        file_stub = FileStub()
        file_stub.set_array(test_input)

        simulator = OctopusFlashSimulator()
        simulator.octopus_grid = [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
        ]
        simulator.MAX_Y = 3
        simulator.MAX_X = 3
        
        simulator.flash_adjacents(1, 1)

        expected_output = [
            [2, 2, 2],
            [2, 0, 2],
            [2, 2, 2]
        ]
        self.assertEqual(simulator.octopus_grid, expected_output)
        self.assertEqual(simulator.flash_count, 1)

    def testOctopusFlashSimulator_FlashAdjacents_WithInnerFlash_ShouldFlashAll(self):
        file_stub = FileStub()
        file_stub.set_array(test_input)

        simulator = OctopusFlashSimulator()
        simulator.octopus_grid = [
            [0, 9, 9],
            [9, 2, 9],
            [9, 9, 9]
        ]
        simulator.MAX_Y = 3
        simulator.MAX_X = 3
        
        simulator.flash_adjacents(0, 0)

        expected_output = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.assertEqual(simulator.octopus_grid, expected_output)
        self.assertEqual(simulator.flash_count, 9)

    def testOctopusFlashSimulator_PassDay_WithoutFlashes_ShouldIncrementAll(self):
        file_stub = FileStub()
        file_stub.set_array(test_input)

        simulator = OctopusFlashSimulator()
        simulator.octopus_grid = [ [ int(char) for char in row ] for row in test_input ]
        simulator.MAX_Y = 10
        simulator.MAX_X = 10
        
        simulator.pass_step()

        expected_output = [
            [6, 5, 9, 4, 2, 5, 4, 3, 3, 4],
            [3, 8, 5, 6, 9, 6, 5, 8, 2, 2],
            [6, 3, 7, 5, 6, 6, 7, 2, 8, 4],
            [7, 2, 5, 2, 4, 4, 7, 2, 5, 7],
            [7, 4, 6, 8, 4, 9, 6, 5, 8, 9],
            [5, 2, 7, 8, 6, 3, 5, 7, 5, 6],
            [3, 2, 8, 7, 9, 5, 2, 8, 3, 2],
            [7, 9, 9, 3, 9, 9, 2, 2, 4, 5],
            [5, 9, 5, 7, 9, 5, 9, 6, 6, 5],
            [6, 3, 9, 4, 8, 6, 2, 6, 3, 7]
        ]
        self.assertEqual(simulator.octopus_grid, expected_output)
        self.assertEqual(simulator.flash_count, 0)

    def testOctopusFlashSimulator_PassDay_WithSingleFlash_ShouldIncrementAndFlash(self):
        file_stub = FileStub()
        file_stub.set_array(test_input)

        simulator = OctopusFlashSimulator()
        simulator.octopus_grid = [
            [0, 0, 0],
            [0, 9, 0],
            [0, 0, 0]
        ]
        simulator.MAX_Y = 3
        simulator.MAX_X = 3

        simulator.pass_step()

        expected_output = [
            [2, 2, 2],
            [2, 0, 2],
            [2, 2, 2]
        ]
        self.assertEqual(simulator.octopus_grid, expected_output)
        self.assertEqual(simulator.flash_count, 1)

    def testOctopusFlashSimulator_PassDay_WithSuccessiveFlashes_ShouldIncrementAndFlash(self):
        file_stub = FileStub()
        file_stub.set_array(test_input)

        simulator = OctopusFlashSimulator()
        simulator.octopus_grid = [
            [1, 1, 1, 1, 1],
            [1, 9, 9, 9, 1],
            [1, 9, 1, 9, 1],
            [1, 9, 9, 9, 1],
            [1, 1, 1, 1, 1]
        ]
        simulator.MAX_Y = 5
        simulator.MAX_X = 5

        simulator.pass_step()

        expected_output = [
            [3, 4, 5, 4, 3],
            [4, 0, 0, 0, 4],
            [5, 0, 0, 0, 5],
            [4, 0, 0, 0, 4],
            [3, 4, 5, 4, 3]
        ]
        self.assertEqual(simulator.octopus_grid, expected_output)
        self.assertEqual(simulator.flash_count, 9)

    def testPart1_RunSolution_WithExampleInput_ShouldBeCorrect(self):
        file_stub = FileStub()
        file_stub.set_array(test_input)

        output = part1_solution(file_stub)

        expected_output = 1656
        self.assertEqual(output, expected_output)

    def testPart2_RunSolution_WithExampleInput_ShouldBeCorrect(self):
        file_stub = FileStub()
        file_stub.set_array(test_input)

        output = part2_solution(file_stub)

        expected_output = 195
        self.assertEqual(output, expected_output)

