class TransparentPaper:

    def __init__(self):
        self.points_array = [[False]]
        self.instructions = []
        self.max_y = 0
        self.max_x = 0

    def read_file_input(self, file_input):
        is_instructions = False
        for line in file_input:
            line = line.replace('\n', '')

            if line == '':
                is_instructions = True
            elif is_instructions:
                line = line.replace('fold along ', '')
                axis, level = line.split('=')
                self.instructions.append((axis, int(level)))
            else:
                x_str, y_str = line.split(',')
                self.mark_point(int(x_str), int(y_str))

    def mark_point(self, x, y):
        self.expand_paper(x, y)
        self.points_array[y][x] = True

    def expand_paper(self, x, y):
        if y > self.max_y:
            diff = y - self.max_y
            for _ in range(diff):
                self.points_array.append([False] * (self.max_x+1))
            self.max_y = y

        if x > self.max_x:
            diff = x - self.max_x
            for i in range(self.max_y+1):
                self.points_array[i] += [False] * (diff)
            self.max_x = x

    def fold(self, axis: str, level: int):
        folded_points = []

        if axis == 'x':
            self.max_x = level-1
            folded_points = [ [] for _ in range(self.max_y+1) ]

            first_part = [ row[:level] for row in self.points_array ]
            last_part = [ row[level+1:] for row in self.points_array ]

            first_len = len(first_part[0])
            last_len = len(last_part[0])
            max_len = max([first_len, last_len])
            
            for i in range(max_len):
                for y in range(self.max_y+1):
                    first_x = i - (max_len - first_len)
                    first_point = first_x >= 0 and first_part[y][first_x]

                    last_x = ((i+1) * -1) + (max_len - last_len)
                    last_point = last_x < 0 and last_part[y][last_x]
                    
                    folded_points[y].append(first_point or last_point)

        else:
            self.max_y = level-1

            first_part = self.points_array[:level]
            last_part = self.points_array[level+1:]

            first_len = len(first_part)
            last_len = len(last_part)
            max_len = max([first_len, last_len])
            
            for i in range(max_len):
                folded_points.append([])
                for x in range(self.max_x+1):
                    first_y = i - (max_len - first_len)
                    first_point = first_y >= 0 and first_part[first_y][x]

                    last_y = ((i+1) * -1) + (max_len - last_len)
                    last_point = last_y < 0 and last_part[last_y][x]
                    
                    folded_points[i].append(first_point or last_point)

        self.points_array = folded_points

    def fold_to_instructions(self):
        for axis, level in self.instructions:
            self.fold(axis, level)

def part1_solution(file_input):
    paper = TransparentPaper()
    paper.read_file_input(file_input)

    first_instruct = paper.instructions[0]
    paper.fold(first_instruct[0], first_instruct[1])

    return sum([ sum([ 1 for point in row if point ]) for row in paper.points_array ])
    
def part2_solution(file_input):
    paper = TransparentPaper()
    paper.read_file_input(file_input)
    paper.fold_to_instructions()

    return '\n'.join([ ''.join([ '#' if point else ' ' for point in row ]) for row in paper.points_array ])

if __name__ == '__main__':
    with open('inputs/13.txt', 'r') as file_input:
        print(part1_solution(file_input))

    with open('inputs/13.txt', 'r') as file_input:
        print(part2_solution(file_input))
