from board import Board
from square import Square
from element import Element
import numpy as np 

class SudokuBoard(Board):

    def __init__(self, nums):
        super().__init__(nums)
        self.box_array = np.zeros((9, 9))    # Box element
        self.col_array = np.zeros((9, 9))    # Column element
        self.row_array = np.zeros((9, 9))    # Row element
    


    # Find box number
    def find_box(self, row_nr, col_nr): # Finds box number of a square
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
    
    # Store box of a square
    def store_box(self, nums): # Stores box values in a list of a square were iterating through
        for i in range(9):
            for j in range(9):
                if self.box_nr == 0:
                    if i < 3 and j < 3:
                        self.box_array[i] = nums[i][j] 
                elif self.box_nr == 1:
                    if i < 3 and j < 6 and j >= 3:
                        self.box_array[i] = nums[i][j] 
                elif self.box_nr == 2:
                    if i < 3 and j < 9 and j >= 6:
                        self.box_array[i] = nums[i][j] 
                elif self.box_nr == 3:
                    if i < 6 and i >= 3 and j < 3:
                        self.box_array[i] = nums[i][j] 
                elif self.box_nr == 4:
                    if i < 6 and i >= 3 and j < 6 and j >= 3:
                        self.box_array[i] = nums[i][j] 
                elif self.box_nr == 5:
                    if i < 6 and i >= 3 and j < 9 and j >= 6:
                        self.box_array[i] = nums[i][j] 
                elif self.box_nr == 6:
                    if i < 9 and i >= 6 and j < 3:
                        self.box_array[i] = nums[i][j] 
                elif self.box_nr == 7:
                    if i < 9 and i >= 6 and j < 6 and j >= 3:
                        self.box_array[i] = nums[i][j] 
                elif self.box_nr == 8:
                    if i < 9 and i >= 6 and j < 9 and j >= 6:
                        self.box_array[i] = nums[i][j] 

    # Store row of a square using element class
    def store_row(self, nums): # Stores row values in an array of a square were iterating through
        for i in range(9):
            self.row_array[i] = nums[self.row][i]
        return self.row_array
        
    # Store column of a square
    def store_col(self, nums): # Stores column values in an array of a square were iterating through
        for i in range(9):
            self.col_array[i] = nums[i][self.col]
        return self.col_array

    def find_possible(self):
        self.possible = []
        for i in range(1, 10):
            if i not in self.row_array and i not in self.col_array and i not in self.box_array:
                self.possible.append(i)
        return self.possible



    # Solve sudoku board
    def solve(self, numbers):
        for i in range(9):
            for j in range(9):
                self.nums = numbers
                self.num = self.nums[i][j]
                self.row = i
                self.col = j
                self.box_nr = self.find_box(self.row, self.col)
                self.row_array = self.store_row(self.nums)
                self.col_array = self.store_col(self.nums)
                self.box_array = self.store_box(numbers)
                if self.num == 0:
                    self.possible = self.find_possible()
                    print(self.nums)
                    possible = self.find_possible()
                    self.nums[i][j] = possible[0]
                    self.solve(self.nums)
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
    b = SudokuBoard(nums)
    b.find_box(0, 0)
    print("BOX NUMBER: ", b.box_nr)
    b.store_box(nums)
    print("BOX ARRAY: ", b.box_array)
    b.solve(nums)
    print("SOLVED BOARD:") 
    print(b.nums)
