class ChunkChecker:
    CORRUPTED_POINTS = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }

    def __init__(self):
        self.corrupted_count = {
            ')': 0,
            ']': 0,
            '}': 0,
            '>': 0
        }

    def read_file_input(self, file_input):
        return 0

    def check_line(self, line):
        previous_chars = []
        opening_chars = '([{<'

        result = {
            'corrupted': ''
        }
        for char in line:
            if char == '\n': break

            if char in opening_chars:
                previous_chars.append(char)
            else:
                last_char = previous_chars.pop()
                if not (last_char == '(' and char == ')'
                    or last_char == '[' and char == ']'
                    or last_char == '{' and char == '}'
                    or last_char == '<' and char == '>'):
                    result['corrupted'] = char
                    break

        return result

    def get_total_corrupted_points(self):
        return 0
