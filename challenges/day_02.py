# -- Common -- #
class SubmarineCommandReader:

    def __init__(self):
        self.depth = 0
        self.horizontal_pos = 0

    def parse_raw_input(self, raw_input):
        command = ''
        previous_char = ''

        for char in raw_input:
            if(char == '\n'):
                self.read_command(command, int(previous_char))
                command = ''
            elif(command == ''):
                command = char

            previous_char = char

        self.read_command(command, int(previous_char))

    def read_command(self, char_command, quantity):
        if(char_command == 'f'):
            self.horizontal_pos += quantity
        elif(char_command == 'u'):
            self.depth -= quantity
        else:
            self.depth += quantity

class SubmarineCommandReaderWithAim(SubmarineCommandReader):

    def __init__(self):
        SubmarineCommandReader.__init__(self)
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
    submarine = SubmarineCommandReader()
    submarine.parse_raw_input(raw_input)

    return submarine.depth * submarine.horizontal_pos

 # -- Part 2 -- #
def part2_solution(raw_input):
    submarine = SubmarineCommandReaderWithAim()
    submarine.parse_raw_input(raw_input)

    return submarine.depth * submarine.horizontal_pos

if __name__ == '__main__':
    input = open('inputs/02.txt', 'r').read()

    print(part1_solution(input))
    print(part2_solution(input))

