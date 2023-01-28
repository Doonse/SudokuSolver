from element import Element
from square import Square
from sudoku_reader import Sudoku_reader

class Board:

    def __init__(self, nums):
        self.n_rows = len(nums[0]) 
        self.n_cols = len(nums)
        self.nums   = [[None for _ in range(self.n_rows)] for _ in range(self.n_cols)]
        self.boxes  = [Element("box") for _ in range(self.n_rows)] # Creates a list of elements with the type box
        self.rows   = [Element("row") for _ in range(self.n_rows)]  # Creates a list of elements with the type row
        self.cols   = [Element("col") for _ in range(self.n_cols)]  # Creates a list of elements with the type col    

    def _find_box(self, row, col):
        return (row // 3) * 3 + col // 3 # Returns the box number

    def _set_up_nums(self, array): # array is a 2D list
        for row in range(self.n_rows): 
            for col in range(self.n_cols): 
                self.nums[row][col] = int(array[row][col]) # Converts string to int and stores it in the board

    def _set_up_elems(self):
        for row in range(self.n_rows):
            for col in range(self.n_cols):
                self.rows[row].add_square(self.nums[row][col])
                self.cols[col].add_square(self.nums[row][col])
                self.boxes[self._find_box(row, col)].add_square(self.nums[row][col])

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
    nums = Sudoku_reader("sudoku_10.csv").next_board()
    board = Board(nums)
    board._set_up_nums(nums)
    print(board)


