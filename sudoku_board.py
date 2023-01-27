from board import Board
from square import Square
from element import Element
import numpy as np 

class SudokuBoard(Board):

    def __init__(self):
        super().__init__()
        self.board = [[ Square() for j in range(9)] for i in range(9)]
        self.box_array = []
        self.col_array = np.zeros(9)
        self.row_array = np.zeros(9)

    # Find box number
    def find_box(self, row_nr, col_nr):
        if row_nr < 3:                              # Top 3 rows
            if col_nr < 3:
                self.box_nr = 0                          # Top left box
            elif col_nr < 6 and col_nr >= 3:
                self.box_nr = 1                          # Top middle box
            else:
                self.box_nr = 2                          # Top right box

        elif row_nr < 6 and row_nr >= 3:          # Middle 3 rows
            if col_nr < 3:
                self.box_nr = 3                          # Middle left box
            elif col_nr < 6 and col_nr >= 3:        
                self.box_nr = 4                          # Middle middle box
            else:
                self.box_nr = 5                          # Middle right box

        else:                                         # Bottom 3 rows
            if col_nr < 3:
                self.box_nr = 6                          # Bottom left box
            elif col_nr < 6 and col_nr >= 3:     
                self.box_nr = 7                          # Bottom middle box    
            else:
                self.box_nr = 8                          # Bottom right box
    
    # # Store box of a square
    def store_box(self, nums):
        for i in range(9):
            for j in range(9):
                if self.box_nr == 0:
                    if i < 3 and j < 3:
                        self.box_array.append(nums[i][j])
                elif self.box_nr == 1:
                    if i < 3 and j < 6 and j >= 3:
                        self.box_array.append(nums[i][j])
                elif self.box_nr == 2:
                    if i < 3 and j < 9 and j >= 6:
                        self.box_array.append(nums[i][j])
                elif self.box_nr == 3:
                    if i < 6 and i >= 3 and j < 3:
                        self.box_array.append(nums[i][j])
                elif self.box_nr == 4:
                    if i < 6 and i >= 3 and j < 6 and j >= 3:
                        self.box_array.append(nums[i][j])
                elif self.box_nr == 5:
                    if i < 6 and i >= 3 and j < 9 and j >= 6:
                        self.box_array.append(nums[i][j])
                elif self.box_nr == 6:
                    if i < 9 and i >= 6 and j < 3:
                        self.box_array.append(nums[i][j])
                elif self.box_nr == 7:
                    if i < 9 and i >= 6 and j < 6 and j >= 3:
                        self.box_array.append(nums[i][j])
                elif self.box_nr == 8:
                    if i < 9 and i >= 6 and j < 9 and j >= 6:
                        self.box_array.append(nums[i][j])
        return self.box_array

    # Store row of a square
    def store_row(self, nums):
        for i in range(9):
            self.row_array[i] = nums[self.row][i]
        return self.row_array

    # Store column of a square
    def store_col(self, nums):
        for i in range(9):
            self.col_array[i] = nums[i][self.col]
        return self.col_array



    # Solve sudoku board
    def solve(self, numbers):
        for i in range(9):
            for j in range(9):
                self.num = numbers[i][j]
                self.row = i
                self.col = j
                self.box = self.find_box(self.row, self.col)

                self.box_array[:] = sorted(self.store_box(numbers))
                self.row_array[:] = sorted(self.store_row(numbers))
                self.col_array[:] = sorted(self.store_col(numbers))

                for k in range(1,10):
                    Square.insert_num(k, numbers)
                    self.solve(numbers)
                    numbers[i][j] = 0
                else:
                    continue


if __name__ == "__main__":
    print("GIVEN BOARD:")
    nums = np.array([[0, 0, 4, 3, 0, 0, 2, 0, 9], 
                    [0, 0, 5, 0, 0, 9, 0, 0, 1], 
                    [0, 7, 0, 0, 6, 0, 0, 4, 3], 
                    [0, 0, 6, 0, 0, 2, 0, 8, 7], 
                    [1, 9, 0, 0, 0, 7, 4, 0, 0], 
                    [0, 5, 0, 0, 8, 3, 0, 0, 0], 
                    [6, 0, 0, 0, 0, 0, 1, 0, 5], 
                    [0, 0, 3, 5, 0, 8, 6, 9, 0], 
                    [0, 4, 2, 9, 1, 0, 3, 0, 0]])
    print(nums)
    board = SudokuBoard()
    board.solve(nums)
    print("\n")
    print(nums)