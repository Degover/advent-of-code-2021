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

    def testCavePath_CreateNew_WithOtherPath_ShouldClone(self):
        path = CavePath()
        node = CaveNode('a')

        path.append(node)
        path.append(node)

        new_path = CavePath(path)

        self.assertNotEqual(path, new_path)
        self.assertDictEqual(path.small_cave_counter, new_path.small_cave_counter)
        self.assertListEqual(path.path_array, new_path.path_array)
        self.assertEqual(path.last_node, new_path.last_node)
        self.assertEqual(path.biggest_count, new_path.biggest_count)

    def testCavePath_Append_WithDefaultNode_ShouldAppendCorrectly(self):
        path = CavePath()
        node = CaveNode('a')

        path.append(node)

        self.assertListEqual(path.path_array, [ node ])
        self.assertEqual(path.last_node, node)

    def testCavePath_Append_WithSmallCaveNode_ShouldIncrementCount(self):
        path = CavePath()
        node = CaveNode('a')

        path.append(node)

        self.assertDictEqual(path.small_cave_counter, { 'a': 1 })

    def testCavePath_Append_WithBigCaveNode_ShouldNotIncrementCount(self):
        path = CavePath()
        node = CaveNode('A')

        path.append(node)

        self.assertDictEqual(path.small_cave_counter, { })

    def testCavePath_GetNodeCount_WithBigCaveNode_ShouldNotHaveCount(self):
        path = CavePath()
        node = CaveNode('A')

        path.append(node)
        output = path.get_node_count(node)

        self.assertEqual(output, 0)

    def testCavePath_GetNodeCount_WithUnexistingCaveNode_ShouldNotHaveCount(self):
        path = CavePath()
        node = CaveNode('a')

        output = path.get_node_count(node)

        self.assertEqual(output, 0)

    def testCavePath_GetNodeCount_WithSmallCaveNode_ShouldHaveCount(self):
        path = CavePath()
        node = CaveNode('a')

        path.append(node)
        path.append(node)
        output = path.get_node_count(node)

        self.assertEqual(output, 2)

    def testCavePath_GetBiggestSmallCaveCount_WithSmallCaveNode_ShouldHaveCorrectCount(self):
        path = CavePath()
        node = CaveNode('a')

        path.append(node)
        path.append(node)
        path.append(CaveNode('b'))
        output = path.get_biggest_small_cave_count()

        self.assertEqual(output, 2)

    def testCavePath_IsIn_WithUnexistingCaveNode_ShouldNotHaveCount(self):
        path = CavePath()
        node = CaveNode('a')

        self.assertFalse(path.is_in(node))

    def testCavePath_IsIn_WithExistingCaveNode_ShouldNotHaveCount(self):
        path = CavePath()
        node = CaveNode('a')

        path.append(node)

        self.assertTrue(path.is_in(node))

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

