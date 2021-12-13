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

class CavePath:

    def __init__(self, path=None):
        if path:
            self.path_array = path.path_array[:]
            self.last_node = path.last_node
            self.small_cave_counter = path.small_cave_counter.copy()
            self.biggest_count = path.biggest_count
        else:
            self.path_array = []
            self.last_node = None
            self.small_cave_counter = {}
            self.biggest_count = 0

    def is_in(self, node: CaveNode):
        return node in self.path_array

    def append(self, node: CaveNode):
        self.path_array.append(node)
        self.last_node = node
        if node.is_small_cave:
            if node.name in self.small_cave_counter:
                self.small_cave_counter[node.name] += 1
            else:
                self.small_cave_counter[node.name] = 1
            count = self.small_cave_counter[node.name]
            if count > self.biggest_count:
                self.biggest_count = count

    def get_biggest_small_cave_count(self):
        return self.biggest_count

    def get_node_count(self, node: CaveNode):
        if node.name in self.small_cave_counter:
            return self.small_cave_counter[node.name]
        else:
            return 0

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
        starting_path = CavePath()
        starting_path.append(self.start_node)

        paths: list[CavePath] = []
        unended_paths: list[CavePath] = [ starting_path ]
        while len(unended_paths) > 0:
            new_paths: list[CavePath] = []
            for path in unended_paths:
                last_node = path.last_node
                for connected_node in last_node.connections:
                    cloned_path = CavePath(path)

                    if connected_node == 'start':    
                        continue
                    elif connected_node == 'end':
                        cloned_path.append(connected_node)
                        paths.append(cloned_path)
                    elif (not connected_node.is_small_cave
                        or path.get_node_count(connected_node) == 0
                        or path.get_biggest_small_cave_count() < self.max_small_cave_len):
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
