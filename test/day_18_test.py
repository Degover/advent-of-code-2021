import unittest
from challenges.day_18 import *
from test.file_stub import FileStub

test_input = [ 
    '[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]',
    '[[[5,[2,8]],4],[5,[[9,9],0]]]',
    '[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]',
    '[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]',
    '[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]',
    '[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]',
    '[[[[5,4],[7,7]],8],[[8,3],8]]',
    '[[9,3],[[9,9],[6,[4,9]]]]',
    '[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]',
    '[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]',
]

class Day_18_Tests(unittest.TestCase):
    
    def testSnailfishNumber_FromString_WithSomeInputs_ShouldBeCorrect(self):
        test_cases = [
            ('[1,2]', ['[',1,2,']']),
            ('[[1,2],3]', ['[','[',1,2,']',3,']']),
            ('[9,[8,7]]', ['[',9,'[',8,7,']',']']),
            ('[[1,9],[8,5]]', ['[','[',1,9,']','[',8,5,']',']']),
            ('[[[[1,2],[3,4]],[[5,6],[7,8]]],9]', ['[','[','[','[',1,2,']','[',3,4,']',']','[','[',5,6,']','[',7,8,']',']',']',9,']']),
            ('[7,[6,[5,[7,0]]]]', ['[',7,'[',6,'[',5,'[',7,0,']',']',']',']']),
            ('[[[[0,9],2],3],4]', ['[','[','[','[',0,9,']',2,']',3,']',4,']'])
        ]
        for input, expected_output in test_cases:
            number = SnailfishNumber.from_string(input)

            self.assertListEqual(number.arr, expected_output)

    def testSnailfishNumber_CalcMagnitude_WithSomeInputs_ShouldBeCorrect(self):
        test_cases = [
            (['[','[',1,2,']','[','[',3,4,']',5,']',']'], 143),
            (['[','[','[','[',0,7,']',4,']','[','[',7,8,']','[',6,0,']',']',']','[',8,1,']',']'], 1384),
            (['[','[','[','[',1,1,']','[',2,2,']',']','[',3,3,']',']','[',4,4,']',']'], 445),
            (['[','[','[','[',3,0,']','[',5,3,']',']','[',4,4,']',']','[',5,5,']',']'], 791),
            (['[','[','[','[',5,0,']','[',7,4,']',']','[',5,5,']',']','[',6,6,']',']'], 1137),
            (['[','[','[','[',8,7,']','[',7,7,']',']','[','[',8,6,']','[',7,7,']',']',']','[','[','[',0,7,']','[',6,6,']',']','[',8,7,']',']',']'], 3488)
        ]
        for input, expected_output in test_cases:
            number = SnailfishNumber(input)

            output = number.calc_magnitude()

            self.assertEqual(output, expected_output)

    def testSnailfishNumber_Reduce_WithExplodingToRight_ShouldReduceCorrectly(self):
        number = SnailfishNumber(['[','[','[','[','[',9,8,']',1,']',2,']',3,']',4,']'])

        number.reduce()

        expected_output = ['[','[','[','[',0,9,']',2,']',3,']',4,']']
        self.assertListEqual(number.arr, expected_output)

    def testSnailfishNumber_Reduce_WithExplodingToLeft_ShouldReduceCorrectly(self):
        number = SnailfishNumber(['[',7,'[',6,'[',5,'[',4,'[',3,2,']',']',']',']',']'])

        number.reduce()

        expected_output = ['[',7,'[',6,'[',5,'[',7,0,']',']',']',']']
        self.assertListEqual(number.arr, expected_output)

    def testSnailfishNumber_Reduce_WithExplodingToRightInAnotherArray_ShouldReduceCorrectly(self):
        number = SnailfishNumber(['[','[',6,'[',5,'[',4,'[',3,2,']',']',']',']','[',1,1,']',']'])

        number.reduce()

        expected_output = ['[','[',6,'[',5,'[',7,0,']',']',']','[',3,1,']',']',]
        self.assertListEqual(number.arr, expected_output)

    def testSnailfishNumber_Reduce_WithExplodingToLeftInAnotherArray_ShouldReduceCorrectly(self):
        number = SnailfishNumber(['[','[',1,1,']','[','[','[','[',4,8,']',1,']',2,']',3,']',']'])

        number.reduce()

        expected_output = ['[','[',1,5,']','[','[','[',0,9,']',2,']',3,']',']']
        self.assertListEqual(number.arr, expected_output)

    def testSnailfishNumber_Reduce_WithSplitingOddNumber_ShouldReduceCorrectly(self):
        number = SnailfishNumber(['[',11,1,']'])

        number.reduce()

        expected_number = ['[','[',5,6,']',1,']']
        self.assertListEqual(number.arr, expected_number)

    def testSnailfishNumber_Reduce_WithSplitingEvenNumber_ShouldReduceCorrectly(self):
        number = SnailfishNumber(['[',12,1,']'])

        number.reduce()

        expected_number = ['[','[',6,6,']',1,']']
        self.assertListEqual(number.arr, expected_number)

    def testSnailfishNumber_Reduce_WithMultipleSteps_ShouldReduceCorrectly(self):
        number = SnailfishNumber(['[','[','[','[','[',4,3,']',4,']',4,']','[',7,'[','[',8,4,']',9,']',']',']','[',1,1,']',']'])

        number.reduce()

        expected_number = ['[','[','[','[',0,7,']',4,']','[','[',7,8,']','[',6,0,']',']',']','[',8,1,']',']']
        self.assertListEqual(number.arr, expected_number)

    def testSnailfishNumber_Reduce_WithBiggerInputMultipleSteps_ShouldReduceCorrectly(self):
        number = SnailfishNumber(['[', '[', '[', '[', 0, '[', 4, 5, ']', ']', '[', 0, 0, ']', ']', '[', '[', '[', 4, 5, ']', '[', 2, 6, ']', ']', '[', 9, 5, ']', ']', ']', '[', 7, '[', '[', '[', 3, 7, ']', '[', 4, 3, ']', ']', '[', '[', 6, 3, ']', '[', 8, 8, ']', ']', ']', ']', ']'])

        number.reduce()

        expected_number = ['[','[','[','[',4,0,']','[',5,4,']',']','[','[',7,7,']','[',6,0,']',']',']','[','[',8,'[',7,7,']',']','[','[',7,9,']','[',5,0,']',']',']',']']
        self.assertListEqual(number.arr, expected_number)

    def testSnailfishCalculator_ReadFileInput_WithExampleInput_ShouldBeCorrect(self):
        file_stub = FileStub()
        file_stub.set_array(test_input)
        calculator = SnailfishCalculator()

        calculator.read_file_input(file_stub)

        expected_numbers = [
            ['[','[','[',0,'[',5,8,']',']','[','[',1,7,']','[',9,6,']',']',']','[','[',4,'[',1,2,']',']','[','[',1,4,']',2,']',']',']'],
            ['[','[','[',5,'[',2,8,']',']',4,']','[',5,'[','[',9,9,']',0,']',']',']'],
            ['[',6,'[','[','[',6,2,']','[',5,6,']',']','[','[',7,6,']','[',4,7,']',']',']',']'],
            ['[','[','[',6,'[',0,7,']',']','[',0,9,']',']','[',4,'[',9,'[',9,0,']',']',']',']'],
            ['[','[','[',7,'[',6,4,']',']','[',3,'[',1,3,']',']',']','[','[','[',5,5,']',1,']',9,']',']'],
            ['[','[',6,'[','[',7,3,']','[',3,2,']',']',']','[','[','[',3,8,']','[',5,7,']',']',4,']',']'],
            ['[','[','[','[',5,4,']','[',7,7,']',']',8,']','[','[',8,3,']',8,']',']'],
            ['[','[',9,3,']','[','[',9,9,']','[',6,'[',4,9,']',']',']',']'],
            ['[','[',2,'[','[',7,7,']',7,']',']','[','[',5,8,']','[','[',9,3,']','[',0,2,']',']',']',']'],
            ['[','[','[','[',5,2,']',5,']','[',8,'[',3,7,']',']',']','[','[',5,'[',7,5,']',']','[',4,4,']',']',']']
        ]
        numbers = [ num.arr for num in calculator.numbers ]
        self.assertListEqual(numbers, expected_numbers)

    def testSnailfishCalculator_SumAll_WithSimpleExampleInput_ShouldBeCorrect(self):
        calculator = SnailfishCalculator()
        calculator.numbers = [
            SnailfishNumber(['[',1,1,']']),
            SnailfishNumber(['[',2,2,']']),
            SnailfishNumber(['[',3,3,']']),
            SnailfishNumber(['[',4,4,']']),
            SnailfishNumber(['[',5,5,']']),
            SnailfishNumber(['[',6,6,']'])
        ]
        
        output = calculator.sum_all().arr

        expected_output = ['[','[','[','[',5,0,']','[',7,4,']',']','[',5,5,']',']','[',6,6,']',']']
        self.assertListEqual(output, expected_output)

    def testSnailfishCalculator_SumAll_WithDetailedExampleInput_ShouldBeCorrect(self):
        file_stub = FileStub()
        file_stub.set_array([
            '[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]',
            '[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]',
            '[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]',
            '[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]',
            '[7,[5,[[3,8],[1,4]]]]',
            '[[2,[2,2]],[8,[8,1]]]',
            '[2,9]',
            '[1,[[[9,3],9],[[9,0],[0,7]]]]',
            '[[[5,[7,4]],7],1]',
            '[[[[4,2],2],6],[8,7]]'
        ])
        calculator = SnailfishCalculator()
        calculator.read_file_input(file_stub)
        
        output = calculator.sum_all().arr

        expected_output = ['[','[','[','[',8,7,']','[',7,7,']',']','[','[',8,6,']','[',7,7,']',']',']','[','[','[',0,7,']','[',6,6,']',']','[',8,7,']',']',']']
        self.assertListEqual(output, expected_output)

    def testSnailfishCalculator_SumAll_WithExampleInput_ShouldBeCorrect(self):
        file_stub = FileStub()
        file_stub.set_array(test_input)
        calculator = SnailfishCalculator()
        calculator.read_file_input(file_stub)
        
        output = calculator.sum_all().arr

        expected_output = ['[','[','[','[',6,6,']','[',7,6,']',']','[','[',7,7,']','[',7,0,']',']',']','[','[','[',7,7,']','[',7,7,']',']','[','[',7,8,']','[',9,9,']',']',']',']']
        self.assertListEqual(output, expected_output)

    def testPart1_RunSolution_WithExampleInput_ShouldBeCorrect(self):
        file_stub = FileStub()
        file_stub.set_array(test_input)

        output = part1_solution(file_stub)

        expected_output = 4140
        self.assertEqual(output, expected_output)

    def testPart2_RunSolution_WithExampleInput_ShouldBeCorrect(self):
        file_stub = FileStub()
        file_stub.set_array(test_input)

        output = part2_solution(file_stub)

        expected_output = -1
        self.assertEqual(output, expected_output)
        