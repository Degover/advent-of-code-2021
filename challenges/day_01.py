class InputParser:
    def __init__(self, raw_input):
        self.input = raw_input

    def parse(self):
        number = ''

        for char in self.input:
            if(char == '\n'):
                yield int(number)
                number = ''
            else:
                number += char

        yield int(number)

    def accumulate_parse(self):
        parser_gen = self.parse()
        previous_depths = [
            next(parser_gen),
            next(parser_gen)
        ]

        for depth in parser_gen:
            previous_depths.append(depth)
            yield previous_depths[0] + previous_depths[1] + previous_depths[2]
            previous_depths.pop(0)


def part1_solution(raw_input):
    previous_depth = -1
    increase_count = -1
    parser = InputParser(raw_input)
    for depth in parser.parse():
        if(depth > previous_depth):
            increase_count += 1
        
        previous_depth = depth

    return increase_count

def part2_solution(raw_input):
    previous_depth = -1
    increase_count = -1
    parser = InputParser(raw_input)
    for depth in parser.accumulate_parse():
        if(depth > previous_depth):
            increase_count += 1
        
        previous_depth = depth

    return increase_count

if __name__ == '__main__':
    input = open('inputs/01.txt', 'r').read()

    print(part1_solution(input))
    print(part2_solution(input))

