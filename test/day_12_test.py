import unittest
from challenges.day_12 import *
from test.file_stub import FileStub

many_test_input = [
    ([
        'start-A',
        'start-b',
        'A-c',
        'A-b',
        'b-d',
        'A-end',
        'b-end'
    ], 10, 36),
    ([
        'dc-end',
        'HN-start',
        'start-kj',
        'dc-start',
        'dc-HN',
        'LN-dc',
        'HN-end',
        'kj-sa',
        'kj-HN',
        'kj-dc'
    ], 19, 103),
    ([
        'fs-end',
        'he-DX',
        'fs-he',
        'start-DX',
        'pj-DX',
        'end-zg',
        'zg-sl',
        'zg-pj',
        'pj-he',
        'RW-he',
        'fs-DX',
        'pj-RW',
        'zg-RW',
        'start-pj',
        'he-WI',
        'zg-he',
        'pj-fs',
        'start-RW'
    ], 226, 3509)
]

class Day_12_Tests(unittest.TestCase):
    
    def testCaveNode_CreateNew_WithSmallCave_ShouldBeSmallCave(self):
        name = 'ab'
        node = CaveNode(name)

        self.assertTrue(node.is_small_cave)
        self.assertEqual(node.name, name)

    def testCaveNode_CreateNew_WithBigCave_ShouldBeSmallCave(self):
        name = 'HJ'
        node = CaveNode(name)

        self.assertFalse(node.is_small_cave)
        self.assertEqual(node.name, name)

    def testCaveNode_Compare_WithSameName_ShouldBeEqual(self):
        node_1 = CaveNode('A')
        node_2 = CaveNode('A')

        self.assertEqual(node_1, node_2)

    def testCaveNode_Compare_WithSameStringName_ShouldBeEqual(self):
        name = 'A'
        node = CaveNode('A')

        self.assertEqual(name, node)

    def testCaveNode_Compare_WithDifferentName_ShouldNotBeEqual(self):
        node_1 = CaveNode('A')
        node_2 = CaveNode('B')

        self.assertNotEqual(node_1, node_2)

    def testCaveNode_Compare_WithDifferentStringName_ShouldNotBeEqual(self):
        name = 'A'
        node = CaveNode('B')

        self.assertNotEqual(name, node)

    def testCaveNode_ConnectNode_WithDefaultNodes_ShouldConnectInBoth(self):
        node_1 = CaveNode('A')
        node_2 = CaveNode('B')

        node_1.connect_node(node_2)

        self.assertTrue(node_1 in node_2.connections)
        self.assertTrue(node_2 in node_1.connections)

    def testCavePathMapper_ReadFileInput_WithSimpleNodes_ShouldReadCorrectly(self):
        file_stub = FileStub()
        file_stub.set_array([
            'start-A\n',
            'A-end',
        ])
        mapper = CavePathMapper()

        mapper.read_file_input(file_stub)

        self.assertTrue('A' in mapper.start_node.connections)
        self.assertTrue('A' in mapper.end_node.connections)
        self.assertTrue('A' in mapper.nodes)

    def testCavePathMapper_MapPaths_WithFirstExample_ShouldBeCorrect(self):
        file_stub = FileStub()
        file_stub.set_array(many_test_input[0][0])
        
        mapper = CavePathMapper()
        mapper.read_file_input(file_stub)
        output = [ [ node.name for node in path ] for path in mapper.map_paths() ]

        expected_output = [
            ['start','A','b','A','c','A','end'],
            ['start','A','b','A','end'],
            ['start','A','b','end'],
            ['start','A','c','A','b','A','end'],
            ['start','A','c','A','b','end'],
            ['start','A','c','A','end'],
            ['start','A','end'],
            ['start','b','A','c','A','end'],
            ['start','b','A','end'],
            ['start','b','end']
        ]
        expected_output.sort()
        output.sort()
        self.assertListEqual(output, expected_output)

    def testCavePathMapper_MapPaths_WithFirstExampleAndMaxLen2_ShouldBeCorrect(self):
        file_stub = FileStub()
        file_stub.set_array(many_test_input[0][0])
        
        mapper = CavePathMapper(2)
        mapper.read_file_input(file_stub)
        output = [ [ node.name for node in path ] for path in mapper.map_paths() ]

        expected_output = [
            ['start','A','b','A','b','A','c','A','end'],
            ['start','A','b','A','b','A','end'],
            ['start','A','b','A','b','end'],
            ['start','A','b','A','c','A','b','A','end'],
            ['start','A','b','A','c','A','b','end'],
            ['start','A','b','A','c','A','c','A','end'],
            ['start','A','b','A','c','A','end'],
            ['start','A','b','A','end'],
            ['start','A','b','d','b','A','c','A','end'],
            ['start','A','b','d','b','A','end'],
            ['start','A','b','d','b','end'],
            ['start','A','b','end'],
            ['start','A','c','A','b','A','b','A','end'],
            ['start','A','c','A','b','A','b','end'],
            ['start','A','c','A','b','A','c','A','end'],
            ['start','A','c','A','b','A','end'],
            ['start','A','c','A','b','d','b','A','end'],
            ['start','A','c','A','b','d','b','end'],
            ['start','A','c','A','b','end'],
            ['start','A','c','A','c','A','b','A','end'],
            ['start','A','c','A','c','A','b','end'],
            ['start','A','c','A','c','A','end'],
            ['start','A','c','A','end'],
            ['start','A','end'],
            ['start','b','A','b','A','c','A','end'],
            ['start','b','A','b','A','end'],
            ['start','b','A','b','end'],
            ['start','b','A','c','A','b','A','end'],
            ['start','b','A','c','A','b','end'],
            ['start','b','A','c','A','c','A','end'],
            ['start','b','A','c','A','end'],
            ['start','b','A','end'],
            ['start','b','d','b','A','c','A','end'],
            ['start','b','d','b','A','end'],
            ['start','b','d','b','end'],
            ['start','b','end']
        ]
        expected_output.sort()
        output.sort()
        self.assertListEqual(output, expected_output)

    def testPart1_RunSolution_WithExampleInput_ShouldBeCorrect(self):
        for input, expected_output, _ in many_test_input:
            file_stub = FileStub()
            file_stub.set_array(input)
            output = part1_solution(file_stub)
            self.assertEqual(output, expected_output)

    def testPart2_RunSolution_WithExampleInput_ShouldBeCorrect(self):
        for input, _, expected_output in many_test_input:
            file_stub = FileStub()
            file_stub.set_array(input)
            output = part1_solution(file_stub)
            self.assertEqual(output, expected_output)

