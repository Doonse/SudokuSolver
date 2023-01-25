from sudoku_reader import Sudoku_reader
from square import Square

import numpy as np

class Board:

    def __init__(self):
        # Nums parameter is a 2D list, like what the sudoku_reader returns
        self.n_rows = 9
        self.n_cols = 9
        self.nums = [[None for _ in range(self.n_rows)] for _ in range(self.n_cols)]
    

    # Makes it possible to print a board in a sensible format
    def __str__(self):
        r = "Board with " + str(self.n_rows) + " rows and " + str(self.n_cols) + " columns:\n"
        r += " ["
        for num in self.nums:
            for elem in num:
                r += elem.__str__() + "  "
            r = r[:-2] + "]" + "\n ["
        r = r[:-3] + ""
        return r
    


if __name__ == "__main__":
    reader = Sudoku_reader("sudoku_10.csv")
    print(reader.next_board())
