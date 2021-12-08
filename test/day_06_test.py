import unittest
from unittest.case import expectedFailure
from challenges.day_06 import *
from test.file_stub import FileStub

class Day_06_Tests(unittest.TestCase):

    def testLanternFishManager_PassDay_WithAgingFish_ShouldAgeCorrectly(self):
        manager = LanternFishManager()
        manager.fish_countdowns[1] = 1

        manager.pass_day()

        expected_output = [0] * 9
        expected_output[0] = 1
        self.assertListEqual(manager.fish_countdowns, expected_output)

    def testLanternFishManager_PassDay_WithAgedFish_ShouldResetAgeAndCreateNewborn(self):
        manager = LanternFishManager()
        manager.fish_countdowns[0] = 1

        manager.pass_day()

        
        expected_output = [0] * 9
        expected_output[6] = 1
        expected_output[8] = 1
        self.assertListEqual(manager.fish_countdowns, expected_output)

    def testLanternFishManager_ReadFileInput_WithAgedFish_ShouldResetAgeAndCreateNewborn(self):
        file = FileStub()
        file.set_array([ '1,2,3,4,1' ])

        manager = LanternFishManager()
        manager.read_file_input(file)

        expected_output = [0] * 9
        expected_output[1] = 2
        expected_output[2] = 1
        expected_output[3] = 1
        expected_output[4] = 1
        self.assertListEqual(manager.fish_countdowns, expected_output)

    def testPart1_RunSolution_WithExampleInput_ShouldBeCorrect(self):
        file = FileStub()
        file.set_array([ '3,4,3,1,2' ])

        output = part1_solution(file)

        expected_output = 5934
        self.assertEqual(output, expected_output)
    
    def testPart2_RunSolution_WithExampleInput_ShouldBeCorrect(self):
        file = FileStub()
        file.set_array([ '3,4,3,1,2' ])

        output = part2_solution(file)

        expected_output = 26984457539
        self.assertEqual(output, expected_output)
