class Polymerator:

    def __init__(self):
        self.rules = {}
        self.template = []

    def read_file_input(self, file_input) -> None:
        self.template = list([ char for char in file_input.readline() if char != '\n' ])
        file_input.readline()

        for line in file_input:
            self.rules[(line[0], line[1])] = line[6]

    def step_pair(self, letter_1: str, letter_2: str, steps_left: int):
        mid_letter = self.rules[(letter_1, letter_2)]
        
        print(f'level: {steps_left}; pair: {letter_1}, {letter_2}; result: {mid_letter}')

        if steps_left == 1: #this is the last step
            return [mid_letter]
        else:
            return (self.step_pair(letter_1, mid_letter, steps_left-1) 
                # + [mid_letter] 
                + self.step_pair(mid_letter, letter_2, steps_left-1))

    def test(self, letter_1: str, letter_2: str, steps_left: int):
        last_arr = [letter_1, letter_2]
        arr = []
        for line in range(1, steps_left+1):
            letter_count = (2+line)*2 - 1
            last_row_len = len(last_arr)
            for i in range(last_row_len):
                # if i is 0:
                #     arr.append(letter_1)
                if i is last_row_len-1:
                    arr.append(letter_2)
                else:
                    arr.append(last_arr[i])
                    arr.append(self.rules[(last_arr[i-1], last_arr[i])])

            last_arr = arr
            arr = []
        
        return last_arr#[1:-1]

def part1_solution(file_input):
    return 0
    
def part2_solution(file_input):
    return 0

if __name__ == '__main__':
    with open('inputs/14.txt', 'r') as file_input:
        print(part1_solution(file_input))

    with open('inputs/14.txt', 'r') as file_input:
        print(part2_solution(file_input))
