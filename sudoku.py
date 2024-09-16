"""Sudoku generator and solver, credits going to ... for the idea."""

class Board:
    def __init__(self, code=None):
        self.board = self.new_board()

        # create board representation from code
        if code:
            self.code = code

            idx = 0
            for row in range(9):
                for column in range(9):
                    self.board[row][column] = int(code[idx])
                    idx += 1


    # def get_code_from_board(self, board):

    def new_board(self):
        return [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 2, 0, 0, 1, 0, 3, 0],
        [1, 8, 0, 0, 0, 6, 7, 2, 0],
        [7, 0, 0, 2, 0, 0, 5, 6, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 6, 9, 0, 0, 3, 0, 0, 7],
        [0, 2, 4, 3, 0, 0, 0, 9, 1],
        [0, 3, 0, 6, 0, 0, 4, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    def display_board(self):
        for row in self.board:
            print(row)

    def board_to_code(self):
        code = ''
        for row in self.board:
            code += ''.join(map(str, row))

        return code

    def find_empty_cell(self):
        for row in range(9):
            for column in range(9):
                if self.board[row][column] == 0:
                    return (row, column)
                
        return False
    
    def try_solution(self, row, column, num):
        if self.board[row][column] != 0:
            return False
        # check row
        for val in range(9):
            if self.board[val][column] == num:
                return False
        # check column
        for val in range(9):
            if self.board[row][val] == num:
                return False    
        # check 3x3 box
        _3x3_row = row // 3
        _3x3_col = column // 3
        for i in range(3):
            for j in range(3):
                if self.board[i + (_3x3_row * 3)][j + (_3x3_col * 3)] == num:
                    return False

        return True
    
    def set_cell(self, row, col, num):
        self.board[row][col] = num

    def solve(self):
        _empty_cell = self.find_empty_cell()

        if not _empty_cell:
            return True
        else:
            row, column = _empty_cell

        for num in range(1, 10):
            if self.try_solution(row, column, num):
                self.board[row][column] = num

                if self.solve():
                    return self.board
                
            self.board[row][column] = 0

        return False


    
test = Board()
print('Start')
test.display_board()
print('...')
print('...')
print('...')
input("Hit enter to solve!")
test.solve()
test.display_board()


