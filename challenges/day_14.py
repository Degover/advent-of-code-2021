class Polymerator:

    def __init__(self):
        self.rules = {}
        self.template = []

    def read_file_input(self, file_input) -> None:
        self.template = list([ char for char in file_input.readline() if char != '\n' ])
        file_input.readline()

        for line in file_input:
            self.rules[(line[0], line[1])] = line[6]

    def do_steps(self, total_stelps: int) -> list[str]:
        last_arr = self.template
        arr = []
        for _ in range(1, total_stelps+1):

            last_row_len = len(last_arr)
            for i in range(last_row_len):
                if i == last_row_len-1:
                    arr.append(self.template[-1])
                else:
                    arr.append(last_arr[i])
                    arr.append(self.rules[(last_arr[i], last_arr[i+1])])

            last_arr = arr
            arr = []
        
        return last_arr

def part1_solution(file_input):
    polymerator = Polymerator()
    polymerator.read_file_input(file_input)
    result = polymerator.do_steps(10)

    counter = {}
    def increment_count(letter: str):
        nonlocal counter
        if letter in counter:
            counter[letter] += 1
        else:
            counter[letter] = 1

    list([ increment_count(letter) for letter in result])
    counts = counter.values()
    return max(counts) - min(counts)
    
def part2_solution(file_input):
    polymerator = Polymerator()
    polymerator.read_file_input(file_input)
    result = polymerator.do_steps(40)

    counter = {}
    def increment_count(letter: str):
        nonlocal counter
        if letter in counter:
            counter[letter] += 1
        else:
            counter[letter] = 1

    list([ increment_count(letter) for letter in result])
    counts = counter.values()
    return max(counts) - min(counts)

if __name__ == '__main__':
    with open('inputs/14.txt', 'r') as file_input:
        print(part1_solution(file_input))

    with open('inputs/14.txt', 'r') as file_input:
        print(part2_solution(file_input))
