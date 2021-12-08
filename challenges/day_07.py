class CrabManager:

    def __init__(self):
        self.crabs_positions = []

    def read_file_input(self, file_input):
        input = file_input.read()
        self.crabs_positions = [ int(num) for num in input.split(',') ]

    def get_final_position(self):
        self.crabs_positions.sort()
        length = len(self.crabs_positions)

        median = 0
        if length % 2 == 1:
            pos = int((length + 1) / 2) - 1
            median = self.crabs_positions[pos]
        else:
            pos = int(length / 2) - 1
            median = (self.crabs_positions[pos] + self.crabs_positions[pos + 1]) / 2

        return median

    def get_total_fuel_consumption(self):
        final_pos = self.get_final_position()
        return sum([ abs(pos - final_pos) for pos in self.crabs_positions ])

class CompleteCrabManager(CrabManager):
    def get_total_fuel_consumption(self):
        begin = min(self.crabs_positions)
        end = max(self.crabs_positions)
        smallest_fuel_consumption = self.get_total_fuel_consumption_for_given_pos(begin)
        for i in range(begin + 1, end):
            fuel_consumption = self.get_total_fuel_consumption_for_given_pos(i)
            if fuel_consumption < smallest_fuel_consumption:
                smallest_fuel_consumption = fuel_consumption

        return smallest_fuel_consumption

    def get_total_fuel_consumption_for_given_pos(self, final_pos):
        return sum([ self.calculate_triangular_sum(abs(pos - final_pos)) for pos in self.crabs_positions ])

    def calculate_triangular_sum(self, number):
        return (number * (number+1)) / 2

def part1_solution(file_input):
    manager = CrabManager()
    manager.read_file_input(file_input)
    return manager.get_total_fuel_consumption()

def part2_solution(file_input):
    manager = CompleteCrabManager()
    manager.read_file_input(file_input)
    return manager.get_total_fuel_consumption()

if __name__ == '__main__':
    with open('inputs/07.txt', 'r') as file_input:
        print(part1_solution(file_input))

    with open('inputs/07.txt', 'r') as file_input:
        print(part2_solution(file_input))
