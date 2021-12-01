# -- Common -- #
def parse_raw_input(raw_input):
    number = ''

    for char in raw_input:
        if(char == '\n'):
            yield int(number)
            number = ''
        else:
            number += char

    yield int(number)

# -- Part 1 -- #
def day_01_part_1_solution(raw_input):
    previous_depth = -1
    increase_count = -1
    for depth in parse_raw_input(raw_input):
        if(depth > previous_depth):
            increase_count += 1
        
        previous_depth = depth

    return increase_count

# -- Part 2 -- #
def accumulate_depth(raw_input):
    previous_depths = []
    for depth in parse_raw_input(raw_input):
        previous_depths.append(depth)

        if(len(previous_depths) == 3):
            yield previous_depths[0] + previous_depths[1] + previous_depths[2]
            previous_depths.pop(0)

def day_01_part_2_solution(raw_input):
    previous_depth = -1
    increase_count = -1
    for depth in accumulate_depth(raw_input):
        if(depth > previous_depth):
            increase_count += 1
        
        previous_depth = depth

    return increase_count

if __name__ == '__main__':
    input = open('inputs/01.txt', 'r').read()

    print(day_01_part_1_solution(input))
    print(day_01_part_2_solution(input))

