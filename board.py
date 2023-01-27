from square import Square
from element import Element


class Board:

    def __init__(self, nums):
    # Nums parameter is a 2D list, like what the sudoku_reader returns
        self.n_rows = len(nums[0])
        self.n_cols = len(nums)
        self.nums = [[None for _ in range(self.n_rows)] for _ in range(self.n_cols)]

    def _set_up_nums(self):
        for i in range(self.n_rows):
            for j in range(self.n_cols):
                self.nums[i][j] = Square()

    def _set_up_elems(self):
        self.rows = [Element("row") for _ in range(self.n_rows)]
        self.cols = [Element("col") for _ in range(self.n_cols)]
        self.boxes = [Element("box") for _ in range(9)]

    def _set_up_squares(self):
        for i in range(self.n_rows):
            for j in range(self.n_cols):
                self.nums[i][j] = Square()
                self.rows[i].add_square(self.nums[i][j])
                self.cols[j].add_square(self.nums[i][j])


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
    b = Board([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    elems = b._set_up_elems()
    b._set_up_squares()
    print(b.rows)
