from element import Element

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
                self.nums[row][col] = int(array[row][col]) # Converts float to whole int and stores it in the board, just for nice look

    # Creates the elements and adds the squares to the elements
    def _set_up_elems(self): 
        for row in range(self.n_rows):
            for col in range(self.n_cols):
                self.rows[row].add_square(self.nums[row][col]) # Adds the square to the row element
                self.cols[col].add_square(self.nums[row][col]) # Adds the square to the column element
                self.boxes[self._find_box(row, col)].add_square(self.nums[row][col]) # Adds the square to the box element

    # Check if number is legal in row, col and box 
    def _check_legal(self, row, col, num): 
        return self.rows[row].check_legal(num) and self.cols[col].check_legal(num) and self.boxes[self._find_box(row, col)].check_legal(num)

    # remove square from row, col and box elements when backtracking
    def remove_square(self, row, col, num): 
        self.rows[row].remove_square(num)
        self.cols[col].remove_square(num)
        self.boxes[self._find_box(row, col)].remove_square(num)