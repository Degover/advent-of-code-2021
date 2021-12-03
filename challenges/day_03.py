class BitCounter:

    def __init__(self):
        self.count_list = [ [0, 0] for _ in range(12) ]

    def read_input(self, raw_input):
        [ self.increment_count(index % 13, 0 if char == '0' else 1) for index, char in enumerate(raw_input) if char != '\n' ]

    def increment_count(self, bit_pos, bit):
        self.count_list[bit_pos][bit] += 1

    def get_most_common_bits(self):
        return list([0 if bit_0 > bit_1 else 1 for bit_0, bit_1 in self.count_list])

def part1_solution(raw_input):
    counter = BitCounter()
    counter.read_input(raw_input)
    bit_list = counter.get_most_common_bits()

    gamma_rate = 0
    epsilon_rate = 0
    for bit in bit_list:
        gamma_rate = (gamma_rate << 1) | bit

        invert_bit = 0 if bit == 1 else 1
        epsilon_rate = (epsilon_rate << 1) | invert_bit

    return epsilon_rate * gamma_rate

def part2_solution(raw_input):
    return 0

if __name__ == '__main__':
    input = open('inputs/03.txt', 'r').read()

    print(part1_solution(input))
    print(part2_solution(input))
