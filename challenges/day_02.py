# -- Common -- #
class Submarine:
    COMMAND_SKIP_COUNT = {
        'f': 8,
        'd': 5,
        'u': 3
    }

    def __init__(self):
        self.depth = 0
        self.horizontal_pos = 0

    def parse_raw_input(self, raw_input):
        index = 0
        max_index = len(raw_input)

        while(index < max_index):
            command = raw_input[index]
            skip_count = self.COMMAND_SKIP_COUNT.get(command)
            quantity = int(raw_input[index + skip_count])

            self.read_command(command, quantity)
            index += skip_count + 2

    def read_command(self, char_command, quantity):
        if(char_command == 'f'):
            self.horizontal_pos += quantity
        elif(char_command == 'u'):
            self.depth -= quantity
        else:
            self.depth += quantity

class AimedSubmarine(Submarine):

    def __init__(self):
        Submarine.__init__(self)
        self.aim = 0

    def read_command(self, char_command, quantity):
        if(char_command == 'f'):
            self.horizontal_pos += quantity
            self.depth += self.aim * quantity
        elif(char_command == 'u'):
            self.aim -= quantity
        else:
            self.aim += quantity
           

 # -- Part 1 -- #
def part1_solution(raw_input):
    submarine = Submarine()
    submarine.parse_raw_input(raw_input)

    return submarine.depth * submarine.horizontal_pos

 # -- Part 2 -- #
def part2_solution(raw_input):
    submarine = AimedSubmarine()
    submarine.parse_raw_input(raw_input)

    return submarine.depth * submarine.horizontal_pos

if __name__ == '__main__':
    input = open('inputs/02.txt', 'r').read()

    print(part1_solution(input))
    print(part2_solution(input))
