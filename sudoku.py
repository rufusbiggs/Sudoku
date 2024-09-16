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
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
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


    
test = Board()

test.display_board()

print(test.board_to_code())
