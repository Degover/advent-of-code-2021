class DigitChecker:
    def __init__(self):
        self.digit_map = {}

    def map_digits(self, input_digits):
        simple_map = {}
        len_dict = {
            5: [], # 2, 3, 5
            6: []  # 0, 6, 9
        }
        for digit in input_digits:
            if len(digit) == 2:
                simple_map['1'] = digit
            elif len(digit) == 3:
                simple_map['7'] = digit
            elif len(digit) == 4:
                simple_map['4'] = digit
            elif len(digit) == 7:
                simple_map['8'] = digit
            else:
                len_dict[len(digit)].append(digit)
        
        def count_equal_segs(digit1, digit2):
            count = 0
            for char in digit1:
                if char in digit2: count += 1
            return count

        for digit in len_dict[6]:
            if count_equal_segs(digit, simple_map['4']) == 4:
                simple_map['9'] = digit
            elif count_equal_segs(digit, simple_map['1']) == 2:
                simple_map['0'] = digit
            else:
                simple_map['6'] = digit

        for digit in len_dict[5]:
            if count_equal_segs(digit, simple_map['6']) == 5:
                simple_map['5'] = digit
            elif count_equal_segs(digit, simple_map['1']) == 2:
                simple_map['3'] = digit
            else:
                simple_map['2'] = digit

        self.digit_map = { self.map_to_int_tuple(digit): num for num, digit in simple_map.items() }

    def get_output(self, output_digits):
        out = ''

        for digit in output_digits:
            mapped_digit = self.map_to_int_tuple(digit)
            out += self.digit_map[mapped_digit]

        return int(out)

    def map_to_int_tuple(self, digit):
        get_val = lambda char: 1 if char in digit else 0
        return (
            get_val('a'),
            get_val('b'),
            get_val('c'),
            get_val('d'),
            get_val('e'),
            get_val('f'),
            get_val('g')
        )

    def read_line(self, line):
        self.digit_map = {}
        split_line = line.split(' ')
        pipe_index = split_line.index('|')

        input_digits = split_line[:pipe_index]
        output_digits = split_line[pipe_index+1:]

        self.map_digits(input_digits)
        return self.get_output(output_digits)


def part1_solution(file_input):
    digits_counts = [2, 3, 4, 7]
    count = 0
    for line in file_input:
        pipe_index = line.find('|')
        output_digits = line.replace('\n', '')[pipe_index+2:].split(' ')
        current_count = sum([ 1 if len(digit) in digits_counts else 0 for digit in output_digits ])
        count += current_count

    return count

def part2_solution(file_input):
    checker = DigitChecker()
    total = 0
    for line in file_input:
        total += checker.read_line(line)

    return total

if __name__ == '__main__':
    with open('inputs/08.txt', 'r') as file_input:
        print(part1_solution(file_input))

    with open('inputs/08.txt', 'r') as file_input:
        print(part2_solution(file_input))
