import numpy as np

class Square:

    def __init__(self, row, col, num, nums):
        self.nums = nums # nums is a 9x9 array
        self.num = num   # num is a number 
        self.row = row   # nums[row_number][col_number]
        self.col = col   # nums[row_number][col_number] 
        self.box = None  # find_box() method will set this

    # Find box number
    def find_box(self):
        if self.row < 3:                              # Top 3 rows
            if self.col < 3:
                self.box = 0                          # Top left box
            elif self.col < 6 and self.col >= 3:
                self.box = 1                          # Top middle box
            else:
                self.box = 2                          # Top right box

        elif self.row < 6 and self.row >= 3:          # Middle 3 rows
            if self.col < 3:
                self.box = 3                          # Middle left box
            elif self.col < 6 and self.col >= 3:        
                self.box = 4                          # Middle middle box
            else:
                self.box = 5                          # Middle right box

        else:                                         # Bottom 3 rows
            if self.col < 3:
                self.box = 6                          # Bottom left box
            elif self.col < 6 and self.col >= 3:     
                self.box = 7                          # Bottom middle box    
            else:
                self.box = 8                          # Bottom right box

    # Box storage
    def store_box(self, nums):
        self.box_array = []
        for i in range(9):
            for j in range(9):
                if self.box == 0:
                    if i < 3 and j < 3:
                        self.box_array.append(nums[i][j])
                elif self.box == 1:
                    if i < 3 and j < 6 and j >= 3:
                        self.box_array.append(nums[i][j])
                elif self.box == 2:
                    if i < 3 and j < 9 and j >= 6:
                        self.box_array.append(nums[i][j])
                elif self.box == 3:
                    if i < 6 and i >= 3 and j < 3:
                        self.box_array.append(nums[i][j])
                elif self.box == 4:
                    if i < 6 and i >= 3 and j < 6 and j >= 3:
                        self.box_array.append(nums[i][j])
                elif self.box == 5:
                    if i < 6 and i >= 3 and j < 9 and j >= 6:
                        self.box_array.append(nums[i][j])
                elif self.box == 6:
                    if i < 9 and i >= 6 and j < 3:
                        self.box_array.append(nums[i][j])
                elif self.box == 7:
                    if i < 9 and i >= 6 and j < 6 and j >= 3:
                        self.box_array.append(nums[i][j])
                elif self.box == 8:
                    if i < 9 and i >= 6 and j < 9 and j >= 6:
                        self.box_array.append(nums[i][j])
        return self.box_array

    # Row storage
    def store_row(self, nums):
        self.row_array = np.zeros(9)
        for i in range(9):
            self.row_array[i] = nums[self.row][i]
        return self.row_array

    # Column storage
    def store_col(self, nums):
        self.col_array = np.zeros(9)
        for i in range(9):
            self.col_array[i] = nums[i][self.col]
        return self.col_array

    # Check legality of number
    def check_legal(self, nums):
        # Check if number is in the row
        if self.num in self.store_row(nums):
            return False
        # Check if number is in the column
        elif self.num in self.store_col(nums):
            return False
        # Check if number is in the box
        elif self.num in self.store_box(nums):
            return False
        # Check if number is zero
        elif self.num == 0:
            return False
        else:
            return True

    # Setters
    def set_num(self, num):
        self.num = num 
    
    def set_row(self, row):
        self.row = row
    
    def set_col(self, col):
        self.col = col
    
    def set_box(self, box): # Assign this value with find_box() method
        self.box = box
    
    # Getters
    def get_num(self):
        return self.num 

    def get_row(self):
        return self.row

    def get_col(self):
        return self.col
    
    def get_box(self):
        return self.box
    
    def get_box_array(self):
        return self.box_array


    # Insert a legal number into the square
    def insert_num(self):
        if self.check_legal(self.nums) == False:
            print("Illegal number")
        else:
            # Insert number into square which is not a duplicate and non zero
            self.nums[self.row][self.col] = self.num


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

    Square = Square(7, 4, 2, nums)
    print("Row number: ", Square.get_row())
    print("Column number: ", Square.get_col())
    print("Num: ", Square.get_num())

    Square.find_box()
    print("Box number: "  +  "\n", Square.get_box())
    print("The box list: "  +  "\n", Square.store_box(nums))
    print("The row list: "  +  "\n", Square.store_row(nums))
    print("The column list: "  +  "\n", Square.store_col(nums))

    Square.insert_num()
    print("The new array: " +  "\n", Square.nums)

