Counter = dict[str:int]
MemorizedCount = dict[tuple[str,str,int]:Counter]

class Polymerator:

    def __init__(self):
        self.rules = {}
        self.template = []
        self.letter_counts: Counter = {}
        self.memorized_iters: MemorizedCount = {}

    def read_file_input(self, file_input) -> None:
        self.template = list([ char for char in file_input.readline() if char != '\n' ])
        file_input.readline()

        for line in file_input:
            self.rules[(line[0], line[1])] = line[6]

    def count_by_steps(self, step_count: int) -> Counter:
        for letter in self.template:
            self.count_letter(letter)

        for i in range(len(self.template)-1):
            self.step_into(self.template[i], self.template[i+1], step_count)

        return self.letter_counts

    def step_into(self, letter_1: str, letter_2: str, steps_left: int) -> None:
        mid_letter = self.rules[(letter_1, letter_2)]
        self.count_letter(mid_letter)
        
        memorized_key = (letter_1, letter_2, steps_left)
        if memorized_key in self.memorized_iters:
            counter = self.memorized_iters[memorized_key]
            self.sum_counter(counter)
            return

        if steps_left == 1:
            return
        else:
            current_count = self.letter_counts.copy()

            self.step_into(letter_1, mid_letter, steps_left-1)
            self.step_into(mid_letter, letter_2, steps_left-1)

            self.memorize_iter(letter_1, letter_2, steps_left, current_count, self.letter_counts)

    def memorize_iter(self, letter_1: str, letter_2: str, steps_left: int, old_counts: Counter, new_counts: Counter) -> None:
        diff_count: Counter = {}
        for letter, count in new_counts.items():
            if letter in old_counts:
                if count > old_counts[letter]:
                    diff_count[letter] = count - old_counts[letter]
            else:
                diff_count[letter] = count
            
        self.memorized_iters[(letter_1, letter_2, steps_left)] = diff_count

    def sum_counter(self, counter: Counter) -> None:
        for letter, count in counter.items():
            if letter in self.letter_counts:
                self.letter_counts[letter] += count
            else:
                self.letter_counts[letter] = count

    def count_letter(self, letter: str) -> None:
        if letter in self.letter_counts:
            self.letter_counts[letter] += 1
        else:
            self.letter_counts[letter] = 1

def part1_solution(file_input):
    polymerator = Polymerator()
    polymerator.read_file_input(file_input)
    result = polymerator.count_by_steps(10)

    counts = result.values()
    return max(counts) - min(counts)
    
def part2_solution(file_input):
    polymerator = Polymerator()
    polymerator.read_file_input(file_input)
    result = polymerator.count_by_steps(40)

    counts = result.values()
    return max(counts) - min(counts)

if __name__ == '__main__':
    with open('inputs/14.txt', 'r') as file_input:
        print(part1_solution(file_input))

    with open('inputs/14.txt', 'r') as file_input:
        print(part2_solution(file_input))
