class LanternFishManager:

    def __init__(self):
        self.fish_countdowns = [0] * 9

    def read_file_input(self, file_input):
        input = file_input.read()
        parsed_input = [ int(char) for char in input if char != ',' ]

        for age in parsed_input:
            self.fish_countdowns[age] += 1
        
    def pass_day(self):
        age_zero_count = self.fish_countdowns.pop(0)
        self.fish_countdowns.append(age_zero_count)
        self.fish_countdowns[6] += age_zero_count

    def get_total_fishes(self):
        return sum(self.fish_countdowns)
            
def part1_solution(file_input):
    manager = LanternFishManager()
    manager.read_file_input(file_input)
    
    for _ in range(80):
        manager.pass_day()

    return manager.get_total_fishes()

def part2_solution(file_input):
    manager = LanternFishManager()
    manager.read_file_input(file_input)
    
    for _ in range(256):
        manager.pass_day()

    return manager.get_total_fishes()

if __name__ == '__main__':
    with open('inputs/06.txt', 'r') as file_input:
        print(part1_solution(file_input))

    with open('inputs/06.txt', 'r') as file_input:
        print(part2_solution(file_input))
