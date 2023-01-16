from board import Board
from sudoku_reader import Sudoku_reader
from square import Square
from element import Element


class SudokuBoard(Board):

    def __init__(self, nums):
        super().__init__(nums)

    def row(self, nums): # Row of numbers we compare when inserting a number to that row
        pass

    def col(self, nums): # Column of numbers we compare when inserting a number to that column
        pass

    def three_three(self,nums): # 3x3 square of numbers we compare when inserting a number to that square
        pass





if __name__ == "__main__":
    reader = Sudoku_reader("sudoku_10.csv")
    board = Board(reader.next_board())
    print(board)