from board import Board
from sudoku_reader import Sudoku_reader
import time




class SudokuBoard(Board):
    def __init__(self, nums):
        super().__init__(nums)

    # Solve sudoku board
    def solve(self, array):
        for row in range(self.n_rows): # Loops through the rows
            for col in range(self.n_cols): # Loops through the columns
                if array[row][col] == 0: # If the square is empty
                    for num in range(1, 10): # Loops through the numbers 1-9
                        if self._check_legal(row, col, num): # Checks if the number is legal
                            array[row][col] = num # Inserts the number into the square
                            # Append the number to the row, column and box elements
                            self.rows[row].add_square(num)
                            self.cols[col].add_square(num)
                            self.boxes[self._find_box(row, col)].add_square(num)
                            # backtracking 
                            if self.solve(array):
                                return True
                            else:
                                array[row][col] = 0
                                self.rows[row].remove_square(num)
                                self.cols[col].remove_square(num)
                                self.boxes[self._find_box(row, col)].remove_square(num)
                    return False
        return True


if __name__ == "__main__":
        nums = Sudoku_reader("sudoku_1M.csv")
        start = time.time()
        for i in range(1000):
            nums_in = nums.next_board()
            board = SudokuBoard(nums_in)
            board._set_up_nums(nums_in)
            board._set_up_elems()
            board.solve(nums_in)
            print(nums_in)
        end = time.time()
        print("Time: ", end - start)








