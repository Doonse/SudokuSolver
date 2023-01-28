class Square:

    def __init__(self):
        self.num = None # Number in square
        self.row = None # Row position
        self.col = None # Column position
        self.box = None # Box position

    # Check legality of number
    def check_legal(self):
        # Check if number is in the row
        if self.num in self.row:
            return False
        # Check if number is in the column
        elif self.num in self.col:
            return False
        # Check if number is in the box
        elif self.num in self.box:
            return False
        # Check if number is zero
        elif self.num == 0:
            return False
        else:
            return True

    # Insert number into square
    def insert_num(self, value):
        return self.num == value
    """ def insert_num(self, value):
        if self.check_legal() == False:
            print("Illegal number")
        else:
            # Insert number into square which is not a duplicate and non zero
            if self.num == 0:
                self.nums[self.row][self.col] = value
                print("Number inserted") """


    # Setters
    def set_num(self, num):
        self.num = num 
    
    def set_row(self, row):
        self.row = row
    
    def set_col(self, col):
        self.col = col
    
    def set_box(self, box): 
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
    



