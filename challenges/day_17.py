import re

def calc_triangular_sum(n):
    return int(n*(n+1)/2)

class LaunchSimulator:

    def __init__(self):
        self.range_x = (0, 0)
        self.range_y = (0, 0)

    def read_file_input(self, file_input) -> None:
        in_text = file_input.read()
        match = re.search('x=(-?\d+)\.\.(-?\d+), y=(-?\d+)\.\.(-?\d+)', in_text)

        x_arr = [int(match.group(1)), int(match.group(2))]
        x_arr.sort()
        self.range_x = tuple(x_arr)

        y_arr = [int(match.group(3)), int(match.group(4))]
        y_arr.sort()
        self.range_y = tuple(y_arr)

    def get_max_y_velocity(self) -> int:
        return abs(self.range_y[0]) - 1

    def get_min_x_velocity(self) -> int:
        for i in range(self.range_x[0]):
            if calc_triangular_sum(i) >= self.range_x[0]:
                return i

    def count_all_possibilities(self) -> int:
        y_diff = self.range_y[1] - self.range_y[0]
        x_diff = self.range_x[1] - self.range_x[0]
        stright_shot_count = (y_diff+1) * (x_diff+1)

        max_y = self.get_max_y_velocity()
        min_y = self.range_y[1]+1

        y_dict = {}
        for y_vel in range(min_y, max_y+1):
            y_dict[y_vel] = []
            step = 0
            curr_vel = y_vel
            curr_pos = 0
            while curr_pos >= self.range_y[0]:
                if curr_pos <= self.range_y[1] and curr_pos >= self.range_y[0]:
                    y_dict[y_vel].append(step)

                curr_pos += curr_vel
                curr_vel -= 1
                step += 1
            
        max_x = self.range_x[1]
        min_x = self.get_min_x_velocity()

        count = 0
        max_step = max([ max(arr) for arr in y_dict.values() if arr != [] ])
        for x_vel in range(min_x, max_x+1):
            matched_ys = []
            step = 0
            curr_vel = x_vel
            curr_pos = 0
            while curr_pos <= self.range_x[1] and step <= max_step:
                if curr_pos <= self.range_x[1] and curr_pos >= self.range_x[0]:
                    matched = [ y for y, arr in y_dict.items() if step in arr ]
                    for y in matched:
                        if y not in matched_ys:
                            matched_ys.append(y)

                curr_pos += curr_vel
                if curr_vel > 0:
                    curr_vel -= 1
                step += 1

            count += len(matched_ys)
            
        return stright_shot_count + count

def part1_solution(file_input):
    simulator = LaunchSimulator()
    simulator.read_file_input(file_input)
    max_y = simulator.get_max_y_velocity()
    
    return calc_triangular_sum(max_y)

def part2_solution(file_input):
    simulator = LaunchSimulator()
    simulator.read_file_input(file_input)
    return simulator.count_all_possibilities()

if __name__ == '__main__':
    with open('inputs/17.txt', 'r') as file_input:
        print(part1_solution(file_input))

    with open('inputs/17.txt', 'r') as file_input:
        print(part2_solution(file_input))
