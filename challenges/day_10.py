class ChunkChecker:
    CORRUPTED_POINTS = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    COMPLETION_POINTS = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }

    def __init__(self):
        self.corrupted_count = { ')': 0, ']': 0, '}': 0, '>': 0 }
        self.completion_scores = []

    def read_file_input(self, file_input):
        for line in file_input:
            result = self.check_line(line)

            corrupted_char = result['corrupted']
            completion_str = result['completion']

            if corrupted_char != '':
                self.corrupted_count[corrupted_char] += 1
            else:
                score = self.calculate_completion_str_points(completion_str)
                self.completion_scores.append(score)
            
    def check_line(self, line):
        previous_chars = []
        opening_chars = '([{<'
        completion_chars = { '(': ')', '[': ']', '{': '}', '<': '>' }

        result = {
            'corrupted': '',
            'completion': ''
        }
        for char in line:
            if char == '\n': break

            if char in opening_chars:
                previous_chars.append(char)
            else:
                last_char = previous_chars.pop()
                if completion_chars[last_char] != char:
                    result['corrupted'] = char
                    break

        while len(previous_chars) > 0:
            char = previous_chars.pop()
            result['completion'] += completion_chars[char]

        return result

    def calculate_completion_str_points(self, completion_string):
        total_score = 0
        for char in completion_string:
            char_val = self.COMPLETION_POINTS[char]
            total_score *= 5
            total_score += char_val

        return total_score

    def get_total_corrupted_points(self):
        total = 0
        for key, count in self.corrupted_count.items():
            total += self.CORRUPTED_POINTS[key] * count

        return total

def part1_solution(file_input):
    checker = ChunkChecker()
    checker.read_file_input(file_input)
    return checker.get_total_corrupted_points()

def part2_solution(file_input):
    checker = ChunkChecker()
    checker.read_file_input(file_input)
    checker.completion_scores.sort()
    middle_index = int(len(checker.completion_scores)/2)

    return checker.completion_scores[middle_index]

if __name__ == '__main__':
    with open('inputs/10.txt', 'r') as file_input:
        print(part1_solution(file_input))

    with open('inputs/10.txt', 'r') as file_input:
        print(part2_solution(file_input))
