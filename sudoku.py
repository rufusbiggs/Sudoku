"""Sudoku generator and solver, credits going to ... for the idea."""

class Board:
    def __init__(self, code=None):
        
        # create board representation from code
        if code:
            self.code = code

            for row in range(9):
                for column in range(9):
                    self.board[row][column] = code[row + column]
        else:
            self.board = self.new_board()

    # def get_code_from_board(self, board):

    def new_board(self):
        return [[0] * 9] * 9

    def display_board(self):
        for row in self.board:
            print(row)

    
test = Board()

test.display_board()
