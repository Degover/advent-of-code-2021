import unittest
from challenges.day_15 import *
from test.file_stub import FileStub

test_input = [
    '1163751742',
    '1381373672',
    '2136511328',
    '3694931569',
    '7463417111',
    '1319128137',
    '1359912421',
    '3125421639',
    '1293138521',
    '2311944581'
]

class Day_15_Tests(unittest.TestCase):
    
    def testNode_CreateNew_WithDefaultArgument_ShouldCreateCorrectly(self):
        node = Node(9)

        self.assertEqual(node.risk_level, 9)
        self.assertEqual(node.risk_distance, float('inf'))
        self.assertIsNone(node.parent)
        self.assertListEqual(node.connections, [])
        self.assertFalse(node.was_visited)

    def testCaveMapper_ReadFileInput_WithSimpleInput_ShouldReadCorrectly(self):
        file_stub = FileStub()
        file_stub.set_array([
            '123',
            '456'
        ])
        cave_mapper = CaveMapper()

        cave_mapper.read_file_input(file_stub)

        nodes_as_num = lambda nodes : [ node.risk_level for node in nodes ]

        expected_grid = [ [0, 2, 3], [4, 5, 6] ]
        current_grid = [ nodes_as_num(row) for row in cave_mapper.grid ]
        self.assertListEqual(current_grid, expected_grid)
        self.assertEqual(cave_mapper.unvisited_nodes, [cave_mapper.source])
        self.assertEqual(cave_mapper.source.risk_level, 0)
        self.assertEqual(cave_mapper.source.risk_distance, 0)
        self.assertEqual(cave_mapper.target.risk_level, 6)

        self.assertListEqual(nodes_as_num(cave_mapper.grid[0][0].connections), [2, 4])
        self.assertListEqual(nodes_as_num(cave_mapper.grid[0][1].connections), [0, 3, 5])
        self.assertListEqual(nodes_as_num(cave_mapper.grid[0][2].connections), [2, 6])
        self.assertListEqual(nodes_as_num(cave_mapper.grid[1][0].connections), [0, 5])
        self.assertListEqual(nodes_as_num(cave_mapper.grid[1][1].connections), [2, 4, 6])
        self.assertListEqual(nodes_as_num(cave_mapper.grid[1][2].connections), [3, 5])

    def testCaveMapper_VisitNode_WithNode_ShouldVisitItCorrectly(self):
        node = Node(1)
        node.risk_distance = 5

        node_a = Node(2)
        node_b = Node(3)
        node.connections = [
            node_a,
            node_b
        ]
        cave_mapper = CaveMapper()
        cave_mapper.unvisited_nodes = [node]
        
        cave_mapper.visit_node(node)

        self.assertListEqual(cave_mapper.unvisited_nodes, node.connections)
        self.assertEqual(node_a.risk_distance, node.risk_distance + node_a.risk_level)
        self.assertEqual(node_b.risk_distance, node.risk_distance + node_b.risk_level)
        self.assertEqual(node_a.parent, node)
        self.assertEqual(node_b.parent, node)
        self.assertTrue(node.was_visited)

    def testPart1_RunSolution_WithExampleInput_ShouldBeCorrect(self):
        file_stub = FileStub()
        file_stub.set_array(test_input)

        output = part1_solution(file_stub)

        expected_output = 40
        self.assertEqual(output, expected_output)

    def testPart2_RunSolution_WithExampleInput_ShouldBeCorrect(self):
        file_stub = FileStub()
        file_stub.set_array(test_input)

        output = part2_solution(file_stub)

        expected_output = 315
        self.assertEqual(output, expected_output)