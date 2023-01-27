from square import Square
import numpy as np


class Element(Square):
    def __init__(self, row, col, box, num, nums):
        super().__init__(row, col, box, num, nums)
        self.nums = nums
        self.row = Square.get_row(self)
        self.col = Square.get_col(self)
        self.box = Square.get_box(self)


if __name__ == "__main__":
    nums = np.array([[0, 0, 4, 3, 0, 0, 2, 0, 9]
                    ,[0, 0, 5, 0, 0, 9, 0, 0, 1]
                    ,[0, 7, 0, 0, 6, 0, 0, 4, 3]
                    ,[0, 0, 6, 0, 0, 2, 0, 8, 7]
                    ,[1, 9, 0, 0, 0, 7, 4, 0, 0]
                    ,[0, 5, 0, 0, 8, 3, 0, 0, 0]
                    ,[6, 0, 0, 0, 0, 0, 1, 0, 5]
                    ,[0, 0, 3, 5, 0, 8, 6, 9, 0]
                    ,[0, 4, 2, 9, 1, 0, 3, 0, 0]]) 

    Element = Element(0, 0, 0, 5, nums)
    print("True if legal, False if illegal: ", Element.check_legal(nums))

    

    print(Element.get_row_array()) 
    print(Element.get_col_array()) 
    print(Element.get_box_array()) 





