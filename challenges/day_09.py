class InputParser():

    def __init__(self, file_input):
        self.file_input = file_input

    def parse_file(self):
        for line in self.file_input:
            yield self.parse_line(line)

    def parse_line(self, line):
        return [ int(char) for char in line if char != '\n' ]

class HeightmapAnalyser:
    def __init__(self, file_input):
        parser = InputParser(file_input)
        self.height_grid = list(parser.parse_file())

    def calculate_total_risk_levels(self):
        lower_points = self.get_lower_points()
        return sum([ num + 1 for num, x, y in lower_points ])

    def get_lower_points(self):
        for y, row in enumerate(self.height_grid):
            for x, num in enumerate(row):
                if (num < self.get_up_value(x, y) 
                    and num < self.get_down_value(x, y)
                    and num < self.get_right_value(x, y)
                    and num < self.get_left_value(x, y)):
                        yield (num, x, y)

    def calculate_basin_size(self, coord, ignore=[]):
        x, y = coord
        if self.get_height(coord) == 9 or coord in ignore:
            return 0
        
        ignore.append(coord)
        current_sum = 1

        next_coords = [
            (x, y+1), #go up
            (x+1, y), #go right
            (x, y-1), #go down
            (x-1, y)  #go left
        ]

        for inn_coord in next_coords:
            current_sum += self.calculate_basin_size(inn_coord, ignore)
        
        return current_sum

    def get_all_basins_sizes(self):
        for _, x, y in self.get_lower_points():
            yield self.calculate_basin_size((x, y), [])

    def get_up_value(self, x, y):
        return self.get_height((x, y-1))

    def get_down_value(self, x, y):
        return self.get_height((x, y+1))

    def get_right_value(self, x, y):
        return self.get_height((x+1, y))

    def get_left_value(self, x, y):
        return self.get_height((x-1, y))

    def get_height(self, coord):
        x, y = coord
        if x == -1 or y == -1 or y >= len(self.height_grid):
            return 9

        row = self.height_grid[y]
        if x == len(row):
            return 9

        return self.height_grid[y][x]
        

def part1_solution(file_input):
    analyser = HeightmapAnalyser(file_input)
    return analyser.calculate_total_risk_levels()

def part2_solution(file_input):
    analyser = HeightmapAnalyser(file_input)
    basins_sizes = list(analyser.get_all_basins_sizes())
    basins_sizes.sort()
    return basins_sizes[-1] * basins_sizes[-2] * basins_sizes[-3]

if __name__ == '__main__':
    with open('inputs/09.txt', 'r') as file_input:
        print(part1_solution(file_input))

    with open('inputs/09.txt', 'r') as file_input:
        print(part2_solution(file_input))
