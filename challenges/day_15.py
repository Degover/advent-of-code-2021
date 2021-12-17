from functools import total_ordering

@total_ordering
class Node:

    def __init__(self, risk_level: int, x: int=0, y: int=0):
        self.risk_level: int = risk_level
        self.risk_distance: int = float('inf')
        self.parent: Node | None = None
        self.connections: list[Node] = []
        self.was_visited = False
        self.x = x
        self.y = y

    def __lt__(self, other):
        return self.risk_distance < other.risk_distance

    def __eq__(self, other):
        return self is other

    def __repr__(self):
        return f'<({self.x}, {self.y}): {self.risk_level}>'

class CaveMapper:

    def __init__(self):
        self.grid: list[list[Node]] = []
        self.unvisited_nodes: list[Node] = []
        self.source: Node = None
        self.target: Node = None

    def read_file_input(self, file_input) -> None:
        for line in file_input:
            self.grid.append([])

            for x, char in enumerate(line):
                if char == '\n':
                    break

                node = Node(int(char), x, len(self.grid)-1)
                self.grid[-1].append(node)

        self.source = self.grid[0][0]
        self.source.risk_distance = 0

        self.target = self.grid[-1][-1]

        self.map_node_connections()
        self.unvisited_nodes.append(self.source)

    def map_node_connections(self) -> None:
        for y, row in enumerate(self.grid):
            for x, node in enumerate(row):
                node.connections = []
                if y > 0:
                    up_node = self.grid[y-1][x]
                    up_node.connections.append(node)
                    node.connections.append(up_node)

                if x > 0:
                    left_node = self.grid[y][x-1]
                    left_node.connections.append(node)
                    node.connections.append(left_node)

    def visit_node(self, node: Node) -> None:
        self.unvisited_nodes.remove(node)
        node.was_visited = True

        for connected_node in node.connections:
            if not connected_node.was_visited and not any([ connected_node is node for node in self.unvisited_nodes ]):
                self.unvisited_nodes.append(connected_node)

            curr_distance = node.risk_distance + connected_node.risk_level
            if curr_distance < connected_node.risk_distance:
                connected_node.risk_distance = int(curr_distance)
                connected_node.parent = node
                
    def calculate_best_route(self) -> int:
        current_node: Node = None

        while len(self.unvisited_nodes) > 0 and current_node is not self.target:
            current_node = min(self.unvisited_nodes)
            self.visit_node(current_node)

        return self.target.risk_distance

    def expand_map(self) -> None:
        first_tile = list([ row.copy() for row in self.grid ])
        tile_height = len(first_tile[0])
        new_grid = list([ [] for _ in range(tile_height) ])
        for i in range(5):
            for y, row in enumerate(first_tile):
                for x, node in enumerate(row):
                    risk_level = node.risk_level + i
                    if risk_level > 9:
                        risk_level -= 9
                    new_grid[y].append(Node(risk_level, x + i*len(row), y))

        first_tile_row = list([ row.copy() for row in new_grid ])
        for i in range(1, 5):
            for y, row in enumerate(first_tile_row):
                new_grid.append([])

                for x, node in enumerate(row):
                    risk_level = node.risk_level + i
                    if risk_level > 9:
                        risk_level -= 9
                    new_grid[-1].append(Node(risk_level, x, y + i*tile_height))

        self.grid = new_grid
        self.map_node_connections()

        self.source = self.grid[0][0]
        self.source.risk_distance = 0

        self.target = self.grid[-1][-1]

        self.unvisited_nodes = [self.source]

    def print_paths(self) -> None:
        '''Debug use only'''
        simple_map = [ [ (
            node.risk_distance,
            node.parent is not None and node.parent.x > node.x,
            node.parent is not None and node.parent.y > node.y
        ) for node in row ] for row in self.grid ]

        final_str = ''
        for row in simple_map:
            for i in range(2):
                for distance, is_left, is_above in row:
                    if i == 0:
                        char = 'v' if is_above else ''
                        final_str += f'\t\t{char}'
                    else:
                        char = '>' if is_left else ''
                        final_str += f'\t{char}\t{distance}'
                final_str += '\n'
            final_str += '\n'

        print(final_str)

def part1_solution(file_input):
    cave_mapper = CaveMapper()
    cave_mapper.read_file_input(file_input)
    return cave_mapper.calculate_best_route()
    
def part2_solution(file_input):
    cave_mapper = CaveMapper()
    cave_mapper.read_file_input(file_input)
    cave_mapper.expand_map()
    return cave_mapper.calculate_best_route()

if __name__ == '__main__':
    with open('inputs/15.txt', 'r') as file_input:
        print(part1_solution(file_input))

    with open('inputs/15.txt', 'r') as file_input:
        print(part2_solution(file_input))
