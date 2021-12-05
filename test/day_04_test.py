import unittest
from challenges.day_04 import *
from test.file_stub import FileStub

test_input = ['7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1',
    '',
    '22 13 17 11  0',
    ' 8  2 23  4 24',
    '21  9 14 16  7',
    ' 6 10  3 18  5',
    ' 1 12 20 15 19',
    '',
    ' 3 15  0  2 22',
    ' 9 18 13 17  5',
    '19  8  7 25 23',
    '20 11 10 24  4',
    '14 21 16 12  6',
    '',
    '14 21 17 24  4',
    '10 16 15  9 19',
    '18  8 23 26 20',
    '22 11 13  6  5',
    ' 2  0 12  3  7'
]

class Day_04_Tests(unittest.TestCase):

    def testBingoBoard_ReadRow_WithNormalRows_ShouldBeCorrect(self):
        expected_out = [ [ '1' for _ in range(5) ] for _ in range(5) ]
        for x in range(5):
            for y in range(5):
                expected_out[x][y] = str((y+1) * 5 + x)

        board = BingoBoard()
        list([ board.read_row('  '.join(row), y) for y, row in enumerate(expected_out) ])

        self.assertListEqual(board.number_grid, expected_out)

    def testBingoBoard_MarkNumber_WithDefaultNumber_ShouldMarkAll(self):
        expected_out = [ [ '' for _ in range(5) ] for _ in range(5) ]

        board = BingoBoard()
        board.mark_number('0')

        self.assertListEqual(board.number_grid, expected_out)
        
    def testBingoBoard_MarkNumber_WithSpecificNumber_ShouldMarkOne(self):
        expected_out = [ [ '0' for _ in range(5) ] for _ in range(5) ]
        expected_out[0][0] = ''

        board = BingoBoard()
        board.number_grid[0][0] = '1'
        board.mark_number('1')

        self.assertListEqual(board.number_grid, expected_out)
        
    def testBingoBoard_MarkNumber_WithNonExistingNumber_ShouldDoNothing(self):
        expected_out = [ [ '0' for _ in range(5) ] for _ in range(5) ]

        board = BingoBoard()
        board.mark_number('1')

        self.assertListEqual(board.number_grid, expected_out)
        
    def testBingoBoard_GetIsWinner_WithWinnerRow_ShouldReturnTrue(self):
        board = BingoBoard()
        board.number_grid[0] = ['1'] * 5
        board.mark_number('1')

        output = board.get_is_winner()

        self.assertEqual(output, True)
        
    def testBingoBoard_GetIsWinner_WithWinnerColumn_ShouldReturnTrue(self):
        board = BingoBoard()
        for i in range(5):
            board.number_grid[i][2] = '1'
        board.mark_number('1')

        output = board.get_is_winner()

        self.assertEqual(output, True)
        
    def testBingoBoard_GetIsWinner_WithNoWinner_ShouldReturnFalse(self):
        board = BingoBoard()
        board.mark_number('1')

        output = board.get_is_winner()

        self.assertEqual(output, False)
        
    def testBingoManager_ReadFileInput_WithMockFile_ShouldBeCorrect(self):
        file_stub = FileStub()
        file_stub.set_array(test_input)
        expected_boards = [
            [['22', '13', '17', '11', '0',], [ '8', '2', '23', '4', '24',], ['21', '9', '14', '16', '7',], [ '6', '10', '3', '18', '5',], [ '1', '12', '20', '15', '19',]],
            [[ '3', '15', '0', '2', '22',], [ '9', '18', '13', '17', '5',], ['19', '8', '7', '25', '23',], ['20', '11', '10', '24', '4',], ['14', '21', '16', '12', '6',]],
            [['14', '21', '17', '24', '4',], ['10', '16', '15', '9', '19',], ['18', '8', '23', '26', '20',], ['22', '11', '13', '6', '5',], [ '2', '0', '12', '3', '7',]]
        ]

        manager = BingoManager()
        manager.read_file_input(file_stub)

        self.assertEqual(manager.numbers, file_stub.array[0])
        self.assertEqual(len(manager.boards), 3)

        for i in range(3):
            self.assertListEqual(manager.boards[i].number_grid, expected_boards[i])

    def testPart1_RunSolution_WithExampleInput_ShouldBeCorrect(self):
        file_stub = FileStub()
        file_stub.set_array(test_input)

        result = part1_solution(file_stub)

        self.assertEqual(result, 4512)

    def testPart2_RunSolution_WithExampleInput_ShouldBeCorrect(self):
        file_stub = FileStub()
        file_stub.set_array(test_input)

        result = part2_solution(file_stub)

        self.assertEqual(result, 1924)
