from square import Square

class Element():
    def __init__(self, type):
        self.element = [] # List of squares 
        self.type = type # Type of element (row, column, box)

    # Method appending a square to the element list
    def add_square(self, square): 
        self.element.append(square) # Append the square to the element list
    
    # Check if the value is legal in the element
    def check_legal(self, value):
        for square in self.element: # Iterate through the element list 
            if square.get_num() == value: # If the value were checking for is in the element list
                return False # Return false
        return True # Return true if the value is not in the element list
    
    def set_row(self):
        self.row = Square().get_row()

    def set_col(self):
        self.col = Square().get_col()

    def set_box(self):
        self.box = Square().get_box()

    
    
    # Get the element list
    def get_element(self):
        return self.element
    
    # Get the type of element (row, col, box)
    def get_type(self):
        return self.type

if __name__ == "__main__":
    row_element = Element("kuk")
    s = Square()
    s.set_num(1)
    row_element.add_square(s)
    print(row_element.get_element()[0].get_num())
    print(row_element.check_legal(row_element.get_element()[0]))
