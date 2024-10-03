"""Sudoku generator and solver, credits going to ... for the idea."""
from random import randint
import copy

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
        # return [
        # [0, 0, 0, 0, 0, 0, 0, 0, 0],
        # [0, 7, 2, 0, 0, 1, 0, 3, 0],
        # [1, 8, 0, 0, 0, 6, 7, 2, 0],
        # [7, 0, 0, 2, 0, 0, 5, 6, 0],
        # [5, 0, 0, 0, 0, 0, 0, 0, 2],
        # [0, 6, 9, 0, 0, 3, 0, 0, 7],
        # [0, 2, 4, 3, 0, 0, 0, 9, 1],
        # [0, 3, 0, 6, 0, 0, 4, 5, 0],
        # [0, 0, 0, 0, 0, 0, 0, 0, 0],
        # ]
    
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

    def board_to_code(self, input_board = None):
        code = ''
        if input_board:
            for row in input_board:
                code += ''.join(map(str, row))
        else:
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
            row, col = _empty_cell

        for num in range(1, 10):
            if self.try_solution(row, col, num):
                self.board[row][col] = num

                if self.solve():
                    return self.board
                
            self.board[row][col] = 0

        return False
    

    # randomly populate 3 diagonal 9x9 boxes top left to bottom right. Then use algorithm to solve rest of the board.
    def generate_random_board(self):
        nums = list(range(1,10))
        for row in range(3):
            for col in range(3):
                rand_idx = randint(0, len(nums)-1)
                rand_num = nums.pop(rand_idx)
                self.board[row][col] = rand_num

        nums = list(range(1,10))
        for row in range(3, 6):
            for col in range(3, 6):
                rand_idx = randint(0, len(nums)-1)
                rand_num = nums.pop(rand_idx)
                self.board[row][col] = rand_num

        nums = list(range(1,10))
        for row in range(6, 9):
            for col in range(6, 9):
                rand_idx = randint(0, len(nums)-1)
                rand_num = nums.pop(rand_idx)
                self.board[row][col] = rand_num

        self.__generateCont()

    def __generateCont(self): # uses recursion to finish generating a random board
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] == 0:
                    _num = randint(1, 9)

                    if self.try_solution(row, col, _num):
                        self.board[row][col] = _num

                        if self.solve():
                            self.__generateCont()
                            return self.board

                        self.board[row][col] = 0

        return False

    def solve_board_for_num_solutions(self, row, col):
        for num in range(1, 10):
            if self.try_solution(row, col, num):
                self.board[row][col] = num

                if self.solve():
                    return self.board
                
                self.board[row][col] = 0

            return False
        
    def find_the_indexth_empty_space_for_num_solutions(self, board_element, idx):
        spaces = 1
        for row in range(len(board_element)):
            for col in range(len(board_element[row])):
                if board_element[row][col] == 0:
                    if spaces == idx:
                        return (row, col)
                    
                    spaces += 1

        return False

    def number_solutions(self):
        empty_cells = 0
        solutions = []

        for row in range(0,9):
            for col in range(0,9):
                if self.board[row][col] == 0:
                    empty_cells += 1

        for i in range(1, empty_cells):
            board_clone = copy.deepcopy(self)

            row, col = self.find_the_indexth_empty_space_for_num_solutions(board_clone.board, i)
            clone_solution = board_clone.solve_board_for_num_solutions(row, col)

            clone_code = self.board_to_code(input_board = clone_solution)
            if clone_code != self.board_to_code():
                solutions.append(clone_code)

        print(len(list(set(solutions))))
        return list(set(solutions))
    
    def generate_board_difficulty(self, complete_board, difficulty):
        self.board = copy.deepcopy(complete_board)

        if difficulty == 1:
            squares_to_remove = 36
        elif difficulty == 2:
            squares_to_remove = 46
        elif difficulty == 3:
            squares_to_remove = 52
        else:
            return
        
        # loop through removing randomly from top to bottom
        removed_count = 0
        while removed_count < 4:
            row = randint(0, 2)
            col = randint(0, 2)
            if self.board[row][col] != 0:
                self.board[row][col] = 0
                removed_count += 1

        while removed_count < 8:
            row = randint(3, 6)
            col = randint(3, 8)
            if self.board[row][col] != 0:
                self.board[row][col] = 0
                removed_count += 1

        while removed_count < 12:
            row = randint(6, 8)
            col = randint(6, 8)
            if self.board[row][col] != 0:
                self.board[row][col] = 0
                removed_count += 1

        while removed_count < squares_to_remove:
            print(removed_count)
            row = randint(0, 8)
            col = randint(0, 8)
            if self.board[row][col] != 0:
                num_cache = self.board[row][col]
                self.board[row][col] = 0
                if len(self.number_solutions()) != 1:
                    self.board[row][col] = num_cache
                    continue
                removed_count += 1
        return self, complete_board
    

    def generate_board_to_solve(self, difficulty):
        self.generate_random_board()
        self, complete_board = self.generate_board_difficulty(self.board, difficulty)
        return self.board_to_code(), self.board_to_code(complete_board)

            
# question_board_code = board.generate_board_to_solve(2) # generates a medium level sudoku
# board.display_board()     

if __name__ == '__main__':
        board = Board()
        board.generate_board_to_solve(1)
        board.display_board()
        print(board.board_to_code())