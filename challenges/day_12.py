import re

class CaveNode:
    UPPERCASE_REGEX = re.compile('[A-Z]')

    def __init__(self, name):
        self.name = name
        self.is_small_cave = not self.UPPERCASE_REGEX.match(name)
        self.connections = []

    def __eq__(self, other):
        if isinstance(other, CaveNode):
            return self.name == other.name
        elif isinstance(other, str):
            return self.name == other
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return f'<{self.name}>'

    def connect_node(self, node):
        self.connections.append(node)
        node.connections.append(self)

class CavePathMapper:

    def __init__(self, max_small_cave_len=1):
        self.start_node = CaveNode('start')
        self.end_node = CaveNode('end')
        self.nodes = [ self.start_node, self.end_node ]
        self.max_small_cave_len = max_small_cave_len

    def read_file_input(self, file_input):
        def get_node(name):
            nonlocal self
            try:
                return self.nodes[self.nodes.index(name)]
            except:
                node = CaveNode(name)
                self.nodes.append(node)
                return node

        for line in file_input:
            splited = line.replace('\n', '').split('-')
            node_1 = get_node(splited[0])
            node_2 = get_node(splited[1])
            node_1.connect_node(node_2)

    def map_paths(self):
        paths = []
        unended_paths = [
            [self.start_node]
        ]
        while len(unended_paths) > 0:
            new_paths = []
            for path in unended_paths:
                last_node = path[-1]
                for connected_node in last_node.connections:
                    cloned_path = path[:]

                    if connected_node == 'start':    
                        continue
                    elif connected_node == 'end':
                        cloned_path.append(connected_node)
                        paths.append(cloned_path)
                    elif not connected_node.is_small_cave or len([node for node in cloned_path if node == connected_node]) < self.max_small_cave_len:
                        cloned_path.append(connected_node)
                        new_paths.append(cloned_path)

            unended_paths = new_paths

        return paths

def part1_solution(file_input):
    mapper = CavePathMapper()
    mapper.read_file_input(file_input)
    return len(mapper.map_paths())
    
def part2_solution(file_input):
    mapper = CavePathMapper(max_small_cave_len=2)
    mapper.read_file_input(file_input)
    return len(mapper.map_paths())

if __name__ == '__main__':
    with open('inputs/12.txt', 'r') as file_input:
        print(part1_solution(file_input))

    with open('inputs/12.txt', 'r') as file_input:
        print(part2_solution(file_input))
