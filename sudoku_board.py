from board import Board
from sudoku_reader import Sudoku_reader
from square import Square
from element import Element
import numpy as np


class SudokuBoard(Board):

    def __init__(self, board):
        super().__init__()
        self.game_board = board # Board, partially filled arrays
        self.obj_nums = np.zeros((9, 9)) # empty array
        pass




if __name__ == "__main__":
    pass
