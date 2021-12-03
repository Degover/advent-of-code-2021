class BitFilter:

    def __init__(self):
        self.filtered_bits = [ [], [] ]
        self.current_index = 0

    def append_bit_arr(self, bit_array, filtered_arr):
        bit = bit_array[self.current_index]
        filtered_arr[bit].append(bit_array)

    def generate_bit_arrays(self, raw_input):
        bit_array = []
        for char in raw_input:
            if char == '\n':
                yield bit_array
                bit_array = []
                continue

            bit = 0 if char == '0' else 1
            bit_array.append(bit)
        yield bit_array
        
    def read_input(self, raw_input):
        for bit_arr in self.generate_bit_arrays(raw_input):
            self.append_bit_arr(bit_arr, self.filtered_bits)

    def get_bigger_arr(self, arr_0, arr_1):
        if len(arr_0) > len(arr_1):
            return arr_0
        elif len(arr_0) <= len(arr_1):
            return arr_1
        
    def get_smaller_arr(self, arr_0, arr_1):
        if len(arr_0) > len(arr_1):
            return arr_1
        elif len(arr_0) <= len(arr_1):
            return arr_0

    def haha(self, get_arr_fn):
        self.current_index = 1
        current_arr = get_arr_fn(self.filtered_bits[0], self.filtered_bits[1])
        filtered_arr = [ [], [] ]
        while len(current_arr) > 1:
            for bit_arr in current_arr:
                self.append_bit_arr(bit_arr, filtered_arr)

            current_arr = get_arr_fn(filtered_arr[0], filtered_arr[1])
            filtered_arr = [ [], [] ]
            self.current_index += 1

        return current_arr[0]

    def get_oxygen_generator_rating(self):
        return self.haha(lambda arr_0, arr_1: self.get_bigger_arr(arr_0, arr_1))

    def get_co2_scrubber_rating(self):
        return self.haha(lambda arr_0, arr_1: self.get_smaller_arr(arr_0, arr_1))


class BitCounter:

    def __init__(self):
        self.count_list = [ [0, 0] for _ in range(12) ]

    def read_input(self, input):
        [ self.increment_count(index % 13, 0 if char == '0' else 1) for index, char in enumerate(input) if char != '\n' ]

    def increment_count(self, bit_pos, bit):
        self.count_list[bit_pos][bit] += 1

    def get_most_common_bits(self):
        return list([0 if bit_0 > bit_1 else 1 for bit_0, bit_1 in self.count_list])

def bit_arr_to_int(bit_array):
    result = 0
    for bit in bit_array:
        result = (result << 1) | bit

    return result

def part1_solution(raw_input):
    counter = BitCounter()
    counter.read_input(raw_input)
    bit_list = counter.get_most_common_bits()

    gamma_rate = bit_arr_to_int(bit_list)
    epsilon_rate = bit_arr_to_int([ 0 if bit == 1 else 1 for bit in bit_list ])
    
    return epsilon_rate * gamma_rate

def part2_solution(raw_input):
    filter = BitFilter()
    filter.read_input(raw_input)
    oxygen_rating = bit_arr_to_int(filter.get_oxygen_generator_rating())
    co2_rating = bit_arr_to_int(filter.get_co2_scrubber_rating())

    return oxygen_rating * co2_rating

if __name__ == '__main__':
    input = open('inputs/03.txt', 'r').read()

    print(part1_solution(input))
    print(part2_solution(input))
