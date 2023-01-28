from board import Board
from sudoku_reader import Sudoku_reader

class SudokuBoard(Board):

    def __init__(self, nums):
        super().__init__(nums)

    # Solve sudoku board
    def solve(self, array):
        for row in range(self.n_rows):
            for col in range(self.n_cols):
                if array[row][col] == 0:
                    for num in range(1, 10):
                        if self._check_legal(row, col, num):
                            array[row][col] = num
    

if __name__ == "__main__":
    nums = Sudoku_reader("sudoku_10.csv").next_board()
    print(nums)
    board = SudokuBoard(nums)
    board._set_up_nums(nums)
    board._set_up_elems()
    board.solve(nums)
    print(board)



