from board import Board
from sudoku_reader import Sudoku_reader
from square import Square
from element import Element
import numpy as np


class SudokuBoard(Board):

    def __init__(self, nums):
        super().__init__(nums)
        self.board = nums

    def _set_up_nums(self, nums):
        # Set up the squares on the board (ints into Square objects)
        self.nums = np.array((9, 9)) # obj arr
        for i in range(9):
            for j in range(9):
                num = Square.setNumber(nums[i, j]) # Gjør til obj
                print(num)
                nums[i, j] = num # Append

    def _set_up_elems(self):
        # You should set up links between your squares and elements
        # (rows, columns, boxes)

        pass

    def solveSudoku(self):
    # Your solving algorithm goes here!


        pass

a = SudokuBoard()
print(a)
    








if __name__ == "__main__":
    reader = Sudoku_reader("sudoku_10.csv")
    board = Board(reader.next_board())
    print(board)