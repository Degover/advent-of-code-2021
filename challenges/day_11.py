class OctopusFlashSimulator:
    def __init__(self):
        self.flash_count = 0
        self.octopus_grid = []
        self.MAX_Y = 0
        self.MAX_X = 0

    def read_file_input(self, file_input):
        self.octopus_grid = [ [ int(char) for char in row if char != '\n' ] for row in file_input ]
        self.MAX_Y = len(self.octopus_grid)
        self.MAX_X = max([ len(row) for row in self.octopus_grid ])

    def pass_step(self):
        coords_to_flash = []

        for y, row in enumerate(self.octopus_grid):
            for x, num in enumerate(row):
                if num == 9:
                    self.octopus_grid[y][x] = 0
                    coords_to_flash.append((x, y))
                else:
                    self.octopus_grid[y][x] = num+1

        for x, y in coords_to_flash:
            self.flash_adjacents(x, y)

    def flash_adjacents(self, x, y):
        self.flash_count += 1
        adjacent_xs = [ x+i for i in range(-1, 2) if x+i >= 0 and x+i < self.MAX_X]
        adjacent_ys = [ y+i for i in range(-1, 2) if y+i >= 0 and y+i < self.MAX_Y]

        for adj_x in adjacent_xs:
            for adj_y in adjacent_ys:
                current_val = self.octopus_grid[adj_y][adj_x]
                if (adj_x != x or adj_y != y) and current_val != 0:
                    if current_val == 9:
                        self.octopus_grid[adj_y][adj_x] = 0
                        self.flash_adjacents(adj_x, adj_y)
                    else:
                        self.octopus_grid[adj_y][adj_x] += 1


def part1_solution(file_input):
    simulator = OctopusFlashSimulator()
    simulator.read_file_input(file_input)
    for _ in range(100):
        simulator.pass_step()
    return simulator.flash_count
    

def part2_solution(file_input):
    simulator = OctopusFlashSimulator()
    simulator.read_file_input(file_input)
    
    step = 0
    while not all([ all([num == 0 for num in row]) for row in simulator.octopus_grid ]):
        step += 1
        simulator.pass_step()

    return step

if __name__ == '__main__':
    with open('inputs/11.txt', 'r') as file_input:
        print(part1_solution(file_input))

    with open('inputs/11.txt', 'r') as file_input:
        print(part2_solution(file_input))
