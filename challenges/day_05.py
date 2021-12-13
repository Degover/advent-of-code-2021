import re

class HotTubesFormation:

    def __init__(self, ignore_diagonal = True):
        self.tubes_grid = [ [ 0 for _ in range(1000) ] for _ in range(1000) ]
        self.ignore_diagonal = ignore_diagonal

    def read_file_input(self, file_input):
        regex = re.compile('(\d{1,3}),(\d{1,3}) -> (\d{1,3}),(\d{1,3})')

        for row in file_input:
            matched = regex.match(row)
            init_coord = (int(matched.group(1)), int(matched.group(2)))
            end_coord = (int(matched.group(3)), int(matched.group(4)))
            self.map_line(init_coord, end_coord)

    def map_line(self, init_coord, end_coord):
        if init_coord[0] == end_coord[0]:
            self.map_vertical_line(init_coord, end_coord)
        elif init_coord[1] == end_coord[1]:
            self.map_horizontal_line(init_coord, end_coord)
        elif not self.ignore_diagonal:
            self.map_diagonal_line(init_coord, end_coord)

    def map_horizontal_line(self, init_coord, end_coord):
        x1, y = init_coord
        x2 = end_coord[0]

        x1, x2 = self.get_sorted(x1, x2)
        for x in range(x1, x2+1):
            self.tubes_grid[y][x] += 1

    def map_vertical_line(self, init_coord, end_coord):
        x, y1 = init_coord
        y2 = end_coord[1]

        y1, y2 = self.get_sorted(y1, y2)
        for y in range(y1, y2+1):
            self.tubes_grid[y][x] += 1

    def map_diagonal_line(self, init_coord, end_coord):
        x1, y1 = init_coord
        x2, y2 = end_coord
        diff = abs(x1 - x2)
        x_factor = 1 if x1 < x2 else -1
        y_factor = 1 if y1 < y2 else -1

        for i in range(diff+1):
            self.tubes_grid[y1 + (i*y_factor)][x1 + (i*x_factor)] += 1

    def get_sorted(self, num1, num2):        
        aux = [num1, num2]
        aux.sort()
        return aux

def part1_solution(file_input):
    formation = HotTubesFormation()
    formation.read_file_input(file_input)
    return sum([ sum([ 1 if count > 1 else 0 for count in row ]) for row in formation.tubes_grid ])
    
def part2_solution(file_input):
    formation = HotTubesFormation(False)
    formation.read_file_input(file_input)
    return sum([ sum([ 1 if count > 1 else 0 for count in row ]) for row in formation.tubes_grid ])

if __name__ == '__main__':
    with open('inputs/05.txt', 'r') as file_input:
        print(part1_solution(file_input))

    with open('inputs/05.txt', 'r') as file_input:
        print(part2_solution(file_input))
