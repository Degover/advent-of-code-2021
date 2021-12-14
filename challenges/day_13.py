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
        pass

def part1_solution(file_input):
    return 0
    
def part2_solution(file_input):
    return 0

if __name__ == '__main__':
    with open('inputs/13.txt', 'r') as file_input:
        print(part1_solution(file_input))

    with open('inputs/13.txt', 'r') as file_input:
        print(part2_solution(file_input))
