from board import Board
from sudoku_reader import Sudoku_reader
import time


class SudokuBoard(Board):
    def __init__(self, nums):
        super().__init__(nums) # Calls the __init__ method from the parent class Board

    # Solve sudoku board
    def solve(self, array):
        for row in range(self.n_rows): # Loops through the rows
            for col in range(self.n_cols): # Loops through the columns
                if array[row][col] == 0: # If the square is empty
                    for num in range(1, 10): # Loops through the numbers 1-9
                        if self._check_legal(row, col, num): # Checks if the number is legal
                            array[row][col] = num # Inserts the number into the square

                            # Append the number to the row, column and box elements
                            self.rows[row].add_square(num) # Adds the square to the row element
                            self.cols[col].add_square(num) # Adds the square to the column element 
                            self.boxes[self._find_box(row, col)].add_square(num) # Adds the square to the box element 
                            
                            # backtracking 
                            if self.solve(array): # Recursively calls the function
                                return True
                            else:
                                array[row][col] = 0 # If the number is not legal, the square is set to 0 
                                self.rows[row].remove_square(num) # Removes the square from the row element
                                self.cols[col].remove_square(num)         # Removes the square from the column element
                                self.boxes[self._find_box(row, col)].remove_square(num)  # Removes the square from the box element
                    return False
        return True


if __name__ == "__main__":
        nums = Sudoku_reader("sudoku_1M.csv") # Creates a Sudoku_reader object. Row of 81 numbers from file
        start = time.time() # Starts the timer
        for i in range(100): # Loops through the games in the file. 
            nums_in = nums.next_board() # Gets the next game from the file
            board = SudokuBoard(nums_in) # Creates a SudokuBoard object
            board._set_up_nums(nums_in) # Sets up the sudokuboard
            board._set_up_elems()     # Sets up the elements
            board.solve(nums_in) # Solves the sudoku board
            print(nums_in) # Prints the solved sudoku board
        end = time.time() # Stops the timer
        print("Time: ", end - start) # Prints the time it took to solve the sudoku boards








