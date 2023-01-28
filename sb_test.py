from board import Board
from sudoku_reader import Sudoku_reader

class SudokuBoard(Board):

    def __init__(self, nums):
        super().__init__(nums)

    

if __name__ == "__main__":
    nums = Sudoku_reader("sudoku_10.csv").next_board()
    board = Board(nums)
    board._set_up_nums().get_nums()
    print(board)
