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
                if self.source is None:
                    self.source = node
                    self.source.risk_distance = 0
                    self.source.risk_level = 0

                self.target = node
                self.grid[-1].append(node)

                if len(self.grid) > 1:
                    up_node = self.grid[-2][x]
                    up_node.connections.append(node)
                    node.connections.append(up_node)

                if len(self.grid[-1]) > 1:
                    left_node = self.grid[-1][x-1]
                    left_node.connections.append(node)
                    node.connections.append(left_node)

        self.unvisited_nodes.append(self.source)

    def visit_node(self, node: Node):
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

def part1_solution(file_input):
    cave_mapper = CaveMapper()
    cave_mapper.read_file_input(file_input)
    return cave_mapper.calculate_best_route()
    
def part2_solution(file_input):
    return 0

if __name__ == '__main__':
    with open('inputs/15.txt', 'r') as file_input:
        print(part1_solution(file_input))

    with open('inputs/15.txt', 'r') as file_input:
        print(part2_solution(file_input))
