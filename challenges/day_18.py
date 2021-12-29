from math import floor, ceil

class SnailfishNumber:

    @classmethod
    def from_string(self, in_str: str) -> 'SnailfishNumber':
        arr = []
        for char in in_str:
            if char == ',' or char == '\n':
                continue
            elif char == '[' or char == ']':
                arr.append(char)
            else:
                arr.append(int(char))

        return SnailfishNumber(arr)

    def __init__(self, arr):
        self.arr = arr

    def __repr__(self):
        joined = ''.join([str(char) for char in self.arr])
        return f'<{joined}>'

    def calc_magnitude(self) -> int:
        queue = []
        for char in self.arr:
            if isinstance(char, int):
                queue.append(char)
            elif char == ']':
                right_val = queue.pop()
                left_val = queue.pop()
                queue.append(3*left_val + 2*right_val)

        return queue[0]

    def reduce(self) -> None:
        continue_loop = True
        last_op = '-'
        while continue_loop:
            level = 0
            continue_loop = False

            all_str = [ str(char) for char in self.arr ]
            print(last_op + ',' + ','.join(all_str))

            for index, char in enumerate(self.arr):
                if char == '[':
                    level += 1
                elif char == ']':
                    level -= 1

                if level == 5:
                    last_op = 'Expl'
                    left_val = self.arr[index+1]
                    first_half = self.arr[:index]
                    for i in range(index):
                        neg_index = i*-1 -1
                        if isinstance(first_half[neg_index], int):
                            first_half[neg_index] += left_val
                            break

                    right_val = self.arr[index+2]
                    scnd_half = self.arr[index+4:]
                    for i in range(len(scnd_half)):
                        if isinstance(scnd_half[i], int):
                            scnd_half[i] += right_val
                            break

                    self.arr = first_half + [0] + scnd_half
                    continue_loop = True
                    break
                elif isinstance(char, int) and char > 9:
                    last_op = 'Spl'
                    half = char / 2
                    left_val = int(floor(half))
                    right_val = int(ceil(half))

                    first_half = self.arr[:index]
                    scnd_half = self.arr[index+1:]

                    self.arr = first_half + ['[',left_val, right_val,']'] + scnd_half
                    continue_loop = True
                    break

class SnailfishCalculator:

    def __init__(self):
        self.numbers = []

    def read_file_input(self, file_input):
        for line in file_input:
            self.numbers.append(SnailfishNumber.from_string(line))

    def sum_all(self) -> SnailfishNumber:
        last_num = self.numbers.pop(0)
        while len(self.numbers) > 0:
            number = self.numbers.pop(0)
            last_num = SnailfishNumber(['['] + last_num.arr + number.arr + [']'])
            last_num.reduce()

        return last_num

def part1_solution(file_input):
    calculator = SnailfishCalculator()
    calculator.read_file_input(file_input)
    resulting_number = calculator.sum_all()
    return resulting_number.calc_magnitude()

def part2_solution(file_input):
    return 0

if __name__ == '__main__':
    with open('inputs/18.txt', 'r') as file_input:
        print(part1_solution(file_input))

    with open('inputs/18.txt', 'r') as file_input:
        print(part2_solution(file_input))
