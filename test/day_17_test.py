import unittest
from challenges.day_17 import *
from test.file_stub import FileStub

test_input = [ 'target area: x=20..30, y=-10..-5' ]

class Day_17_Tests(unittest.TestCase):
    
    def testLaunchSimulator_ReadFileInput_WithExampleInput_ShouldReadCorrectly(self):
        file_stub = FileStub()
        file_stub.set_array(test_input)
        simulator = LaunchSimulator()

        simulator.read_file_input(file_stub)

        self.assertTupleEqual(simulator.range_x, (20, 30))
        self.assertTupleEqual(simulator.range_y, (-10, -5))

    def testLaunchSimulator_GetMaxYVelocity_WithExampleInput_ShouldBeCorrect(self):
        file_stub = FileStub()
        file_stub.set_array(test_input)
        simulator = LaunchSimulator()
        simulator.range_x = (20, 30)
        simulator.range_y = (-10, -5)

        output = simulator.get_max_y_velocity()

        self.assertEqual(output, 9)

    def testLaunchSimulator_GetMinXVelocity_WithExampleInput_ShouldBeCorrect(self):
        file_stub = FileStub()
        file_stub.set_array(test_input)
        simulator = LaunchSimulator()
        simulator.range_x = (20, 30)
        simulator.range_y = (-10, -5)

        output = simulator.get_min_x_velocity()

        self.assertEqual(output, 6)

    def testPart1_RunSolution_WithExampleInput_ShouldBeCorrect(self):
        file_stub = FileStub()
        file_stub.set_array(test_input)

        output = part1_solution(file_stub)

        expected_output = 45
        self.assertEqual(output, expected_output)

    def testPart2_RunSolution_WithExampleInput_ShouldBeCorrect(self):
        file_stub = FileStub()
        file_stub.set_array(test_input)

        output = part2_solution(file_stub)

        expected_output = 112
        self.assertEqual(output, expected_output)
        