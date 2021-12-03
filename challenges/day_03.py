class BitCounter:

    def __init__(self):
        self.count_list = [ [0, 0] for _ in range(8) ]

    def read_input(self, raw_input):
        [ self.increment_count(index % 9, 0 if char == '0' else 1) for index, char in enumerate(raw_input) if char != '\n' ]

    def increment_count(self, bit_pos, bit):
        self.count_list[bit_pos][bit] += 1

    def get_most_common_bits(self):
        return list([0 if bit_0 > bit_1 else 1 for bit_0, bit_1 in self.count_list])
