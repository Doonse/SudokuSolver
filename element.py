import numpy as np
from square import Square
from sudoku_board import SudokuBoard
from sudoku_reader import Sudoku_reader


class Element():

    def __init__(self, array):
        self.array = array
        self.row_squares = []
        self.col_squares = []
        self.box_squares = []
        self.row_nums = []
        self.col_nums = []
        self.box_nums = []

    def set_row_squares(self, array):
        for i in range(9):
            self.row_squares.append(array[i]) # 1x9 array

    def set_col_squares(self, array):
        for i in range(9):
            self.col_squares.append(array[:, i]) # 9x1 array

    def set_box_squares(self, array):
        for i in range(3):
            for j in range(3):
                self.box_squares.append(array[i*3 : (i+1)*3, j*3 : (j+1)*3]) # 3x3 array

    def set_row_nums(self, array):
        for i in range(9):
            self.row_nums.append(array[i])

    def set_col_nums(self, array):
        for i in range(9):
            self.col_nums.append(array[:, i])

    def set_box_nums(self, array):
        for i in range(3):
            for j in range(3):
                self.box_nums.append(array[i*3 : (i+1)*3, j*3 : (j+1)*3])

    def get_row_squares(self):
        return self.row_squares

    def get_col_squares(self):
        return self.col_squares

    def get_box_squares(self):
        return self.box_squares

    def get_num(self):
        return self.array




if __name__ == "__main__":
    reader = Sudoku_reader("sudoku_10.csv")
    nums_array = reader.next_board()
    obj_nums = SudokuBoard().set_num(nums_array)
    elem = Element(obj_nums)
    elem.set_row_squares(obj_nums)
    elem.set_col_squares(obj_nums)
    elem.set_box_squares(obj_nums)
    elem.set_row_nums(obj_nums)
    elem.set_col_nums(obj_nums)
    elem.set_box_nums(obj_nums)
    print(elem.get_row_squares())
    print(elem.get_col_squares())
    print(elem.get_box_squares())

