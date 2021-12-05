class BingoManager:
    def __init__(self):
        self.boards = []
        self.numbers = ''
        self.last_number = ''

    def read_file_input(self, file_input):
        self.numbers = file_input.readline().strip()
        file_input.readline()

        current_board = BingoBoard()
        current_y = 0
        def append_new_board():
            nonlocal self
            nonlocal current_board
            nonlocal current_y

            self.boards.append(current_board)
            current_board = BingoBoard()
            current_y = 0

        for line in file_input:
            if line == '\n':
                append_new_board()
            else:
                current_board.read_row(line, current_y)
                current_y += 1

        append_new_board()

    def calculate_score(self, winner_board):
        num_sum = sum([ sum([ int(num) for num in row if num != '' ]) for row in winner_board.number_grid ])
        return num_sum * int(self.last_number)

    def generate_numbers(self):
        self.last_number = ''
        for char in self.numbers:
            if char != ',':
                self.last_number += char
            else:
                yield self.last_number
                self.last_number = ''

    def get_winner_score(self):
        for number in self.generate_numbers():
            for bingo_board in self.boards:
                bingo_board.mark_number(number)

                if bingo_board.get_is_winner():
                    return self.calculate_score(bingo_board)

    def get_last_winner_score(self):
        remaining_boards = self.boards
        for number in self.generate_numbers():
            winner_boards_idx = []
            for index, bingo_board in enumerate(remaining_boards):
                bingo_board.mark_number(number)
                if bingo_board.get_is_winner():
                    winner_boards_idx.append(index)
            
            if len(remaining_boards) == 1 and len(winner_boards_idx) == 1:
                return self.calculate_score(remaining_boards[0])

            remaining_boards = [ board for index, board in enumerate(remaining_boards) if index not in winner_boards_idx ]

class BingoBoard:
    def __init__(self):
        self.number_grid = [ [ '0' for _ in range(5) ] for _ in range(5) ]

    def mark_number(self, number):
        def mark_number(x, y):
            self.number_grid[y][x] = ''

        for y, row in enumerate(self.number_grid):
            list([ mark_number(x, y) for x, row_num in enumerate(row) if row_num == number])

    def read_row(self, row, y):
        number = ''
        x = 0
        for char in row:
            if char != ' ' and char != '\n':
                number += char
            elif len(number) > 0:
                self.number_grid[y][x] = number
                number = ''
                x += 1

        if len(number) > 0:
            self.number_grid[y][x] = number
        number = ''

    def get_is_winner(self):
        if any([ all([ num == '' for num in row ]) for row in self.number_grid ]):
            return True
        
        if any([ all([ row[i] == '' for row in self.number_grid ]) for i in range(5) ]):
            return True

        return False

def part1_solution(file_input):
    manager = BingoManager()
    manager.read_file_input(file_input)
    return manager.get_winner_score()

def part2_solution(file_input):
    manager = BingoManager()
    manager.read_file_input(file_input)
    return manager.get_last_winner_score()

if __name__ == '__main__':
    with open('inputs/04.txt', 'r') as file_input:
        print(part1_solution(file_input))

    with open('inputs/04.txt', 'r') as file_input:
        print(part2_solution(file_input))
