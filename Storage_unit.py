"""     def store_rows(self):
        for i in range(9):
            self.rows[:,i] = self.nums[:,i] # Store 9 rows in array

    def store_cols(self):
        for i in range(9):
            self.cols[:,i] = self.nums[i,:] # Store 9 columns in array

    def store_boxes(self):
        for i in range(9):
            self.boxes.append(self.nums[3*(i//3):3*(i//3)+3, 3*(i%3):3*(i%3)+3].flatten()) # Store 9 boxes in a list
"""