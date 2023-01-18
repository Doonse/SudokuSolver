from board import Board
from sudoku_reader import Sudoku_reader
from square import Square
import numpy as np


class SudokuBoard(Board):

    def __init__(self): # initializes board and squares
        super().__init__()
        self.board = None
        self.squares = None
        self.elements = None

    def set_squares(self): # sets 2D array of Square objects to board 
        squares = np.zeros((9, 9), dtype=object) 
        for i in range(9):
            for j in range(9):
                squares[i][j] = Square(self.board[i][j])
        return squares

    def set_num(self, array): # sets 2D array of numbers to board 
        self.board = array
        self.squares = self.set_squares()
        return self.squares

    def set_elem(self, array):
        self.elements = array

    def get_elem(self):
        return self.elements


    def get_squares(self): # returns 2D array of Square objects
        return self.squares

    def __str__(self): # prints 2D array of numbers
        return str(self.board)


if __name__ == "__main__":
    reader = Sudoku_reader("sudoku_10.csv") # path to csv file with sudoku board numbers
    nums_array = reader.next_board() # 2D array of numbers
    print(nums_array)
    # obj_nums = SudokuBoard().set_num(nums_array) # 2D array of Square objects 
    # print(obj_nums) # prints 2D array of numbers 
